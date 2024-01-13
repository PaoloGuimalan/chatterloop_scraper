from django.http import JsonResponse
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
import requests

def scraped_feed(request):

    script_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(script_directory)
    driver_folder = 'driver'
    webdriver_filename = 'chromedriver.exe' if os.environ.get("ENVIRONMENT") == "Windows" else 'chromedriverlinux'

    webdriver_path = os.path.join(parent_directory, driver_folder, webdriver_filename)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")
    browser = webdriver.Chrome(options=chrome_options)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = 'https://www.reddit.com/search/?q=programming'

    browser.get(url=url)
    time.sleep(5)

    time.sleep(5)

    page_source = browser.page_source

    browser.quit()

    soup = BeautifulSoup(page_source, 'lxml')
    list_response = soup.find_all('faceplate-tracker', {'data-testid': 'search-post'})

    list_holder = []

    for items in list_response:
        # try:
            username = items.find('a', class_="flex items-center text-neutral-content-weak font-semibold").text
            content = items.find('a', {'data-testid': 'post-title'}).text
            date_posted = items.find('faceplate-timeago').text

            print(content)

            list_holder.append({
                "username": username,
                "content": content,
                "date_posted": date_posted
            })
        # except:
        #     print("No Title")

    # print(list_response)
    # print(soup.find_all('faceplate-tracker'))
    return JsonResponse({ "status": True, "result": list_holder },safe=False)