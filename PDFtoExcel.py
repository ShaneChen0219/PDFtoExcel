import pandas as pd
import pdfplumber

pdf = pdfplumber.open("/Users/hsiangyuan/Desktop/CS50/VScode/practice/test/TEST.pdf")#位置

firstpage = pdf.pages[0]#抓第幾頁
table = firstpage.extract_tables()#抓Excel內的內容
# print(table)
table_df = pd.DataFrame(table[1:],columns=table[0]) #從table第二行開始抓 columns欄=table第幾行
# print(table_df)
writer = pd.ExcelWriter("巨大飯.xlsx")#檔名
table_df.to_excel(writer)
writer.save()