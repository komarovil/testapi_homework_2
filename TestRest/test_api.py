import pytest
import sys


@pytest.mark.skipif(not '--url1' in sys.argv, reason="not url1 in here")
def test_one_service_1(requests_get_service_1):

    assert requests_get_service_1.status_code == 200


@pytest.mark.skipif(not '--url1' in sys.argv, reason="not url1 in here")
def test_two_service_1(requests_post_service_1):

    assert requests_post_service_1.status_code != 200


@pytest.mark.skipif(not '--url1' in sys.argv, reason="not url1 in here")
def test_three_service_1(requests_get_service_1):

    data = requests_get_service_1.json()
    assert data['status'] == 'success'


####################################################


@pytest.mark.skipif(not '--url2' in sys.argv, reason="not url2 in here")
def test_one_service_2(request_get_service_2):

    assert request_get_service_2.status_code == 200


@pytest.mark.skipif(not '--url2' in sys.argv, reason="not url2 in here")
def test_two_service_2(request_get_service_2):

    data = request_get_service_2.headers
    assert data['Content-Type'] == 'application/json; charset=utf-8'


# ####################################################

@pytest.mark.skipif(not '--url3' in sys.argv, reason="not url3 in here")
def test_one_service_3(filename_version_name_service_3):

    assert filename_version_name_service_3.status_code == 200


@pytest.mark.skipif(not '--url3' in sys.argv, reason="not url3 in here")
def test_two_service_3(filename_version_name_service_3):

    assert filename_version_name_service_3.headers['server'] == 'cloudflare'


@pytest.mark.skipif(not '--url3' in sys.argv, reason="not url3 in here")
def test_three_service_3(filename_version_name_service_3):

    assert filename_version_name_service_3.headers['access-control-allow-methods'] == 'GET,PUT,POST,DELETE,OPTIONS'
