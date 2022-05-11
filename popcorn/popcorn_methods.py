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
    sleep(1)
    if kernel is not None:
        print(f'Kernel Korner is displayed: {kernel}.')
    else:
        print(f'Kernel Korner is not displayed: {kernel}.')

    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35333"]').click()
    sleep(1)
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
    sleep(2)

    element = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35358"]')
    driver.execute_script("arguments[0].scrollIntoView()", element)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35358"]').click()
    sleep(1)
    commitment = driver.find_element(By.XPATH, '//h1[contains(., "Popcorn’s Commitment to Serving Small Businesses")]').is_displayed()
    sleep(1)
    commitment_title= driver.find_element(By.XPATH, '//h1[contains(., "Popcorn’s Commitment to Serving Small Businesses")]')
    if commitment is not None:
        print('You are on the ', commitment_title.text, 'blog page.')
    else:
        print('You are not on the ', commitment_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(2)

    element1= driver.find_element(By.CSS_SELECTOR, 'article[id="post-35370"]')
    driver.execute_script("arguments[0].scrollIntoView()", element1)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35370"]').click()
    sleep(1)
    social = driver.find_element(By.XPATH, '//h1[contains(., "Which Social Media Platform Is Right for Me?")]').is_displayed()
    sleep(1)
    social_title = driver.find_element(By.XPATH, '//h1[contains(., "Which Social Media Platform Is Right for Me?")]')
    if social is not None:
        print('You are on the ', social_title.text, 'blog page.')
    else:
        print('You are not on the ', social_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(2)

    element2 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35377"]')
    driver.execute_script("arguments[0].scrollIntoView()", element2)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35377"]').click()
    sleep(1)
    happy = driver.find_element(By.XPATH, '//h1[contains(., "  Let’s Get Creative!")]').is_displayed()
    sleep(1)
    happy_title = driver.find_element(By.XPATH, '//h1[contains(., "  Let’s Get Creative!")]')
    if happy is not None:
        print('You are on the ', happy_title.text, 'blog page.')
    else:
        print('You are not on the ', happy_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(2)

    element3 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35383"]')
    driver.execute_script("arguments[0].scrollIntoView()", element3)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35383"] ').click()
    sleep(1)
    news = driver.find_element(By.XPATH, '//h1[contains(., "The News on Tues #7: TikTok Restrictions, PBN’s and Facebook Expansion")]').is_displayed()
    sleep(1)
    news_title = driver.find_element(By.XPATH, '//h1[contains(., "The News on Tues #7: TikTok Restrictions, PBN’s and Facebook Expansion")]')
    if news is not None:
        print('You are on the ', news_title.text, 'blog page.')
    else:
        print('You are not on the ', news_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(2)

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
    sleep(2)

    element5 = driver.find_element(By.CSS_SELECTOR, 'article[id="post-35414"]')
    driver.execute_script("arguments[0].scrollIntoView()", element5)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'article[id="post-35414"]').click()
    sleep(1)
    home = driver.find_element(By.XPATH,'//h1[contains(., "The News on Tues #5: Working from home, moving on from COVID, supporting SMB’s.")]').is_displayed()
    sleep(1)
    home_title = driver.find_element(By.XPATH,'//h1[contains(., "The News on Tues #5: Working from home, moving on from COVID, supporting SMB’s.")]')
    sleep(1)
    if home is not None:
        print('You are on the ', home_title.text, 'blog page.')
    else:
        print('You are not on the ', home_title.text, 'blog page.')

    driver.find_element(By.LINK_TEXT, 'BLOG').click()
    sleep(2)



def tearDown():
    if driver is not None:
        print('------------------------------------~*~------------------------------------------------')
        print(f'-----The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
#check_homepage()
#check_who_we_are()
check_blog()
#check_contact_us_page()
tearDown()