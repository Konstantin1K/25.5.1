import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driverChrome():
    pytest.driver = webdriver.Chrome("c:\chromedriver.exe")
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


@pytest.fixture()
def show_my_pets():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('kostya.kalustov@mail.ru')

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('0422Ludmila')

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button['
                                                                                            'type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()


@pytest.fixture()
def get_my_pets():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
    pet_list = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    returned_list = []
    for pets in pet_list:
        pet = pets.text.split()
        returned_list.append({'name': pet[0], 'breed': pet[1], 'age': pet[2]})

    yield returned_list


@pytest.fixture()
def get_my_pet_photos():
    pet_photos = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr th img')
    returned_photo_list = []

    for photo in pet_photos:
        returned_photo_list.append({'photo', photo.get_attribute('src')})
    yield returned_photo_list