from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get("https://openedu.ru/")
    time.sleep(10)
    # driver.switch_to.frame("banner")
    driver.implicitly_wait(10)
    elem = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/a[1]")
    elem.click()
    print('1')
    time.sleep(10)
    
    driver.close()

if __name__=='__main__':
    main()