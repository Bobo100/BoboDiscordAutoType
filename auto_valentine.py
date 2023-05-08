from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import click
import os
import json

import shutil
from tqdm import tqdm


base_path = os.path.dirname(os.path.abspath(__file__))
pokemon_dataset_path = os.path.join(
    base_path, "data", "pokemon_dataset.json")

# Opening JSON file
f = open(pokemon_dataset_path, encoding="utf-8")
data = json.load(f)
f.close()


def copy_with_progress(src, dst):
    """
    Copy the contents of directory src to directory dst and display progress using tqdm.
    """
    # Get the total size of the source directory
    total_size = sum(f.stat().st_size for f in os.path(
        src).rglob('*') if f.is_file())

    # Use tqdm to display progress
    with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
        # Use shutil.copytree() to copy the directory
        shutil.copytree(src, dst, copy_function=lambda f, d: shutil.copy2(f, d, follow_symlinks=False),
                        ignore=None, dirs_exist_ok=True)
        # Update the progress bar with the current size of the copied files
        pbar.update(f.stat().st_size for f in os.path(
            dst).rglob('*') if f.is_file())


def switch(lang):
    if lang == "Doduo":
        return "Icy Wind"
    elif lang == "Galarian Zapdos":
        return "Moonblast"
    elif lang == "Dragonite":
        return "Freeze Dry"
    elif lang == "Shuckle":
        return "Iron Head"
    elif lang == "Slugma":
        return "Water Shuriken"
    elif lang == "Ho-Oh":
        return "Thunder"
    elif lang == "Spinda":
        return "Close Combat"
    elif lang == "Bergmite":
        return "Stone Edge"
    elif lang == "Xerneas":
        return "Sludge Wave"
    elif lang == "Rockruff":
        return "Flash Cannon"


valentine = [{'id': '35', 'name': 'Clefairy', 'attack': 'Steel Wing'}, {'id': '36', 'name': 'Clefable', 'attack': 'Steel Wing'}, {'id': '133', 'name': 'Eevee', 'attack': 'Rock Smash'}, {'id': '134', 'name': 'Vaporeon', 'attack': 'Grass Pledge'}, {'id': '135', 'name': 'Jolteon', 'attack': 'Earth Power'}, {'id': '136', 'name': 'Flareon', 'attack': 'Stone Axe'}, {'id': '151', 'name': 'Mew', 'attack': 'Dark Pulse'}, {'id': '161', 'name': 'Sentret', 'attack': 'Dynamic Punch'}, {'id': '162', 'name': 'Furret', 'attack': 'Dynamic Punch'}, {'id': '173', 'name': 'Cleffa', 'attack': 'Steel Wing'}, {'id': '179', 'name': 'Mareep', 'attack': 'Earth Power'}, {'id': '180', 'name': 'Flaaffy', 'attack': 'Earth Power'}, {'id': '181', 'name': 'Ampharos', 'attack': 'Earth Power'}, {'id': '181-1', 'name': 'Ampharos-Mega', 'attack': 'Dragon Pulse'}, {'id': '196', 'name': 'Espeon', 'attack': 'Assurance'}, {'id': '197', 'name': 'Umbreon', 'attack': 'Moonblast'}, {'id': '250', 'name': 'Ho-oh', 'attack': 'Stone Axe'}, {'id': '370', 'name': 'Luvdisc', 'attack': 'Grass Knot'}, {'id': '377', 'name': 'Regirock', 'attack': 'Frenzy Plant'}, {'id': '378', 'name': 'Regice', 'attack': 'Fire Blast'}, {'id': '379', 'name': 'Registeel', 'attack': 'Precipice Blades'}, {'id': '470', 'name': 'Leafeon', 'attack': 'Sky Attack'}, {'id': '471', 'name': 'Glaceon', 'attack': 'Fire Blast'}, {'id': '486',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'name': 'Regigigas', 'attack': 'Close Combat'}, {'id': '491', 'name': 'Darkrai', 'attack': 'Moonblast'}, {'id': '548', 'name': 'Petilil', 'attack': 'Sky Attack'}, {'id': '549', 'name': 'Lilligant', 'attack': 'Sky Attack'}, {'id': '549-1', 'name': 'Hisuian Lilligant', 'attack': 'Sky Attack'}, {'id': '582', 'name': 'Vanillite', 'attack': 'Blast Burn'}, {'id': '583', 'name': 'Vanillish', 'attack': 'Blast Burn'}, {'id': '584', 'name': 'Vanilluxe', 'attack': 'Blast Burn'}, {'id': '653', 'name': 'Fennekin', 'attack': 'Scald'}, {'id': '654', 'name': 'Braixen', 'attack': 'Scald'}, {'id': '655', 'name': 'Delphox', 'attack': 'Mud Shot'}, {'id': '700', 'name': 'Sylveon', 'attack': 'Metal Claw'}, {'id': '736', 'name': 'Grubbin', 'attack': 'Psyshock'}, {'id': '737', 'name': 'Charjabug', 'attack': 'Fire Blast'}, {'id': '738', 'name': 'Vikavolt', 'attack': 'Fire Blast'}, {'id': '775', 'name': 'Komala', 'attack': 'Axe Kick'}, {'id': '782', 'name': 'Jangmo-o', 'attack': 'Confusion'}, {'id': '783', 'name': 'Hakamo-o', 'attack': 'Fairy Wind'}, {'id': '784', 'name': 'Kommo-o', 'attack': 'Fairy Wind'}, {'id': '786', 'name': 'Tapu-Lele', 'attack': 'Metal Claw'}, {'id': '794', 'name': 'Buzzwole', 'attack': 'Fly'}, {'id': '795', 'name': 'Pheromosa', 'attack': 'Gust'}, {'id': '802', 'name': 'Marshadow', 'attack': 'Shadow Sneak'}, {'id': '895', 'name': 'Regidrago', 'attack': 'Outrage'}]


