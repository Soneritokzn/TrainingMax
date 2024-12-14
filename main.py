import requests
from data import *

def print_response(root):
    print("Response from server: ")
    print(root)
    print("")

def print_data(root):
    print("Data: ")
    print(root.data)

def get_raw_data(url):
    response = requests.get(url)
    return response.text

def get_data(url) -> Root:
    data = requests.get(url)
    myjsonstring = data.text
    root = Root.from_json(myjsonstring)
    return root

def test_root_not_null(root: Root):
    print("Run Test 1 ... ", end='')
    assert root.page is not None
    assert root.per_page is not None
    print("test passed.")

def test_data1(data: Data):
    print("Run Test data 1 ... ", end='')
    assert data.id == 1
    assert data.name == 'cerulean'
    assert data.year == 2000
    assert data.color == '#98B2D1'
    assert data.pantone_value == '15-4020'
    print("test passed.")

def test_data_list(data: list[Data], referenceData: list[Data]):
    print("Run Test all data list ... ", end='')
    for i in range(len(root.data)):
        assert data[i].id == referenceData[i].id
        assert data[i].name == referenceData[i].name
        assert data[i].year == referenceData[i].year
        assert data[i].color == referenceData[i].color
        assert data[i].pantone_value == referenceData[i].pantone_value

    print("test passed.")

if __name__ == '__main__':
    # Получаем данные с сервера
    url = "https://reqres.in/api/{resource}"
    root = get_data(url)
    print_response(root)
    print_data(root)

    # Простые тесты
    test_root_not_null(root)
    test_data1(root.data[0])

    # Имитируем получение эталонных данных
    referenceResponse_raw = get_raw_data(url)
    referenceRoot = Root.from_json(referenceResponse_raw)

    # Сравниваем весь список данных с эталоном
    test_data_list(root.data, referenceRoot.data)

    # Меняем эталонные данные
   # print("Change reference data.")
    #referenceRoot.data[2].year = 1234

    # Убеждаемся, что теперь тест не проходит
    #test_data_list(root.data, referenceRoot.data)
