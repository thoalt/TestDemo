import time

import pytest
import softest

from pages.search_flight_results_page import SeachFligthResults
from pages.yatra_launch_page import LauchPage
from utilites.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        # Create all class object that require
        self.lp = LauchPage(self.driver)
        self.ut = Utils()

    def test_search_flight_one_stop(self):
        # Lauching Browser
        print("Using setup fixtures in conftest.py")
        sf = self.lp.searchFlights("New Delhi", "Goa", "24/12/2021")
        self.lp.scroll_to_bottom_page()
        sf.filter_flights_by_stops("1 Stop")
        allStop1 = sf.get_search_fligth_results()
        self.ut.assert_value_in_list(allStop1, '1 Stop')

