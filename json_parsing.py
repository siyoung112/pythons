import requests
import xmltodict
import json
from openpyxl import Workbook


file_path = 'C:/Users/장시영/OneDrive/바탕 화면/sy_home/10.파이선스/2주차/kb-json.json'
with open(file_path, 'r') as f:
    data = json.load(f)
data1=data.get('getContractDemandCostListResponse')['contractDemandCostList']

#print('Index', 'product Name', 'Detail Name', 'unitUsage', 'totalUnitUsageQuantity','product price', 'cost')
#for i in range(5):
#  print(i+1,  data1[i]['demandType']['codeName'], data1[i]['demandTypeDetail']['codeName'],  data1[i]['unitUsageQuantity'], data1[i]['totalUnitUsageQuantity'], data1[i]['productPrice'], data1[i]['useAmount'])

wb = Workbook()
sheet = wb.active
sheet.title = "서비스이용내역서1"
print('타입')
#print(type(data1['demandType']['codeName']))
print(type(data1[0]['demandTypeDetail']['codeName']))

sheet.append(['항목', '청구연월', '상품명', '상품상세', '단위사용', '비용합계'])

for i in range(len(data.get('getContractDemandCostListResponse')['contractDemandCostList'])):
  '''
    if data1[i]['demandType']['codeName'] in ('Backup','Cloud Insight','Simple &amp; Easy Notification Service','Cloud Outbound Mailter'):    
        #col1 = i+1
            col2 = data1[i]['demandMonth']
            col3 = data1[i]['demandType']['codeName']
            col4 = data1[i]['demandTypeDetail']['codeName']
            #col5 = data1[i]['unitUsageQuantity']
            col6 = data1[i]['totalUnitUsageQuantity']
            #col5 = data1[i]['productPrice']
            col7 = data1[i]['useAmount']
            #sheet.append([col1, col2, col3, col4, col6,col7])
            sheet.append(col2, col3, col4, col6,col7])
            '''
obj=[data1[i]['demandMonth'],data1[i]['demandType']['codeName']] 
sheet.append(obj)
wb.save('C:/Users/장시영/OneDrive/바탕 화면/sy_home/10.파이선스/3주차/test_new_이용내역서.xlsx')

# total count 개수 확인
#print(type(data.get('getContractDemandCostListResponse')['totalRows']))
#print(len(data.get('getContractDemandCostListResponse')['contractDemandCostList']))
#print(len(data1))
'''


print('\n-------모든 행/열 출력----------')
all_values = []
for row in load_ws.rows:
   row_value = []
   for cell in row:
      row_value.append(cell.value)
    all_values.append(row_value)
print(all_values)

wb.save('openpyxl_test.xlsx')
'''

########### 중요 시작 ################
# key, value 형태를 가짐
#딕셔너리에서 for 문으로 돌릴 때 [i]를 넣는 곳이 중요함. --> 리스트형이 나오기 전

'''
data1=data.get('getContractDemandCostListResponse')['contractDemandCostList']
print('Index',"|", 'product Name', "|",'Detail Name', "|",'unitUsage',"|", 'totalUnitUsageQuantity',"|",'product price', "|",'cost')
for i in range(5):
    
    #data2=i+1, data1[i]['demandType']['codeName'], data1[i]['demandTypeDetail']['codeName'], data1[i]['unitUsageQuantity'], data1[i]['totalUnitUsageQuantity'],data1[i]['productPrice'], data1[i]['useAmount']
    #print('출력값: ',data2) #튜플
    print(i+1, "|", data1[i]['demandType']['codeName'], "|", data1[i]['demandTypeDetail']['codeName'], "|", data1[i]['unitUsageQuantity'],"|", data1[i]['totalUnitUsageQuantity'],"|",data1[i]['productPrice'],"|", data1[i]['useAmount'])
    #data1=(data.get('getContractDemandCostListResponse')['contractDemandCostList'][i]['demandType']['codeName']) #146 total rows
'''
# 엑셀 시트에 데이터 넣기
# 엑셀 붙여넣을 때 "|" 부분을 slice 하여 넣는 방법
# openpyxl 활용


########### 중요 끝 ################

##a=[1,2,3,4,5]
#print(a[3])
'''
a="12"
b=3

ab='STRING'
print(ab)
print(ab[0])
for i in ab:
    print(i)
print(ab[2:4])


#print(data.keys()) #getContractDemandCostListResponse
#print(data.values()) #그 외 나머지



keyList = list(data.keys())
valueList = list(data.values())


print(type(data.items()))
print(data.items())
'''