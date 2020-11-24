from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains


class TestAlert:
    def test_alert(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(3)
        self.dr.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.dr.switch_to_frame("iframeResult")

        drag = self.dr.find_element_by_id("draggable")
        drop = self.dr.find_element_by_id("droppable")
        ac = ActionChains(self.dr)
        ac.drag_and_drop(drag, drop)
        ac.perform()
        self.dr.switch_to_alert().accept()
        sleep(2)
        self.dr.switch_to_default_content()
        self.dr.find_element_by_id("submitBTN").click()
        sleep(1)
        self.dr.quit()
