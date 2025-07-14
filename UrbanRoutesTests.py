from selenium import webdriver

import data
form UrbanRoutesMethods import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(urban_routes_url)
        cls.routes_page = UrbanRoutesPage

        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
            capabilities = DesiredCapabilities.CHROME
            capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
            cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
#este no tiene init?

#Test 1. ingresar direcciones
    def test_set_route(self):
            address_from = data.address_from
            address_to = data.address_to
            self.routes_page.set_route(address_from, address_to)
            assert self.routes_page.get_from() == address_from
            assert self.routes_page.get_to() == address_to

#Test 2 seleccionar tarifa comfort
        def test_select_tariff_comfort(self):
            #cómo hago un assert de esto xd
            self.routes_page = UrbanRoutesPage(self.driver)
            self.routes_page.active_tariff()
            assert

 #Test 3 añador número de teléfono
        def test_add_phone_number(self):
            phone_number = data.phone_number
            self.routes_page.add_phone_number(phone_number, driver) #aquí no sé exactamente por qué meter el driver, porque lo requiere como atributo retrieve phone code
            assert self.routes_page.get_phone_number() == phone_number

#Test 4 Añadir tarjeta
        def test_add_payment_method(self):
            card_number = data.card_number
            card_code = data.card_code
            self.routes_page.add_payment_method(card_number,card_code)
            assert self.routes_page.get_pm_text() == 'Tarjeta'

#Test 5 Escribir algo al conductor
        def test_add_message_for_driver(self):
            message_for_driver = data.message_for_driver
            self.routes_page.add_message_for_driver(message_for_driver)
            assert self.routes_page.add_message_for_driver() == message_for_driver

#Test 6 Pedir una manta y pañuelos
        def test_add_manta_y_panuelos(self):
            self.routes_page.add_manta_y_panuelos()
            assert self.routes_page.get_slider_for_manta_y_panuelos() == True

#Test 7 Pedir manta y pañuelos
        def test_add_ice_cream(self):
            ice_cream_count = data.ice_cream_count
            self.routes_page.add_ice_cream()
            assert self.routes_page.get_ice_cream_count() == ice_cream_count

#Test 9 Pedir el taxi
        def test_taxi_demanded(self):
            self.routes_page.demand_taxi()
            assert self.routes_page.get_if_taxi_was_demanded() == 'order shown'

#Test 10 Ver si aparece el modal



        @classmethod
        def teardown_class(cls):
            cls.driver.quit()

