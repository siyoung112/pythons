import requests
url="http://www.cloit.co.kr/nothanks"
res=requests.get(url)
#print(res)
#print(type(res))
res2=res.status_code
#print(type(res.status_code))

if res2==200:
   print("정상 접속",res2)
else:
   print("호출 실패", res2)