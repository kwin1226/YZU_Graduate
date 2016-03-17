"""
Crawler for YZUportal test

	#Parser
	# 1.姓名 v
	# 2.系名 
	# 3.休業年度
	# 4.課程資料
	# 5.經典五十
	# 6.服務時數

"""
import requests
import getpass
from bs4 import BeautifulSoup
from time import sleep

def main():
	# User input
	print('\n------------Login YZUportal------------\n')
	__USERNAME = input('Username: ')
	__PASSWORD = getpass.getpass('Password: ')

	# Variable 
	data_package =[]
	login_url = 'https://portalx.yzu.edu.tw/PortalSocialVB/Login.aspx'
	index_url = 'https://portalx.yzu.edu.tw/PortalSocialVB/FMain/DefaultPage.aspx?Menu=Default&LogExcute=Y'
	r = requests.Session()   
	login_res = r.get(login_url)
	login_dom = BeautifulSoup(login_res.text) 

	# Token
	__VIEWSTATE = login_dom.select('#__VIEWSTATE')[0]['value']
	__VIEWSTATEGENERATOR = login_dom.select("#__VIEWSTATEGENERATOR")[0]['value']
	__EVENTVALIDATION = login_dom.select("#__EVENTVALIDATION")[0]['value']

	# Login Page
	login_form = {
		        '__VIEWSTATE' : __VIEWSTATE,
	            '__VIEWSTATEGENERATOR' : __VIEWSTATEGENERATOR,
	            '__EVENTVALIDATION' : __EVENTVALIDATION,
	            'Txt_UserID' : __USERNAME,
	            'Txt_Password' : __PASSWORD,
	            'ibnSubmit' : '登入'
	}
	res = r.post(login_url, data=login_form)
	
	# Index Page
	index_res = r.get(index_url)
	index_dom = BeautifulSoup(index_res.text)
	std_name = index_dom.select('#MainBar_lbnUserName')[0].text
	# 左側Menu 系名、修業年度、課程資料 需抓ajax回傳 (json "Typecode":"A2") //用selenium !?
	# std_dept = index_dom.find("div",{"id":"MainLeftMenu_L2"})
	# print("Department:", std_dept)
	# for title in (index_dom.find_all(id='')):
	#     print("\n|| Data:", title.text) 

	data_package.append({'std_name':std_name})
	print("\n|| Name:", std_name)


if __name__ == '__main__':
	main()