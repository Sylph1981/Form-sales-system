# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:13:46 2021

@author: iorin
"""

import gspread
import re
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Selectモジュールをインポート
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.alert import Alert
#from selenium.webdriver.support.ui import WebDriverWait

#例外処理用のlibraryをimport
from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import WebDriverException
#from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException

#Selectモジュールをインポート
#from selenium.webdriver.support.select import Select

#オプションの作成
option = Options()

#起動オプション
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
#option.add_argument('--headless')

#「unknown error: net::ERR_CONNECTION_CLOSED」の回避用
option.add_argument('--disable-dev-shm-usage')

#最初のHTMLドキュメントが完全に読み込まれて解析されるまで待機し、スタイルシート、画像、およびサブフレームの読み込みを破棄します。
option.page_load_strategy = 'eager'

# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome("C:/Users/iorin/OneDrive/ドキュメント/Python Scripts/chromedriver.exe",options=option)
driver.set_page_load_timeout(120)

#指定したdriverに対して最大で5秒間待つように設定する
#wait = WebDriverWait(driver, 5)

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name('inquiry-form-automatic-posting-6e2409a1cc4a.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#「キー」で取得
SPREADSHEET_KEY = '1FrygfVLHP8fMZh8HdBYboZtkg4fCH8lcDUsbQ58Hbqs'

wb = gc.open_by_key(SPREADSHEET_KEY)

#「名前」で取得
ws1 = wb.worksheet('imitsu')
ws2 = wb.worksheet('Profile')
ws3 = wb.worksheet('DM本文')
ws4 = wb.worksheet('DM本文_タイトル')
ws5 = wb.worksheet('SELECT')

start = time.time()
#ws1の行数を取得
lastrow = len(ws1.col_values(1))
for k in tqdm(range(114, 115)):
    
#シートの初期化
 ws5.clear()
 lastcol = len(list(ws1.row_values(k)))
 cell_list2 = ws1.range(k, 9, k, lastcol)
 print(cell_list2)
 for cell in cell_list2:
             cell.value = ""
#             time.sleep(1)
 ws1.update_cells(cell_list2)
 
   
# 入力されているk行目の配列を取得
# lastcol = len(list(ws1.row_values(k)))  
#UI2comboBox = Screen_Transition.ui2.comboBox.currentText(0)
#driver.get('https://www.ekiten.jp/gen_relax/' + UI2comboBox)
# try:
 if not ws1.cell(k, 8).value == r"-" \
       or not ws1.cell(k, 8).value == "" \
           or not ws1.cell(k, 8).value == r"Time out!!" \
               or not ws1.cell(k, 8).value == r"unknown error!!":
    driver.get(ws1.cell(k, 8).value)
    time.sleep(5)
 
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
#    print(soup)
#    print(soup.find("form"))

#    alert = driver.switch_to.alert
#    alert = wait.until(expected_conditions.alert_is_present())
#    text = alert.text
#    print(text)
    
    
#フォーム送信ＮＧ
    if "営業のご連絡" in html \
        or "営業のお問い合わせ" in html \
            or "営業を目的" in html \
                or "営業目的" in html \
                    or "営業メール" in html \
                        or "弊社への営業" in html \
                            or "広告メール" in html \
                                or "フォームからの営業" in html \
                                    or "セールスのお問い合わせ" in html:
     ws1.update_cell(k, 9, "営業お断り！！")
    elif "recaptcha" in html:
     ws1.update_cell(k, 9, "reCAPTCHA")
#    elif "予算" in str(soup.find_all("form")) \
#        or "納期" in str(soup.find_all("form")) \
#    or "サービスに関する" in str(soup.find_all("form")):
#     ws1.update_cell(k, 9, "サービスに関する専用フォーム")
    elif "無料相談" in html \
        or "に関するご相談" in str(soup.find_all("form")):
     ws1.update_cell(k, 9, "無料相談専用フォーム")
#    elif "求人" in html \
#        or "採用" in str(soup.find_all("form")):
#     ws1.update_cell(k, 9, "人材関連専用フォーム")
#自動送信対象     
    elif "確認" in str(soup.find_all("form")) \
        or "送信" in str(soup.find_all("form")) \
            or "お問い合わせ" in str(soup.find_all("form")) \
                or "メールアドレス" in str(soup.find_all("form")):
     ws1.update_cell(k, 9, "フォーム要素あり")


#labelタグのテキストを取得
     if "お問い合わせ" in str(soup.find_all("label")) \
         or "メールアドレス" in str(soup.find_all("label")):
      element1 = soup.find_all("label")
      list_1 = []   
      for list_ in element1:
        if "企業" in list_.getText() \
                or "社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                                        or "役職" in list_.getText() \
                                            or "部署" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "所在地" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                            or "姓" in list_.getText() \
                                                or "名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "TEL" in list_.getText() \
                                                or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "mail" in list_.getText() \
                                                        or "URL" in list_.getText() \
                                                            or "サイト" in list_.getText() \
                                                                or "ホームページ" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "件名" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText() \
                                                                                            or "項目" in list_.getText():
         list_1.append(re.sub("[\n]", "", list_.getText(), 3))
      print(list_1)

#tdタグのテキストを取得
     if "お問い合わせ" in str(soup.find_all("td")) \
         or "メールアドレス" in str(soup.find_all("td")):
      element1 = soup.find_all("td")
      list_1 = []   
      for list_ in element1:
        if "企業" in list_.getText() \
                or "社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                                        or "役職" in list_.getText() \
                                            or "部署" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "所在地" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                            or "姓" in list_.getText() \
                                                or "名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "TEL" in list_.getText() \
                                                or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "mail" in list_.getText() \
                                                        or "URL" in list_.getText() \
                                                            or "サイト" in list_.getText() \
                                                                or "ホームページ" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "件名" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText() \
                                                                                            or "項目" in list_.getText():
         list_1.append(re.sub("[\n]", "", list_.getText(), 3))
#         print(list_1)

#dtタグのテキストを取得
     if "お問い合わせ" in str(soup.find_all("dt")) \
         or "メールアドレス" in str(soup.find_all("dt")):
      element1 = soup.find_all("dt")
      list_1 = []   
      for list_ in element1:
        if "企業" in list_.getText() \
                or "社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                                        or "役職" in list_.getText() \
                                            or "部署" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "所在地" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                            or "姓" in list_.getText() \
                                                or "名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "TEL" in list_.getText() \
                                                or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "mail" in list_.getText() \
                                                        or "URL" in list_.getText() \
                                                            or "サイト" in list_.getText() \
                                                                or "ホームページ" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "件名" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText() \
                                                                                            or "項目" in list_.getText():
         list_1.append(re.sub("[\n]", "", list_.getText(), 3))
      print(list_1)

#pタグのテキストを取得
     if "お問い合わせ" in str(soup.find_all("p")) \
         or "メールアドレス" in str(soup.find_all("p")):
      element1 = soup.find_all("p")
      list_1 = []   
      for list_ in element1:
        if "企業" in list_.getText() \
                or "社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                                        or "役職" in list_.getText() \
                                            or "部署" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "所在地" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                            or "姓" in list_.getText() \
                                                or "名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "TEL" in list_.getText() \
                                                or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "mail" in list_.getText() \
                                                        or "URL" in list_.getText() \
                                                            or "サイト" in list_.getText() \
                                                                or "ホームページ" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "件名" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText() \
                                                                                            or "項目" in list_.getText():
         list_1.append(re.sub("[\n]", "", list_.getText(), 3))
#         print(list_1)

#thタグのテキストを取得
     if "お問い合わせ" in str(soup.find_all("th")) \
         or "メールアドレス" in str(soup.find_all("th")):
      element1 = soup.find_all("th")
      list_1 = []   
      for list_ in element1:
        if "企業" in list_.getText() \
                or "社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                                        or "役職" in list_.getText() \
                                            or "部署" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "所在地" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                            or "姓" in list_.getText() \
                                                or "名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "TEL" in list_.getText() \
                                                or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "mail" in list_.getText() \
                                                        or "URL" in list_.getText() \
                                                            or "サイト" in list_.getText() \
                                                                or "ホームページ" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "件名" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText() \
                                                                                            or "項目" in list_.getText():
         list_1.append(re.sub("[\n]", "", list_.getText(), 3))
      print(list_1)


#指定のタグからテキストを取得しない場合
     else:
      element1 = soup.find_all("form")
#      print(element1)
      list_1 = []   
      for list_ in element1:
        if "企業" in list_.getText() \
                or "社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                                        or "役職" in list_.getText() \
                                            or "部署" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                            or "姓" in list_.getText() \
                                                or "名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "TEL" in list_.getText() \
                                                or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "mail" in list_.getText() \
                                                        or "URL" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "件名" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText() \
                                                                                            or "項目" in list_.getText():
         list_1.append(re.sub("[\n]", "", list_.getText(), 3))
      print(list_1)

#文字列置換
     items_1 =[i.replace("必須", "") \
                .replace("半角英数字", "") \
                    .replace("全角漢字", "") \
                        .replace("携帯電話可", "") \
                            .replace("携帯可", "") \
                                .replace("全角", "") \
                                    .replace(r"()","") \
                                        .replace(r"（）","") \
                                            .replace(" ","") \
                                                .replace(r"*","") \
                                                    .replace(r"※","") \
                                                        .split(r"・")[0] \
                                                        for i in list_1]                  
#     print(items_1)

      
#inputタグの各要素を取得
     element2 = soup.find_all("input")
#      print(element2)
     list_2 = []
     list_2c = []
     list_2d = []
     list_2t = []

#各属性値
     for name in element2:
       list_2.append(name.get("name"))
#     print(list_2)
     print(len(list_2))
             
     for elem in element2:
#       items_1.append(name.get("placeholder"))
       list_2d.append(elem.get("id"))
#       print(items_2)


     for elem in element2:
#       items_1.append(name.get("placeholder"))
       list_2c.append(elem.get("class"))
#     print(list_2c)

     for elem in element2:
#       items_1.append(name.get("placeholder"))
       list_2t.append(elem.get("type"))
     print(list_2t)


#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理

#name値
#     if not len(list_2) == 0:
     list_2 = [i for i in list_2 if i is not None]
     print(list_2)
       
#id値
#     if not len(list_2d) == 0:
     list_2d = [i for i in list_2d if i is not None]
#     print(list_2d)

#class値
#     if not len(list_2c) == 0:
     list_2c = [i for i in list_2c if i is not None]
     print(list_2c)        


#ラジオボタン
     element5 = soup.find_all("input",type="radio")
#     print(element5)
     element6 = soup.find_all("input",class_="questionTypeRadio")
#     print(element6)
     element7 = soup.find_all("input",attrs={"name":"questioner_type","type":"radio"})
#     print(element7)
      
     SELECT_list1 = []
     SELECT_list2 = []
     SELECT_list3 = []
     SELECT_list4 = []
     SELECT_list5 = []

     for elem in element5: 
        SELECT_list1.append(elem.get("value"))
        SELECT_list1 = [i for i in SELECT_list1 if i is not None]
     print(SELECT_list1)

     for elem in element5:
        SELECT_list2.append(elem.get("id"))
        SELECT_list2 = [i for i in SELECT_list2 if i is not None]
     print(SELECT_list2)

     for elem in element6: 
        SELECT_list3.append(elem.get("id"))
        SELECT_list3 = [i for i in SELECT_list3 if i is not None]
#        print(SELECT_list3)

     for elem in element7: 
        SELECT_list4.append(elem.get("id"))
        SELECT_list4 = [i for i in SELECT_list4 if i is not None]
     print(SELECT_list4)

     for elem in element5:
        SELECT_list5.append(elem.get("name"))
        SELECT_list5 = [i for i in SELECT_list5 if i is not None]
     print(SELECT_list5)

        
#value値のみ、id値なしの場合
     if len(SELECT_list1) > 0 \
          and len(SELECT_list2) == 0 \
              and len(SELECT_list3) == 0 \
                  and len(SELECT_list4) == 0 \
                      and len(SELECT_list5) == 0:
       print(len(SELECT_list1))
       print(len(SELECT_list2))
       print(len(SELECT_list3))
       print(len(SELECT_list4))
       print(len(SELECT_list5))

#（区別）
       if len([i for i in SELECT_list1 if "法人" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='法人']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "法人")
           print(radiobutton.is_selected())

#（種別）
       if len([i for i in SELECT_list1 if "その他" == i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='その他']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(radiobutton.is_selected())
           
#（アンケート）
       if "知りましたか" in str(soup.find_all("form")) \
           and len([i for i in list_2 if "知りましたか" in i]) > 0:
        radiobutton = driver.find_element_by_name(SELECT_list5[0])
        print(SELECT_list5[0])
        driver.execute_script("arguments[0].click();", radiobutton)
        print(radiobutton.is_selected())
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, SELECT_list5[0])
        Cell_list9 = [i for i in list_2 if "知りましたか" in i]
        print(Cell_list9)
        driver.find_element_by_name(Cell_list9[0]).send_keys(ws2.cell(1, 3).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, ws2.cell(1, 3).value)
            
#（連絡方法）
       if len([i for i in SELECT_list1 if "メール" in i]) > 0:
         radiobutton = driver.find_element_by_css_selector("[value='メール']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "メール")
           print(radiobutton.is_selected())


#value値及びid値有りの場合
     elif len(SELECT_list1) > 0 \
          and len(SELECT_list2) > 0 \
              and len(SELECT_list3) == 0 \
                  and len(SELECT_list4) == 0:
       print(len(SELECT_list1))
       print(len(SELECT_list2))
       print(len(SELECT_list3))
       print(len(SELECT_list4))

#（区別）
       if len([i for i in SELECT_list1 if "法人" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='法人']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "法人")
           print(radiobutton.is_selected())

#（種別）
       if "種別" in str(soup.find_all("form")) \
           or "項目" in str(soup.find_all("form")) \
               or "内容" in str(soup.find_all("form")):
        try:
         radiobutton = driver.find_elements_by_name(SELECT_list5[len(SELECT_list5)-1])[len(SELECT_list5)-1]
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         lastcol = len(list(ws1.row_values(k)))                
         ws1.update_cell(k, lastcol+1, "その他")

#操作できない要素の回避
        except NoSuchElementException:
         try:   
          radiobutton = driver.find_element_by_css_selector("[value='その他']")
          driver.execute_script("arguments[0].click();", radiobutton)
          print(radiobutton.is_selected())
          lastcol = len(list(ws1.row_values(k)))                
          ws1.update_cell(k, lastcol+1, "その他")

#操作できない要素の回避
         except NoSuchElementException:
           pass

#value値及びname値有りの場合
     elif len(SELECT_list1) > 0 \
          and len(SELECT_list2) == 0 \
              and len(SELECT_list3) == 0 \
                  and len(SELECT_list4) == 0 \
                      and len(SELECT_list5) > 0:
       print(len(SELECT_list1))
       print(len(SELECT_list2))
       print(len(SELECT_list3))
       print(len(SELECT_list4))
       print(len(SELECT_list5))

#（区別）
       if len([i for i in SELECT_list1 if "法人" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='法人']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "法人")
           print(radiobutton.is_selected())

#（種別）
       if "種別" in str(soup.find_all("form")) \
           or "項目" in str(soup.find_all("form")) \
               or "内容" in str(soup.find_all("form")) \
                   or "件名" in str(soup.find_all("form")):
#        radiobutton = driver.find_elements_by_name(SELECT_list5[len(SELECT_list5)-1])[len(SELECT_list5)-1]
        radiobutton = driver.find_element_by_css_selector("[value='other']")
        driver.execute_script("arguments[0].click();", radiobutton)
        print(radiobutton.is_selected())
        if radiobutton.is_selected() is True:        
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)
         ws1.update_cell(k, lastcol+1, "その他")


#id値有りの場合（パターン注意）
     elif len(SELECT_list3) > 0 \
          and len(SELECT_list4) > 0:
       print(len(SELECT_list3))
       print(len(SELECT_list4))

#（種別）
       if len([i for i in items_1 if "種別" in i]) == 1:
         radiobutton = driver.find_element_by_id(SELECT_list3[len(SELECT_list3)-1])
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list3[len(SELECT_list3)-1])
           print(radiobutton.is_selected())

#（法人／個人）
     if len([i for i in items_1 if "法人" in i]) == 1:
         radiobutton = driver.find_element_by_id(SELECT_list4[0])
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[0])
           print(radiobutton.is_selected())

      
#会社名
     if len([i for i in items_1 if "社名" in i \
               or "企業" in i]) == 0 \
                   and len([i for i in list_2 if "社名" in i \
               or "企業" in i]) == 0:
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "会社名入力欄なし")

#（Googleフォーム）
     elif not len([i for i in list_2c if "exportInput" in i]) == 0:
      driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput.exportInput")[1].send_keys(ws2.cell(2, 2).value)
      lastcol = len(list(ws1.row_values(k)))
      time.sleep(3)
      ws1.update_cell(k, lastcol+1, "会社名")

     elif not len([i for i in items_1 if "社名" in i \
               or "企業" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                      or "organization" in i \
                     or "your-company" in i \
                         or "company-name" in i \
                             or "kaisha-name" in i \
                             or "company" == i \
                                 or "contact_company" == i \
                                 or "campany" in i \
                                 or "your-corp" in i \
                                     or "corporate" in i \
                                         or "企業" in i \
                                             or "社名" in i \
                                                 or "text-978" == i \
                                                     or "Company" in i \
                                                         or "company3" == i]
        driver.find_element_by_name(Cell_list1[0]).send_keys(ws2.cell(2, 2).value + "　")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "会社名")
        print(Cell_list1)

     elif not len([i for i in list_2 if "facility" in i \
               or "organization" in i \
                     or "your-company" in i \
                         or "company-name" in i \
                             or "company" == i \
                                 or "contact_company" == i \
                                 or "campany" in i \
                                 or "your-corp" in i \
                                     or "corporate" in i \
                             or "name" in i \
                                         or "企業" in i \
                                             or "社名" in i \
                                                 or "text-978" == i \
                                                     or "Company" in i \
                                                         or "company3" == i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                      or "organization" in i \
                     or "your-company" in i \
                         or "company-name" in i \
                             or "company" == i \
                                 or "contact_company" == i \
                                 or "campany" in i \
                                 or "your-corp" in i \
                                     or "corporate" in i \
                             or "name" in i \
                                         or "企業" in i \
                                             or "社名" in i \
                                                 or "text-978" == i \
                                                     or "Company" in i \
                                                         or "company3" == i]
        print(Cell_list1)
        driver.find_element_by_name(Cell_list1[0]).send_keys(ws2.cell(2, 2).value + "　")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "会社名")


     elif len([i for i in list_2 if "facility" in i \
               or "organization" in i \
                     or "your-company" in i \
                         or "company-name" in i \
                             or "company" == i \
                                 or "contact_company" == i \
                                 or "campany" in i \
                                 or "your-corp" in i \
                                     or "corporate" in i \
                             or "name" in i \
                                         or "企業" in i \
                                             or "社名" in i \
                                                 or "text-978" == i \
                                                     or "Company" in i \
                                                         or "company3" == i]) == 0:
        Cell_list1 = [i for i in list_2c if "facility" in i \
                      or "organization" in i \
                     or "your-company" in i \
                         or "company-name" in i \
                             or "company" == i \
                                 or "contact_company" == i \
                                 or "campany" in i \
                                 or "your-corp" in i \
                                     or "corporate" in i \
                             or "name" in i \
                                             or "企業" in i \
                                                 or "社名" in i \
                                                 or "text-978" == i \
                                                     or "Company" in i \
                                                         or "company3" == i]
        print(Cell_list1)
        driver.find_elements_by_class_name(Cell_list1[0])[1].send_keys(ws2.cell(2, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "会社名")


#会社名ふりがな
     if len([i for i in list_1 if "ふりがな（カナ）" in i]) == 0:
         pass
     elif len([i for i in list_1 if "ふりがな（カナ）" in i]) > 0:
       Cell_list2 = [i for i in list_2 if "企業名ふりがな（カナ）" in i]
       print(Cell_list2)
#テキスト入力
       driver.find_element_by_name(Cell_list2[0]).send_keys(ws2.cell(3, 2).value)
       lastcol = len(list(ws1.row_values(k)))       
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "会社名カナ")


#フルネーム（氏名）
#     if len([i for i in items_1 if "担当者" in i \
#               or "名前" in i \
#                   or "氏名" in i]) == 0 \
#                       and len([i for i in list_2 if "担当者" in i \
#               or "名前" in i \
#                   or "氏名" in i]) == 0:
#        lastcol = len(list(ws1.row_values(k)))
#        time.sleep(1) 
#        ws1.update_cell(k, lastcol+1, "氏名入力欄なし")
        
#（Googleフォーム）
     if not len([i for i in list_2c if "exportInput" in i]) == 0:
      driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput.exportInput")[0].send_keys(ws2.cell(6, 2).value)
      lastcol = len(list(ws1.row_values(k)))
      time.sleep(3)
      ws1.update_cell(k, lastcol+1, "氏名")

     elif not len([i for i in items_1 if "担当者" in i \
               or "名前" in i \
                   or "氏名" in i \
                       or "姓" in i \
                           or "名" in i]) == 0 \
                       or not len([i for i in list_2 if "担当者" in i \
               or "名前" in i \
                   or "氏名" in i]) == 0:

#フルネーム（姓＋名）
      if len([i for i in list_2 if "姓" == i \
                 or "firstName" == i \
                     or "first_name" == i \
                         or "name1" == i \
                             or "FirstName" in i \
                      or "名" == i \
                          or "lastName" == i \
                              or "name2" == i \
                                  or "LastName" in i \
                                      or "name3" in i]) > 0:
         Cell_list3 = [i for i in list_2 if "姓" == i \
                 or "firstName" == i \
                     or "first_name" == i \
                         or "name1" == i \
                             or "FirstName" in i \
                      or "名" == i \
                          or "lastName" == i \
                              or "name2" == i \
                                  or "LastName" in i \
                                      or "name3" in i]
         print(Cell_list3)
         for j in range(1,len(Cell_list3)+1):
          elemName0 = driver.find_element_by_name(Cell_list3[0])
          elemName1 = driver.find_element_by_name(Cell_list3[1])
          elemName2 = driver.find_element_by_name(Cell_list3[2])
          try:
           if elemName0.is_displayed() is False \
               or elemName1.is_displayed() is False \
                   or elemName2.is_displayed() is False:
               print(Cell_list3[j-1])
               if "1" in Cell_list3[j-1]:
                driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(6, 3).value
                                                                       + ws2.cell(6, 4).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "氏名")

               elif "2" in Cell_list3[j-1]:
                driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(6, 3).value
                                                                       + ws2.cell(6, 4).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "氏名")

               elif "3" in Cell_list3[j-1]:
                driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(6, 3).value
                                                                       + ws2.cell(6, 4).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "氏名")

           else:
               driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(6, 2+j).value)
               lastcol = len(list(ws1.row_values(k)))
               time.sleep(1) 
               ws1.update_cell(k, lastcol+1, ws1.cell(6, 2+j).value)
#操作できない要素の回避
          except ElementNotInteractableException:
            pass
        
#フルネーム（通常パターン）
      elif not len([i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "contact_name" in i \
                         or "名前" in i \
                             or "f4a6f2b" in i \
                                 or "担当者" in i \
                                     or "氏名" in i \
                                         or "name" == i \
                                             or "name1" == i \
                                                 or "text-978" == i \
                                                     or "firstname" == i \
                                                         or "full_name" == i]) == 0:
        Cell_list3 = [i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "contact_name" in i \
                         or "名前" in i \
                             or "f4a6f2b" in i \
                                 or "担当者" in i \
                                     or "氏名" in i \
                                         or "name" == i \
                                             or "name1" == i \
                                                 or "text-978" == i \
                                                     or "firstname" == i \
                                                         or "full_name" == i]
        print(Cell_list3)
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "氏名")

      elif len([i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "contact_name" in i \
                         or "名前" in i \
                             or "f4a6f2b" in i \
                                 or "担当者" in i \
                                     or "氏名" in i \
                                         or "name" == i \
                                             or "name1" == i]) == 0:
        Cell_list3 = [i for i in list_2d if r"user_name" in i \
                     or r"your-name" in i \
                         or "contact_name" in i \
                         or "名前" in i \
                             or "f4a6f2b" in i \
                                 or "担当者" in i \
                                     or "氏名" in i \
                                         or "name" == i \
                                             or "name1" == i]
        print(Cell_list3)
        driver.find_element_by_id(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "氏名")

      elif len([i for i in list_2d if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "contact_name" in i \
                             or "f4a6f2b" in i \
                                 or "担当者" in i \
                                     or "氏名" in i \
                                         or "name" == i \
                                             or "name1" == i]) == 0:
        Cell_list3 = [i for i in list_2c if r"user_name" in i \
                     or r"your-name" in i \
                         or "contact_name" in i \
                         or "名前" in i \
                             or "f4a6f2b" in i \
                                 or "担当者" in i \
                                     or "氏名" in i \
                                             or "name" == i \
                                                 or "name1" == i]
        print(Cell_list3)
        driver.find_elements_by_class_name(list_2c[0])[0].send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "氏名")


#フルネームふりがな
     if len([i for i in list_1 if "ふりがな" in i]) == 0:
      pass
     elif not len([i for i in list_1 if "ふりがな" in i]) == 0:
       if len([i for i in list_2 if "せい" == i \
                      or "めい" == i]) > 0:
        Cell_list5 = [i for i in list_2 if "せい" == i \
                      or "めい" == i]
        print(Cell_list5)
        for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)
       elif len([i for i in list_2 if "your-kana" in i \
                     or "userKana" in i \
                         or "personal_kana_name" in i \
                             or "name_ruby" in i
                             or "ふりがな" in i]) > 0:
        Cell_list5 = [i for i in list_2 if "your-kana" in i \
                     or "userKana" in i \
                         or "personal_kana_name" in i \
                             or "name_ruby" in i
                             or "ふりがな" in i]
        print(Cell_list5)
        driver.find_element_by_name(Cell_list5[0]).send_keys(ws2.cell(7, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "氏名ふりがな")


#フルネームカタカナ
     if len([i for i in list_1 if "フリガナ" in i]) == 0:
         pass
     elif not len([i for i in list_1 if "フリガナ" in i]) == 0:
         
#（セイ＋メイ）
       if len([i for i in list_2 if "セイ" == i \
                     or "メイ" == i \
                         or "firstKanaName" == i \
                             or "lastKanaName" == i \
                                 or "kana_first_name" in i \
                                     or "kana_last_name" in i]) > 0:
        Cell_list5 = [i for i in list_2 if "セイ" == i \
                     or "メイ" == i \
                         or "firstKanaName" == i \
                             or "lastKanaName" == i \
                                 or "kana_first_name" in i \
                                     or "kana_last_name" in i]
        print(Cell_list5)
        for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(8, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(8, 2+j).value)

#（セイメイ）
       elif len([i for i in list_2 if "your-kana" in i \
                     or "name_furi" in i \
                         or "フリガナ" in i \
                             or "name1-kana" == i \
                                 or "furigana" == i]) > 0:
        Cell_list5 = [i for i in list_2 if "your-kana" in i \
                     or "name_furi" in i \
                         or "フリガナ" in i \
                             or "name1-kana" == i \
                                 or "furigana" == i]
        print(Cell_list5)
        driver.find_element_by_name(Cell_list5[0]).send_keys(ws2.cell(8, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "氏名フリガナ")


#電話番号

#（入力欄なしの場合は何もしない）
     if len([i for i in list_1 if "電話" in i \
                  or "TEL" in i]) == 0 \
         and len([i for i in list_2 if "電話" in i \
                  or "TEL" in i \
                      or "tel" in i \
                          or "Tel" in i \
                              or "phone" in i]) == 0:
             print(len([i for i in list_1 if "電話" in i \
                  or "TEL" in i]))
             print(len([i for i in list_2 if "電話" in i \
                  or "TEL" in i \
                      or "tel" in i \
                          or "Tel" in i \
                              or "phone" in i]))
             pass

#（ハイフン有り）
     elif not len([i for i in list_1 if "電話" in i \
                  or "TEL" in i]) == 0 \
                  or len([i for i in list_2 if "電話" in i \
                  or "TEL" in i \
                      or "tel" in i \
                          or "Tel" in i \
                              or "phone" in i \
                                  or "Phone" in i]) > 0:
         Cell_list7 = [i for i in list_2 if "tel" in i \
                      or "TEL" in i \
                          or "Tel" in i \
                              or "電話" in i \
                                  or "phone" in i \
                                      or "Phone" in i]
         print(Cell_list7)

         if len(Cell_list7) > 1:
          elemName0 = driver.find_element_by_name(Cell_list7[0])
          elemName1 = driver.find_element_by_name(Cell_list7[1])
          elemName2 = driver.find_element_by_name(Cell_list7[2])
          try:
           if elemName0.is_displayed() is False \
               or elemName1.is_displayed() is False \
                   or elemName2.is_displayed() is False:
               print(Cell_list7[j-1])
               if "1" in Cell_list7[j-1]:
                driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(14, 2).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")

               elif "2" in Cell_list7[j-1]:
                driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(14, 2).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")

               elif "3" in Cell_list7[j-1]:
                driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(14, 2).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")

#操作できない要素の回避
          except ElementNotInteractableException:
           pass

         elif len(Cell_list7) == 1:
            driver.find_element_by_name(Cell_list7[0]).send_keys(ws2.cell(14, 2).value)
            lastcol = len(list(ws1.row_values(k)))
            time.sleep(1) 
            ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")


     elif len(list_2d) > 0:
       if len([i for i in list_2 if "tel" in i \
                or "TEL" in i \
                     or "電話" in i \
                             or "phone" in i \
                                  or "Phone" in i]) == 0:
         Cell_list7 = [i for i in list_2d if "tel" in i \
                      or "TEL" in i \
                          or "Tel" in i \
                              or "電話" in i \
                                  or "phone" in i \
                                      or "Phone" in i]
         print(Cell_list7)
         driver.find_element_by_id(Cell_list7[0]).send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1) 
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")

     elif len(list_2c) > 0:
       if len([i for i in list_2d if "tel" in i \
                      or "TEL" in i \
                          or "Tel" in i \
                              or "電話" in i \
                                  or "phone" in i \
                                      or "Phone" in i]) == 0:
         driver.find_elements_by_class_name(list_2c[0])[1].send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1) 
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")


#（ハイフンなし市外局番別）
     elif not len([i for i in list_1 if "電話" in i \
                  or "TEL" in i]) == 0 \
         and len([i for i in list_2 if "[0]" in i \
                  or "[1]" in i \
                      or "tel1" in i]) > 0:
        Cell_list7 = [i for i in list_2 if "tel" in i \
                      or "TEL" in i \
                          or "Tel" in i \
                              or "電話" in i \
                                  or "phone" in i \
                                      or "Phone" in i]

        for j in range(1, len(Cell_list7)+1):
          driver.find_element_by_name(Cell_list7[j-1]) \
           .send_keys(ws2.cell(14, 2+j).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)         
            
#（ハイフンなし）
     elif not len([i for i in items_1 if "電話" in i \
                  or "TEL" in i \
                      and "ハイフンなし" in i]) == 0:
        Cell_list7 = [i for i in list_2 if "tel" in i \
                      or "TEL" in i \
                          or "Tel" in i \
                              or "電話" in i \
                                  or "phone" in i \
                                      or "Phone" in i]
        print(Cell_list7)
        driver.find_element_by_name(Cell_list7[0]).send_keys(ws2.cell(14, 3).value \
                                                             + ws2.cell(14, 4).value \
                                                                 + ws2.cell(14, 5).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "電話（ハイフンなし）")


#住所（郵便番号＋都道府県＋市区町村＋建物名）
     if len([i for i in list_1 if "郵便番号" in i \
             or "住所" in i \
                 or "都道府県" in i \
                     or "所在地" in i]) == 0:
#         or len([i for i in list_2 if "address" == i \
#                       or "addr" == i \
#                          or "住所" in i \
#                              or "所在地" in i]) == 0:
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "住所入力欄なし")

#（郵便番号入力から開始）
     elif len([i for i in items_1 if "郵便番号" in i]) > 0:
       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i \
                         or "postalCode" in i \
                             or "zip" in i]
       print(Cell_list6)
       if len(Cell_list6) > 0:
        driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(4, 3).value + ws2.cell(4, 4).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "郵便番号")
                
       if len([i for i in items_1 if "住所" in i]) > 0 \
           or len([i for i in list_2 if "address" == i \
                      or "city" in i]) > 0:
        Cell_list6 = [i for i in list_2 if "address" == i \
                      or "city" in i]
        print(Cell_list6)

        
#郵便番号以降の住所入力が連番（0～4）
        if len([i for i in Cell_list6 if "0" in i \
                or "1" in i \
                    or "2" in i \
                         or "3" in i \
                             or "4" in i]) > 0:
         Cell_list7 =[i for i in Cell_list6 if "1" in i \
                     or "2" in i \
                         or "3" in i \
                             or "4" in i]
         print(Cell_list7)
         if len([i for i in items_1 if "マンション" in i \
                 or "ビル" in i]) > 0:
          for j in range(1,len(Cell_list7)):
           driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)
           ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)
           driver.find_element_by_name(Cell_list7[len(Cell_list7)+1]).send_keys(ws2.cell(5, 5).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)
           ws1.update_cell(k, lastcol+1, ws2.cell(5, 5).value)
         elif len([i for i in items_1 if "マンション" in i \
                 or "ビル" in i]) == 0:
          for j in range(1,len(Cell_list7)+1):
           driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)
#         else:
#           driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(5, 2).value \
#                                                                + ws2.cell(5, 3).value \
#                                                                   + ws2.cell(5, 4).value \
#                                                                       + ws2.cell(5, 5).value)
#           lastcol = len(list(ws1.row_values(k)))
#           time.sleep(1)             
#           ws1.update_cell(k, lastcol+1, "住所")


#郵便番号以降の住所入力が連番でない（値：都道府県・市区町村・建物名毎）

#（「都道府県」～「建物」の全てがテキストに含まれない）
        elif len([i for i in Cell_list6 if "0" in i or "1" in i]) == 0 \
            and len([i for i in list_1 if "都道府県" in i \
                     and "市区町村" in i \
                         or "市町村" in i \
                         and "ビル" in i \
                             or "建物" in i]) == 0:
         Municipal = driver.find_element_by_name(Cell_list6[0])
         Municipal.clear()   
         Municipal.send_keys(ws2.cell(5, 2).value \
                             + ws2.cell(5, 3).value \
                                 + ws2.cell(5, 4).value \
                                     + ws2.cell(5, 5).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "住所")


#「都道府県」～「建物」がテキストに含まれる         
        elif len([i for i in Cell_list6 if "0" in i or "1" in i]) == 0 \
            and len([i for i in items_1 if "都道府県" in i]) > 0:
         Cell_list5 = [i for i in list_2 if "pref" in i]
         pref = driver.find_element_by_name(Cell_list5[0])
         pref.clear()
         pref.send_keys("東京都")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "都道府県")

#（都道府県＋市区町村）
         if len([i for i in Cell_list6 if "0" in i or "1" in i]) == 0 \
             and len([i for i in items_1 if "都道府県" in i]) > 0 \
                 and len([i for i in items_1 if "市区町村" in i \
                         and "市区町村" in i]) > 0:
             Municipal = driver.find_element_by_name(Cell_list6[0])
             Municipal.clear()
             Municipal.send_keys(ws2.cell(5, 3).value + ws2.cell(5, 4).value)
             lastcol = len(list(ws1.row_values(k)))
             time.sleep(1)             
             ws1.update_cell(k, lastcol+1, "市区町村")

#（都道府県＋市区町村＋建物）
             if len([i for i in Cell_list6 if "0" in i or "1" in i]) == 0 \
               and len([i for i in items_1 if "都道府県" in i]) > 0 \
                  and len([i for i in items_1 if "市区町村" in i \
                         and "市区町村" in i]) > 0 \
                    and len([i for i in items_1 if "ビル" in i \
                             or "建物" in i \
                                 or "マンション" in i]) > 0:
              Cell_list7 = [i for i in list_2 if "build" in i \
                           or "address_name" in i]
              Building = driver.find_element_by_name(Cell_list7[0])
              Building.clear()   
              Building.send_keys(ws2.cell(5, 5).value )
              lastcol = len(list(ws1.row_values(k)))
              time.sleep(1)             
              ws1.update_cell(k, lastcol+1, "建物名")
             
#       if len([i for i in items_1 if "建物" in i]) > 0:
#        Cell_list6 = [i for i in list_2 if "address_name" in i]
#        print(Cell_list6)
#        build = driver.find_element_by_name(Cell_list6[0])
#        build.send_keys(ws2.cell(5, 5).value)
#        lastcol = len(list(ws1.row_values(k)))
#        time.sleep(1)             
#        ws1.update_cell(k, lastcol+1, "建物名")        

#（都道府県入力から開始）
     elif len([i for i in items_1 if "都道府県" in i \
               or "住所" in i]) > 0:
       Cell_list6 = [i for i in list_2 if "都道府県" in i \
                     or "your-address" in i \
                         or "your-add" in i]
       print(Cell_list6)

       if len([i for i in Cell_list6 if "0" in i or "1" in i]) > 0:
        Cell_list7 =[i for i in Cell_list6 if "1" in i \
                     or "2" in i \
                         or "3" in i \
                             or "4" in i]
        print(Cell_list7)
        if len(Cell_list7) == 2:
              driver.find_element_by_name(Cell_list7[0]).send_keys(ws2.cell(5, 2).value
                                                                     + ws2.cell(5, 3).value)
              driver.find_element_by_name(Cell_list7[1]).send_keys(ws2.cell(5, 4).value
                                                                     + ws2.cell(5, 5).value)              
              lastcol = len(list(ws1.row_values(k)))
              time.sleep(1)             
              ws1.update_cell(k, lastcol+1, "住所")
        elif len(Cell_list7) > 2:
          for j in range(1,len(Cell_list7)+1):
            driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
            lastcol = len(list(ws1.row_values(k)))
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)


#郵便番号～住所

#（郵便番号入力欄１個）
     elif len([i for i in list_1 if "住所" in i]) > 0 \
       and len([i for i in list_2 if "郵便番号" in i \
                or "your-post" in i \
                         or "zip" in i \
                             or "code" in i]) > 0:
         Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i \
                         or "zip" in i \
                             or "code" in i]
         print(Cell_list6)
         driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(4, 3).value + ws2.cell(4, 4).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)
         ws1.update_cell(k, lastcol+1, "郵便番号")
         
         if len([i for i in list_1 if "住所" in i]) > 0 \
          and len([i for i in list_2 if "address1" in i \
                  or "adress1" in i \
                      or "住所1" in i]) > 0:
          Cell_list6 = [i for i in list_2 if "adr" in i \
                      or "addr" in i \
                          or "住所" in i]
          print(Cell_list6)
          for j in range(1,len(Cell_list6)+1):
           driver.find_element_by_name(Cell_list6[j-1]).clear()
           driver.find_element_by_name(Cell_list6[j-1]).send_keys(ws2.cell(5, 1+j).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)
           ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)

         elif len([i for i in list_1 if "住所" in i]) > 0 \
          and len([i for i in list_2 if "address" == i \
                  or "addr" == i \
                      or "adr" == i \
                          or "住所" == i]) > 0:
          Cell_list6 = [i for i in list_2 if "address" == i \
                      or "addr" == i \
                          or "adr" == i \
                              or "住所" == i]
          driver.find_element_by_name(Cell_list6[0]).clear()
          driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(5, 2).value \
                                                             + ws2.cell(5, 3).value \
                                                                 + ws2.cell(5, 4).value \
                                                                     + ws2.cell(5, 5).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)
          ws1.update_cell(k, lastcol+1, "住所")
         

#郵便番号入力欄２個
     elif len([i for i in list_1 if "住所" in i]) > 0 \
       and len([i for i in list_2 if "郵便番号" in i \
                or "your-post" in i \
                         or "zip" in i]) > 1:
         Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i \
                         or "zip" in i]
         print(Cell_list6)
         for j in range(1,len(Cell_list6)+1):
           driver.find_element_by_name(Cell_list6[j-1]).send_keys(ws2.cell(4, 2+j).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)
           ws1.update_cell(k, lastcol+1, ws2.cell(4, 2+j).value)


         if len([i for i in items_1 if "住所" in i]) > 0 \
          and len([i for i in list_2 if "address1" in i \
                  or "adress1" in i \
                      or "住所1"]) > 0:
          Cell_list6 = [i for i in list_2 if "adr" in i \
                      or "addr" in i \
                          or "住所" in i]
          print(Cell_list6)
          for j in range(1,len(Cell_list6)+1):
           driver.find_element_by_name(Cell_list6[j-1]).clear()
           driver.find_element_by_name(Cell_list6[j-1]).send_keys(ws2.cell(5, 1+j).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)
           ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)

         elif len([i for i in items_1 if "住所" in i]) > 0:
          Cell_list6 = [i for i in list_2 if "address" == i \
                      or "addr" == i \
                          or "住所" == i]
          driver.find_element_by_name(Cell_list6[0]).clear()
          driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(5, 2).value \
                                                             + ws2.cell(5, 3).value \
                                                                 + ws2.cell(5, 4).value \
                                                                     + ws2.cell(5, 5).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)
          ws1.update_cell(k, lastcol+1, "住所")

         else:
          Municipal = driver.find_element_by_name(Cell_list6[0])
          Municipal.clear()   
          Municipal.send_keys(ws2.cell(5, 3).value + ws2.cell(5, 4).value + "　")
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, "市区町村")
          if len([i for i in items_1 if "建物" in i \
               or "ビル" in i]) > 0:
           Cell_list6 = [i for i in list_2 if "address_name" in i \
                       or "住所" in i]
           print(Cell_list6)
           build = driver.find_element_by_name(Cell_list6[0])
           build.send_keys(ws2.cell(5, 5).value)
           lastcol = len(list(ws1.row_values(k)))
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "建物名")        
        
#（郵便番号入力欄なし）
     elif len([i for i in list_1 if "住所" in i \
               or "所在地" in i]) > 0 \
         or len([i for i in list_2 if "住所" in i]) > 0 \
       and len([i for i in list_1 if "郵便番号" in i]) == 0:
         Cell_list6 = [i for i in list_2 if "address" == i \
                       or "addr" == i \
                          or "住所" in i \
                              or "所在地" in i]
             
         if not Cell_list6 == []:
          print(Cell_list6)
          driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(5, 2).value \
                                                             + ws2.cell(5, 3).value \
                                                                 + ws2.cell(5, 4).value \
                                                                     + ws2.cell(5, 5).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)
          ws1.update_cell(k, lastcol+1, "住所")
         
        
#（テキストに市町村、アパートが含まれない場合は都道府県のみ）
     elif len([i for i in items_1 if "都道府県" in i]) > 0:
       Cell_list6 = [i for i in list_2 if "pref" in i]
       print(Cell_list6)
       pref = driver.find_element_by_name(Cell_list6[0])
       pref.clear()
       pref.send_keys("東京都")
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "都道府県")

       if len([i for i in items_1 if "市町村" in i]) > 0:
        Cell_list6 = [i for i in list_2 if "市町村" in i]
        print(Cell_list6)
        Municipal = driver.find_element_by_name(Cell_list6[0])
        Municipal.clear()   
        Municipal.send_keys("新宿区新宿5-4-1")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "市区町村")

        if len([i for i in items_1 if "アパート" in i]) > 0:
         Cell_list6 = [i for i in list_2 if "アパート" in i]
         print(Cell_list6)
         build = driver.find_element_by_name(Cell_list6[0])
         build.send_keys("新宿Qフラットビル8F")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "アパート")       

                           
#メールアドレス

#（Googleフォーム）
     if not len([i for i in list_2c if "exportInput" in i]) == 0:
      driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput.exportInput")[2].send_keys(ws2.cell(17, 2).value)
      lastcol = len(list(ws1.row_values(k)))
      time.sleep(3)
      ws1.update_cell(k, lastcol+1, "メールアドレス")

#（タグテキストに含まれる）
     elif not len([i for i in list_1 if "メールアドレス" in i \
                   or "MAIL" in i]) == 0:
       if not len([i for i in list_2 if "mail" in i \
                  or "メール" in i]) == 0:
         
        Cell_list8 = [i for i in list_2 if "mail" in i \
                     or "メール" in i \
                         or "confirm" in i]
        print(Cell_list8)
        for j in range(1,len(Cell_list8)+1):
            try:
             if "biz" in ws2.cell(17, 2).value:
              driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
              print(Cell_list8[j-1])
              lastcol = len(list(ws1.row_values(k)))
              time.sleep(3)
              ws1.update_cell(k, lastcol+1, "メールアドレス")
              
#操作できない要素の回避
            except ElementNotInteractableException:
              pass
          
       elif len([i for i in list_2 if "mail" in i \
                  or "メール" in i]) == 0:
         Cell_list8 = [i for i in list_2c if "mail" in i \
                           or "メール" in i]
#         for j in range(1,len(Cell_list8)+1):
         driver.find_elements_by_class_name(Cell_list8[0])[2].send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[0])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
         ws1.update_cell(k, lastcol+1, "メールアドレス")

       elif len([i for i in list_2c if "mail" in i \
                  or "メール" in i]) == 0:
         Cell_list8 = [i for i in list_2d if "mail" in i \
                     or "メール" in i]
         for j in range(1,len(Cell_list8)+1):
          driver.find_element_by_id(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1) 
          ws1.update_cell(k, lastcol+1, "メールアドレス")

#（タグテキストに含まれない）
     elif len([i for i in list_1 if "メールアドレス" in i \
               or "MAIL" in i]) == 0:
       if not len([i for i in list_2 if "mail" in i \
                  or "メール" in i]) == 0:
         
        Cell_list8 = [i for i in list_2 if "mail" in i \
                     or "メール" in i]
        for j in range(1,len(Cell_list8)+1):
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
         ws1.update_cell(k, lastcol+1, "メールアドレス")
         
       elif len([i for i in list_2 if "mail" in i \
                  or "メール" in i]) == 0:
         Cell_list8 = [i for i in list_2c if "mail" in i \
                           or "メール" in i]
#         for j in range(1,len(Cell_list8)+1):
         driver.find_elements_by_class_name(Cell_list8[0])[2].send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[0])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
         ws1.update_cell(k, lastcol+1, "メールアドレス")

       elif len([i for i in list_2c if "mail" in i \
                  or "メール" in i]) == 0:
         Cell_list8 = [i for i in list_2d if "mail" in i \
                     or "メール" in i]
         for j in range(1,len(Cell_list8)+1):
          driver.find_element_by_id(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)
          ws1.update_cell(k, lastcol+1, "メールアドレス")

    
#ホームページアドレス
     if not len([i for i in items_1 if "URL" in i \
         or "ウェブ" in i \
             or "サイト" in i \
                 or "ホームページ" in i]) == 0 \
             or not len([i for i in list_2 if "URL" in i \
         or "ウェブ" in i \
                          or "サイト" in i \
                 or "ホームページ" in i \
                     or "site" in i]) == 0:

       Cell_list8 = [i for i in list_2 if "url" in i \
                     or "URL" in i \
                         or "ウェブ" in i \
                             or "site" in i]
       print(Cell_list8)
       
       elemName0 = driver.find_element_by_name(Cell_list8[0])
       try:
           if elemName0.is_displayed() is False:
            pass
           elif not Cell_list8 == []:
            driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(16, 2).value)       
            lastcol = len(list(ws1.row_values(k)))
            time.sleep(1)
            ws1.update_cell(k, lastcol+1, "URL")

#操作できない要素の回避
       except ElementNotInteractableException:
         pass

#業種
     if not len([i for i in items_1 if "業種" in i]) == 0:
       Cell_list8 = [i for i in list_2 if "industry" in i \
                     or "businesstype" in i]
       print(Cell_list8)
       if not Cell_list8 == []:
        driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(10, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "業種")
      

#部署名
     if not len([i for i in items_1 if "部署" in i \
                  or "所属" in i]) == 0:
        Cell_list3 = [i for i in list_2 if "dept" in i \
                      or "department" in i \
                          or "userDivision" in i \
                              or "division" in i \
                              or "section" in i \
                              or "部署" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(9, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "部署名")

#役職
     if not len([i for i in items_1 if "役職" in i]) == 0:
        Cell_list3 = [i for i in list_2 if "class" in i \
                      or "position" in i \
                          or "役職" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(11, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "役職")


#件名
     if len([i for i in items_1 if "サービス名" in i \
               or "題名" in i \
                   or "キーワード" in i \
                       or "件名" in i]) > 0 \
         or len([i for i in list_2 if "サービス名" in i \
               or "題名" in i \
                   or "キーワード" in i \
                       or "件名" in i]) > 0:
        SELECT_list1 = [i for i in list_2 if "text_field" in i \
                        or "subject" in i \
                            or "題名" in i \
                                or "サービス名" in i \
               or "題名" in i \
                   or "キーワード" in i \
                       or "件名" in i]
        print(SELECT_list1)
        if len(SELECT_list1) == 1:
         driver.find_element_by_name(SELECT_list1[0]).send_keys(ws2.cell(1, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)            
         ws1.update_cell(k, lastcol+1, "タイトル")
        if len(SELECT_list1) > 1:
         for j in range(1, len(SELECT_list1)+1):
          driver.find_element_by_name(SELECT_list1[j-1]).send_keys(ws2.cell(1, 1+j).value)
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)            
          ws1.update_cell(k, lastcol+1, ws2.cell(1, 1+j).value)

         
#textareaタグのname値を取得
     TEXTAREA_list1 = []
     TEXTAREA_list2 = []
     TEXTAREA_list3 = []
     element3 = soup.find_all("textarea")
#     print(element3)
       
     for textarea in element3:
        TEXTAREA_list1.append(textarea.get("id"))
        TEXTAREA_list2.append(textarea.get("name"))
        TEXTAREA_list3.append(textarea.get("class"))
        TEXTAREA_list1 = [i for i in TEXTAREA_list1 if i is not None]
        TEXTAREA_list2 = [i for i in TEXTAREA_list2 if i is not None]
        TEXTAREA_list3 = [i for i in TEXTAREA_list3 if i is not None]
#        print(TEXTAREA_list1)
     print(TEXTAREA_list2)
#        print(TEXTAREA_list3)
#       for elem3 in element3: 
#        items_1.append(name.get("placeholder"))
#        print(items_1)

#（Googleフォーム）
     if not len([i for i in TEXTAREA_list3 if "exportTextarea" in i]) == 0:
      driver.find_elements_by_css_selector(".quantumWizTextinputPapertextareaInput.exportTextarea")[0].send_keys(ws3.cell(1, 1).value)
      lastcol = len(list(ws1.row_values(k)))
      time.sleep(1)
      ws1.update_cell(k, lastcol+1, "本文")

#id値が存在する場合
     elif len(TEXTAREA_list1) > 0 \
         and len(TEXTAREA_list2) == 0 \
             and len(TEXTAREA_list3) == 0:
        driver.find_element_by_id(TEXTAREA_list1[0]).send_keys(ws3.cell(1, 1).value)
        print(TEXTAREA_list1[0])
        lastcol = len(list(ws1.row_values(k)))
        ws1.update_cell(k, lastcol+1, "本文")        

#name値のみ存在
     elif len(TEXTAREA_list1) == 0 \
         and len(TEXTAREA_list2) > 0 \
             and len(TEXTAREA_list3) == 0:
          driver.find_element_by_name(TEXTAREA_list2[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list2[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")

#name値及びclass値が存在する場合
     elif len(TEXTAREA_list1) == 0 \
         and len(TEXTAREA_list2) > 0 \
             and len(TEXTAREA_list3) > 0:
          driver.find_element_by_name(TEXTAREA_list2[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list2[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")

#id値及びclass値の両方が存在
     elif len(TEXTAREA_list1) > 0 \
         and len(TEXTAREA_list2) == 0 \
             and len(TEXTAREA_list3) > 0:
          driver.find_element_by_id(TEXTAREA_list1[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list1[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")

#id値及びname値が存在しない場合
     elif len(TEXTAREA_list1) == 0 \
         and len(TEXTAREA_list2) == 0 \
             and len(TEXTAREA_list3) > 0:
          driver.find_element_by_class_name(TEXTAREA_list3[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list3[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")         

#id値及びname値の両方が存在
     elif len(TEXTAREA_list1) > 0 \
            and len(TEXTAREA_list2) > 0 \
                and len(TEXTAREA_list3) == 0:      
          print(TEXTAREA_list2[0])
          
          elemName0 = driver.find_element_by_name(TEXTAREA_list2[0])
          elemName1 = driver.find_element_by_name(TEXTAREA_list2[1])
          elemName2 = driver.find_element_by_name(TEXTAREA_list2[2])
          try:
           if elemName0.is_displayed() is False \
               or elemName1.is_displayed() is False \
                   or elemName2.is_displayed() is False:
               print(TEXTAREA_list2[j-1])
               if "1" in TEXTAREA_list2[j-1]:
                driver.find_element_by_name(TEXTAREA_list2[j-1]).send_keys(ws3.cell(1, 1).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "本文")

               elif "2" in TEXTAREA_list2[j-1]:
                driver.find_element_by_name(TEXTAREA_list2[j-1]).send_keys(ws3.cell(1, 1).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "本文")

               elif "3" in TEXTAREA_list2[j-1]:
                driver.find_element_by_name(TEXTAREA_list2[j-1]).send_keys(ws3.cell(1, 1).value)
                lastcol = len(list(ws1.row_values(k)))
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "本文")
           else:
            driver.find_element_by_name(TEXTAREA_list2[0]).send_keys(ws3.cell(1, 1).value)
            lastcol = len(list(ws1.row_values(k)))
            time.sleep(1) 
            ws1.update_cell(k, lastcol+1, "本文")
          
#操作できない要素の回避
          except ElementNotInteractableException:
            pass
          
#全て存在
     elif len(TEXTAREA_list1) > 0 \
            and len(TEXTAREA_list2) > 0 \
                and len(TEXTAREA_list3) > 0:
          driver.find_element_by_name(TEXTAREA_list2[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list2[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")

  
#プルダウンメニュー
     list_6 = []
     for element5 in soup.find_all("select"):
       list_6.append(element5.get("name"))
     list_6 =[i for i in list_6 if i is not None]
     print(list_6)
     list_7 = []
     for element5 in soup.find_all("select"):
       list_7.append(element5.get("id"))
     print(list_7)
     list_7 =[i for i in list_7 if i is not None]

#（お問い合わせ内容）
     SELECT_list1 = []
     for element in soup.find_all("option"): 
        SELECT_list1.append(element.get("value"))
     print(SELECT_list1)
        
     if len(SELECT_list1) == 0:
         pass
     elif len(SELECT_list1) > 0:
      SELECT_list2 = [i for i in SELECT_list1 if "お問い合わせ" == i \
                      or "その他" in i \
                          or "営業" in i \
                              or "宣伝" in i]
      print(len(SELECT_list2))
      print(len(list_6))
      print(len(list_7))
      if len(SELECT_list2) > 0 \
         and not len(list_6) == 0:
         list_6 = [i for i in list_6 if "product" in i \
                   or "koumoku" in i \
                       or "custom" in i \
                           or "collection" in i \
                               or "menu" in i]
         if len([i for i in items_1 if "連絡方法" in i]) > 0:
             pass
#          for j in range(1, len(SELECT_list2)+1):
         else:
          if not list_6 == []:             
           dropdown = driver.find_element_by_name(list_6[0])
           print(list_6[0])
           select = Select(dropdown)
           select.select_by_value(SELECT_list2[len(SELECT_list2)-1])
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list2[len(SELECT_list2)-1])
           
      elif len(SELECT_list2) > 0 \
         and not len(list_7) == 0:
         list_7 = [i for i in list_7 if "product" in i \
                   or "koumoku" in i \
                       or "custom" in i \
                           or "collection" in i \
                               or "menu" in i]
#        for j in range(1, len(SELECT_list2)+1):
         dropdown = driver.find_element_by_id(list_7[0])
         print(list_7[0])
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[len(SELECT_list2)-1])
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, SELECT_list2[len(SELECT_list2)-1])
      elif len(SELECT_list2) == 0:
         lastcol = len(list(ws1.row_values(k)))
         ws1.update_cell(k, lastcol+1, "ドロップボックスなし（又は未選択）")


#プルダウンメニュー
      list_6 = []
      for element5 in soup.find_all("select"):
       list_6.append(element5.get("name"))
      list_6 =[i for i in list_6 if i is not None]
      print(list_6)
      list_7 = []
      for element5 in soup.find_all("select"):
       list_7.append(element5.get("id"))
      list_7 =[i for i in list_7 if i is not None]
      print(list_7)

#（都道府県）
      if len([i for i in items_1 if "都道府県" in i]) > 0 \
         or "都道府県" in str(soup.find_all("select")) > 0:
         list_6 = [i for i in list_6 if "pref" in i \
                   or "都道府県" in i \
                       or "address1" == i]
             
         if not list_6 == []:         
          print(list_6[0])
          dropdown = driver.find_element_by_name(list_6[0])
          select = Select(dropdown)
          SELECT_list3 = [i for i in SELECT_list1 if "東京都" in i]
          print(SELECT_list3)
          select.select_by_value(SELECT_list3[0])
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list3[0])
          if len([i for i in items_1 if "建物" in i \
               or "ビル" in i \
                   or "アパート" in i]) == 0:
           Cell_list6 = [i for i in list_2 if "address" == i \
                        or "address2" in i]
           print(Cell_list6)
           driver.find_element_by_name(Cell_list6[0]).clear()
           driver.find_element_by_name(Cell_list6[0]).send_keys(ws2.cell(5, 3).value \
                                                                 + ws2.cell(5, 4).value \
                                                                     + ws2.cell(5, 5).value)
             
#（連絡方法）
      SELECT_list2 = []       
      SELECT_list2 = [i for i in SELECT_list1 if "メール" in i]
      print(SELECT_list2)
       
      if len(list_6) > 0:
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
#        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[j-1])
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])


#（アンケート）
      if "知りましたか" in str(soup.find_all("form")) \
          or "お知りに" in str(soup.find_all("form")):
       SELECT_list2 = [i for i in SELECT_list1 if "ネット" in i]
       print(SELECT_list2)
       
       if len(list_6) == 1:
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
#        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[j-1])
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
         
       if len(list_6) > 1:
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
#        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[j-1])
         dropdown = driver.find_element_by_name(list_6[1])
         print(list_6[1])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])         

      elif len([i for i in list_2 if "知りましたか" in i \
                          or "お知りに" in i]) > 0:
            Cell_list9 = [i for i in list_2 if "知りましたか" in i \
                          or "お知りに" in i]
            print(Cell_list9)
            driver.find_element_by_name(Cell_list9[0]).send_keys(ws2.cell(1, 3).value)
            lastcol = len(list(ws1.row_values(k)))
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, ws2.cell(1, 3).value)


#チェックボックス
     element6 = soup.find_all("input",type="checkbox")
     list_6 = []
       
#（お問い合わせ内容）
#data-name
     SELECT_list3 = []
     for elem1 in element6: 
       SELECT_list3.append(elem1.get("data-name"))

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
     SELECT_list3 = [i for i in SELECT_list3 if i is not None]
     print(SELECT_list3)

#id
     SELECT_list4 = []
     for elem2 in element6: 
        SELECT_list4.append(elem2.get("id"))
        
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
     SELECT_list4 = [i for i in SELECT_list4 if i is not None]
     print(SELECT_list4)

#value
     SELECT_list5 = []
     for elem1 in element6: 
        SELECT_list5.append(elem1.get("value"))
     print(SELECT_list5)

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
#選択肢：その他
     SELECT_list6 = [i for i in SELECT_list5 if "その他" in i \
                     and i is not None]
     print(SELECT_list6)

#name
     SELECT_list7 = []
     for elem1 in element6:
        SELECT_list7.append(elem1.get("name"))
     print(SELECT_list7)


#お問い合わせの内容、項目選択

#（指定のキーワードが含まれない）
     if len([i for i in list_1 if "内容" in i \
                 or "件名" in i \
                     or "項目" in i \
                         or "種別" in i]) == 0:
      pass

#（指定のキーワードが含まれる）
     elif not len([i for i in list_1 if "内容" in i \
                 or "件名" in i \
                     or "項目" in i \
                         or "種別" in i]) == 0:
          
#両リスト（SELECT_list3及びSELECT_list4）の要素が1個以上存在する場合において、
#更にリスト内包表記で処理
         if len(SELECT_list3) > 0 \
             and len(SELECT_list4) > 0 \
                 and len(SELECT_list6) == 0 \
                     and len(SELECT_list7) == 0:
          SELECT_list4 = [i for i in SELECT_list3 if "その他" in i]
          print(len(SELECT_list3))
          print(len(SELECT_list4))
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())          
          if checkbox.is_selected() is True:           
            lastcol = len(list(ws1.row_values(k)))    
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list4)-1])
            print(checkbox.is_selected())

#valueのみしか存在しない
         elif len(SELECT_list3) == 0 \
             and len(SELECT_list4) == 0 \
                 and len(SELECT_list6) > 0 \
                     and len(SELECT_list7) == 0:
#          SELECT_list5 = [i for i in SELECT_list5 if "その他" in i]
#          print(SELECT_list5)
          print(len(SELECT_list3))
          print(len(SELECT_list4))
          print(len(SELECT_list6))
          print(len(SELECT_list7))

          checkbox = driver.find_element_by_css_selector("[value='その他']")
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())          
          if checkbox.is_selected() is True:           
            lastcol = len(list(ws1.row_values(k)))    
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, SELECT_list6[len(SELECT_list6)-1])
            print(checkbox.is_selected())

#id且つvalueの両方存在
         elif len(SELECT_list3) == 0 \
             and len(SELECT_list4) > 0 \
                 and len(SELECT_list6) > 0 \
                     and len(SELECT_list7) == 0:
          print(len(SELECT_list3))
          print(len(SELECT_list4))
          print(len(SELECT_list6))
          print(len(SELECT_list7))

          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())          
          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list4)-1])
           print(checkbox.is_selected())

#value且つnameの両方存在
         elif len(SELECT_list3) == 0 \
             and len(SELECT_list4) == 0 \
                 and len(SELECT_list6) > 0 \
                     and len(SELECT_list7) > 0:
          print(len(SELECT_list3))
          print(len(SELECT_list4))
          print(len(SELECT_list6))
          print(len(SELECT_list7))

#一旦チェックボックスを外す
          try:
           checkbox1 = driver.find_elements_by_name(SELECT_list7[0])[0]
           
#選択状態にある場合
           if checkbox1.is_selected() is True:
             driver.execute_script("arguments[0].click();", checkbox1)

#選択状態にない場合
           elif checkbox1.is_selected() is False:
              checkbox = driver.find_elements_by_css_selector("[value='その他']")[0]
              driver.execute_script("arguments[0].click();", checkbox)
              print(checkbox.is_selected())          
              if checkbox.is_selected() is True:           
                lastcol = len(list(ws1.row_values(k)))    
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "その他1")

#一旦チェックボックスを外す
           checkbox2 = driver.find_element_by_name(SELECT_list7[len(SELECT_list7)-1])

#選択状態にある場合
           if checkbox2.is_selected() is True:
             driver.execute_script("arguments[0].click();", checkbox2)           

#選択状態にない場合
           elif checkbox2.is_selected() is False:
              checkbox = driver.find_elements_by_css_selector("[value='その他']")[1]
              driver.execute_script("arguments[0].click();", checkbox)
              print(checkbox.is_selected())          
              if checkbox.is_selected() is True:           
                lastcol = len(list(ws1.row_values(k)))    
                time.sleep(1)             
                ws1.update_cell(k, lastcol+1, "その他2")
#エラー回避
          except:
            pass


#どちらの回答方法を希望するか？
     if "返信方法" in str(soup.find_all("form")) \
         or "連絡方法" in str(soup.find_all("form")):
         SELECT_list3 = [i for i in SELECT_list3 if "メール" in i \
                         or "mail" in i \
                             and i is not None]
         SELECT_list4 = [i for i in SELECT_list4 if "メール" in i \
                         or "mail" in i \
                             and i is not None]
#         SELECT_list5 = [i for i in SELECT_list5 if "メール" in i \
#                         or "mail" in i \
#                             and i is not None]             
         
#両リスト（SELECT_list3及びSELECT_list4）の要素が1個以上存在する場合において、
#更にリスト内包表記で処理
         if len(SELECT_list3) > 0 \
             and len(SELECT_list4) > 0 \
                 and len(SELECT_list5) == 0:
          print(SELECT_list3)
          print(SELECT_list4)
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list3)-2])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list3)-2])
           print(checkbox.is_selected())

#（idのみ）
         elif len(SELECT_list3) == 0 \
             and len(SELECT_list4) > 0 \
                 and len(SELECT_list5) == 0:
          print(SELECT_list4)
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:           
            lastcol = len(list(ws1.row_values(k)))    
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list4)-1])
            print(checkbox.is_selected())

#（valueのみ）
         elif len(SELECT_list3) == 0 \
             and len(SELECT_list4) == 0 \
                 and len(SELECT_list5) > 0:
          print(SELECT_list5)
          if len([i for i in SELECT_list5 if "メール" in i]) > 0:
           checkbox = driver.find_element_by_css_selector("[value='メール']")
           driver.execute_script("arguments[0].click();", checkbox)
           print(checkbox.is_selected())
#          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "メール")
          elif len([i for i in SELECT_list5 if "mail" in i]) > 0:
           checkbox = driver.find_element_by_css_selector("[value='E-mail']")
           driver.execute_script("arguments[0].click();", checkbox)
           print(checkbox.is_selected())
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "メール")

        
#（メール配信）
     if "希望しない" in str(soup.find_all("form")):
                 
       SELECT_list3 = []
       for elem1 in element6: 
        SELECT_list3.append(elem1.get("name"))

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list3 = [i for i in SELECT_list3 if i is not None]
       print(SELECT_list3)
       
       SELECT_list4 = []
       for elem2 in element6: 
        SELECT_list4.append(elem2.get("id"))
        
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list4 = [i for i in SELECT_list4 if i is not None]
       print(SELECT_list4)
#       for i in range(1, len(SELECT_list3)+1):
           
#name、idの両方が存在する場合
       if len(SELECT_list3) == 1 \
            and len(SELECT_list4) == 1:
         checkbox = driver.find_element_by_id(SELECT_list4[0])
         driver.execute_script("arguments[0].click();", checkbox)
         if checkbox.is_selected() is True:
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list4[0])
         else:
          checkbox = driver.find_element_by_name(SELECT_list3[0])
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list3[0])

       elif len(SELECT_list3) > 1 \
            and len(SELECT_list4) > 1:
         checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "希望しない")         
#         break
#nameのみ存在
       elif len(SELECT_list3) == 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[0])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "希望しない")
       elif len(SELECT_list3) > 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "希望しない")
#         break


#（個人情報取り扱いに関する同意）
     if "個人情報" in str(soup.find_all("form")) \
         or "同意" in str(soup.find_all("form")) \
             or "プライバシーポリシー" in str(soup.find_all("form")) \
                 and not len([i for i in SELECT_list5 if "個人情報" in i \
                          or "同意" in i \
                              or "プライバシーポリシー" in i \
                                  and i is not None]) == 0:
                 
       SELECT_list3 = []
       for elem1 in element6: 
        SELECT_list3.append(elem1.get("name"))

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list3 = [i for i in SELECT_list3 if i is not None]
       print(SELECT_list3)
       print(len(SELECT_list3))
       
       SELECT_list4 = []
       for elem2 in element6: 
        SELECT_list4.append(elem2.get("id"))
        
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list4 = [i for i in SELECT_list4 if i is not None]
       print(SELECT_list4)
       print(len(SELECT_list4))       
#       for i in range(1, len(SELECT_list3)+1):
           
#name、idの両方が存在する場合
       if len(SELECT_list3) == 1 \
            and len(SELECT_list4) == 1:
         checkbox = driver.find_element_by_id(SELECT_list4[0])
         if checkbox.is_selected() is not True:
          driver.execute_script("arguments[0].click();", checkbox)             
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list4[0])
          print(checkbox.is_selected())          
#         else:
#          checkbox = driver.find_element_by_name(SELECT_list3[0])
#          driver.execute_script("arguments[0].click();", checkbox)
#          print(checkbox.is_selected())
#          lastcol = len(list(ws1.row_values(k)))
#          time.sleep(1)             
#          ws1.update_cell(k, lastcol+1, SELECT_list3[0])

       elif len(SELECT_list3) > 1 \
            and len(SELECT_list4) > 1:
         checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         print(checkbox.is_selected())         
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")         
#         break
#nameのみ存在
       elif len(SELECT_list3) == 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[0])
         if checkbox.is_selected() is not True:
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())         
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, "同意")
       elif len(SELECT_list3) > 1 \
            and len(SELECT_list4) == 0 \
                 and not len([i for i in SELECT_list5 if "個人情報" in i \
                          or "同意" in i \
                              or "プライバシーポリシー" in i \
                                  and i is not None]) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
         if checkbox.is_selected() is not True:
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())                  
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, "同意")
#         break
#idのみ存在する場合
       elif len(SELECT_list3) == 0 \
            and len(SELECT_list4) == 1:
         checkbox = driver.find_element_by_id(SELECT_list4[0])
         if checkbox.is_selected() is not True:
          driver.execute_script("arguments[0].click();", checkbox)
          print(checkbox.is_selected())         
#         if checkbox.is_selected() is True:
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list4[0])
          

#送信ボタン押下

#（スパムメール防止のためのチェックボックス）
     if not len([i for i in list_2c if "spam" in i]) == 0:
           checkbox = driver.find_element_by_css_selector("[value='1']")
           driver.execute_script("arguments[0].click();", checkbox)
#           print(checkbox.is_selected())
#           lastcol = len(list(ws1.row_values(k)))    
#           time.sleep(1)             
#           ws1.update_cell(k, lastcol+1, "スパムメール防止チェック済")

#（name値に指定キーワードが含まれる）
     if not len([i for i in list_2 if "submit" in i]) == 0:
          driver.find_element_by_name("submit").click()
          time.sleep(1)
          html = driver.page_source
          soup = BeautifulSoup(html, 'html.parser')
#          print(soup)

#エラーメッセージ
          for result in soup.select(".error-box"):
           ws1.update_cell(k, 9, result.getText())
          print(soup.select(".error-box"))

#（name値に指定キーワードが含まれない、且つtype値に指定キーワードが含まれる）
     elif len([i for i in list_2 if "submit" in i]) == 0 \
           or len([i for i in list_2t if "submit" in i]) > 0:
          
#対象物が画面の外にあると、
#「ElementClickInterceptedException: element click intercepted: Element is not clickable at point」
#になってしまうので以下の方法で回避
        try:
          driver.execute_script("window.scrollTo(0, 200);")
          driver.find_element_by_css_selector("input[value='送信']").click()
          time.sleep(1)
          html = driver.page_source
          soup = BeautifulSoup(html, 'html.parser')

#エラーメッセージ
          for result in soup.select(".text"):
           Content = re.sub("[\n]", "", result.getText(), 4)
           ws1.update_cell(k, 9, Content)
          print(soup.select(".text"))

        except NoSuchElementException:
          try:
           elemName0 = driver.find_elements_by_css_selector('.basic-button.is-slim.form-confirmation-button')[0]
           elemName1 = driver.find_elements_by_css_selector('.basic-button.is-slim.form-confirmation-button')[1]
           elemName2 = driver.find_elements_by_css_selector('.basic-button.is-slim.form-confirmation-button')[2]
           if elemName0.is_displayed() is True:
            driver.find_elements_by_css_selector('.basic-button.is-slim.form-confirmation-button')[0].click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
           elif elemName1.is_displayed() is True:
            driver.find_elements_by_css_selector('.basic-button.is-slim.form-confirmation-button')[1].click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
           elif elemName2.is_displayed() is True:
            driver.find_elements_by_css_selector('.basic-button.is-slim.form-confirmation-button')[2].click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')            
           else:
            driver.find_element_by_css_selector('.basic-button.is-slim.form-confirmation-button').click()
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

#エラーメッセージ
           for result in soup.select(".alert-text"):
            Content = re.sub("[\n]", "", result.getText(), 4)
            ws1.update_cell(k, 9, Content)
           print(soup.select(".alert-text"))

#エラー回避
          except:
#対象物が画面の外にあると、
#「ElementClickInterceptedException: element click intercepted: Element is not clickable at point」
#になってしまうので以下の方法で回避              
            try:
              elem = driver.find_element_by_css_selector('.wpcf7-form-control.wpcf7-submit')
              driver.execute_script("arguments[0].click();", elem)
              time.sleep(5)
              html = driver.page_source
              soup = BeautifulSoup(html, 'html.parser')
                
#エラーメッセージ
              for result in soup.select(".wpcf7-response-output"):
                Content = re.sub("[\n]", "", result.getText(), 4)
                ws1.update_cell(k, 9, Content)
              print(soup.select(".wpcf7-response-output"))

#結果出力
              for result in soup.select(".wpcf7-not-valid-tip"):
                Content = re.sub("[\n]", "", result.getText(), 4)
                ws1.update_cell(k, 9, Content)
              print(soup.select(".wpcf7-not-valid-tip"))

#エラー回避
            except:                
              ws1.update_cell(k, 9, "送信ボタン押下不可")

    else:
     ws1.update_cell(k, 9, "フォーム要素取得不可")
# except:
#  ws1.update_cell(k, 9, "無限ページロードによりスキップしました。")
#   elif ws1.cell(k, 8).value == r"-":
#    ws1.cell(k, 9).value == "フォーム要素なし"
#driver.quit()      

# calculate elapsed time
elapsed_time = int(time.time() - start)

# convert second to hour, minute and seconds
elapsed_hour = elapsed_time // 3600
elapsed_minute = (elapsed_time % 3600) // 60
elapsed_second = (elapsed_time % 3600 % 60)

# print as 00:00:00
print("所要時間：" + str(elapsed_hour).zfill(2) + "h" \
      + str(elapsed_minute).zfill(2) + "m" + str(elapsed_second).zfill(2) + "s")
