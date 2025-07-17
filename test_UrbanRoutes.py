from UrbanRoutesLocators import LocatorsUrbanRoutes
from UrbanRoutesMethods import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import data

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)
        cls.locators = LocatorsUrbanRoutes

    #Test 1 poner las direcciones
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.paso_set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to
        print(address_from, address_to)
        self.routes_page.click_command_button()

#Test 2 seleccionar tarifa comfort
    def test_select_tariff_comfort(self):
        expected_price = '$10'
        self.routes_page.click_comfort_tariff()
        assert self.routes_page.get_tcard_price() in expected_price


 #Test 3 añador número de teléfono
    def test_add_phone_number(self):
        phone_number = data.phone_number
        self.routes_page.paso_add_phone_number(phone_number)
        assert self.routes_page.get_phone_number() == phone_number
        print(phone_number)

#Test 4 Añadir tarjeta
    def test_add_payment_method(self):
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.paso_add_payment_method(card_number,card_code)
        assert self.routes_page.get_pm_text() == 'Tarjeta'

#Test 5 Escribir algo al conductor
    def test_add_message_for_driver(self):
        message = data.message_for_driver
        self.routes_page.add_message_for_driver(message)
        assert self.routes_page.get_message_for_driver() == message

#Test 6 Pedir una manta y pañuelos
    def test_add_manta_y_panuelos(self):
        self.routes_page.paso_add_manta_y_panuelos()
        assert self.routes_page.get_slider_for_manta_y_panuelos() is True

#Test 7 Pedir manta y pañuelos
    def test_add_ice_cream(self):
        count = data.ice_cream_count
        self.routes_page.paso_add_ice_cream()
        assert self.routes_page.get_ice_cream_count() == count

#Test 9 Pedir el taxi
    def test_taxi_demanded(self):
        self.routes_page.paso_demand_taxi()
        expected_order_header_title = 'Buscar automóvil'
        order_header_title = self.routes_page.get_if_taxi_was_demanded()
        assert order_header_title == expected_order_header_title

#Test 10 OPCIONAL Ver si aparece el modal
    def test_check_order_info(self):
        order_header_title = 'Buscar automóvil'
        new_order_header_title = self.routes_page.get_order_info()
        assert new_order_header_title != order_header_title

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

