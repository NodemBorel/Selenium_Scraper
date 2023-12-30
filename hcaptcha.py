import os
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def solvehCaptcha():
    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey='41b778e7-8f20-45cc-a804-1f1ebb45c579',
            url='https://2captcha.com/demo/hcaptcha',
        )

    except Exception as e:
        print(e)
        return False

    else:
        return result 
       

browser = webdriver.Firefox()
browser.get('https://2captcha.com/demo/hcaptcha')

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > main > div > section > form > div > div > div > iframe')))

result = solvehCaptcha()
#solvehCaptcha(url=browser.current_url)

if result:
    code = result['code']

    browser.execute_script("document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerHTML = " + "'" + code + "'")

    browser.find_element(By.CSS_SELECTOR, "#root > div > main > div > section > form > button._2iYm2u0v9LWjjsuiyfKsv4._1z3RdCK9ek3YQYwshGZNjf._3zBeuZ3zVV-s2YdppESngy._28oc7jlCOdc1KAtktSUZvQ").click()
