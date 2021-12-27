import time

import pytest
import softest

from pages.search_flight_results_page import SeachFligthResults
from pages.yatra_launch_page import LauchPage
from utilites.utils import Utils
from ddt import ddt, data, unpack, file_data

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        # Create all class object that require
        self.lp = LauchPage(self.driver)
        self.ut = Utils()

    @file_data("E:/Auto_WorkingTesting/ATFDemo/testdata/testdata.json")
    def test_search_flight_one_stop(self, goingfrom, goingto, date, stops):
        sf = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.scroll_to_bottom_page()
        sf.filter_flights_by_stops(stops)
        allStop1 = sf.get_search_fligth_results()
        self.ut.assert_value_in_list(allStop1, stops)

