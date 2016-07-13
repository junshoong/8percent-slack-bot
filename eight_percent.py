from urllib.request import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(urlopen('http://8percent.kr/investments').read(),'html.parser')

def investments():
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
