import time

import pytest
import self as self
import softest
import openpyxl
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet

from pages.search_flight_results_page import SeachFligthResults
from pages.yatra_launch_page import LauchPage
from utilites.utils import Utils
from ddt import ddt, data, unpack, file_data
import sys

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    path = sys.path[2]
    print(path + "/testdata/testdata.xlsx")
    @pytest.fixture(autouse=True)
    def class_setup(self):
        # Create all class object that require
        self.lp = LauchPage(self.driver)
        self.ut = Utils()

    # get test data from specified excle spreadsheet
    @data(*Utils.read_data_from_exel(path + "/testdata/testdata.xlsx", "Sheet1"))
    @unpack
    def test_search_flight_one_stop(self, goingfrom, goingto, date, stops):
        print("Using setup fixtures in conftest.py")
        sf = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.scroll_to_bottom_page()
        sf.filter_flights_by_stops(stops)
        allStop1 = sf.get_search_fligth_results()
        self.ut.assert_value_in_list(allStop1, stops)
