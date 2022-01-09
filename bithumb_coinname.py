"""
1. 웹사이트 접속 후 URL확인
2. 원하는 정보의 위치를 확인
3. 원하는 형태로 출력하도록 프로그래밍
"""

# 1. 라이브러리 호출

import requests
import json
from bs4 import BeautifulSoup as bs

# 2. 데이터 요청 단계

reqKo = requests.get("https://www.bithumb.com/trade/order/BTC_KRW")
reqEn = requests.get("https://en.bithumb.com/trade/order/BTC_KRW")

soupKoSym = bs(reqKo.text, "lxml")
soupEn = bs(reqEn.text, "lxml")

# 3. 데이터 파싱(추출) + 저장 단계

f_Ko = open('/Users/bj/Desktop/currenciesnameKo.json', 'w')
f_En = open('/Users/bj/Desktop/currenciesnameEn.json', 'w')
f_Sym = open('/Users/bj/Desktop/currenciesnameSym.json', 'w')
currenciesKoSym = soupKoSym.find_all("div", {'class': "tx_l tx_link"})
currenciesEn = soupEn.find_all("div", {'class': "tx_l tx_link"})

i = 0
j = 0

currenciesKoList = []
currenciesEnList = []
currenciesSymKoList = []
currenciesSymEnList = []

for span in currenciesKoSym:
    currenciesKoName = currenciesKoSym[i].find("span", {'class': "coinSymbol"})["data-sorting"]
    currenciesSymKoName = currenciesKoSym[i].find("span", {'class': "coinSymbol sort_coin"})
    currenciesSymKoName = currenciesSymKoName.text
    currenciesSymKoName = currenciesSymKoName.replace("/KRW", "")
    currenciesKoList.append((currenciesSymKoName, currenciesKoName))
    currenciesSymKoList.append(currenciesSymKoName)
    i = i + 1

for span in currenciesEn:
    currenciesEnName = currenciesEn[j].find("span", {'class': "coinSymbol"})["data-sorting"]
    currenciesSymEnName = currenciesEn[j].find("span", {'class': "coinSymbol sort_coin"})
    currenciesSymEnName = currenciesSymEnName.text
    currenciesSymEnName = currenciesSymEnName.replace("/KRW", "")
    currenciesEnList.append((currenciesSymEnName, currenciesEnName))
    j = j + 1

json_string_Ko = json.dumps(currenciesKoList, ensure_ascii = False)
f_Ko.write(json_string_Ko)
print(json_string_Ko)
f_Ko.close()

json_string_En = json.dumps(currenciesEnList, ensure_ascii = False)
f_En.write(json_string_En)
print(json_string_En)
f_En.close()