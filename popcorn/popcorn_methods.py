import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import popcorn_locators as locators
from selenium.webdriver.support.ui import Select  # this is for drop down lists
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)




def setUp():
    print(f'Test starts at {datetime.datetime.now()}.')
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

def check_homepage():
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


        #check if 'OUR MISSION' is displayed:
        if driver.find_element(By.XPATH, '//h2[contains(.,"OUR MISSION")]').is_displayed():
            sleep(1)
            print('OUR MISSION is displayed.')
        else:
            print('OUR MISSION is not displayed.')

        #check if LEARN MORE button is working:
        driver.find_element(By.XPATH, '//span[contains(.,"LEARN MORE")]').click()
        sleep(1)
        if driver.current_url == locators.services_url and driver.title == locators.services_title_page:
            sleep(1)
            print('You are on the Services page.')
            driver.find_element(By.XPATH, '//a[contains(., "Home")]').click()
            sleep(1)
        else:
            print('Something is wrong, you are not on the Services page.')

        #check that 'Brands we work with' is displayed:
        assert driver.find_element(By.XPATH, '//h2[contains(., "Brands We Work With")]').is_displayed()
        sleep(1)
        brands = driver.find_element(By.XPATH, '//h2[contains(., "Brands We Work With")]').is_displayed()
        print(f'The brands are displayed on the page: {brands}.')

        # check that 'Case Studies' is displayed
        assert driver.find_element(By.XPATH, '//h2[contains(., "CASE STUDIES")]').is_displayed()
        sleep(1)
        case_studies = driver.find_element(By.XPATH, '//h2[contains(., "CASE STUDIES")]').is_displayed()
        print(f'Case studies are displayed: {case_studies}.')

        #click on Tourism Vancouver
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

        #click on Skip the Dish
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

        #click on Canadian Workplace Culture Leader button and get back to Popcorn home page
        #driver.get(locators.popcorn_url)
        #oldtab = driver.current_window_handle
        #sleep(1)
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



        #fill on contact form
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
    else:
        print('Something is wrong.')


