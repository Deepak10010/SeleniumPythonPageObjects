import pytest
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class Test_SignUp(BaseTest):

    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password",
                             dataProvider.get_data("LoginTest"))
    def test_doSignUp(self, name, phoneNum, email, country, city, username, password):
        log.logger.info("Test Do Sign up started")
        regPage = RegistrationPage(self.driver)
        regPage.fillForm(name, phoneNum, email, country, city, username, password)
        # log.logger.info("Entering name")
        # log.logger.info("Entering Phone Number")
        # log.logger.info("Entering Email")
        # log.logger.info("Entering Country")
        # log.logger.info("Entering city")
        # log.logger.info("Entering username")
        # log.logger.info("Entering password")
        log.logger.info("Test Do Sign up successfully executed")