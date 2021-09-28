#import pytest
# from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select

import Testdata
from Testdata.FormTestData import testdata


#@pytest.mark.usefixture("invoke")

from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_testcase1(self,invoke,getdata):
        log = self.test_log()
        #self.driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Hari simha")
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getdata)
        log.info("First name is "+getdata)
        homepage.getemail().send_keys("vuppralhari@gmail.com")
        homepage.getpassword().send_keys("Harisimha@96")
        #self.driver.find_element_by_xpath("//input[@name='email']").send_keys("vuppralhari@gmail.com")
        #self.driver.find_element_by_id("exampleInputPassword1").send_keys("Harisimha@96")
        homepage.markbutton().click()
        #self.driver.find_element_by_id("exampleCheck1").click()
        dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_visible_text("Female")
        self.driver.find_element_by_id("inlineRadio2").click()
        self.driver.find_element_by_name("bday").send_keys("19-09-1996")
        self.driver.find_element_by_class_name("btn-success").click()                   #click missing
        self.driver.refresh()
        log.warning("Raghu Prem is printing twice")
        textmatch = self.driver.current_url
        Text_title = self.driver.title
        assert ( "ProtoCommerce" in Text_title)
        assert ("https://rahulshettyacademy.com/angularpractice/" in textmatch)
    @pytest.fixture(params = testdata.T_data,)
    def getdata(self,request):
            return request.param

        #print(self.driver.find_element_by_class_name("alert").text)

            #Title =  self.driver.title





