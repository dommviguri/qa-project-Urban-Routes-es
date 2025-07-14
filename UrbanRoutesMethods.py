from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from UrbanRoutesLocators import LocatorsUrbanRoutes
from data import phone_number, card_number, card_code, message_for_driver
from selenium.webdriver.common.keys import Keys
import main
import helpers


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorsUrbanRoutes


# añadir las direcciones
    ###ejemplo
    def set_from(self, from_address):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(*self.locators.from_field))
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')


# click command_button

    def click_command_button(self):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(*self.locators.command_button)
        self.driver.find_element(*self.locators.command_button).click()

# escoger tarifa comfort
    def click_comfort_tariff(self):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(*self.locators.comfort_tariff)
        self.driver.find_element(*self.locators.comfort_tariff).click()
    def get_tcard_4_active(self):
        return self.driver.find_element(*self.locators.tcard_4).get_attribute('class')

# añadir número de teléfono
    def click_add_phone_number_button(self):
        self.driver.find_element(*self.locators.add_phone_number_button).click()
    def click_add_phone_number_field(self):
        self.driver.fiend_element(*self.locators.phone_number_field).click()
    def add_phone_number(self):
        self.driver.find_element(*self.locators.phone_number_field).send_keys(phone_number)
    def click_somewhere_else(self):
        self.driver.fiend_element(*self.locators.phone_number_field).Keys.RETURN
    # poner el código de verificación
    # retrieve_phone_code
    # click en 'confirmar'
    def click_phone_number_confirmation_button(self):
        self.driver.find_element(*self.locators.phone_number_confirmation_button).click()
    def get_phone_number(self):
        added_phone_number = self.driver.find_element(*self.locators.phone_number_field)
        return added_phone_number.text

#añadir método de pago
    # click en metodo de pago
    def click_payment_method(self):
        self.driver.find_element(*self.locators.payment_method_button).click()
    #click en agregar tarjeta
    def click_add_card_1(self):
        self.driver.find_element(*self.locators.add_card_button).click()
    #añadir número de tarjeta
    def input_card_number(self):
        self.driver.find_element(*self.locators.input_card_number_field).click().send_keys(card_number)
    #añadir CVV
    def input_card_code(self):
        self.driver.find_element(*self.locators.input_card_code_field).send_keys(card_code)
    #click en agregar
    def click_add_card_2(self):
        self.driver.find_element(*self.locators.confirmation_add_card_button).click()
    #close payment method window
    def click_close_pm_button(self):
        self.driver.find_element(*self.locators.close_pm_button).click()
    #para el assert
    def get_pm_text(self):
        pm_text = self.driver.find_element(*self.locators.payment_method_text_card_or_cash)
        return pm_text.text

#añadir mensaje para el conductor
    def add_message_for_driver(self):
        self.driver.find_element(*self.locators.message_for_driver_field).send_keys(message_for_driver)
    #para el assert
    def get_message_for_driver(self):
        message_for_driver = self.driver.find_element(*self.locators.message_for_driver_field)
        return message_for_driver.text

#Requisitos del pedido
    #click en slider manta y pañuelos
    def click_slider_for_manta_y_panuelos(self):
        self.driver.find_element(*self.locators.slider_manta_y_panuelos).click()
    #para el assert
    def get_slider_for_manta_y_panuelos(self):
        checkbox_manta_y_panuelos = self.driver.find_element(*self.locators.manta_y_panuelos_checkbox)
        if checkbox_manta_y_panuelos.is_selected():
            print("El switch está ACTIVADO")
        else:
            print("El switch está DESACTIVADO")

    #añadir dos helados
    def click_ice_cream_plus_button(self):
        self.driver.find_element(*self.locators.ice_cream_plus_button.click()
    #para el assert
    def get_ice_cream_count(self):
        ice_cream_count = self.driver.find_element(*self.locators.ice_cream_counter)
        return ice_cream_count.text
#pedir taxi
    def click_demand_taxi(self):
        self.driver.find_element(*self.locators.demand_taxi_button).click()
    def get_if_taxi_was_demanded(self):
        modal = self.driver.find_element(*self.locators.demand_taxi_modal)
        return modal.text

####PASOS####

#añadir direcciones y empezar a pedir un taxi
def add_directions(self, addres_from, address_to):
    self.add_from(addres_from)
    self.add_to(address_to)
    self.click_command_button()

#escoger tarifa
def active_tariff()
    self.click_comfort_tariff()
    self.get_tcard_4_active()

#add phone number
def add_phone_number(self,phone_number, driver):
    self.click_phone_number_field()
    self.add_phone_number(phone_number)
    self.click_somewhere_else()
    self.retrieve_phone_code(driver)
    self.click_phone_number_confirmation_button()
    self.get_phone_number()

#add payment method
def add_payment_method(self, card_number, card_code):
    self.click_payment_method()
    self.click_add_card_1()
    self.input_card_number(card_number)
    self.input_card_code(card_code)
    self.click_add_card_2()
    self.click_close_pm_button()
    self.get_pm_text()

#mensaje para el conductor
def add_message_for_driver(self, message_for_driver)
    self.add_message_for_driver(message_for_driver)
    self.get_message_for_driver()

#manta y panuelos
def add_manta_y_panuelos(self):
    self.click_slider_for_manta_y_panuelos()
    self.get_slider_for_manta_y_panuelos()

#helados
def add_ice_cream(self):
    self.click_ice_cream_plus_button()
    self.get_ice_cream_count()

#pedir el taxi
def demand_taxi(self):
    self.click_demand_taxi()
    self.get_if_taxi_was_demanded()
