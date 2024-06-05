import pytest
from city_functions import get_location


def test_get_location(city,state,country):
    test_city = get_location("santiago", "", "chile", 5000)
    assert test_city == "-Santiago, , Chile: Population 5000-"
