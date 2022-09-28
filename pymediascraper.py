from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import time
import datetime
import json
import requests

fin = open("examplesheet.csv", 'r')
fout = open("Output File", 'w')

# get insta user/pass
'''
with open("iglogin.txt", 'r') as ig:
    text = ig.readlines()
    ig_username = text[1].strip()
    ig_pass = text[2].strip()
    '''

# get urls
urls = []
lines = fin.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip().split(',')

# add to urls list
for line in lines[2:]:
    urls.append(line[0])

# clean up url list
urls = [ele for ele in urls if len(ele) > 3]
print(urls)

fin.close()
fout.close()

while (len(urls) > 0):
    # we will remove the first element each loop and iterate through each first element.
    url = urls[0]

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }

    # tiktok video
    if "tiktok" in url:
        page = requests.get(url, headers=headers)

        # page.text returns the entire html as a string, create soup object
        soup = BeautifulSoup(page.text, "html.parser")

        print("TikTok Video Detected...")

        # currently, tiktok will always return the username under h3, so we can just use .find() method
        # video duration is a struggle
        try:
            username_data = soup.find('h3')
            like_data = soup.find("strong", class_="tiktok-1y2yo26-StrongText e1bs7gq22")

            likes = like_data.text
            username = username_data.text
        except:
            print("Error With Link \"" + url + "\", skipping to next link...")
            urls.pop(0)
            continue

        print("username = " + username)
        # print("length = " + length)
        print("likes = " + likes)

    elif "instagram" in url:
        print("Instagram Video Detected...")

        # login_url = 'https://www.instagram.com/accounts/login/ajax/'

        current_time = int(datetime.datetime.now().timestamp())
        response = requests.get(url)
        csrf = response.cookies['csrftoken']

        payload = {
            'username': ig_username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{current_time}:{ig_pass}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        login_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        }

        login_response = requests.post(login_url, data=payload, headers=login_header)
        json_data = json.loads(login_response.text)

        print(json_data)
        if "authenticated" in json_data:

            print("login successful")
            cookies = login_response.cookies
            cookie_jar = cookies.get_dict()
            csrf_token = cookie_jar['csrftoken']
            print("csrf_token: ", csrf_token)
            session_id = cookie_jar['sessionid']
            print("session_id: ", session_id)
        else:
            print("login failed ", login_response.text)

    else:
        print("The link was of a type other than instagram / tiktok: \"" + url + "\"")

    # if url == '' no link inputted / detected, inform and restart loop

    urls.pop(0)
