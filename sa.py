import requests
from bs4 import BeautifulSoup
from random import choice

print('''
      ###########################

      @ if you want random  movie just press Enter

      #############################
''')
type_mo = input('Enter type : ')
s = requests.Session()
s.headers.update({
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
})
if type_mo =='':
    page = s.get('https://www.fushaar.com/')
else:

    page = s.get(f'https://www.fushaar.com/gerne/{type_mo}/')

if page.status_code==200:
  soup = BeautifulSoup(page.text, 'html.parser')
  s = soup.select(".info h3")
  movie_cho = choice(s)
  print(movie_cho.get_text())

elif page.status_code ==404:
  print('[+] page not found')

