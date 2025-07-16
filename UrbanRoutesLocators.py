from selenium.webdriver.common.by import By

class LocatorsUrbanRoutes:
    #direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    command_button = (By.CSS_SELECTOR, '.button.round')

    #tarifa
    comfort_tariff = (By.XPATH, '//div[contains(@class, "tcard") and .//div[text()="Comfort"]]')
    tcard_price = (By.XPATH, '//div[@class="tcard-price" and contains(normalize-space(), "10")]')

    #telefono
    add_phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    phone_number_confirmation_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')

    #método de pago
    payment_method_button = (By.CLASS_NAME, 'pp-button filled')
    payment_method_text_card_or_cash = (By.CLASS_NAME, 'pp-value-text')
    add_card_button = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    input_card_number_field = (By.XPATH, '//div[@class="card-number-input"]//input')
    input_card_code_field = (By.XPATH, '//div[@class="card-code-input"]//input')
    confirmation_add_card_button = (By.XPATH, '//button[text()="Agregar" and contains(@class,"button")]')
    close_pm_button = (By.XPATH, '//button[contains(@class,"close-button")]')

    #mensaje para el conductor
    message_for_driver_field = (By.CLASS_NAME, 'input-container')

    #requisitos
    slider_manta_y_panuelos = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]/following-sibling::div//span[@class="slider round"]')
    manta_y_panuelos_checkbox = (By.CSS_SELECTOR, "input.switch-input")
    ice_cream_plus_button = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div//div[@class="counter-plus"]')
    ice_cream_counter = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div//div[@class="counter-value"]')

    #pedir taxi
    demand_taxi_button = (By.CLASS_NAME, 'smart-button')
    demand_taxi_modal = (By.CLASS_NAME, 'order shown')

    #modal
