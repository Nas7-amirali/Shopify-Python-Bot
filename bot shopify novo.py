#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:24:51 2019

@author: nasser7
"""

from selenium import webdriver

import requests
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#check stock code
def availabilitycheck():
    


    r = requests.get('https://pampamlondon.com/products.json')
    products = json.loads((r.text))['products']
        
    for product in products:
            #print(product['title'])
            productname = product['title']
            
            if productname== 'adidas Originals Track Pants - Ash Pearl':
                print(productname)
                #producturl = 'https://pampamlondon.com/products/adidasoriginalstrackpants-ashpearl'
                producturl = 'https://pampamlondon.com/products/' + product['handle']
                print(producturl)
            return producturl
   
        


#open chrome
driver = webdriver.Chrome(executable_path=r'/Applications/chromedriver') 
#link opened in chrome
driver.get('https://pampamlondon.com/products/vansuaogoldskool-suedecanvasblacktruewhite?variant=32425282764849')
#once product page loads up the size gets chosen 
driver.find_element_by_xpath('//div[@data-value="UK7"]').click()
#adds to cart
driver.find_element_by_xpath('//input[@name="add"]').click()
time.sleep(5) #4 seconds to let the page fully load, could go lower
#clicks the proceed to checkout button
driver.find_element_by_xpath('//input[@type="submit"][@name="checkout"][@value="Proceed to Checkout"][@class="btn"]').click()


#at the checkout page#
#auto fill personal details
time.sleep(5)
driver.find_element_by_xpath('//input[@placeholder="Email"][@autocomplete="shipping email"][@data-backup="customer_email"]').send_keys("ressanamirali@gmail.com")
driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys("Nasser")
driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys("Amirali")
driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys("Rua da Liberdade, 123, A das Lebres")
driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys("Lisbon")
driver.find_element_by_xpath('//input[@placeholder="Postal code"]').send_keys("2660-181")
driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys("932980054" + u"\ue007")
#last part added is to press enter"
time.sleep(7)
driver.find_element_by_xpath('//button[@name="button"][@type="submit"][@id="continue_button"]').click()

#credit card page
time.sleep(3)

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]'))
driver.find_element_by_xpath('//input[@placeholder="Card number"]').send_keys('1234123412341234')
driver.switch_to.default_content()


driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]'))
driver.find_element_by_xpath('//input[@placeholder="Name on card"]').send_keys('Nasser Amirali')
driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"][@id="card-fields-expiry-42sg5uv979j00000"]'))
driver.find_element_by_xpath('//input[@placeholder="placeholder="Expiration date (MM / YY)""]').send_keys('041998')
driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"][@id="card-fields-verification_value-qussvb4u5e000000"]'))
driver.find_element_by_xpath('//input[@placeholder="placeholder="Security code""]').send_keys('123')
driver.switch_to.default_content()
