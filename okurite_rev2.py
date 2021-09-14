# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:46:36 2021

@author: iorin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:00:20 2021

@author: iorin
"""
import time
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#例外処理用のlibraryをimport
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

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
driver.set_page_load_timeout(60)

#スプレッドシートのセルに書き込む準備
import gspread

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name('inquiry-form-automatic-posting-6e2409a1cc4a.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#「キー」で取得
SPREADSHEET_KEY = '1FrygfVLHP8fMZh8HdBYboZtkg4fCH8lcDUsbQ58Hbqs'
#SPREADSHEET_KEY2 = '1BazsXmS9dW8oAOmvjMNVabvvw1dYAgW9SR-qbyAylEU'

wb = gc.open_by_key(SPREADSHEET_KEY)
#wb2 = gc.open_by_key(SPREADSHEET_KEY2)
#ws1 = wb.worksheet('sheet1')
#ws2 = wb2.worksheet('imc-pager__item')
ws3 = wb.worksheet('okurite')
#ws3.clear()


#使用者ログイン
driver.get("https://tcare.pro/senders/sign_in")
time.sleep(1)
driver.find_element_by_id("sender_email").send_keys("sales_support@winbridge.biz")
driver.find_element_by_id("sender_password").send_keys("6ru2jp5s")
driver.find_element_by_name("commit").click()
time.sleep(2)


#Okuriteリスト（所要時間計測開始）
start = time.time()

#50ページまでスクレイピング
for k in tqdm(range(1, 51)):
  try:  
    driver.get("https://tcare.pro/okurite?page=" + str(k))
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

#「〇～○件を表示」
    KEN1 = driver.find_element_by_class_name('headline').text
#     HEN1 = KEN1.replace('件','')
    print(KEN1)

#エラー回避
  except WebDriverException:
     break

  except TimeoutException:
     print("Time out!!")
     continue

  except WebDriverException:
     print("unknown error!!")
     continue

  except NoSuchElementException:
     print("no such element!!")
     continue

#ヘッダを除くtrタグ数
  print(len(soup.find_all('tr'))-2)

#①trタグに含まれるtdタグは8個なのでその分の積算を行う。
#②増分を「8」に設定（「URL1」「URL2」「ステータス」「Created at」「編集/削除」を含めない為）
#③lenにはヘッダー分とインデックスが0番目から始めることに注意し、取得データ数合わせの為に「-2」を行っている。
#（参考リンク）https://atmarkit.itmedia.co.jp/ait/articles/1904/19/news027.html
    
  td_urls = []
  td_mails = []    
  for l in range(1, (len(soup.find_all('tr'))-2)*8, 8):
        for td in soup.find_all('td')[l+1]:
#         print(td)
         if "townpage" in td \
             or "map.goo" in td \
                 or "googl" in td \
                    or "itp.ne.jp" in td \
                        or "mapio" in td \
                            or "navitime" in td:
          pass
         else:
          for td in soup.find_all('td')[l]:
            td_urls.append(td.get('href'))
            print(td.get('href'))
          for td in soup.find_all('td')[l+3]:
            td_mails.append(td)
            print(td)
  print(td_urls)
  print(len(td_urls))
  print(td_mails)
  print(len(td_mails))    
  
#ws1の行数を取得
  lastrow1 = len(ws3.col_values(1))
  print(lastrow1)       


#顧客情報リンク一覧           
  if lastrow1 == 0:
            cell_list2 = ws3.range(1, 1, str(len(td_urls)), 1)

#スプレッドシートに入力
            for v2,c2 in zip(td_urls,cell_list2):
             c2.value = v2
             time.sleep(1)
             ws3.update_cells(cell_list2)
#            ws3.batch_update([
#                {
#                'range': cell_list2, 
#                'values': [td_urls],
#                }])            
  elif lastrow1 > 0:
            cell_list3 = ws3.range(lastrow1+1, 1, lastrow1+1+len(td_urls), 1)
            for v2,c2 in zip(td_urls,cell_list3):
             c2.value = v2
             time.sleep(1)
             ws3.update_cells(cell_list3)


#メールアドレス一覧
  if lastrow1 == 0:
            cell_list2 = ws3.range(1, 6, str(len(td_mails)), 6)

#スプレッドシートに入力
            for v2,c2 in zip(td_mails,cell_list2):
             c2.value = v2
             time.sleep(1)
             ws3.update_cells(cell_list2)
#            ws3.batch_update([
#                {
#                'range': cell_list2, 
#                'values': [td_mails],
#                }])            
  elif lastrow1 > 0:
            cell_list3 = ws3.range(lastrow1+1, 6, lastrow1+1+len(td_mails), 6)
            for v2,c2 in zip(td_mails,cell_list3):
             c2.value = v2
             time.sleep(1)
             ws3.update_cells(cell_list3)


#顧客情報
#ws1の行数を取得
  lastrow1 = len(ws3.col_values(1))
  print(lastrow1)
  lastrow2 = len(ws3.col_values(2))
  print(lastrow2)
  
#  if lastrow2 == 0:
  for k in range(lastrow2+1, lastrow1+1):
              try:
               driver.get('https://tcare.pro' + ws3.cell(k,1).value)
               time.sleep(5)
               ws3.update_cell(k, 1, driver.current_url)

               if driver.title == 'Error 502 (Server Error)!!1':
                lastcol = len(list(ws3.row_values(k)))
                ws3.update_cell(k,lastcol,driver.title)
                break

               html = driver.page_source
               soup = BeautifulSoup(html, 'html.parser')
#               print(soup)

#エラー回避
              except WebDriverException:
               break

              except TimeoutException:
                   print("Time out!!")
                   lastcol = len(list(ws3.row_values(k)))                   
                   ws3.update_cell(k, lastcol, "Time out!!")
                   continue

              except WebDriverException:
                   print("unknown error!!")
                   lastcol = len(list(ws3.row_values(k)))                   
                   ws3.update_cell(k, lastcol, "unknown error!!")        
                   continue

#ヘッダを除くtrタグ数
              print(len(soup.find_all('tr'))-1)
              
#会社名              
              for td1 in soup.find_all('td')[0]:
                ws3.update_cell(k, 2, td1)
                print(td1)

#電話番号
              for td2 in soup.find_all('td')[3]:
                ws3.update_cell(k, 4, td2)
                print(td2)

#住所
              for td3 in soup.find_all('td')[4]:
                ws3.update_cell(k, 3, td3)
                print(td3)
                    
#Webサイト
              for td4 in soup.find_all('td')[6]:
                   ws3.update_cell(k, 5, td4.get('href'))
                   print(td4.get('href'))
   

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

