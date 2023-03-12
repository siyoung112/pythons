import requests
import sys

url="https://api.thecatapi.com/v1/images/search"
data=requests.get(url).json()
print(type(data))
print(data)

sys.stdout=open('siyoung2.txt','w')
sys.stdout.close()