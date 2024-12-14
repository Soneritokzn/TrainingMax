import requests, json
import pytest
from pytest import *
import data
from data import *


def print_response(root):
    print("Response: ")
    print(root)

def print_data(root):
    print("Data: ")
    print(root.data)

def get_data() -> Root:
    data = requests.get("https://reqres.in/api/{resource}")
    myjsonstring = data.text
    root = Root.from_json(myjsonstring)
    return root

def test_root(root: Root):
    print("Test 1:")
    assert root.page is not None
    assert root.per_page is not None
    print("Test passed.")

def test_data1(data: Data):
    print("Test data 1 ...")
    assert data.id == 1
    assert data.name == 'cerulean'
    assert data.year == 2000
    assert data.color == '#98B2D1'
    assert data.pantone_value == '15-4020'
    print("Test data 1 passed.")

if __name__ == '__main__':
    root = get_data()
    print_response(root)
    print_data(root)
    test_root(root)
    test_data1(root.data[0])

