from webserver import keep_alive
import datetime
import time
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from requests import Session
import json
import pytz

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sh = client.open("Portfolio")
wks = sh.worksheet("Coin API")
wks2 = sh.worksheet("UDP")


def get_BTC():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'bitcoin', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["1"]["quote"]["USD"]["price"]

    return price


def get_ETH():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'ethereum', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["1027"]["quote"]["USD"]["price"]

    return price


def get_LUNA():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'terra-luna', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["4172"]["quote"]["USD"]["price"]

    return price


def get_ETC():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'ethereum-classic', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["1321"]["quote"]["USD"]["price"]

    return price


def get_CFX():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'conflux-network', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["7334"]["quote"]["USD"]["price"]

    return price


def get_ZIL():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'zilliqa', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["2469"]["quote"]["USD"]["price"]

    return price


def get_SERO():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'super-zero-protocol', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["4078"]["quote"]["USD"]["price"]

    return price


def get_RVN():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'ravencoin', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["2577"]["quote"]["USD"]["price"]

    return price


def get_mSLV():
    url = 'https://api.extraterrestrial.money/v1/api/prices?symbol=mSLV'
    get = requests.get(url)
    data = json.loads(get.text)
    price = data["prices"]["mSLV"]["price"]

    return price


def get_aUST():
    url = 'https://api.extraterrestrial.money/v1/api/prices?symbol=aUST'
    get = requests.get(url)
    data = json.loads(get.text)
    price = data["prices"]["aUST"]["price"]

    return price


def get_pLUNA():
    url = 'https://api.extraterrestrial.money/v1/api/prices?symbol=pLUNA'
    get = requests.get(url)
    data = json.loads(get.text)
    price = data["prices"]["pLUNA"]["price"]

    return price


def get_yLUNA():
    url = 'https://api.extraterrestrial.money/v1/api/prices?symbol=yLUNA'
    get = requests.get(url)
    data = json.loads(get.text)
    price = data["prices"]["yLUNA"]["price"]

    return price


def get_PRISM():
    url = 'https://api.extraterrestrial.money/v1/api/prices?symbol=PRISM'
    get = requests.get(url)
    data = json.loads(get.text)
    price = data["prices"]["PRISM"]["price"]

    return price


def get_xPRISM():
    url = 'https://api.extraterrestrial.money/v1/api/prices?symbol=xPRISM'
    get = requests.get(url)
    data = json.loads(get.text)
    price = data["prices"]["xPRISM"]["price"]

    return price

def get_ERGO():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'ergo', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["1762"]["quote"]["USD"]["price"]

    return price

def get_EVMOS():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'evmos', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["19899"]["quote"]["USD"]["price"]

    return price

def get_LUNA2():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'slug': 'terra-luna-v2', 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'ee59a1a4-998b-4e01-8cd1-1c7f8c8b2ed4'
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["20314"]["quote"]["USD"]["price"]

    return price

def update():
    wks.update('B2', get_BTC())
    wks.update('B3', get_ETH())
    wks.update('B4', get_LUNA())
    wks.update('B5', get_ETC())
    wks.update('B6', get_CFX())
    wks.update('B7', get_ZIL())
    wks.update('B8', get_SERO())
    wks.update('B9', get_RVN())
    # wks.update('B10', get_mSLV())
    # wks.update('B11', get_aUST())
    # wks.update('B12', get_pLUNA())
    # wks.update('B13', get_yLUNA())
    # wks.update('B14', get_PRISM())
    # wks.update('B15', get_xPRISM())
    wks.update('B16', get_ERGO())
    wks.update('B17', get_EVMOS())
    wks.update('B18', get_LUNA2())

keep_alive()
run = False
begin = 56
check = 0
while True:
    check = wks2.acell(f"D{begin}").value
    if check is not None:
        begin += 1
    else:
        UpRow = begin
        break
while True:
    now = datetime.datetime.now()
    wait_time = 0
    for i in range(0, 24):
        then = now.replace(hour=i, minute=59)
        wait_time = (then - now).total_seconds()
        if wait_time > 0:
            check = i
            break
          
    if run is False:
        print("Start")
        print(f"Next: {wait_time + 60} seconds")
        print(f"Current Row: {UpRow}")
        run = True
      
    time.sleep(wait_time + 60)
    # print(check)
    # if check == 11:
    #     aUST = get_aUST()
    #     aUST1 = float(wks2.acell("F5").value)
    #     aUST2 = float(wks2.acell("J4").value)
    #     wks2.update(f'D{UpRow}', aUST * aUST1)
    #     wks2.update(f'J{UpRow}', aUST * aUST2)
    #     print("Done")
    #     UpRow += 1

    current = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).strftime("%H:%M - %d/%m/%Y")
    wks.update('D1', f"{current}")
    print(f"Updated - Time: {current}")

    update()
