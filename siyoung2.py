import requests
import sys
sys.stdout=open('siyoung2.txt','w')

url="https://api.thecatapi.com/v1/images/search"
data=requests.get(url).json()

print(data)
sys.stdout.close()
