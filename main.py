from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from playsound import playsound
import datetime

# Dictionary mapping course numbers to their sections to check
COURSES = {
    "۱۲۰۶۳۱۸۰۱": [4, 5],
    "۱۲۰۶۳۱۱۴۱": [1]
    # "۲۹۰۳۳۲۲۱۱": [1]
}
SOUND_PATH = "alarm.mp3"
WAIT_TIME = 15

# playsound(SOUND_PATH)


def persian_to_english(number_in_string):
    difference = ord("۱") - ord("1")
    result = 0
    for i in number_in_string:
        result *= 10
        if (ord(i) < 256):
            result += int(i)
            pass
        else:
            result += int(chr(ord(i) - difference))
    return result


driver = webdriver.Chrome()

driver.get(r'http://sess.shirazu.ac.ir/')

input('Navigate to desired page and press enter to continue ')

err_count = 0
while True:
    if err_count > 3:
        playsound(SOUND_PATH)

    for course_number, course_sections in COURSES.items():
        for section in course_sections:
            try:
                course_number_elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{course_number}')]")
                course_row = course_number_elements[section - 1].find_element(By.XPATH, "..")
                course_row.click()
                sleep(3)

                student_count = persian_to_english(driver.find_element(By.ID, "edStdCount").text)
                total_capacity = persian_to_english(driver.find_element(By.ID, "edCapacity").text)
                free_capacity = total_capacity - student_count

                print(
                    f"{datetime.datetime.now()} | section: {section} | student count: {student_count} | total capacity: {total_capacity} | free capacity: {free_capacity}")

                if free_capacity != 0:
                    print("AHHHHHHHHHHH")
                    while True:
                        playsound(SOUND_PATH)
            except Exception as e:
                print(e)
                err_count += 1
            else:
                err_count = 0

            driver.back()
        sleep(WAIT_TIME)
