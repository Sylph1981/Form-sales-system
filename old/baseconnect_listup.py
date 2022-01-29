# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:07:06 2021

@author: iorin
"""

import gspread
import re

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#例外処理用のlibraryをimport
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

#Selectモジュールをインポート
#from selenium.webdriver.support.select import Select

#オプションの作成
option = Options()

#起動オプション
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
option.add_argument('--headless')

#「unknown error: net::ERR_CONNECTION_CLOSED」の回避用
option.add_argument('--disable-dev-shm-usage')

# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome("C:/Users/iorin/OneDrive/ドキュメント/Python Scripts/chromedriver.exe",options=option)

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name('ekiten-07cd3f32afc9.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#「キー」で取得
SPREADSHEET_KEY = '1rrdlH_7EZypw32hNWqjvuWFayvNGTU_xcyB4cDvauRY'

wb = gc.open_by_key(SPREADSHEET_KEY)
#print(wb)

#「名前」で取得
ws1 = wb.worksheet('Major agricultural corp')
#print(ws1)
#ws2 = wb.worksheet('grouped_list')
#print(ws2)
ws3 = wb.worksheet('pagenation')
#print(ws3)
#ws4 = wb.worksheet('Item_number')
#print(ws4)

#シートの初期化
#ws1.clear()
#ws1.range("A2:K"+len(ws1.col_values(1))).clear()

#掲載商品数リセット
#ws4.update_cell(2, 4, 0)

#所要時間計測開始
start = time.time()


#全国のホームページ制作会社一覧
for j in tqdm(range(142,len(ws3.col_values(1))+1)): #49ページで終わってしまわないよう「50+1」としている       
#     if ws2.cell(i,3).value == '404 Not Found ｜エキテン':
#      break      
#     time.sleep(3)  
     driver.get(ws3.cell(j,1).value)
     time.sleep(5)
     
     html = driver.page_source
#     print(html)
     soup = BeautifulSoup(html, 'html.parser')

#「〇～○件を表示」
     KEN1 = driver.find_element_by_class_name('searches__result__number').text
#     HEN1 = KEN1.replace('件','')
     print(KEN1)

     service_urls = []
#「None」が返って来ないように必ず「a」タグを付けること！！
     for service_url in soup.select(".searches__result__list__header__title a"):
       print(service_url.get("href"))
       service_urls.append(service_url.get("href"))
#       print(len(Shop_urls))
#後で「https://imitsu.jp」と連結させること！！
       time.sleep(5)
       
#A列を配列として入れ込む
#       values1 = ws1.col_values(1)
#       values4 = ws4.col_values(1)
       
#ws1の行数を取得
       lastrow1 = len(ws1.col_values(1))
       print(lastrow1)       
       
#ws4の行数を取得
#       lastrow4 = len(values4)
#       print(lastrow4)
    
       if lastrow1 == 0:
        cell_list_2 = ws1.range("A1:A" + str(len(service_urls)))
#スプレッドシートに入力
        for v2,c2 in zip(service_urls,cell_list_2):
         time.sleep(1)
         c2.value = v2
         ws1.update_cells(cell_list_2)

       elif lastrow1 > 0:
#          for k in range(1,len(Shop_urls)):
           ws1.update_cell(lastrow1+1, 1,service_url.get('href'))

#会社概要
#ws1の行数を取得
lastrow1 = len(ws1.col_values(1))
print(lastrow1)       
for k in tqdm(range(1,lastrow1+1)):        
     try:
      driver.get('https://baseconnect.in' + ws1.cell(k,1).value)
      time.sleep(5)
      ws1.update_cell(k, 1, driver.current_url)

      if driver.title == 'Error 502 (Server Error)!!1':
       lastcol = len(list(ws1.row_values(k)))                            
       ws1.update_cell(k,lastcol,driver.title)          
       break

      html = driver.page_source
#      print(html)
      soup = BeautifulSoup(html, 'html.parser')

#エラー発生時に回避（①～⑤は実施されない）
     except WebDriverException:
      break


#①各詳細データ

#法人名
     for Content in soup.select(".node__header__text__title"):
       print(Content.getText())
       time.sleep(3)       
       lastcol = len(list(ws1.row_values(k)))
       ws1.update_cell(k, lastcol+1, re.sub("[\n]", "", Content.getText(), 4))

#事業内容
     for Content in soup.select(".node__header__cont__text__heading"):
       print(Content.getText())
       time.sleep(3)       
#改行置換
       lastcol = len(list(ws1.row_values(k)))
       ws1.update_cell(k, lastcol+1, re.sub("[\n]", "", Content.getText(), 4))
#空白置換
       lastcol = len(list(ws1.row_values(k)))
       ws1.update_cell(k, lastcol, re.sub("[\s]", "", ws1.cell(k, lastcol).value, 34))

#住所
     for Content in soup.select(".mincho"):
      if "〒" in Content.getText():
       print(Content.getText())
       time.sleep(3)
#改行置換
       lastcol = len(list(ws1.row_values(k)))                  
       ws1.update_cell(k, lastcol+1, re.sub("[\n]", "", Content.getText(), 4))
#空白置換
       lastcol = len(list(ws1.row_values(k)))
       ws1.update_cell(k, lastcol, re.sub("[\s]", "", ws1.cell(k, lastcol).value, 34))

#売上高
#     for Content in soup.select(".node__box.node__basicinfo"):
     if "売上高" in str(soup.select(".node__box.node__basicinfo")) \
           and "円" in str(soup.select(".mincho.nodeTable__text--other")):
        for Content in soup.select(".mincho.nodeTable__text--other"):
         if "円" in Content.getText():
          print(Content.getText())
#          time.sleep(3)
#改行置換        
          lastcol = len(list(ws1.row_values(k)))                  
          ws1.update_cell(k, lastcol+1, re.sub("[\n]", "", Content.getText(), 5))
#空白置換
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol, re.sub("[\s]", "", ws1.cell(k, lastcol).value, 40))                
     elif "売上高" in str(soup.select(".node__box.node__basicinfo")) \
           and not "円" in str(soup.select(".mincho.nodeTable__text--other")):
          for Content in soup.select(".mincho"):             
           if "万" in Content.getText() \
               and not "円" in Content.getText():
            print(Content.getText())
            time.sleep(3)
#改行置換        
            lastcol = len(list(ws1.row_values(k)))                  
            ws1.update_cell(k, lastcol+1, re.sub("[\n]", "", Content.getText(), 5))
#空白置換
            lastcol = len(list(ws1.row_values(k)))
            ws1.update_cell(k, lastcol, re.sub("[\s]", "", ws1.cell(k, lastcol).value, 40))
            lastcol = len(list(ws1.row_values(k)))
     elif not "売上高" in soup.select(".node__box.node__basicinfo"):
         lastcol = len(list(ws1.row_values(k)))                  
         ws1.update_cell(k, lastcol+1, "-")

#連絡先
     for Content in soup.select(".node__box.node__contact"):
       if "会社サイト" in Content.getText():
        Contents = []
        for Content in soup.select(".node__box__heading__link.node__box__heading__link-othersite a"):
         Contents.append(Content.get("href"))
         print(Contents)
        if len(Contents) > 1:
         for j in range(1, len(Contents)+1):
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, Contents[j-1])
        elif len(Contents) == 1:
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, Contents[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "-")          
       elif not "会社サイト" in Content.getText():
        lastcol = len(list(ws1.row_values(k)))
        ws1.update_cell(k, lastcol+1, "-")

          
#chromeドライバーの終了
driver.quit()      

# calculate elapsed time
elapsed_time = int(time.time() - start)

# convert second to hour, minute and seconds
elapsed_hour = elapsed_time // 3600
elapsed_minute = (elapsed_time % 3600) // 60
elapsed_second = (elapsed_time % 3600 % 60)

# print as 00:00:00
print("所要時間：" + str(elapsed_hour).zfill(2) + "h" \
      + str(elapsed_minute).zfill(2) + "m" + str(elapsed_second).zfill(2) + "s")                