from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    name = (By.XPATH,"/html/body/app-root/form-comp/div/form/div[1]/input")
    email = (By.XPATH,"//input[@name='email']")
    password = (By.ID,"exampleInputPassword1")
    button = (By.ID,"exampleCheck1")

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def markbutton(self):
        return self.driver.find_element(*HomePage.button)







