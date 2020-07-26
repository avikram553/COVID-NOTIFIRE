from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyme(title,message):
	notification.notify(
		title=title,
		message=message,
		app_icon="C:\\Users\\avikr\\COVID 19 NOTIFIER\\img\\covid.ico",
		timeout=5)

def getCovidData(url):
	r=requests.get(url)
	soup=BeautifulSoup(r.text,'html.parser')
	#print(soup.prettify)
	mydataString=''
	for tr in soup.find('tbody').find_all('tr'):
		if tr.text[1]=='*' or '#' in tr.text:
			continue
		else:
			mydataString+=tr.text

	datalist=mydataString.split('\n\n')
	#print(datalist)
	data=[]
	for item in datalist:
		data.append(item.split('\n'))

	data[0].pop(0)
	data[len(data)-1].pop(-1)
	Total=0
	TotalCured=0
	TotalDeaths=0
	for i in range(len(data)):
		#print(data[i])
		Total+=int(data[i][5])
		TotalCured+=int(data[i][3])
		TotalDeaths+=int(data[i][4])
	#print(Total)
	#print(TotalDeaths)
	notiTitle='Cases of COVID 19'
	notiText=f"Total:	{Total}\nCured:	{TotalCured}\nDeaths:	{TotalDeaths}"
	notifyme(notiTitle,notiText)
	time.sleep(5)
	#print(*data)
	states=['Uttar Pradesh','Delhi','Maharashtra']
	for i in range(len(data)):
		if data[i][1] in states:
			endProcess=False
			#print(data[i])
			notiTitle='Cases of COVID 19'
			notiText=f"STATE:	{data[i][1]}\nTotal:	{int(data[i][5])}\nCured:	{data[i][3]}\nDeaths:	{data[i][4]}"
			notifyme(notiTitle,notiText)
			'''while not endProcess:
				pass'''
			time.sleep(5)
if __name__ == '__main__':
	#notifyme("COVID 19 ALERT","Help to spread awareness")
	#while True:
	getCovidData("https://www.mohfw.gov.in/")
	endProcess=False
		#time.sleep(3)
