from browser import Browser
import time

class HeaderPageEelements():
    INPUT_BUSCA = '#id-search-field'
    CLICK_BTN = '#submit'


class HeaderPage(Browser):
    def preenche_input_busca(self, texto):
        self.driver.find_element_by_css_selector(HeaderPageEelements.INPUT_BUSCA).send_keys(texto)
        time.sleep(5)

    def click_btn_go(self):
        self.driver.find_element_by_css_selector(HeaderPageEelements.CLICK_BTN).click()
        time.sleep(5)

