from selenium.webdriver import ActionChains
from selenium import webdriver
import time


while(True):
    print("Started Running")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome("./chromedriver.exe")

    message_text = '''Hey



    Thanks for backing our project.

    Please click on the link below to add compute modules and accessories info and help us build a better product:



    https://turingpi.com/add-accessories/



    Thanks,

    The Turing Pi Team'''

    url = "https://www.kickstarter.com/projects/turingpi/turing-pi-cluster-board/backers/report/index"

    driver.maximize_window()

    driver.get(url)

    time.sleep(2)

    '''authentication'''
    email = driver.find_element_by_id("user_session_email")
    email.clear()
    email.send_keys("stan@turingpi.com")

    password = driver.find_element_by_id("user_session_password")
    password.clear()
    password.send_keys("sujhen-vijhaf-Zugmu2")

    button = driver.find_element_by_name("commit")
    button.click()

    time.sleep(10)

    '''making agreements'''
    try:
        checkbox = driver.find_element_by_id("agreement-0")
        actions = ActionChains(driver)
        actions.move_to_element(checkbox).click().perform()
        checkbox = driver.find_element_by_id("agreement-1")
        actions = ActionChains(driver)
        actions.move_to_element(checkbox).click().perform()
        checkbox = driver.find_element_by_id("agreement-2")
        actions = ActionChains(driver)
        actions.move_to_element(checkbox).click().perform()
        agr_btn = driver.find_element_by_xpath(
            "//*[@id='react-backer-report']/div/div/div/div/div/form/button").click()
    except:
        print("HERE")
        pass

    time.sleep(10)
    '''finding first client'''
    row = driver.find_element_by_xpath(
        "//*[@id='backer-report-table']/tbody/tr[1]")
    row.click()

    first_path = "//*[@id='backer_report_index']/div[11]/div/div/div/div/div[2]/div/div/a"
    second_path = "//*[@id='backer_report_index']/div[11]/div/div/div/div/div[2]/div/div/a[2]"

    flag = False
    send_flag = True

    while(True):
        time.sleep(10)
        try:
            message_button = driver.find_element_by_link_text(
                "Send message").click()
        except Exception as e:
            message_button = driver.find_element_by_class_name(
                "messages_link").click()

        try:
            message_exist = driver.find_elements_by_class_name("messages")
            if len(message_exist) > 0:
                for message in message_exist:
                    list_message = message.text.split("\n")
                    for txt in list_message:
                        if "https://turingpi.com/add-accessories/" in txt.strip():
                            send_flag = False
                            break
        except Exception as e:
            send_flag = True

        if send_flag:
            message_body = driver.find_element_by_id("message_body")
            message_body.clear()
            message_body.send_keys(message_text)
            time.sleep(15)
            send_button = driver.find_element_by_name("commit")
            send_button.click()
            print("Message Sent")
            time.sleep(10)
        else:
            break

        if not flag:
            path = first_path
            flag = True
        else:
            path = second_path

        next_button = driver.find_element_by_xpath(path).click()
    driver.quit()
    print("loop Done")
    time.sleep(60)