def catch(driver):
    time_count = 0
    id_list = []
    last_time_code = 0
    while True:
        try:
            base = driver.find_elements(
                By.XPATH, './/article/div/div/div[contains(concat(" ",normalize-space(@class)," ")," imageContent-3Av-9c ")][contains(concat(" ",normalize-space(@class)," ")," embedThumbnail-2nTasl ")]/div/div/a[contains(@class, "originalLink-Azwuo9")]')

            if (time_count >= 25):
                lastbutton = driver.find_elements(
                    By.XPATH, '//*[@id="app-mount"]/div/div/div/div/div/div/div/div/div/div/div/main/div/div/div/ol/li')
                driver.execute_script(
                    "arguments[0].scrollIntoView(true);", lastbutton[-1])
                print("refresh")
                time_count = 0
                
            print(len(id_list))
            if(len(id_list) > 20):
                id_list = id_list[-1:]

            time_count += 1

            pokemon_url = base[-1].get_attribute('href')
            pokemon_number = pokemon_url.split('/')[-1].split('-')[0]
            pokemon_number_region = pokemon_url.split(
                '/')[-1].split('-')[1]
            article_id = base[-1].find_element(
                By.XPATH, "../../../../../../..").get_attribute("id")
            
            # 想要做個處理
            time_code = article_id.split('-')[-1]
            time.sleep(1)
                            
            if article_id:
                if article_id in id_list:
                    time_count -= 1
                    continue
                if "valentines2023" in pokemon_url:
                    if pokemon_number_region != "0":
                        pokemon_number = pokemon_number + "-" + pokemon_number_region
                    for i in data:
                        if (i["id"] == pokemon_number):
                            pokemon_name = i["name"]
                            chinese_name = i["chinese_name"]
                    
                    # 如果是新的一個
                    # if(last_time_code < time_code):
                    
                    id_list.append(article_id)
                    last_time_code = time_code
                    print(f'快來和 {chinese_name} + 情人節寶可夢，戰鬥啦')
                    
                    # 按下join
                    article_selector = ".//*[@id='" + \
                        article_id + "']/div/div/div/button"
                    driver.find_element(
                        By.XPATH,  article_selector).click()
                    # 找正確的技能名稱
                    for i in valentine:
                        if (pokemon_number == i["id"]):
                            keyword = i["attack"]
                    print("請使用:" + keyword)
                    # 文字1
                    time.sleep(10)
                    text1_xpath = './/*[@id="'+article_id + \
                        '"]/div[contains(concat(" ",normalize-space(@class)," ")," container-3Sqbyb ")]/div/div/button[(count(preceding-sibling::*)+1) = 1]/div/div/div'
                    text2_xpath = './/*[@id="'+article_id + \
                        '"]/div[contains(concat(" ",normalize-space(@class)," ")," container-3Sqbyb ")]/div/div/button[(count(preceding-sibling::*)+1) = 2]/div/div/div'
                    text3_xpath = './/*[@id="'+article_id + \
                        '"]/div[contains(concat(" ",normalize-space(@class)," ")," container-3Sqbyb ")]/div/div/button[(count(preceding-sibling::*)+1) = 3]/div/div/div'
                    text4_xpath = './/*[@id="'+article_id + \
                        '"]/div[contains(concat(" ",normalize-space(@class)," ")," container-3Sqbyb ")]/div/div/button[(count(preceding-sibling::*)+1) = 4]/div/div/div'
                    wait.until(EC.presence_of_element_located(
                        (By.XPATH, text2_xpath)))
                    text1 = driver.find_element(
                        By.XPATH, text1_xpath).get_attribute("innerText")
                    text2 = driver.find_element(
                        By.XPATH, text2_xpath).get_attribute("innerText")
                    text3 = driver.find_element(
                        By.XPATH, text3_xpath).get_attribute("innerText")
                    text4 = driver.find_element(
                        By.XPATH, text4_xpath).get_attribute("innerText")
                    if (keyword in text1):
                        button = './/*[@id="'+article_id + \
                            '"]/div/div/div/button[1]'
                        print("使用第一招")
                    elif (keyword in text2):
                        button = './/*[@id="'+article_id + \
                            '"]/div/div/div/button[2]'
                        print("使用第二招")
                    elif (keyword in text3):
                        button = './/*[@id="'+article_id + \
                            '"]/div/div/div/button[3]'
                        print("使用第三招")
                    elif (keyword in text4):
                        button = './/*[@id="'+article_id + \
                            '"]/div/div/div/button[4]'
                        print("使用第四招")
                    driver.find_element(
                        By.XPATH,  button).click()
                    
        except Exception as e:
            print(e)
            time_count += 1
            time.sleep(2)
            pass


