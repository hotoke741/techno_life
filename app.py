import requests
from bs4 import BeautifulSoup


url = 'https://www.python.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# items = soup.find_all('a')
# print(len(items))

# for title in items:
#     print(title.get_text())
#     print(title.get('href'))

# items = soup.find_all('div', attrs={'class': 'medium-widget blog-widget'})
# print(items)
# print(len(items))
# new_items = items[0].find_all('a')
# dates = items[0].find_all('time')
# for title in new_items:
#     print(title.get_text())

# for date in dates:
#     print(date.get_text())

titles = soup.select('div.medium-widget.blog-widget a')
dates= soup.select('div.medium-widget.blog-widget time')
for title in titles:
    print(title.get_text())

for date in dates:
    print(date.get_text())











# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://www.w3schools.com/html/default.asp')
# # print(response)

# soap = BeautifulSoup(response.text, 'html.parser')
# # print(soap)
# # item = soap.find('h1')
# items = soap.find_all('div', attrs = {'id': 'leftmenuinnerinner'})

# if len(items) == 0:
#     print('Not Found')  
# else:
#     titles = items[0].find_all('a')
   
#     for item in titles:
#         print(item.getText())






# # import requests
# # from bs4 import BeautifulSoup

# # response = requests.get('https://www.w3schools.com/html/default.asp')
# # # print(response)

# # soup = BeautifulSoup(response.text, 'html.parser')

# # # print(soup)
# # items = soup.find_all('div', attrs={'id' : 'leftmenuinnerinner'})

# # # print(len(items))

# # if len(items) == 0:
# #     print('Not Found')
# # else:
# #     titles = items[0].find_all('a')
# #     # list_item = titles.find_all('h1')
    
# # for item in titles:
# #         print(item.getText())

# # # list_item = soup.find_all()
# # # list_item2 = soup.find_all()
