import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# 1. Присутствуют все питомцы.
def test_all_animals_are_present(show_my_pets, get_my_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    statistic_pet = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity = int(statistic_pet[0].text.split('\n')[1].split(' ')[1])
    assert quantity == len(get_my_pets)


# 2. Хотя бы у половины питомцев есть фото.
def test_pets_have_photos(show_my_pets, get_my_pets, get_my_pet_photos):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    assert len(get_my_pet_photos) >= len(get_my_pets) / 2


# 3. У всех питомцев есть имя, возраст и порода.
def test_pets_have_photos_have_a_name_age_breed(show_my_pets, get_my_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    for pet in get_my_pets:
        assert pet['name'] != '' and pet['age'] != '' and pet['breed'] != ''


# 4. У всех питомцев разные имена.
def test_pets_with_different_names(show_my_pets, get_my_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pets_name = []
    for pet in get_my_pets:
        if pet['name'] in pets_name:
            print("Contains")
        else:
            pets_name.append(pet)

    assert len(get_my_pets) == len(pets_name)


# 5. В списке нет повторяющихся питомцев. (Сложное задание).
def test_different_pets(show_my_pets, get_my_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pets = []
    for pet in get_my_pets:
        if pet in pets:
            print("Contains")
        else:
            pets.append(pet)

    assert len(get_my_pets) == len(pets)


# 6. Проверка карточек питомцев(фото, имя питомца, его возраст)
def test_checking_by_pet_photo(show_my_pets, get_my_pets, get_my_pet_photos):
    pytest.driver.implicitly_wait(3)
    images = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    names = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


# 7. Проверка таблицы питомцев
def test_checking_table_of_animals(show_my_pets, get_my_pets):
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    statistic_pet = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    quantity = int(statistic_pet[0].text.split('\n')[1].split(' ')[1])
    assert quantity == len(get_my_pets)