def check_who_we_are():
    driver.get(locators.who_we_are_url)
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        print('You are on the Who We Are page.')
    else:
        print('You are not on the Who We Are page.')

    #click on each team member and verify if their home page is opening
    driver.find_element(By.XPATH, '//a[normalize-space()="Dennis Pang"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Dennis Pang page.')
    else:
        print('Something is wrong, you are not on Dennis Pang page.')
    #click on 'Team page' button
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Shaan Coelho
    driver.find_element(By.XPATH, '//a[normalize-space()="Shaan Coelho"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Shaan Coelho page.')
    else:
        print('Something is wrong, you are not on Shaan Coelho page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Alexander Leung
    driver.find_element(By.XPATH, '//a[normalize-space()="Alexander Leung"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Alexander Leung page.')
    else:
        print('Something is wrong, you are not on Alexander Leung page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Jaydene Govender
    driver.find_element(By.XPATH, '//a[normalize-space()="Jaydene Govender"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Jaydene Govender page.')
    else:
        print('Something is wrong, you are not on Jaydene Govender page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Goda Linkute
    driver.find_element(By.XPATH, '//a[normalize-space()="Goda Linkute"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Goda Linkute page.')
    else:
        print('Something is wrong, you are not on Goda Linkute page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Widya Sulistiani
    driver.find_element(By.XPATH, '//a[normalize-space()="Widya Sulistiani"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Widya Sulistiani page.')
    else:
        print('Something is wrong, you are not on Widya Sulistiani page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Brigitta Arthamevia
    driver.find_element(By.XPATH, '//a[normalize-space()="Brigitta Arthamevia"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Brigitta Arthamevia page.')
    else:
        print('Something is wrong, you are not on Brigitta Arthamevia page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Erick Alvergue
    driver.find_element(By.XPATH, '//a[normalize-space()="Erick Alvergue"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Erick Alvergue page.')
    else:
        print('Something is wrong, you are not on Erick Alvergue page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #check Karen Li
    driver.find_element(By.XPATH, '//a[normalize-space()="Karen Li"]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').is_displayed():
        sleep(1)
        print('You are on Karen Li page.')
    else:
        print('Something is wrong, you are not on Karen Li page.')
    driver.find_element(By.XPATH, '//span[contains(text(),"TEAM PAGE")]').click()
    sleep(1)
    if driver.current_url == locators.who_we_are_url and driver.title == locators.who_we_are_title_page:
        sleep(1)
        print('You are back on the Teams page.')
    else:
        print('Something is wrong, you are not the Teams page.')

    #click 'Let's work together'
    driver.find_element(By.XPATH, '//span[@class="elementor-button-text"]').click()
    sleep(1)


def check_contact_us_page():
    driver.get(locators.popcorn_url)
    sleep(1)
    driver.find_element(By.XPATH, '//a[normalize-space()="Contact Us"]').click()
    sleep(1)

    #assert Contact Us is displayed
    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    contact = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    if contact is not None:
        print(f'Contact us is displayed: {contact}. ')
    else:
        print(f'Contact us is not displayed: {contact}.')

    #start filling out the form
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

def verify_service_page():
    driver.get(locators.popcorn_service_url)
    sleep(1)
    if driver.current_url == locators.popcorn_service_url and driver.title == locators.popcorn_service_title:
        print(f'----- We are in Service Page!!!!')
        print(f'-----{locators.app} Service page url: {driver.current_url}, homepage title: {driver.title}')
    else:
        print(f'----{locators.app} Service page, did not displayed.')
        sleep(1)

    assert driver.find_element(By.XPATH, '//h2[normalize-space()="STRATEGY & CONSULTING"]').is_displayed()
    strategy = driver.find_element(By.XPATH, '//h2[normalize-space()="STRATEGY & CONSULTING"]').is_displayed()
    print(f' Strategy and Consulting is displayed:{strategy}')
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"LEARN MORE")]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/social-media-marketing/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/digital-marketing/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/influencer-marketing/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/content-creation/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)

    assert driver.find_element(By.XPATH, '//h2[normalize-space()="PUBLIC RELATIONS"]').is_displayed()
    pr = driver.find_element(By.XPATH, '//h2[normalize-space()="PUBLIC RELATIONS"]').is_displayed()
    print(f' PUBLIC RELATIONS is displayed:{pr}')
    sleep(1)

    driver.find_element(By.XPATH, '//a[@href="https://www.gopopcorn.ca/public-relations/"]'
                                  '//span[@class="elementor-button-content-wrapper"]'
                                  '//span[@class="elementor-button-text"][normalize-space()="LEARN MORE"]').click()
    sleep(1)
    # Back to service page
    driver.find_element(By.XPATH, '//a[normalize-space()="Services"]').click()
    sleep(1)

    # assert is used to check Elements is displayed and its TRUE!
    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xl"]').is_displayed()
    hwcwt = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xl"]').is_displayed()
    print(f'HOW CAN WE WORK TOGETHER is displayed: {hwcwt}')
    sleep(1)
    print(f'All the service page Elements is clickable')
    sleep(1)



def jobs_page():
    driver.get(locators.popcorn_jobs_url)
    sleep(1)
    if driver.current_url == locators.popcorn_jobs_url and driver.title == locators.popcorn_jobs_title:
        print(f'----- We are in Jobs Page!!!!')
        print(f'-----{locators.app} Jobs page url: {driver.current_url}, Jobs title: {driver.title}')
    else:
        print(f'----{locators.app} Jobs page, did not displayed.')
        sleep(1)

    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    jobs = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    print(f' JOBS page is displayed: {jobs}')
    sleep(1)

    driver.find_element(By.XPATH, '//h3[normalize-space()="Account Executive"]').click()
    sleep(1)
    if driver.current_url == locators.popcorn_jobs_account_executive_url and driver.title == locators.popcorn_jobs_account_executive_title:
        sleep(3)
        print(f'You are in Account Executive page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Jobs"]').click()
        sleep(1)
    else:
        print(f'Something is wrong you are not is correct web page')

    driver.find_element(By.XPATH, '//strong[normalize-space()="Load more listings"]').click()
    sleep(2)

    driver.find_element(By.XPATH, '//h3[normalize-space()="Account Associate"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[normalize-space()="Jobs"]').click()
    sleep(3)


def case_studies():
    driver.get(locators.popcorn_case_studies_url)
    if driver.current_url == locators.popcorn_case_studies_url and driver.title == locators.popcorn_case_studies_title:
        sleep(3)
        print(f'CASE STUDIES page is displayed')
        print(f'{locators.app} Case Studies url {locators.popcorn_case_studies_url}, Case studies {locators.popcorn_case_studies_title}')
    else:
        print(f'Something went wrong')
        sleep(1)

    assert driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    CS = driver.find_element(By.XPATH, '//h2[@class="elementor-heading-title elementor-size-xxl"]').is_displayed()
    print(f'Case Studies page is displayed: {CS}')
    sleep(1)

    assert driver.find_element(By.XPATH, '//h2[normalize-space()="Here are a few examples of our work:"]').is_displayed()
    workexamples = driver.find_element(By.XPATH, '//h2[normalize-space()="Here are a few examples of our work:"]').is_displayed()
    print(f'Here are a few examples of our work title is displayed: {workexamples}')
    sleep(1)

    # Skype footware
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                     '//h3[@class="elementor-portfolio-item__title"][normalize-space()="SKYE Footwear"]').click()
    if driver.current_url == locators.popcorn_portfolio_skye_footware_url and driver.title == locators.popcorn_portfolio_skye_footware_title:
        print(f'You are in Skype Footware Page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # NETGEAR
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Netgear"]').click()
    if driver.current_url == locators.popcorn_portfolio_netgear_url and driver.title == locators.popcorn_portfolio_netgear_title:
        print(f'You are in Netgear page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # SAMSUNG
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Samsung"]').click()
    if driver.current_url == locators.popcorn_portfolio_samsung_url and driver.title == locators.popcorn_portfolio_samsung_title:
        print(f'Your are in SAMSUNG page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # NEST DESIGNS
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Nest Designs"]').click()
    if driver.current_url == locators.popcorn_portfolio_nest_design_url and driver.title == locators.popcorn_portfolio_nest_design_title:
        print(f'Your are in NEST DESIGN page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # Michael Hill Jewellery
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                      '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Michael Hill Jeweller"]').click()
    if driver.current_url == locators.popcorn_portfolio_michaelhilljewel_url and driver.title == locators.popcorn_portfolio_michaelhilljewel_title:
        print(f'Your are in MICHAEL HILL JEWELLERY page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # JUST EAT
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Just Eat (Skip The Dishes)"]').click()
    if driver.current_url == locators.popcorn_portfolio_justeat_url and driver.title == locators.popcorn_portfolio_justeat_title:
        print(f'Your are in JUST EAT (SKIP THE DISH) page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # PURDY CHOCOLATIER
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Purdys Chocolatier"]').click()
    if driver.current_url == locators.popcorn_portfolio_purdy_url and driver.title == locators.popcorn_portfolio_purdy_title:
        print(f'Your are in PURDY CHOCOLATIER page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # TOURISUM VANCOUVER
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Tourism Vancouver"]').click()
    if driver.current_url == locators.popcorn_portfolio_tourisum_vancouver_url and driver.title == locators.popcorn_portfolio_tourisum_vancouver_title:
        print(f'Your are in TOURISUM VANCOUVER page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # BETTER THAN BOUILLON
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Better Than Bouillon"]').click()
    if driver.current_url == locators.popcorn_portfolio_better_than_bouillon_url and driver.title == locators.popcorn_portfolio_better_than_bouillon_title:
        print(f'Your are in BETTER THAN BOUILLON page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # SHANGRI-LA HOTEL
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Shangri-La Hotel"]').click()
    if driver.current_url == locators.popcorn_portfolio_shangri_la_hotel_url and driver.title == locators.popcorn_portfolio_shangri_la_hotel_title:
        print(f'Your are in SHANGRI-LA HOTEL page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # VIRTUOUS PIE
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Virtuous Pie"]').click()
    if driver.current_url == locators.popcorn_portfolio_virtuous_pie_url and driver.title == locators.popcorn_portfolio_virtuous_pie_title:
        print(f'Your are in VIRTUOUS PIE page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    # Canadian Federation of Independent Grocers - Popcorn
    driver.find_element(By.XPATH, '//div[@class="elementor-portfolio elementor-grid elementor-posts-container elementor-posts-masonry"]'
                                  '//h3[@class="elementor-portfolio-item__title"][normalize-space()="Canadian Federation of Independent Grocers"]').click()
    if driver.current_url == locators.popcorn_portfolio_CFOIG_url and driver.title == locators.popcorn_portfolio_CFOIG_title:
        print(f'Your are in Canadian Federation of Independent Grocers - Popcorn page')
        driver.find_element(By.XPATH, '//a[normalize-space()="Case Studies"]').click()
    else:
        print(f'Something is wrong check your code')
        sleep(1)

    driver.find_element(By.XPATH, '//span[@class="elementor-button-text"]').click()
    sleep(1)



def check_blog():
    driver.get(locators.popcorn_url)
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    print(driver.title)
    sleep(3)

    # first_article = driver.find_element(By.CLASS_NAME, 'firstp')
    # print('PUTTING PEOPLE FIRST AT POPCORN:', first_article.text) # it's gives you the text from the article
    # sleep(1)
    #check if Kernel Korner is displayed
    kernel = driver.find_element(By.XPATH, '//h2[contains(., "Kernels Korner")]').is_displayed()
    sleep(2)
    if kernel is not None:
        print(f'Kernel Korner is displayed: {kernel}.')
    else:
        print(f'Kernel Korner is not displayed: {kernel}.')

    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35333"]').click()
    sleep(5)
    # driver.find_element(By.XPATH, '//span[contains(., "Read More")]').click()
    # sleep(1)
    people = driver.find_element(By.XPATH, '//h1[contains(., " Putting People First at Popcorn")]').is_displayed()
    sleep(1)
    people_title = driver.find_element(By.XPATH, '//h1[contains(., " Putting People First at Popcorn")]')
    sleep(1)
    if people is not None:
        print(f'You are on the ', people_title.text, 'blog page.')
    else:
        print(f'You are not on the ', people_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)

    element = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35358"]')
    driver.execute_script("arguments[0].scrollIntoView()", element)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35358"]').click()
    sleep(3)
    commitment = driver.find_element(By.XPATH, '//h1[contains(., "Popcorn’s Commitment to Serving Small Businesses")]').is_displayed()
    sleep(1)
    commitment_title= driver.find_element(By.XPATH, '//h1[contains(., "Popcorn’s Commitment to Serving Small Businesses")]')
    if commitment is not None:
        print('You are on the ', commitment_title.text, 'blog page.')
    else:
        print('You are not on the ', commitment_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)

    element1= driver.find_element(By.CSS_SELECTOR, 'article[id="post-35370"]')
    driver.execute_script("arguments[0].scrollIntoView()", element1)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35370"]').click()
    sleep(3)
    social = driver.find_element(By.XPATH, '//h1[contains(., "Which Social Media Platform Is Right for Me?")]').is_displayed()
    sleep(1)
    social_title = driver.find_element(By.XPATH, '//h1[contains(., "Which Social Media Platform Is Right for Me?")]')
    if social is not None:
        print('You are on the ', social_title.text, 'blog page.')
    else:
        print('You are not on the ', social_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)

    element2 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35377"]')
    driver.execute_script("arguments[0].scrollIntoView()", element2)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35377"]').click()
    sleep(3)
    happy = driver.find_element(By.XPATH, '//h1[contains(., "  Let’s Get Creative!")]').is_displayed()
    sleep(1)
    happy_title = driver.find_element(By.XPATH, '//h1[contains(., "  Let’s Get Creative!")]')
    if happy is not None:
        print('You are on the ', happy_title.text, 'blog page.')
    else:
        print('You are not on the ', happy_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)

    element3 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35383"]')
    driver.execute_script("arguments[0].scrollIntoView()", element3)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35383"] ').click()
    sleep(3)
    news = driver.find_element(By.XPATH, '//h1[contains(., "The News on Tues #7: TikTok Restrictions, PBN’s and Facebook Expansion")]').is_displayed()
    sleep(1)
    news_title = driver.find_element(By.XPATH, '//h1[contains(., "The News on Tues #7: TikTok Restrictions, PBN’s and Facebook Expansion")]')
    if news is not None:
        print('You are on the ', news_title.text, 'blog page.')
    else:
        print('You are not on the ', news_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)

    element4 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35405"]')
    driver.execute_script("arguments[0].scrollIntoView()", element4)
    sleep(2)
    driver.find_element(By.XPATH, '//article[@id="post-35405"]//span[@class="gem-text-button"][normalize-space()="Read More"]').click()
    sleep(3)
    news2 = driver.find_element(By.XPATH, '//h1[contains(., "The News on Tues #6: A TikTok Uptick, Google Skills and New Reviews!")]').is_displayed()
    sleep(1)
    news2_title = driver.find_element(By.XPATH, '//h1[contains(., "The News on Tues #6: A TikTok Uptick, Google Skills and New Reviews!")]')
    if news2 is not None:
        print('You are on the ', news2_title.text, 'blog page.')
    else:
        print('You are not on the ', news2_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)

    element5 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35414"]')
    driver.execute_script("arguments[0].scrollIntoView()", element5)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35414"]').click()
    sleep(3)
    home = driver.find_element(By.XPATH,'//h1[contains(., "The News on Tues #5: Working from home, moving on from COVID, supporting SMB’s.")]').is_displayed()
    sleep(1)
    home_title = driver.find_element(By.XPATH,'//h1[contains(., "The News on Tues #5: Working from home, moving on from COVID, supporting SMB’s.")]')
    sleep(1)
    if home is not None:
        print('You are on the ', home_title.text, 'blog page.')
    else:
        print('You are not on the ', home_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(3)



def tearDown():
    if driver is not None:
        print('------------------------------------~*~------------------------------------------------')
        print(f'-----The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# setUp()
# check_homepage()
# check_who_we_are()
# verify_service_page()
# case_studies()
# jobs_page()
#check_blog()
# check_contact_us_page()
#tearDown()