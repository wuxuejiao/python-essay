import requests

r=requests.get('https://passport.126.com/dl/ini?pd=mail126&pkid=QdQXWEQ&pkht=mail.126.com&topURL=https://www.126.com/')
cookie1=str(r.headers)
cookie1=cookie1.split('l_s_mail126QdQXWEQ=',7)[-1].split(';')[0]
print cookie1

url='https://passport.126.com/dl/gt?un=xxx@126.com&pkid=QdQXWEQ&pd=mail126&topURL=https://www.126.com/'
cookie2={'l_s_mail126QdQXWEQ':cookie1,
         'P_INFO':'xxx@126.com|1525848856|2|mail126|00&99|gud&1525418327&mail126#gud&440100#10#0#0|&0|mail126|xxx@126.com',
         'THE_LAST_LOGIN':'xxx@126.com',
         'JESSIONID':'abcgJWKS13ypc7Uas7dnw'}
r2=requests.get(url,cookies=cookie2)
tk1=eval(r2.text)
tk = tk1['tk']
print tk

url='https://passport.126.com/dl/l'
data1={'un':'xxx@126.com',
       'pw':'a19931029',
       'tk':tk,
       'pkid':'QdQXWEQ',
       'domains':'126.com',
       'pwdKeyUp':1,
       'l':1,
       'd':10,
      # 'pd':'mail126',
       'rtid':'oxjWTccdSJgqwV0HSeKk0I85Zij5P3PT',
       'topURL':'https://www.126.com/#return'
       }
print data1
r3=requests.post(url,json=data1,cookies=cookie2)
print r3
print r3.text


    
'''

s = requests.Session()
r=s.get('https://passport.126.com/dl/ini?pd=mail126&pkid=QdQXWEQ&pkht=mail.126.com&topURL=https://www.126.com/&nocache=1525853005608')
url='https://passport.126.com/dl/gt?un=xxx@126.com&pkid=QdQXWEQ&pd=mail126&topURL=https://www.126.com/&nocache=1525853012414'
r2=s.get(url)
tk1=eval(r2.text)
tk = tk1['tk']
print tk
url='http://passport.126.com/dl/l'
data1={'un':'xxx@126.com',
       'tk':tk,
       'pw':'a19931029',
       'pkid':'QdQXWEQ',
       'domains':'126.com',
       'pwdKeyUp':1,
       'l':1,
       'd':10,
       't':25853012414,
       'topURL':'https://www.126.com/'
       }
r3=s.post(url,json=data1)
print r3
print r3.text
'''
