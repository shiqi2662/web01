from selenium.webdriver.support.wait import WebDriverWait



class Base:

    def __init__(self,driver):

        self.driver = driver

    def find_base(self, loc, timeout=10, poll=0.5):

        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).\
            until(lambda d: d.find_element(*loc))

    def click_base(self, loc):

        self.find_base(loc).click()

    def input_base(self, loc, data):

        kt = self.find_base(loc)
        kt.clear()
        kt.send_keys(data)



