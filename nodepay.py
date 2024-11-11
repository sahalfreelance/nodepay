import cloudscraper
import json
import time
import os
import uuid
from fake_useragent import UserAgent
from loguru import logger
os.system("clear")
banner = """\033[36m
███╗   ██╗ ██████╗ ██████╗ ███████╗██████╗  █████╗ ██╗   ██╗
████╗  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
██╔██╗ ██║██║   ██║██║  ██║█████╗  ██████╔╝███████║ ╚████╔╝ 
██║╚██╗██║██║   ██║██║  ██║██╔══╝  ██╔═══╝ ██╔══██║  ╚██╔╝  
██║ ╚████║╚██████╔╝██████╔╝███████╗██║     ██║  ██║   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝   ╚═╝ Node
--------------------------------------------------------------
                  Author : Sahal Pramudya
--------------------------------------------------------------"""
print(banner)
np_token = input("Masukkan NP_Token : ")#"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzAyMzI1NDI2MjAyMzQ1NDcyIiwiaWF0IjoxNzMxMTAzOTYxLCJleHAiOjE3MzIzMTM1NjF9.p1Q4XDnlrvpVJ7W8IB2z7Mvt5ZUvm5gbFUVZZFm_dBtvUHofbFwo42_srpgfxRNkOBhVZk8J-sD9DXyT7B4HLw"
os.system("clear")
print(banner)
user_agent = UserAgent().random
url = {
    "user_reward": "https://api.nodepay.org/api/mission/user-reward"
}
def get_user(url):
    global user_id
    headers = {
        "Authorization": f"Bearer {np_token}",
        "Accept": "application/json",
        "User-Agent": user_agent
    }
    scraper = cloudscraper.create_scraper()
    opt = scraper.get(url, headers=headers)
    if opt.status_code == 200:
        ress = opt.json()
        ress_data = ress["data"]
        user_id = ress_data['user_id']
        logger.info(f"Login Successfull, User ID : {ress_data['user_id']}")
        get_info("https://api.nodepay.org/api/earn/info")
        while True:
            time.sleep(60)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            session("https://api.nodepay.org/api/auth/session")
            time.sleep(120)
            ping("https://nw.nodepay.org/api/network/ping")
    else:
        logger.error("Login Error! Check your NP_TOKEN!")


def get_info(url):
    headers = {
        "Authorization": f"Bearer {np_token}",
        "Accept": "application/json",
        "User-Agent": user_agent
    }
    scraper = cloudscraper.create_scraper()
    opt = scraper.get(url, headers=headers)
    try:
        response = opt.json()
        ress = response['data']
        logger.info(f"Today earnings : {ress['today_earning']}, Current points : {ress['current_point']}, Pending points : {ress['pending_point']}")
    except:
        logger.error("Getting info failed!")
        pass
def session(url):
    headers = {
        "Authorization": f"Bearer {np_token}",
        "Accept": "application/json",
        "User-Agent": user_agent
    }
    data = {}
    scraper = cloudscraper.create_scraper()
    opt = scraper.post(url, headers=headers, json=data)
    response = opt.json()
    if response['success'] == True:
        ress_data = response['data']
        logger.info(f"Post session success, Name : {ress_data['name']}, UID : {ress_data['uid']}, Status : {ress_data['state']}")
    else:
        logger.debug("Post session Failure!, Trying post in a few minutes")
        pass

def ping(url):
    headers = {
        "Authorization": f"Bearer {np_token}",
        "Accept": "application/json",
        "User-Agent": user_agent,
        "origin": "chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm"
    }
    data = {
        "browser_id": str(uuid.uuid4()),
        "id": user_id,
        "timestamp": time.time(),
        "version": "2.2.7"
    }
    scraper = cloudscraper.create_scraper()
    opt = scraper.post(url, headers=headers, json=data)
    response = opt.json()
    if response['success'] == True:
        logger.info("Ping succeffsull!")
    else:
        logger.debug("Ping failed!, Trying again in a few minutes")
        pass


get_user(url["user_reward"])
