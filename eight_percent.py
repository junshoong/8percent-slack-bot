from urllib.request import urlopen
from bs4 import BeautifulSoup

INVESTMENTS = 'https://8percent.kr/investments/'
DEALS = 'https://8percent.kr/investment/deals/'

def investments():
    soup = BeautifulSoup(urlopen(INVESTMENTS).read(),'html.parser')
    titles = soup.find_all('div', {'class': "TitleText"})
    grades = soup.find_all('div', {'class': "GradeBox"})
    interests = soup.find_all('div', {'class': "InterestText"})
    durations = soup.find_all('div', {'class': "LengthText"})
    amounts = soup.find_all('div', {'class': "AmountText"})
    progresses = soup.find_all('div', {'class': "ProgressText"})
    statuses = soup.find_all('div', {'class': "Box_132"})

    deallist = []
    deal={}
    for i in range(0, len(titles)):
        deal['title'] = titles[i].p.string
        deal['grade'] = grades[i].p.string
        deal['interest'] = interests[i].p.string
        deal['duration'] = durations[i].p.string
        deal['amount'] = amounts[i].p.string
        deal['progress'] = progresses[i].p.string
        deal['status'] = statuses[i].div.p.string
        deallist.append(deal.copy())

    return deallist

def deal_detail(number):
    deal_url = DEALS+str(number)
    soup = BeautifulSoup(urlopen(deal_url).read(),'html.parser')

    deal = {}
    if soup:
        deal['title'] = soup.find('div', {'id': "Text_201"}).p.string
        deal['detail'] = soup.find('div', {'id': "Text_147"}).p.string
        deal['grade'] = soup.find('div', {'id': "Text_226"}).p.string
        deal['interest'] = soup.find('div', {'id': "Text_220"}).p.string
        deal['duration'] = soup.find('div', {'id': "Text_223"}).p.string
        deal['amount'] = soup.find('div', {'id': "Text_228"}).p.string
        deal['progress'] = soup.find('div', {'id': "DealProgressText"}).p.string
        deal['refund_method'] = soup.find('div', {'id': "Text_237"}).p.string

    return deal
