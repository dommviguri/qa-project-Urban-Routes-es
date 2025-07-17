from selenium.webdriver.support.expected_conditions import visibility_of_element_located

import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
from UrbanRoutesLocators import LocatorsUrbanRoutes

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorsUrbanRoutes

# SET ROUTE
    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.from_field))
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)
    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)
    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')
    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    #Paso
    def paso_set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

# click command_button
    def click_command_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.command_button))
        self.driver.find_element(*self.locators.command_button).click()

# TARIFA
    def click_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.comfort_tariff))
        self.driver.find_element(*self.locators.comfort_tariff).click()
    def get_tcard_price(self):
        return self.driver.find_element(*self.locators.tcard_price).text


# TELEFONO
    def click_add_phone_number_button(self):
        self.driver.find_element(*self.locators.add_phone_number_button).click()
    def add_phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.phone_number_field))
        self.driver.find_element(*self.locators.phone_number_field).send_keys(phone_number)
        self.driver.find_element(*self.locators.phone_number_field).send_keys(Keys.RETURN)
    def add_verification_code(self):
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.locators.phone_number_code_field).send_keys(phone_code)
    def click_phone_number_confirmation_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.phone_number_confirmation_button))
        self.driver.find_element(*self.locators.phone_number_confirmation_button).click()
    def get_phone_number(self):
        return self.driver.find_element(*self.locators.phone_number_field).get_property('value')

    #paso
    def paso_add_phone_number(self, phone_number):
        self.click_add_phone_number_button()
        self.add_phone_number(phone_number)
        self.add_verification_code()
        self.click_phone_number_confirmation_button()
        return self.get_phone_number()

# MÉTODO DE PAGO
    # click en metodo de pago
    def click_payment_method(self):
        self.driver.find_element(*self.locators.payment_method_button).click()
    #click en agregar tarjeta
    def click_add_card_1(self):
        self.driver.find_element(*self.locators.add_card_button).click()
    #añadir número de tarjeta
    def input_card_number(self,card_number):
        card_input = (self.driver.find_element(*self.locators.input_card_number_field))
        card_input.click()
        card_input.send_keys(card_number)
    #añadir CVV
    def input_card_code(self,card_code):
        self.driver.find_element(*self.locators.input_card_code_field).send_keys(card_code)
    #click en agregar
    def click_add_card_2(self):
        self.driver.find_element(*self.locators.confirmation_add_card_button).click()
    #close payment method window
    def click_close_pm_button(self):
        self.driver.find_element(*self.locators.close_pm_button).click()
    #para el assert
    def get_pm_text(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.locators.payment_method_text_card_or_cash))
        pm_text = self.driver.find_element(*self.locators.payment_method_text_card_or_cash)
        return pm_text.text

    #paso
    def paso_add_payment_method(self, card_number, card_code):
        self.click_payment_method()
        self.click_add_card_1()
        self.input_card_number(card_number)
        self.input_card_code(card_code)
        self.click_add_card_2()
        self.click_close_pm_button()
        self.get_pm_text()

#añadir mensaje para el conductor
    def add_message_for_driver(self, message):
        self.driver.find_element(*self.locators.message_for_driver_field).send_keys(message)
    #para el assert
    def get_message_for_driver(self):
        return self.driver.find_element(*self.locators.message_for_driver_field).get_attribute('value')
    #paso
    def paso_add_message_for_driver(self, message_for_driver):
        self.add_message_for_driver(message_for_driver)
        self.get_message_for_driver()

#Requisitos del pedido
    #click en slider manta y pañuelos
    def click_slider_for_manta_y_panuelos(self):
        self.driver.find_element(*self.locators.slider_manta_y_panuelos).click()
    #para el assert
    def get_slider_for_manta_y_panuelos(self):
        return self.driver.find_element(*self.locators.manta_y_panuelos_checkbox).is_selected()

    #paso
    def paso_add_manta_y_panuelos(self):
        self.click_slider_for_manta_y_panuelos()
        self.get_slider_for_manta_y_panuelos()

    #añadir dos helados
    def click_ice_cream_plus_button(self):
        self.driver.find_element(*self.locators.ice_cream_plus_button).click()
    #para el assert
    def get_ice_cream_count(self):
        ice_cream_count = self.driver.find_element(*self.locators.ice_cream_counter)
        return ice_cream_count.text

    #paso
    def paso_add_ice_cream(self):
        self.click_ice_cream_plus_button()
        self.click_ice_cream_plus_button()
        WebDriverWait(self.driver, 3)
        self.get_ice_cream_count()

#pedir taxi
    def click_demand_taxi(self):
        self.driver.find_element(*self.locators.demand_taxi_button).click()
    def get_if_taxi_was_demanded(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.order_body))
        return self.driver.find_element(*self.locators.order_header_title).text

    #paso
    def paso_demand_taxi(self):
        self.click_demand_taxi()
        self.get_if_taxi_was_demanded()

#Ver la información de la orden
    def get_order_info(self):
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(self.locators.order_number))
        return self.driver.find_element(*self.locators.order_header_title).text