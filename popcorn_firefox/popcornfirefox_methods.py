import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import popcornfirefox_locators as locators
from selenium.webdriver.support.ui import Select  # this is for drop down lists
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, executable_path="C:\Automation\Python\Popcorn_project\geckodriver.exe")



def setUp():
    print(f'-----Launch {locators.app} website.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.popcorn_url)

    if driver.current_url == locators.popcorn_url and driver.title == locators.popcorn_home_page_title:
        print(f'-----Yey! {locators.app} website launched successfully!')
        print(f'-----{locators.app} homepage URL: {driver.current_url}, homepage title: {driver.title}')
        sleep(5)

    else:
        print(f'-----{locators.app} did not launched, check your code or application.')
        print(f'-----Current URL: {driver.current_url}, page title: {driver.title}')


def verify_homepage():
    if driver.current_url == locators.popcorn_url and driver.title == locators.popcorn_home_page_title:
        # check if 'A fresh approach for marketing & PR' is displayed
        assert driver.find_element(By.ID, 'slider-1-slide-1-layer-20').is_displayed()
        sleep(1)
        slider = driver.find_element(By.ID, 'slider-1-slide-1-layer-20').is_displayed()
        print(f'A fresh approach for marketing & PR is displayed: {slider}.')

        # check if LET'S CHAT button is working:
        driver.find_element(By.ID, 'slidebut').click()
        sleep(1)
        if driver.current_url == locators.contact_us_url and driver.title == locators.contact_us_title_page:
            print('You are now on the Contact us page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the Contact us page.')

        # check if 'OUR MISSION' is displayed:
        if driver.find_element(By.XPATH, '//h2[contains(.,"OUR MISSION")]').is_displayed():
            sleep(1)
            print('OUR MISSION is displayed.')
        else:
            print('OUR MISSION is not displayed.')

        # check if LEARN MORE button is working:
        driver.find_element(By.XPATH, '//span[contains(.,"LEARN MORE")]').click()
        sleep(1)
        if driver.current_url == locators.services_url and driver.title == locators.services_title_page:
            sleep(1)
            print('You are on the Services page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the Services page.')

        # check that 'Brands we work with' is displayed:
        assert driver.find_element(By.XPATH, '//h2[contains(., "Brands We Work With")]').is_displayed()
        sleep(1)
        brands = driver.find_element(By.XPATH, '//h2[contains(., "Brands We Work With")]').is_displayed()
        print(f'The brands are displayed on the page: {brands}.')

        # check that 'Case Studies' is displayed
        assert driver.find_element(By.XPATH, '//h2[contains(., "CASE STUDIES")]').is_displayed()
        sleep(1)
        case_studies = driver.find_element(By.XPATH, '//h2[contains(., "CASE STUDIES")]').is_displayed()
        print(f'Case studies are displayed: {case_studies}.')

        # click on Tourism Vancouver
        driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/portfolio/tourism-vancouver/"]'
                                      '//i[@class="gem-elegant arrow-right"]').click()
        sleep(1)
        if driver.current_url == locators.tourism_vancouver_url and driver.title == locators.tourism_vancouver_title_page:
            sleep(1)
            print('You are on the Tourism Vancouver page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the correct web page.')

        # click on Nest Design
        driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/portfolio/nest-designs/"]'
                                      '//i[@class="gem-elegant arrow-right"]').click()
        sleep(1)
        if driver.current_url == locators.nest_design_url and driver.title == locators.nest_design_title_page:
            sleep(1)
            print('You are on the Nest Design page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the correct web page.')

        # click on Skip the Dish
        driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/portfolio/just-eat/"]'
                                      '//i[@class="gem-elegant arrow-right"]').click()
        sleep(1)
        if driver.current_url == locators.skip_the_dish_url and driver.title == locators.skip_the_dish_title_page:
            sleep(1)
            print('You are on the Skip the Dish/Just Eat page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the correct web page.')

        # click on View all Cases
        driver.find_element(By.XPATH, '//span[contains(text(),"View All Case Studies")]').click()
        sleep(1)
        if driver.current_url == locators.case_studies_url and driver.title == locators.case_studies_title_page:
            sleep(1)
            print('You are on the Case Studies page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the correct web page.')

        # click on Canadian Workplace Culture Leader button and get back to Popcorn home page
        # driver.get(locators.popcorn_url)
        # oldtab = driver.current_window_handle
        # sleep(1)
        # driver.find_element(By.XPATH, '//img[@class="attachment-large size-large"]').click()
        # if driver.current_url == locators.canadian_workplace_url and driver.title == locators.canadian_workplace_title_page:
        #     sleep(1)
        #     #driver.switch_to_window(oldtab)
        #     driver.close()
        #     sleep(1)
        #     print('You are now on the Canadian Workplace Index page.')
        # else:
        #     print('Something is wrong, you are not back on Popcorn home page.')
        # driver.switch_to.window(driver.window_handles).close()
        # sleep(1)

        # click on Meet Our Team:
        driver.find_element(By.XPATH, '//span[contains(text(),"MEET OUR TEAM")]').click()
        sleep(1)
        if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
            sleep(1)
            print('You are on the Who We Are page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the correct web page.')

        # fill on contact form
        driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys(locators.full_name)
        sleep(1)
        driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys(locators.email)
        sleep(1)
        driver.find_element(By.XPATH, '//textarea[@placeholder="Message"]').send_keys(locators.subject)
        sleep(1)
        driver.find_element(By.XPATH, '//span[@class="checkbox-sign"]').click()
        sleep(1)
        driver.find_element(By.XPATH, '//input[@value="Submit"]').click()
        sleep(1)


def tearDown():
    if driver is not None:
        print('------------------------------------~*~------------------------------------------------')
        print(f'-----The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
verify_homepage()
tearDown()
