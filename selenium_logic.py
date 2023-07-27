from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from xvfbwrapper import Xvfb



# Open the space
def open_space():
    global vdisplay, driver

    vdisplay = Xvfb()
    vdisplay.start()
    driver = webdriver.Firefox()

    driver.get('https://billing.interdom.kg')
    driver.find_element(By.NAME, 'username').send_keys('DjumagazievA')
    driver.find_element(By.NAME, 'password').send_keys('86308W4YEZ')
    driver.find_element(By.XPATH, '//form[@class="ubLoginForm"]/input[4]').click()


# Add new users
def add_info(info: dict):
    driver.get('https://billing.interdom.kg/index.php?module=userreg')
    add_to_city = info.get('city')
    driver.find_element(By.NAME, 'citysel').send_keys(add_to_city)
    sleep(1)

    add_to_street = info.get('street')
    street = Select(driver.find_element(By.NAME, 'streetsel'))
    street.select_by_visible_text(add_to_street)
    sleep(1)

    house = Select(driver.find_element(By.NAME, 'buildsel'))
    house.select_by_visible_text(info.get('house'))
    sleep(1)

    driver.find_element(By.NAME, 'entrance').send_keys(info.get('ent'))
    driver.find_element(By.NAME, 'floor').send_keys(info.get('floor'))
    driver.find_element(By.NAME, 'apt').send_keys(info.get('appart'))
    sleep(1)

    driver.find_elements(By.XPATH, '//tr[@class="row3"]/td/input')[-1].click()
    sleep(1)

    driver.close()
    vdisplay.stop()

    try:
        if driver.find_element(By.ID, 'ui-id-3').text == 'Предупреждение':
            driver.close()
            raise ZeroDivisionError
    
    except NoSuchElementException:
        driver.find_elements(By.XPATH, '//div[@class="module_content"]/input')[-1].click()
        sleep(1)

        driver.find_elements(By.XPATH, '//div[@class="dashtask"]')[-1].click()
        get_user_id = driver.current_url[-5:]
        sleep(1)

        ### Change LastName
        driver.get(f'https://billing.interdom.kg/index.php?module=realnameedit&username={get_user_id}')
        driver.find_element(By.NAME, 'newrealname').send_keys(info.get('name'))
        driver.find_elements(By.XPATH, '//input')[-1].click()
        sleep(1)

        ### Change tarif
        driver.get(f'https://billing.interdom.kg/index.php?module=tariffedit&username={get_user_id}')
        tarif = Select(driver.find_element(By.NAME, 'newtariff'))
        tarif.select_by_visible_text('Domofon_Promo')
        driver.find_elements(By.XPATH, '//input')[-1].click()
        sleep(1)

        ### Change phone_num
        driver.get(f'https://billing.interdom.kg/index.php?module=phoneedit&username={get_user_id}')
        driver.find_element(By.NAME, 'newphone').send_keys(info.get('phone_num'))
        driver.find_elements(By.XPATH, '//input')[-1].click()
        sleep(1)


        ### post special requests
        req = info.get('requests', False)
        if req:
            driver.get(f'https://billing.interdom.kg/?module=notesedit&username={get_user_id}')
            driver.find_element(By.NAME, 'newnotes').send_keys(req)
            driver.find_elements(By.XPATH, '//input')[-1].click()
            sleep(1)


        driver.get(f'https://billing.interdom.kg/index.php?module=userprofile&username={get_user_id}')
        driver.close()
        return get_user_id
            



# open_space()
# add_info(
#     {
#         'city': 'г. Бишкек',
#         'street': 'ул. Юнусалиева',
#         'house': '174/4',
#         'ent': '2',
#         'floor': '3',
#         'appart': '101',
#     }
# )