import urllib.request
import json

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
htmlfile = urllib.request.urlopen(url)
text = htmlfile.read().decode()
print(type(text))  # <class 'str'>


j = json.loads(text, encoding='utf-8')  #To parse JSON from URL or file, use json.load(). To parse string with JSON content, use json.loads()
print(type(j))  # <class 'dict'>

# 測試資料輸出的結果
# result=j["result"]["results"]
# print(len(result))
# print(result[12]['stitle'])
# print(result[12]['address'][5:8])
# print(result[12]['longitude'])
# print(result[12]['latitude'])
# a=result[12]['file'].lower().find("jpg")
# print(result[12]['file'][0:a+3])
# l=[result[12]['stitle'],result[12]['address'][5:8],result[12]['longitude'],result[12]['latitude'],result[12]['file'][0:a+3]]
# print(l)

# 建立CSV檔案
import csv
result=j["result"]["results"]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["景點名稱","區域", "經度", "緯度", "第一張圖檔網址"])
    for i in range(len(result)):
        a=result[i]['file'].lower().find("jpg")
        l=[result[i]['stitle'],result[i]['address'][5:8],result[i]['longitude'],result[i]['latitude'],result[i]['file'][0:a+3]]
        writer.writerow(l)
