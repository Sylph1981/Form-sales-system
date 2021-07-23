# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 05:32:53 2021

@author: iorin
"""

import gspread
import re
#import requests
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

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

#最初のHTMLドキュメントが完全に読み込まれて解析されるまで待機し、スタイルシート、画像、およびサブフレームの読み込みを破棄します。
option.page_load_strategy = 'eager'

# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome("C:/Users/iorin/OneDrive/ドキュメント/Python Scripts/chromedriver.exe",options=option)
driver.set_page_load_timeout(60)

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name('ekiten-07cd3f32afc9.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#「キー」で取得
SPREADSHEET_KEY = '1FrygfVLHP8fMZh8HdBYboZtkg4fCH8lcDUsbQ58Hbqs'

wb = gc.open_by_key(SPREADSHEET_KEY)

#「名前」で取得
ws1 = wb.worksheet('imitsu')

#所要時間計測開始
start = time.time()

    
#お問い合わせページのリンク
#def scrape_contact_emails(link):
#ws1の行数を取得
lastrow1 = len(ws1.col_values(2))
for k in tqdm(range(53, 54)):
#  lastcol = len(list(ws1.row_values(k)))                      
   if not ws1.cell(k, 5).value == "-":    
    try:
     driver.get(ws1.cell(k, 5).value)
     time.sleep(5)

     if 'Error 502 (Server Error)!!1' in driver.title:
       ws1.update_cell(k, 8, driver.title)          
       continue
     elif 'Not Found' in driver.title:
       ws1.update_cell(k, 8, driver.title)          
       continue   
     elif 'エラー' in driver.title:
       ws1.update_cell(k, 8, driver.title)          
       continue      

     html = driver.page_source  
#   print(res.status_code)
     soup = BeautifulSoup(html, 'html.parser')


#エラー発生時に回避（①～⑤は実施されない）
    except TimeoutException:
     print("Time out!!")   
     ws1.update_cell(k, 8, "Time out!!")
     continue

    except WebDriverException:
     print("unknown error!!")   
     ws1.update_cell(k, 8, "unknown error!!")        
     continue   

#抽出開始
    if not "このサイトにアクセスできません" in html:
     links_1 = []
     for link in soup.select('a[href]'):
#      print(soup.find_all('a'))
      if "contact" in str(link.get("href")) \
           and not "actover" in str(link.get("href")) \
               and not "projection" in str(link.get("href")) \
                  and not "consultation" in str(link.get("href")) \
                      and not "regist" in str(link.get("href")) \
                          and not "research" in str(link.get("href")) \
                              and not "mailto" in str(link.get("href")) \
                                  and not "privacy" in str(link.get("href")) \
                                      and not "service" in str(link.get("href")) \
                                          and not "recruit" in str(link.get("href")) \
                                              and not "sdgs" in str(link.get("href")) \
                                                  or "form2" in str(link.get("href")) \
                                                      and "inq" in str(link.get("href")) \
                                                  or "contact" in str(link.get("href")) \
                                                     and "salesmarketingservice" in str(link.get("href")) \
                                                          or r"contact/inq" in str(link.get("href")) \
          or "CONTACT" in str(link.get("href")) \
              and not "mailto" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
            or "Contact" in str(link.get("href")) \
              and not "mailto" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
            or "INQ" in str(link.get("href")) \
              and not "mailto" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
            or "Inq" in str(link.get("href")) \
              and not "mailto" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
            or "inq" in str(link.get("href")) \
              and not "mailto" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
            or r".info/" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
            or r"/info" in str(link.get("href")) \
                  and not "privacy" in str(link.get("href")) \
                      and not "service" in str(link.get("href")) \
                          and not "recruit" in str(link.get("href")) \
                              and not "sdgs" in str(link.get("href")) \
                      or "お問い合わせ" in str(link.get("href")) \
                          and not r"/よくある質問" in str(link.get("href")) \
                          or "お問合せ" in str(link.get("href")) \
                              and not r"/よくある質問" in str(link.get("href")) \
                              or "お問い合せ" in str(link.get("href")) \
                                  and not r"/よくある質問" in str(link.get("href")) \
                                  or "お問合わせ" in str(link.get("href")) \
                                      and not r"/よくある質問" in str(link.get("href")) \
                                  or "mail" in str(link.get("href")) \
                                      and not "download" in str(link.get("href")) \
                                          and not "mailto" in str(link.get("href")) \
                                              and not "privacy" in str(link.get("href")) \
                                                  and not "service" in str(link.get("href")) \
                                                      and not "recruit" in str(link.get("href")) \
                                                          and not "sdgs" in str(link.get("href")) \
                                  or "mailto" in str(link.get("href")) \
                                          and not "privacy" in str(link.get("href")) \
                                              and not "service" in str(link.get("href")) \
                                                  and not "recruit" in str(link.get("href")) \
                                                      and not "sdgs" in str(link.get("href")) \
                     or "page_id=233" in str(link.get("href")) \
                         or "page_id=39" in str(link.get("href")) \
                             or "page_id=93" in str(link.get("href")) \
                        or "page_id=15" in str(link.get("href")) \
                          or "page_id=3781" in str(link.get("href")) \
                            or r"form.run" in str(link.get("href")) \
                              or r"form.php" in str(link.get("href")) \
                                or r"/form$" in str(link.get("href")) \
                                    or r"form.html" in str(link.get("href")) \
                                        or r"%e3%81%8a%e5%95%8f%e3%81%84%e5%90%88%e3%82%8f%e3%81%9b" in str(link.get("href")) \
                                            or r"ask.html" in str(link.get("href")) \
                                              or r"/ask" in str(link.get("href")) \
                                                or r"forms.gle" in str(link.get("href")) \
                                                    or "toiawase" in str(link.get("href")) \
                                                       and not "mailto" in str(link.get("href")):
       links_1.append(link.get("href"))   
       print(links_1)
       print(len(links_1))

#「http」で始まる文字列のリスト
#       if len([i for i in links_1 if r"^http" in i]) > 0:
     links_2 = [i for i in links_1 if "http" in i and r".info/contact" in i \
                      or "http" in i and not r"/faq" in i or "http" in i and not r"/info" in i \
                          or "http" in i and not "recruit" in i or "http" in i and r"/ask" in i \
                              or "http" in i and r"form2/B01" in i \
                                  or "http" in i and "contact" in i \
                                      or "http" in i and "mail" in i]
     print(len(links_2))
#それ以外（"http"は含めない）
#       elif len([j for j in links_1 if r"^http" in j]) == 0:
     links_3 = [j for j in links_1 if r"/contact" in j and not "http" in j \
                  or r"/CONTACT" in j and not "http" in j \
                      or r"/Contact" in j and not "http" in j \
                          or r"Contact/" in j and not "http" in j \
                              or r"mail/" in j and not "http" in j \
                          or r"#contact" in j and not "http" in j \
                              or r"#CONTACT" in j and not "http" in j \
                                  or r"#Contact" in j and not "http" in j \
                                      or not "05contact" in j and not "http" in j \
                                          or r"CONTACT" in j and not "http" in j \
                          or r"Contact" in j and not "http" in j \
                              or r"/お問い合わせ" in j and not "http" in j \
                                  or r"/お問合せ" in j and not "http" in j \
                                  or r"/お問い合せ" in j and not "http" in j \
                                      or r"/お問合わせ" in j and not "http" in j \
                                      or r"page_id" in j and not "http" in j \
                                          or r"ask" in j and not "http" in j \
                                          or r".info/contact" in j and not "http" in j \
                                      or r"%e3%81%8a%e5%95%8f%e3%81%84%e5%90%88%e3%82%8f%e3%81%9b" in j and not "http" in j \
                                          or r"contact.html" in j and not "http" in j \
                                              or r"/contact.html" in j and not "http" in j \
                                              or r"_contact" in j and not "http" in j \
                                                  or r"contact.php" in j and not "http" in j \
                                                  or r"/mail" in j and not "http" in j \
                                                      or r"forms.gle" in j and not "http" in j \
                                                      or r"form.run" in j and not "http" in j \
                                                          or r"section_contact" in j and not "http" in j \
                                                        or r"form.php" in j and not "http" in j \
                                                          or r"/form$" in j and not "http" in j \
                                                            or "toiawase" in j and not "mailto" in j and not "http" in j \
                                                              or "inq" in j and not "mailto" in j and not "http" in j \
                                                                  or "INQ" in j and not "mailto" in j and not "http" in j \
                                                                      or "Inq" in j and not "mailto" in j and not "http" in j]

     print(len(links_3))
#メールアドレス（今は使用しない）
     links_4 = [l for l in links_1 if "mailto" in l]
     print(links_4)
           
#       if "http" in link.get("href"):
    
#リストlinks_3、且つリストlinks_2が空でない    
     if not links_2 == [] and not links_3 == []:
           if len(links_2) == 1 and len(links_3) == 1:
            ws1.update_cell(k, 8, links_2[0])
            print(ws1.cell(k, 8).value)                         
#            ws1.update_cell(k, 9, ws1.cell(k, 5).value + links_3[0])
#            print(ws1.cell(k, 9).value)                         
            
           elif len(links_2) > 1 and len(links_3) == 1:
            for i in range(1,len(links_3)+1):    
             time.sleep(1)
             if r"//" in links_3[i-1]:
              ws1.update_cell(k, 8, r"https:" + links_3[i-1])
              print(ws1.cell(k, 8).value)
             else:
              ws1.update_cell(k, 8, ws1.cell(k, 5).value + links_3[i-1])
              print(ws1.cell(k, 8).value)
            
           elif len(links_2) == 1 and len(links_3) > 1:
            ws1.update_cell(k, 8, links_2[0])
            print(ws1.cell(k, 8).value)                                        
#            for j in range(1,len(links_3)):    
#             time.sleep(1)
#             ws1.update_cell(k, 9, links_3[j-1]) 
#             print(ws1.cell(k, 9).value)
             
           elif len(links_2) > 1 and len(links_3) > 1:           
            for i in range(1,len(links_2)):    
             time.sleep(1)
             ws1.update_cell(k, 8, links_2[i-1])
             print(ws1.cell(k, 8).value)           
#            for j in range(1,len(links_3)):    
#             time.sleep(1)            
#             ws1.update_cell(k, 9, ws1.cell(k, 5).value + links_3[j-1])
#             print(ws1.cell(k, 9).value)
   
#             if "contact" in ws1.cell(k, 9).value and not "http" in ws1.cell(k, 9).value:
#              time.sleep(1)
#              ws1.update_cell(k, 8, ws1.cell(k, 5).value + ws1.cell(k, 9).value)
#              print(ws1.cell(k, 8).value)
              
#リストlinks_3が空、且つリストlinks_2が空でない                   
     elif not links_2 == [] and links_3 == []:
           if len(links_2) == 1:
            ws1.update_cell(k, 8, links_2[0])
            print(ws1.cell(k, 8).value)
            break
           elif len(links_2) > 1:
            links_2 = [i for i in links_2 if "contact" in i \
                       or "page_id=93" in i]
            for i in range(1,len(links_2)+1):
             time.sleep(1)            
             ws1.update_cell(k, 8, links_2[i-1])           
             print(ws1.cell(k, 8).value)
#             break
#リストlinks_2が空、且つリストlinks_3が空でない        
     elif links_2 == [] and not links_3 == []:
           if len(links_3) == 1:
            ws1.update_cell(k, 8, ws1.cell(k, 5).value + links_3[0])
            print(ws1.cell(k, 8).value)                                 
           elif 1 <= len(links_3) <= 5:
            for j in range(1,len(links_3)):
             time.sleep(3) 
             ws1.update_cell(k, 8, ws1.cell(k, 5).value + links_3[j])
             print(ws1.cell(k, 8).value)
           elif len(links_3) > 5:
            for j in range(1,len(links_3)):
             time.sleep(3) 
             ws1.update_cell(k, 8, ws1.cell(k, 5).value + links_3[j-1])
             print(ws1.cell(k, 8).value)             
             break
         
#リストlink_4が空でない
     elif links_2 == [] and links_3 == [] and not links_4 == []:
            ws1.update_cell(k, 8, links_4[0])
            print(ws1.cell(k, 8).value)                                 
           
     elif links_2 == [] and links_3 == []:
            ws1.update_cell(k, 8, "-")                                 
     else:
        ws1.update_cell(k, 8, "-")
    else:
     ws1.update_cell(k, 8, "このサイトにアクセスできません")
   else:
    ws1.update_cell(k, 8, "-")

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