import requests
import pytest

####################################################


def pytest_addoption(parser):
    parser.addoption("--url1", action="store", default=None, help="For service_1")
    parser.addoption("--url2", action="store", default=None, help="For service 2")
    parser.addoption("--url3", action="store", default=None, help="For service 3")


####################################################


@pytest.fixture()
def use_url1(request):

    return request.config.getoption("--url1")


@pytest.fixture
def requests_get_service_1(use_url1):
    try:
        return requests.get(use_url1)
    except requests.exceptions.MissingSchema:
        print("Неподдерживаемый URL")


@pytest.fixture()
def requests_post_service_1(use_url1):
    try:
        return requests.post(use_url1)
    except requests.exceptions.MissingSchema:
        print("Неподдерживаемый URL")


####################################################
@pytest.fixture()
def use_url2(request):

    return request.config.getoption("--url2")


@pytest.fixture
def request_get_service_2(use_url2):
    try:
        return requests.get(use_url2)
    except requests.exceptions.MissingSchema:
        print("Неподдерживаемый URL")


####################################################


@pytest.fixture()
def use_url3(request):

    return request.config.getoption("--url3")


@pytest.fixture()
def filename_version_name_service_3(use_url3):
    try:
        return requests.get(use_url3)
    except requests.exceptions.MissingSchema:
        print("Неподдерживаемый URL")
