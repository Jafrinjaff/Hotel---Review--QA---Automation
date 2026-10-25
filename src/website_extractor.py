import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

def get_website_rating(file_path):

    driver = webdriver.Chrome()

    try:

        driver.get(file_path.as_uri())
        cleanliness = driver.find_element(By.XPATH,"//strong[@id = 'cleanliness']").text
        facilities = driver.find_element(By.XPATH,"//strong[@id = 'facilities']").text
        staff = driver.find_element(By.XPATH,"//strong[@id = 'staff']").text
        value_for_money = driver.find_element(By.XPATH,"//strong[@id ='value-for-money']").text
        overall_rating = driver.find_element(By.XPATH,"//strong[@id ='overall-rating']").text
        review_count = driver.find_element(By.XPATH,"//strong[@id = 'review-count']").text

        return {
            "cleanliness":float(cleanliness),
            "facilities":float(facilities),
            "staff":float(staff),
            "value_for_money":float(value_for_money),
            "review_count":int(review_count),
            "overall_rating":float(overall_rating)
        }
    
    

    finally:

        driver.quit()


   








    


