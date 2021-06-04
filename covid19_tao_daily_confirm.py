import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# df = pd.read_json("https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json")
df = pd.read_json("Day_Confirmation_Age_County_Gender_19CoV.json")
font = FontProperties(fname=r'NotoSansCJKtc-Medium.otf')

tao_case = df[df["縣市"]=="桃園市"]
tao_case = tao_case[tao_case["是否為境外移入"]=="否"]
tao_daily_cases = tao_case["個案研判日"].value_counts()
tao_daily_cases_sorted = tao_daily_cases.sort_index(ascending=True)
# 只讀取近30筆的資料
tao_daily_cases_sorted = tao_daily_cases_sorted.tail(30)
tao_daily_cases_sorted.plot(kind='bar')
print(tao_daily_cases_sorted.shape)
print(tao_daily_cases_sorted)

plt.title("桃園市COVID-19近期本土個案人數統計圖(依個案研判日)", fontproperties=font)
plt.xlabel("個案研判日", fontproperties=font)  #x軸說明文字
plt.ylabel("確診數", fontproperties=font)  #y軸說明文字
plt.subplots_adjust(bottom = 0.24)
plt.show()