if __name__ == '__main__':

    if (not os.path.isdir(os.path.join(base_path, "data"))):
        os.mkdir(os.path.join(base_path, "data"))

    if (os.path.exists(os.path.join(base_path, "data", "account_data.json"))):
        f = open(os.path.join(base_path, "data",
                 "account_data.json"), encoding="utf-8")
        accuont_data = json.load(f)
        f.close()
    else:
        print("第一次使用")
        username = input('請輸入DC帳號')
        print(username)
        userpassword = input('請輸入DC密碼')
        print(userpassword)
        channel_url = input(
            '要抓取頻道的網址')
        print(channel_url)

        accuont_data = {
            "username": username,
            "userpassword": userpassword,
            "channel_url": channel_url
        }
        with open(os.path.join(base_path, "data", "account_data.json"), "w") as outfile:
            json.dump(accuont_data, outfile)

    username = input('請輸入DC帳號') or accuont_data["username"]
    print(username)
    userpassword = input('請輸入DC密碼') or accuont_data["userpassword"]
    print(userpassword)

    value = click.confirm('要開啟瀏覽器嗎', default=True)
    print(value)
    channel_url = input(
        '要抓取頻道的網址') or accuont_data["channel_url"]
    print(channel_url)

    broswer_origin_path = "C:\\Users\\" + \
        os.getlogin() + "\\AppData\\Local\\Microsoft\\Edge\\User Data"
    broswer_copy_folder_path = "C:\\Users\\" + \
        os.getlogin() + "\\AppData\\Local\\Microsoft\\Edge\\User Data1"

    broswer_copy_path = "user-data-dir=C:\\Users\\" + \
        os.getlogin() + "\\AppData\\Local\\Microsoft\\Edge\\User Data1"

    if (not os.path.isdir(broswer_copy_folder_path)):
        copy_with_progress(broswer_origin_path, broswer_copy_folder_path)

    options = webdriver.EdgeOptions()
    if not value:
        options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument(
        broswer_copy_path)
    driver = webdriver.Edge(
        EdgeChromiumDriverManager().install(), options=options)

    driver.get(channel_url)
    wait = WebDriverWait(driver, 20)

    if (not os.path.isdir(broswer_copy_folder_path)):
        input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div > div > section > div.centeringWrapper-dGnJPQ > button.marginTop8-24uXGp.marginCenterHorz-574Oxy.linkButton-2ax8wP.button-f2h6uQ.lookLink-15mFoz.lowSaturationUnderline-Z6CW6z.colorLink-1Md3RZ.sizeMin-DfpWCE.grow-2sR_-F')))
        driver.find_element(By.CSS_SELECTOR,  "#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div > div > section > div.centeringWrapper-dGnJPQ > button.marginTop8-24uXGp.marginCenterHorz-574Oxy.linkButton-2ax8wP.button-f2h6uQ.lookLink-15mFoz.lowSaturationUnderline-Z6CW6z.colorLink-1Md3RZ.sizeMin-DfpWCE.grow-2sR_-F").click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#uid_5").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "#uid_8").send_keys(userpassword)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,  "#app-mount > div.appDevToolsWrapper-1QxdQf > div > div.app-3xd6d0 > div > div > div > div > form > div.centeringWrapper-dGnJPQ > div > div.mainLoginContainer-wHmAjP > div.block-3uVSn4.marginTop20-2T8ZJx > button.marginBottom8-emkd0_.button-1cRKG6.button-f2h6uQ.lookFilled-yCfaCM.colorBrand-I6CyqQ.sizeLarge-3mScP9.fullWidth-fJIsjq.grow-2sR_-F").click()
        time.sleep(8)

    catch(driver)
