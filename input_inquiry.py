# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:39:48 2021

@author: iorin
"""

#import Screen_Transition
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

#Selectモジュールをインポート
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

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
credentials = ServiceAccountCredentials.from_json_keyfile_name('ekiten-07cd3f32afc9.json', scope)

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
for k in tqdm(range(49, 54)):
    
#シートの初期化
 ws5.clear()
   
# 入力されているk行目の配列を取得
 lastcol = len(list(ws1.row_values(k)))  
#UI2comboBox = Screen_Transition.ui2.comboBox.currentText(0)
#driver.get('https://www.ekiten.jp/gen_relax/' + UI2comboBox)
 try:
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
        or "営業のお問い合わせ" in html:
     ws1.update_cell(k, 9, "営業お断り！！")
    elif "recaptcha" in html:
     ws1.update_cell(k, 9, "reCAPTCHA")
    elif "予算" in str(soup.find_all("form")) \
        or "納期" in str(soup.find_all("form")):
     ws1.update_cell(k, 9, "サービスに関する専用フォーム")
    elif "無料相談" in html \
        or "ご相談" in str(soup.find_all("form")):
     ws1.update_cell(k, 9, "無料相談専用フォーム")
#    elif "求人" in html \
#        or "採用" in str(soup.find_all("form")):
#     ws1.update_cell(k, 9, "人材関連専用フォーム")
#自動送信対象     
    elif "確認" in str(soup.find_all("form")) \
        or "送信" in str(soup.find_all("form")) \
            or "お問い合わせ" in str(soup.find_all("form")):
     ws1.update_cell(k, 9, "フォーム要素あり")
     
#dtタグのテキストを取得
     if "お問い合わせ" in str(soup.find_all("dt")) \
         or "メールアドレス" in str(soup.find_all("dt")):
         
#dtタグのテキストを取得
      element1 = soup.find_all("dt")
      list_1 = []   
      for list_ in element1:
        if "企業名" in list_.getText() \
            or "貴社名" in list_.getText() \
                or "会社名" in list_.getText() \
                    or "御社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "業種" in list_.getText() \
                                                    or "題名" in list_.getText() \
                                                        or "本文" in list_.getText() \
                                                            or "詳細" in list_.getText() \
                                                                or "連絡方法" in list_.getText():
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
      print(items_1)


#inputタグのname値を取得
      element2 = soup.find_all("input",type="text")
      list_2 = []

      element3 = soup.find_all("input",type="email")
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []


#type属性：text
      for name in element2:
       list_2.append(name.get("name"))
       
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       list_2 = [i for i in list_2 if i is not None]
       print(list_2)

#type属性：email
      for name in element3:
       list_3.append(name.get("name"))
       print(list_3)

#type属性：tel
      for name in element4:
       list_4.append(name.get("name"))
       print(list_4)


#会社名
      if not len([i for i in items_1 if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i \
                       or "貴社名" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or r"your-company" in i \
                         or "company" in i \
                             or "会社名" in i]
        print(Cell_list1)    
#テキスト入力          
        driver.find_element_by_name(Cell_list1[0]).send_keys(ws2.cell(2, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "会社名")

#会社名ふりがな         
      if len([i for i in items_1 if "ふりがな（カナ）" in i]) > 1:
       Cell_list2 = [i for i in list_2 if "企業名ふりがな（カナ）" in i]
       print(Cell_list2)
#テキスト入力
       driver.find_element_by_name(Cell_list2[0]).send_keys(ws2.cell(3, 2).value)
       lastcol = len(list(ws1.row_values(k)))       
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "会社名カナ")

#フルネーム（姓＋名）
      Cell_list3 = [i for i in list_2 if "姓" == i \
                      or "名" == i \
                          or "family_name" in i \
                              or "given_name" in i]
      print(Cell_list3)
      for j in range(1,len(Cell_list3)+1):
         print(Cell_list3[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)


#フルネーム（氏名）
      if not len([i for i in items_1 if "名前" in i \
               or "担当者" in i \
                   or "氏名" in i]) == 0:
        Cell_list3 = [i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "r-name" in i \
                                 or "yourname" in i \
                                     or "fullname" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)             
        ws1.update_cell(k, lastcol+1, "氏名")


#フルネームふりがな
#      try:
      if len([i for i in items_1 if "ふりがな" in i]) > 0:
       Cell_list5 = [i for i in list_2 if "せい" == i \
                      or "めい" == i]
       print(Cell_list5)
       for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)


#フルネームカタカナ（セイ＋メイ）
      if len([i for i in items_1 if "フリガナ" in i \
              or "カナ" in i]) > 0:
       Cell_list5 = [i for i in list_2 if "セイ" == i or "メイ" == i]
       print(Cell_list5)
       for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(8, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(8, 2+j).value)

#フルネームカタカナ（セイメイ）
      if len([i for i in items_1 if "フリガナ" in i \
              or "カナ" in i]) > 0:
       Cell_list5 = [i for i in list_2 if "your-kana" in i \
                    or "r-furi" in i \
                        or "furigana" in i]
       print(Cell_list5)

#テキスト入力
       driver.find_element_by_name(Cell_list5[0]).send_keys(ws2.cell(8, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "氏名フリガナ")

    
#住所（郵便番号＋都道府県＋市町村＋建物名）
      if len([i for i in items_1 if "郵便番号" in i]) > 0:

       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i]
       print(Cell_list6)
       driver.find_element_by_name(Cell_list6[0]).send_keys("1600022")
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "郵便番号")
    
      if len([i for i in items_1 if "都道府県" in i]) > 0:
       Cell_list6 = [i for i in list_2 if "都道府県" in i \
                     or "your-address" in i]
       print(Cell_list6)
       if "都道府県" in Cell_list6: 
        pref = driver.find_element_by_name(Cell_list6[0])
        pref.clear()
        pref.send_keys("東京都")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "都道府県")


        Cell_list6 = [i for i in list_2 if "市町村" in i]
        print(Cell_list6)
        Municipal = driver.find_element_by_name(Cell_list6[0])
        Municipal.clear()   
        Municipal.send_keys("新宿区新宿5-4-1")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "市区町村")


        Cell_list6 = [i for i in list_2 if "アパート" in i]
        print(Cell_list6)
        build = driver.find_element_by_name(Cell_list6[0])
        build.send_keys("新宿Qフラットビル8F")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "アパート")       

       elif len([i for i in Cell_list6 if "0" in i or "1" in i]) > 1:
        Cell_list7 =[i for i in Cell_list6 if "01" in i \
                     or "02" in i \
                         or "03" in i \
                             or "04" in i]
        print(Cell_list7)
        for j in range(1,len(Cell_list7)+1):
         driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)
         
                           

#メールアドレス
#「import email」はライブラリ参照のコマンドなので使用不可
      if not list_3 == []:
        Cell_list8 = [i for i in list_3 if "mail" in i \
                     or "メール" in i]
        print(Cell_list8)
#テキスト入力
        for j in range(1,len(Cell_list8)+1):           
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)
         ws1.update_cell(k, lastcol+1, "メールアドレス")
         
      elif list_3 == []:
        Cell_list8 = [i for i in list_2 if "mail" in i \
                     or "メール" in i]
        print(Cell_list8)
#テキスト入力
        for j in range(1,len(Cell_list8)+1):           
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)
         ws1.update_cell(k, lastcol+1, "メールアドレス")


#ホームページアドレス
      try:
       Cell_list8 = [i for i in list_2 if "url" in i]

#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(16, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "URL")
      except:
       pass

#業種
      try:
       Cell_list8 = [i for i in list_2 if "industry" in i]
#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(10, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "業種")
      except:
       pass

#電話番号
#「type属性：tel」が存在する
      if not list_4 == []:
          
#（ハイフンあり）          
        Cell_list7 = [i for i in list_4 if "tel" in i \
                     or "電話" in i \
                         or r"your-phone" in i]
        print(Cell_list7)                      
        if not "ハイフンなし" in items_1:
         driver.find_element_by_name(Cell_list7[0]) \
             .send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")
            
        elif not "ハイフンなし" in items_1 \
           and "0" in list_4 \
               or "1" in list_4:
         Cell_list8 =[i for i in Cell_list7 if "0" in i \
                     or "1" in i \
                         or "2" in i]
         print(Cell_list8)
        
#テキスト入力＋市外局番別
         driver.find_element_by_name(Cell_list8[0]) \
           .send_keys("03")
         driver.find_element_by_name(Cell_list8[1]) \
           .send_keys("6384")
         driver.find_element_by_name(Cell_list8[2]) \
           .send_keys("1059")
         for j in range(1, len(Cell_list8)+1):
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)         


#「type属性：tel」が存在しない
      elif list_4 == []:
        Cell_list7 = [i for i in list_2 if "tel" in i \
                     or "電話" in i \
                         or "phone" in i]
        print(Cell_list7)                      
        if len([i for i in items_1 if "ハイフンなし" in i]) > 1:
         driver.find_element_by_name(Cell_list7[0]) \
             .send_keys(ws2.cell(14, 3).value \
                        + ws2.cell(14, 4).value + ws2.cell(14, 5).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンなし）")     
            
        elif not "ハイフンなし" in items_1 \
           and "0" in list_2 \
               or "1" in list_2:
         Cell_list8 =[i for i in Cell_list7 if "0" in i \
                     or "1" in i \
                         or "2" in i]
         print(Cell_list8)
        
#テキスト入力＋市外局番別
         driver.find_element_by_name(Cell_list8[0]) \
           .send_keys("03")
         driver.find_element_by_name(Cell_list8[1]) \
           .send_keys("6384")
         driver.find_element_by_name(Cell_list8[2]) \
           .send_keys("1059")
         for j in range(1, len(Cell_list8)+1):
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)
          
        else:
         driver.find_element_by_name(Cell_list7[0]) \
           .send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")


#件名
      try:
       if len([i for i in str(soup.find_all("form")) if "サービス名" in i \
               or "題名" in i \
                   or "キーワード" in i]) > 0:
        SELECT_list1 = [i for i in list_2 if "text_field" in i \
                        or "題名" in i]
        print(SELECT_list1)

#テキスト入力
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
      except:
       pass
   
        
#textareaタグのname値を取得
      TEXTAREA_list = []
      element3 = soup.find_all("textarea")
      textarea = soup.textarea["name"]
      for textarea in element3:
       TEXTAREA_list.append(textarea.get("name"))   
       print(textarea.get("name"))

#（詳細）
      if len(TEXTAREA_list) == 1:
       driver.find_element_by_name(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
       print(TEXTAREA_list[0])
       lastcol = len(list(ws1.row_values(k)))
#      time.sleep(1)            
       ws1.update_cell(k, lastcol+1, "本文")        

      elif len(TEXTAREA_list) > 1:
       if len([i for i in TEXTAREA_list if "件名" in i \
               or "内容" in i]) > 0:
        SELECT_list1 = [i for i in list_2 if "件名" in i \
                        or "内容" in i]
        print(SELECT_list1)
        for j in range(1, len(SELECT_list1)+1):
         driver.find_element_by_name(SELECT_list1[j-1]).send_keys(ws4.cell(j, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)            
         ws1.update_cell(k, lastcol+1, ws4.cell(j, 1).value)
        
#複数のテキストボックスが存在する場合
       elif len([i for i in TEXTAREA_list if "件名" in i \
               or "内容" in i]) == 0:
        for j in range(1, len(TEXTAREA_list)):
         driver.find_element_by_name(SELECT_list1[j-1]).send_keys(ws4.cell(1+j, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)            
         ws1.update_cell(k, lastcol+1, ws4.cell(1+j, 1).value)
        
       else:
        driver.find_element_by_name(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
        print(TEXTAREA_list[0])
        lastcol = len(list(ws1.row_values(k)))
#      time.sleep(1)            
        ws1.update_cell(k, lastcol+1, "本文")        




#プルダウンメニューの選択
#      import select_type
      list_6 = []
      for element5 in soup.find_all("select"):
       list_6.append(element5.get("name"))

#（お問い合わせ内容）
      SELECT_list1 = []
      SELECT_list2 = []
#      element2 = soup.find("select")
      for element in soup.find_all("option"): 
        SELECT_list1.append(element.get("value"))
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
      SELECT_list1 = [i for i in SELECT_list1 if i is not None]
      print(SELECT_list1)      
      SELECT_list2 = [i for i in SELECT_list1 if "お問い合わせ" in i \
                      or "その他" in i \
                          or "営業" in i \
                              or "宣伝" in i]

      if len(SELECT_list2) > 0:
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, SELECT_list2[j-1])
      elif len(SELECT_list2) == 0:
         ws1.update_cell(k, 9, "適切なお問い合わせ種別なし（送信不可）")
          

#プルダウンメニュー（連絡方法）
      try:
#       import select_type
#       Cell_12 = select_type.Cell_12
#       print(Cell_12.value)
#       SELECT_list1 = []
       SELECT_list2 = []       
       SELECT_list2 = [i for i in SELECT_list1 if "メール" in i]
       print(SELECT_list2)
       
       if len(list_6) > 1:       
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
#        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[j-1])
         dropdown = driver.find_element_by_name(list_6[1])
         print(list_6[1])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
      except:
       pass    
   
    
#チェックボックス
      element6 = soup.find_all("input",type="checkbox")
      list_6 = []
      
#（お問い合わせ内容）
#      try:
      if len([i for i in items_1 if "お問い合わせ内容" in i \
              or "ご依頼内容" in i]) == 1:
          
       SELECT_list3 = []
       for elem1 in element6: 
        SELECT_list3.append(elem1.get("value"))

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
       for i in range(1, len(SELECT_list3)+1):
        if "個人情報" in str(soup.find_all("form")) \
          or "同意" in str(soup.find_all("form")) \
             or "プライバシーポリシー" in str(soup.find_all("form")) == 1:

         if "その他" in SELECT_list3[i-1]:
          checkbox = driver.find_element_by_id(SELECT_list4[i-1])
          driver.execute_script("arguments[0].click();", checkbox)
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list3[i-1])
          break
         else:
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list3)-2])
          driver.execute_script("arguments[0].click();", checkbox)
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list3)-2])
          break

        
#（個人情報取り扱いに関する同意）
      if "個人情報" in str(soup.find_all("form")) \
         or "同意" in str(soup.find_all("form")) \
             or "プライバシーポリシー" in str(soup.find_all("form")) == 1:
                 
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
       if not len(SELECT_list3) == 0 \
            and not len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")
#         break
#nameのみ存在
       elif not len(SELECT_list3) == 0 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")
#         break
#      except:
#       pass   

       
#ラジオボタン（連絡方法）
      element5 = soup.find_all("input",type="radio")
      print(element5)
      SELECT_list1 = []
      SELECT_list2 = []

      for elem in element5: 
        SELECT_list1.append(elem.get("value"))
        print(SELECT_list1)

      for elem in element5:
        SELECT_list2.append(elem.get("id"))
        print(SELECT_list2)


#value値のみ、id値なしの場合
      if len(SELECT_list1) > 0 \
           and len(SELECT_list2) == 0:
#         print(len(SELECT_list3))
#         print(len(SELECT_list4))
#         print(list_6[len(list_6)-1])
#         print([len(list_6)-1])
#        for i in range(1, len(list_6)+1):
         radiobutton = driver.find_element_by_css_selector("[value='その他']")
#         radiobutton.click()
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())         
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(radiobutton.is_selected())
        

#pタグのテキストを取得
     elif "お問い合せ" in str(soup.find_all("p")) \
         or "お問い合わせ" in str(soup.find_all("p")) \
             or "メールアドレス" in str(soup.find_all("p")):
      element1 = soup.find_all("p")
      list_1 = []
      for list_ in element1:
        if "企業名" in list_.getText() \
            or "貴社名" in list_.getText() \
                or "会社名" in list_.getText() \
                    or "御社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "業種" in list_.getText() \
                                                    or "題名" in list_.getText() \
                                                        or "本文" in list_.getText() \
                                                            or "詳細" in list_.getText() \
                                                                or "連絡方法" in list_.getText() \
                                                                    or "件名" in list_.getText() \
                                                                        or "同意" in list_.getText():
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
      print(items_1)


#inputタグのname値を取得
      element2 = soup.find_all("input",type="text")
      list_2 = []

      element3 = soup.find_all("input",type="email")
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []


#type属性：text
      for name in element2:
       list_2.append(name.get("name"))
       
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       list_2 = [i for i in list_2 if i is not None]
       list_2 = [i for i in list_2 if not "s" == i]
       print(list_2)

#type属性：email
      for name in element3:
       list_3.append(name.get("name"))
       print(list_3)

#type属性：tel
      for name in element4:
       list_4.append(name.get("name"))
       print(list_4)


#会社名
      if len([i for i in items_1 if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i \
                       or "貴社名" in i]) > 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or r"your-company" in i \
                         or "company" in i \
                             or "会社名" in i \
                                 or r"your-name" in i]
        print(Cell_list1)
        driver.find_element_by_name(Cell_list1[0]).send_keys(ws2.cell(2, 2).value + "　")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "会社名")

        
#会社名ふりがな         
      if len([i for i in items_1 if "ふりがな（カナ）" in i]) > 0:
       Cell_list2 = [i for i in list_2 if "企業名ふりがな（カナ）" in i]
       print(Cell_list2)
#テキスト入力
       driver.find_element_by_name(Cell_list2[0]).send_keys(ws2.cell(3, 2).value)
       lastcol = len(list(ws1.row_values(k)))       
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "会社名カナ")


#フルネーム（姓＋名）
      if len([i for i in items_1 if "ふりがな" in i]) > 0:
       Cell_list3 = [i for i in list_2 if "姓" == i \
                      or "名" == i \
                          or "family_name" in i \
                              or "given_name" in i]
       print(Cell_list3)
       for j in range(1,len(Cell_list3)+1):
         print(Cell_list3[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)


#フルネーム（氏名）
      if len([i for i in items_1 if "名前" in i \
               or "担当者" in i \
                   or "氏名" in i]) > 0:
        Cell_list3 = [i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "r-name" in i \
                                 or "yourname" in i \
                                     or "fullname" in i \
                                         or "responsible-name" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)             
        ws1.update_cell(k, lastcol+1, "氏名")


#フルネームふりがな
#      try:
      if len([i for i in items_1 if "ふりがな" in i]) > 0:
       Cell_list5 = [i for i in list_2 if "せい" == i \
                      or "めい" == i]
       print(Cell_list5)
       for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)


#フルネームカタカナ（セイ＋メイ）
      if len([i for i in items_1 if "フリガナ" in i \
              or "カナ" in i]) > 0:
       Cell_list5 = [i for i in list_2 if "セイ" == i or "メイ" == i]
       print(Cell_list5)
       for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(8, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(8, 2+j).value)

#フルネームカタカナ（セイメイ）
      if len([i for i in items_1 if "フリガナ" in i \
              or "カナ" in i]) > 0:
       Cell_list5 = [i for i in list_2 if "your-kana" in i \
                    or "r-furi" in i \
                        or "furigana" in i]
       print(Cell_list5)

#テキスト入力
       driver.find_element_by_name(Cell_list5[0]).send_keys(ws2.cell(8, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "氏名フリガナ")

    
#メールアドレス
#「import email」はライブラリ参照のコマンドなので使用不可
      if not list_3 == []:
        Cell_list8 = [i for i in list_3 if "mail" in i \
                     or "メール" in i]
        print(Cell_list8)
#テキスト入力
        for j in range(1,len(Cell_list8)+1):           
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)
         ws1.update_cell(k, lastcol+1, "メールアドレス")
         
      elif list_3 == []:
        Cell_list8 = [i for i in list_2 if "mail" in i \
                     or "メール" in i]
        print(Cell_list8)
#テキスト入力
        for j in range(1,len(Cell_list8)+1):           
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)
         ws1.update_cell(k, lastcol+1, "メールアドレス")

        
#textareaタグのname値を取得
      TEXTAREA_list = []
      element3 = soup.find_all("textarea")
      textarea = soup.textarea["name"]
      for textarea in element3:
       TEXTAREA_list.append(textarea.get("name"))   
       print(textarea.get("name"))

#（詳細）
      if len(TEXTAREA_list) == 1:
       driver.find_element_by_name(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
       print(TEXTAREA_list[0])
       lastcol = len(list(ws1.row_values(k)))
#      time.sleep(1)            
       ws1.update_cell(k, lastcol+1, "本文")        

      elif len(TEXTAREA_list) > 1:
       if len([i for i in TEXTAREA_list if "件名" in i \
               or "内容" in i]) > 0:
        SELECT_list1 = [i for i in list_2 if "件名" in i \
                        or "内容" in i]
        print(SELECT_list1)
        for j in range(1, len(SELECT_list1)+1):
         driver.find_element_by_name(SELECT_list1[j-1]).send_keys(ws4.cell(j, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)            
         ws1.update_cell(k, lastcol+1, ws4.cell(j, 1).value)
        
#複数のテキストボックスが存在する場合
       elif len([i for i in TEXTAREA_list if "件名" in i \
               or "内容" in i]) == 0:
        for j in range(1, len(TEXTAREA_list)):
         driver.find_element_by_name(SELECT_list1[j-1]).send_keys(ws4.cell(1+j, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)            
         ws1.update_cell(k, lastcol+1, ws4.cell(1+j, 1).value)
        
       else:
        driver.find_element_by_name(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
        print(TEXTAREA_list[0])
        lastcol = len(list(ws1.row_values(k)))
#      time.sleep(1)            
        ws1.update_cell(k, lastcol+1, "本文")        


#プルダウンメニューの選択
      list_6 = []
      for element5 in soup.find_all("select"):
       list_6.append(element5.get("name"))

#（お問い合わせ内容）
      SELECT_list1 = []
      SELECT_list2 = []
      for element in soup.find_all("option"): 
        SELECT_list1.append(element.get("value"))
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
      SELECT_list1 = [i for i in SELECT_list1 if i is not None]
      print(SELECT_list1)      
      SELECT_list2 = [i for i in SELECT_list1 if "お問い合わせ" in i \
                      or "その他" in i \
                          or "営業" in i \
                              or "宣伝" in i]

      if len(SELECT_list2) > 0:
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, SELECT_list2[j-1])
      elif len(SELECT_list2) == 0:
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "適切なお問い合わせ種別なし")
          

#プルダウンメニュー（連絡方法）
      SELECT_list2 = []       
      SELECT_list2 = [i for i in SELECT_list1 if "メール" in i]
      print(SELECT_list2)
       
      if len(list_6) > 1:       
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
         dropdown = driver.find_element_by_name(list_6[1])
         print(list_6[1])
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
    
    
#チェックボックス
      element6 = soup.find_all("input",type="checkbox")
      list_6 = []
      
#（お問い合わせ内容）
#      try:
      if len([i for i in items_1 if "お問い合わせ内容" in i \
              or "ご依頼内容" in i \
                  or "件名" in i]) == 1:
          
       SELECT_list3 = []
       for elem1 in element6: 
        SELECT_list3.append(elem1.get("value"))

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
#選択肢：その他
       SELECT_list3 = [i for i in SELECT_list3 if i is not None \
                       and "その他" in i]
       print(SELECT_list3)

       SELECT_list4 = []
       for elem2 in element6: 
        SELECT_list4.append(elem2.get("id"))        
        
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
        SELECT_list4 = [i for i in SELECT_list4 if i is not None]
        print(SELECT_list4)

       
#value値のみ、id値なしの場合
       if len(SELECT_list3) > 0:
         print(len(SELECT_list3))
         if len([i for i in SELECT_list3 if "その他" == i]) == 1:
          checkbox = driver.find_element_by_css_selector("[value='その他']")
          driver.execute_script("arguments[0].click();", checkbox)
         elif len([i for i in SELECT_list3 if "その他ご質問" == i]) == 1:
          checkbox = driver.find_element_by_css_selector("[value='その他ご質問']")
          driver.execute_script("arguments[0].click();", checkbox)
         print(checkbox.is_selected())         
         if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(checkbox.is_selected())

         
#value値及びid値が存在する場合
       elif len(SELECT_list3) > 0 \
           and len(SELECT_list4) > 0:
         for i in range(1, len(SELECT_list3)+1):
          checkbox = driver.find_element_by_id(SELECT_list4[i-1])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[i-1])
           print(checkbox.is_selected())

        
#（個人情報取り扱いに関する同意）
      SELECT_list3 = []
      for elem1 in element6: 
       SELECT_list3.append(elem1.get("value"))
       print(SELECT_list3)

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
      SELECT_list3 = [i for i in SELECT_list3 if i is not None]
      print(SELECT_list3)

      if len([i for i in SELECT_list3 if "個人情報" in i]) == 1:
       pass
      if len([i for i in SELECT_list3 if "同意" in i]) == 1:
#       for elem1 in element6: 
#        SELECT_list3.append(elem1.get("name"))
       
       SELECT_list4 = []
       for elem2 in element6: 
        SELECT_list4.append(elem2.get("id"))

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
#       SELECT_list3 = [i for i in SELECT_list3 if i is not None]
#       print(SELECT_list3)
        
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list4 = [i for i in SELECT_list4 if i is not None]
       print(SELECT_list4)
           
#name、idの両方が存在する場合
#       if not len(SELECT_list3) == 0 \
#            and not len(SELECT_list4) == 0:
       checkbox = driver.find_element_by_id(SELECT_list4[0])
       driver.execute_script("arguments[0].click();", checkbox)
       print(checkbox.is_selected())
       if checkbox.is_selected() is True:       
        lastcol = len(list(ws1.row_values(k)))    
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "同意")

#nameのみ存在
#       elif not len(SELECT_list3) == 0 \
#            and len(SELECT_list4) == 0:
#         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
#         driver.execute_script("arguments[0].click();", checkbox)
#         lastcol = len(list(ws1.row_values(k)))    
#         time.sleep(1)             
#         ws1.update_cell(k, lastcol+1, "同意")
       
      elif "個人情報" in str(soup.find_all("form")) > 1 \
         or "同意" in str(soup.find_all("form")) > 0 \
             or "プライバシーポリシー" in str(soup.find_all("form")) > 0:
                 
       for elem1 in element6: 
        SELECT_list3.append(elem1.get("name"))
       
       SELECT_list4 = []
       for elem2 in element6: 
        SELECT_list4.append(elem2.get("id"))

#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list3 = [i for i in SELECT_list3 if i is not None]
       print(SELECT_list3)
        
#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理
       SELECT_list4 = [i for i in SELECT_list4 if i is not None]
       print(SELECT_list4)
#       for i in range(1, len(SELECT_list3)+1):
           
#name、idの両方が存在する場合
       if not len(SELECT_list3) == 0 \
            and not len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         print(checkbox.is_selected())
         if checkbox.is_selected() is True:       
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, "同意")
#         break
#nameのみ存在
       elif not len(SELECT_list3) == 0 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         print(checkbox.is_selected())
         if checkbox.is_selected() is True:       
          lastcol = len(list(ws1.row_values(k)))    
          time.sleep(1)             
          ws1.update_cell(k, lastcol+1, "同意")
#         break
#      except:
#       pass   

       
#ラジオボタン
      element5 = soup.find_all("input",type="radio")
#      print(element5)
      SELECT_list1 = []
      SELECT_list2 = []

      for elem in element5: 
        SELECT_list1.append(elem.get("value"))
        print(SELECT_list1)

      for elem in element5:
        SELECT_list2.append(elem.get("id"))
#        print(SELECT_list2)


#value値のみ、id値なしの場合
      if len(SELECT_list1) > 0 \
          and len(SELECT_list2) == 0:
       print(len(SELECT_list1))

#（種別）
       if len([i for i in SELECT_list1 if "その他" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='その他']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(radiobutton.is_selected())

#（連絡方法）
       if len([i for i in SELECT_list1 if "メール" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='メール']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "メール")
           print(radiobutton.is_selected())


#value値且つid値有りの場合
      elif len(SELECT_list1) > 0 \
          and len(SELECT_list2) > 0:
       print(len(SELECT_list1))
       print(len(SELECT_list2))

#（種別）
       if len([i for i in SELECT_list1 if "その他" in i]) > 0:
         radiobutton = driver.find_element_by_css_selector("[value='その他']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(radiobutton.is_selected())



#住所（郵便番号＋都道府県＋市町村＋建物名）
      if len([i for i in items_1 if "住所" in i]) > 0:
       Cell_list6 = [i for i in list_2 if "住所" in i \
                     or "addr" in i \
                         or "your-address" in i]
       print(Cell_list6)
       if len([i for i in Cell_list6 if "0" in i or "1" in i]) > 1:
        Cell_list7 =[i for i in Cell_list6 if "01" in i \
                     or "02" in i \
                         or "03" in i \
                             or "04" in i]
        print(Cell_list7)
        for j in range(1,len(Cell_list7)+1):
         driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)       
       else:
        driver.find_element_by_name(Cell_list6[0]) \
          .send_keys(ws2.cell(5, 2).value + ws2.cell(5, 3).value + ws2.cell(5, 4).value + ws2.cell(5, 5).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "住所")


      elif len([i for i in items_1 if "郵便番号" in i]) > 0:
       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i \
                         or "postalcode"
                         or "zip" in i]
       print(Cell_list6)
       driver.find_element_by_name(Cell_list6[0]) \
           .send_keys(ws2.cell(4, 3).value + ws2.cell(4, 4).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "郵便番号")
       
       if len([i for i in items_1 if "都道府県" in i]) > 0:
        Cell_list6 = [i for i in list_2 if "都道府県" in i]
        print(Cell_list6)
        if "都道府県" in Cell_list6:
         pref = driver.find_element_by_name(Cell_list6[0])
         pref.clear()
         pref.send_keys("東京都")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "都道府県")


         Cell_list6 = [i for i in list_2 if "市町村" in i]
         print(Cell_list6)
         Municipal = driver.find_element_by_name(Cell_list6[0])
         Municipal.clear()   
         Municipal.send_keys("新宿区新宿5-4-1")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "市区町村")


         Cell_list6 = [i for i in list_2 if "アパート" in i]
         print(Cell_list6)
         build = driver.find_element_by_name(Cell_list6[0])
         build.send_keys("新宿Qフラットビル8F")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "アパート")       


#ホームページアドレス
      try:
       Cell_list8 = [i for i in list_2 if "url" in i]

#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(16, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "URL")
      except:
       pass

#業種
      try:
       Cell_list8 = [i for i in list_2 if "industry" in i]
#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(10, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "業種")
      except:
       pass

#電話番号
#「type属性：tel」が存在する
      if not list_4 == []:
          
#（ハイフンあり）          
        Cell_list7 = [i for i in list_4 if "tel" in i \
                     or "電話" in i \
                         or r"your-phone" in i]
        print(Cell_list7)                      
        if not "ハイフンなし" in items_1:
         driver.find_element_by_name(Cell_list7[0]) \
             .send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")
            
        elif not "ハイフンなし" in items_1 \
           and "0" in list_4 \
               or "1" in list_4:
         Cell_list8 =[i for i in Cell_list7 if "0" in i \
                     or "1" in i \
                         or "2" in i]
         print(Cell_list8)
        
#テキスト入力＋市外局番別
         driver.find_element_by_name(Cell_list8[0]) \
           .send_keys("03")
         driver.find_element_by_name(Cell_list8[1]) \
           .send_keys("6384")
         driver.find_element_by_name(Cell_list8[2]) \
           .send_keys("1059")
         for j in range(1, len(Cell_list8)+1):
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)         


#「type属性：tel」が存在しない
      elif list_4 == []:
        Cell_list7 = [i for i in list_2 if "tel" in i \
                     or "電話" in i \
                         or "phone" in i]
        print(Cell_list7)                      
        if len([i for i in items_1 if "ハイフンなし" in i]) > 0:
         driver.find_element_by_name(Cell_list7[0]) \
             .send_keys(ws2.cell(14, 3).value \
                        + ws2.cell(14, 4).value + ws2.cell(14, 5).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンなし）")     
            
        elif not "ハイフンなし" in items_1 \
           and "0" in list_2 \
               or "1" in list_2:
         Cell_list8 =[i for i in Cell_list7 if "0" in i \
                     or "1" in i \
                         or "2" in i]
         print(Cell_list8)
        
#テキスト入力＋市外局番別
         driver.find_element_by_name(Cell_list8[0]) \
           .send_keys("03")
         driver.find_element_by_name(Cell_list8[1]) \
           .send_keys("6384")
         driver.find_element_by_name(Cell_list8[2]) \
           .send_keys("1059")
         for j in range(1, len(Cell_list8)+1):
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)
          
        else:
         driver.find_element_by_name(Cell_list7[0]) \
           .send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")


#件名
      try:
       if len([i for i in str(soup.find_all("form")) if "サービス名" in i \
               or "題名" in i \
                   or "キーワード" in i]) > 0:
        SELECT_list1 = [i for i in list_2 if "text_field" in i \
                        or "題名" in i]
        print(SELECT_list1)

#テキスト入力
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
      except:
       pass


    
#thタグのテキストを取得
     elif "お問い合わせ" in str(soup.find_all("th")) \
         or "メールアドレス" in str(soup.find_all("th")):
      element1 = soup.find_all("th")
      list_1 = []   
      for list_ in element1:
        if "企業名" in list_.getText() \
            or "貴社名" in list_.getText() \
                or "会社名" in list_.getText() \
                    or "御社名" in list_.getText() \
                        or "法人" in list_.getText() \
                        or "部署" in list_.getText() \
                            or "役職" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "お問合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "業種" in list_.getText() \
                                                    or "題名" in list_.getText() \
                                                        or "本文" in list_.getText() \
                                                            or "詳細" in list_.getText() \
                                                                or "連絡方法" in list_.getText() \
                                                                    or "用件" in list_.getText() \
                                                                        or "ご相談"in list_.getText() \
                                                                            or "ご要望" in list_.getText():
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
      print(items_1)


#inputタグのname値を取得
      element2 = soup.find_all("input",type="text")
      list_2 = []

      element3 = soup.find_all("input",type="email")
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []


#type属性：text
      for name in element2:
       list_2.append(name.get("name"))
       print(list_2)

#type属性：email
      for name in element3:
       list_3.append(name.get("name"))
       print(list_3)

#type属性：tel
      for name in element4:
       list_4.append(name.get("name"))
       print(list_4)

#会社名
      if not len([i for i in items_1 if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or "your-company" in i \
                         or "company_name" in i \
                             or "company-name" in i \
                                 or "customform_company" in i \
                                     or "会社名" in i]
        print(Cell_list1)    
        driver.find_element_by_name(Cell_list1[0]).send_keys(ws2.cell(2, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "会社名")

#会社名ふりがな         
      if len([i for i in items_1 if "ふりがな（カナ）" in i \
              or "御社名" in i]) > 0:
       Cell_list2 = [i for i in list_2 if "企業名ふりがな（カナ）" in i \
                     or "company_kana_name" in i]
       print(Cell_list2)
       driver.find_element_by_name(Cell_list2[0]).send_keys(ws2.cell(3, 2).value)
       lastcol = len(list(ws1.row_values(k)))       
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "会社名カナ")

#フルネーム（姓＋名）
      Cell_list3 = [i for i in list_2 if "姓" == i \
                      or "名" == i]
      print(Cell_list3)
      for j in range(1,len(Cell_list3)+1):
         print(Cell_list3[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)

#フルネーム（氏名）
      if not len([i for i in items_1 if "名前" in i \
               or "担当者" in i \
                   or "氏名" in i]) == 0:
        Cell_list3 = [i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "c_name" in i \
                                 or "customform_name" in i \
                                     or "personal_name" in i \
                                 or "name" == i]
        print(Cell_list3)    
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "氏名")


#フルネームふりがな
#      try:
      Cell_list5 = [i for i in list_2 if "せい" == i \
                      or "めい" == i]
      print(Cell_list5)
      for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)
#      except:
#       pass


#フルネームカタカナ（セイ＋メイ）
#      try:
      Cell_list5 = [i for i in list_2 if "セイ" == i or "メイ" == i]
      print(Cell_list5)
      for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(8, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(8, 2+j).value)


#フルネームカタカナ（セイメイ）
      if not len([i for i in items_1 if "氏名" in i]) == 0:
       Cell_list5 = [i for i in list_2 if "your-kana" in i \
                     or "personal_kana_name" in i]
       print(Cell_list5)
       driver.find_element_by_name(Cell_list5[0]).send_keys(ws2.cell(8, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "氏名フリガナ")


#部署名
      if not len([i for i in items_1 if "部署" in i]) == 0:
        Cell_list3 = [i for i in list_2 if "dept" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(9, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "部署名")

#役職
      if not len([i for i in items_1 if "役職" in i]) == 0:
        Cell_list3 = [i for i in list_2 if "class" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(11, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "役職")



#住所（郵便番号＋都道府県＋市町村＋建物名）
      if len([i for i in items_1 if "住所" in i]) == 1:
#      try:
#       Cell_list6 = []    
       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i \
                         or "postalcode"
                         or "zip" in i]
#       if "ハイフンなし" in items_1:
       print(Cell_list6)
       driver.find_element_by_name(Cell_list6[0]) \
           .send_keys(ws2.cell(4, 3).value + ws2.cell(4, 4).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "郵便番号")
#      except:
#        pass

       Cell_list6 = [i for i in list_2 if "住所" in i \
                     or "addr" in i]
#       if "ハイフンなし" in items_1:
       print(Cell_list6)
       driver.find_element_by_name(Cell_list6[0]) \
          .send_keys(ws2.cell(5, 2).value + ws2.cell(5, 3).value + ws2.cell(5, 4).value + ws2.cell(5, 5).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "住所")
    
#      try:
#       Cell_list6 = []
       Cell_list6 = [i for i in list_2 if "都道府県" in i \
                     or "your-address" in i]
       print(Cell_list6)

       if len([i for i in Cell_list6 if "0" in i or "1" in i]) > 1:
        Cell_list7 =[i for i in Cell_list6 if "01" in i \
                     or "02" in i \
                         or "03" in i \
                             or "04" in i]
        print(Cell_list7)
        for j in range(1,len(Cell_list7)+1):
         driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)

       
       elif "都道府県" in Cell_list6:
        list_6 = []
        for element5 in soup.find_all("select"):
         list_6.append(element5.get("name"))
        SELECT_list1 = []
        SELECT_list2 = []
        for element in soup.find_all("option"):
         SELECT_list1.append(element.get("value"))
         print(SELECT_list1)
        if len([i for i in SELECT_list1 if ws2.cell(5, 2).value in i]) > 0:
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
         select = Select(dropdown)
         select.select_by_value(ws2.cell(5, 2).value)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "都道府県")
         
         Cell_list6 = [i for i in list_2 if "customform_address" in i]
         print(Cell_list6)
         Municipal = driver.find_element_by_name(Cell_list6[0])
         Municipal.clear()   
         Municipal.send_keys(ws2.cell(5, 3).value \
                             + ws2.cell(5, 4).value \
                                 + ws2.cell(5, 5).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "市区町村建物名")
         
        else:
         pref = driver.find_element_by_name(Cell_list6[0])
         pref.clear()
         pref.send_keys("東京都")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "都道府県")
        
         Cell_list6 = [i for i in list_2 if "市町村" in i]
         print(Cell_list6)
         Municipal = driver.find_element_by_name(Cell_list6[0])
         Municipal.clear()   
         Municipal.send_keys("新宿区新宿5-4-1")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "市区町村")

         Cell_list6 = [i for i in list_2 if "アパート" in i]
         print(Cell_list6)
         build = driver.find_element_by_name(Cell_list6[0])
         build.send_keys("新宿Qフラットビル8F")
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "建物名")
                           

#メールアドレス
#「import email」はライブラリ参照のコマンドなので使用不可
#      try:
#       import email_addr
#       Cell_8 = email_addr.Cell_8
      if not list_3 == []:
        Cell_list8 = [i for i in list_3 if "mail" in i \
                     or "メール" in i]
#テキスト入力
        for j in range(1,len(Cell_list8)+1):           
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
         ws1.update_cell(k, lastcol+1, "メールアドレス")
         
      elif list_3 == []:
        Cell_list8 = [i for i in list_2 if "mail" in i \
                     or "メール" in i]
#テキスト入力      
        driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(17, 2).value)
        print(Cell_list8)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)
        ws1.update_cell(k, lastcol+1, "メールアドレス")
#      except:
#       pass

#ホームページアドレス
      try:
#       if not list_2 == []:
       Cell_list8 = [i for i in list_2 if "url" in i]
#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(16, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "URL")
      except:
       pass

#業種
      try:
#       if not list_2 == []:
       Cell_list8 = [i for i in list_2 if "industry" in i]
#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(10, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "業種")
      except:
       pass


         
#電話番号
#「type属性：tel」が存在する
      if not list_4 == []:
          
#（ハイフンあり）          
        Cell_list7 = [i for i in list_4 if "tel" in i \
                     or "電話" in i \
                         or r"your-phone" in i]
        print(Cell_list7)                      
        if not "ハイフンなし" in items_1:
         driver.find_element_by_name(Cell_list7[0]) \
             .send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")
            
        elif not "ハイフンなし" in items_1 \
           and "0" in list_4 \
               or "1" in list_4:
         Cell_list8 =[i for i in Cell_list7 if "0" in i \
                     or "1" in i \
                         or "2" in i]
         print(Cell_list8)
        
#テキスト入力＋市外局番別
         driver.find_element_by_name(Cell_list8[0]) \
           .send_keys(ws2.cell(14, 3).value)
         driver.find_element_by_name(Cell_list8[1]) \
           .send_keys(ws2.cell(14, 4).value)
         driver.find_element_by_name(Cell_list8[2]) \
           .send_keys(ws2.cell(14, 5).value)
         for j in range(1, len(Cell_list8)+1):
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)         


#「type属性：tel」が存在しない
      elif list_4 == []:
        Cell_list7 = [i for i in list_2 if "tel" in i \
                     or "電話" in i \
                         or "phone" in i]
        print(Cell_list7)                      
        if len([i for i in items_1 if "ハイフンなし" in i]) > 1:
         driver.find_element_by_name(Cell_list7[0]) \
             .send_keys(ws2.cell(14, 3).value \
                        + ws2.cell(14, 4).value + ws2.cell(14, 5).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "電話（ハイフンなし）")     
            
        elif not "ハイフンなし" in items_1 \
           and "0" in list_2 \
               or "1" in list_2:
         Cell_list8 =[i for i in Cell_list7 if "0" in i \
                     or "1" in i \
                         or "2" in i]
         print(Cell_list8)
        
#テキスト入力＋市外局番別
         driver.find_element_by_name(Cell_list8[0]) \
           .send_keys(ws2.cell(14, 3).value)
         driver.find_element_by_name(Cell_list8[1]) \
           .send_keys(ws2.cell(14, 4).value)
         driver.find_element_by_name(Cell_list8[2]) \
           .send_keys(ws2.cell(14, 5).value)
         for j in range(1, len(Cell_list8)+1):
          lastcol = len(list(ws1.row_values(k)))
          time.sleep(3)
          ws1.update_cell(k, lastcol+1, ws2.cell(14, 2+j).value)         
             
        elif not "ハイフンなし" in items_1 \
           and not "0" in list_2 \
               or not "1" in list_2:
        
         driver.find_element_by_name(Cell_list7[0]) \
           .send_keys(ws2.cell(14, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
         ws1.update_cell(k, lastcol+1, "電話番号")


#textareaタグのname値を取得
      TEXTAREA_list = []
      element3 = soup.find_all("textarea")
      textarea = soup.textarea["name"]
      for textarea in element3:
       TEXTAREA_list.append(textarea.get("name"))   
       print(textarea.get("name"))

#件名
      try:
       import subject
       Cell_9 = subject.Cell_9
       time.sleep(1)          
       ws4.update_cell(Cell_9.row, Cell_9.col+1, TEXTAREA_list[0])
       print(ws4.cell(Cell_9.row, Cell_9.col+1).value)        

#テキスト入力
       driver.find_element_by_name(ws4.cell(Cell_9.row, Cell_9.col+1).value).send_keys(ws2.cell(1, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)            
       ws1.update_cell(k, lastcol+1, "タイトル")
      except:
       pass
  
#詳細
      driver.find_element_by_name(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
      print(TEXTAREA_list[0])
      lastcol = len(list(ws1.row_values(k)))
#      time.sleep(1)            
      ws1.update_cell(k, lastcol+1, "本文")        


#プルダウンメニュー
#      import select_type
      list_6 = []
      for element5 in soup.find_all("select"):
       list_6.append(element5.get("name"))

#（お問い合わせ内容）
#      try:
#       Cell_11 = select_type.Cell_11
      SELECT_list1 = []
      SELECT_list2 = []
#      element2 = soup.find("select")
      for element in soup.find_all("option"): 
        SELECT_list1.append(element.get("value"))
        print(SELECT_list1)
      
      SELECT_list2 = [i for i in SELECT_list1 if "お問い合わせ" in i \
                      or "その他" in i \
                          or "営業" in i \
                              or "宣伝" in i]
      print(SELECT_list2)
      if len(list_6) == 1 \
           or len(list_6) > 1:
#        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[len(SELECT_list2)-1])
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, SELECT_list2[len(SELECT_list2)-1])
#      except:
#       pass

#プルダウンメニュー（連絡方法）
      try:
#       import select_type
#       Cell_12 = select_type.Cell_12
#       print(Cell_12.value)
#       SELECT_list1 = []
       SELECT_list2 = []       
       SELECT_list2 = [i for i in SELECT_list1 if "メール" in i]
       print(SELECT_list2)
       
       if len(list_6) > 1:       
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
#        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[j-1])
         dropdown = driver.find_element_by_name(list_6[1])
         print(list_6[1])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
      except:
       pass    


#チェックボックス
      list_6 = []
      element6 = soup.find_all("input",type="checkbox")
      for elem in element6:
       list_6.append(elem.get("name"))
       print(list_6)
      
#（お問い合わせ内容）
#      try:
      if len([i for i in items_1 if "お問い合わせ内容" in i \
              or "ご依頼内容" in i \
                  or "ご相談内容" in i]) == 1:
          
       SELECT_list3 = []
       for elem1 in element6: 
        SELECT_list3.append(elem1.get("value"))

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
#        if "個人情報" in str(soup.find_all("form")) \
#          or "同意" in str(soup.find_all("form")) \
#             or "プライバシーポリシー" in str(soup.find_all("form")) == 1:

#選択肢：その他                 
       SELECT_list3 = [i for i in SELECT_list3 if "その他" in i]
       print(SELECT_list3)
       
#value値のみ、id値なしの場合
       if len(SELECT_list3) > 0 \
           and len(SELECT_list4) == 0:
#        for i in range(1, len(list_6)+1):
         checkbox = driver.find_element_by_css_selector("[value='その他']")
#         checkbox.click()
         driver.execute_script("arguments[0].click();", checkbox)
         print(checkbox.is_selected())         
         if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(checkbox.is_selected())
       
#value値及びid値が存在する場合
       elif len(SELECT_list3) > 0 \
           and len(SELECT_list4) > 0:
         for i in range(1, len(SELECT_list3)+1):
          checkbox = driver.find_element_by_id(SELECT_list4[i-1])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[i-1])
           print(checkbox.is_selected())

#         else:
#          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list3)-2])
#          driver.execute_script("arguments[0].click();", checkbox)
#          if checkbox.is_selected() is True:
#           lastcol = len(list(ws1.row_values(k)))    
#           time.sleep(1)             
#           ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list3)-2])
#           print(checkbox.is_selected())
#           break

        
#（個人情報取り扱いに関する同意）
      if "個人情報" in str(soup.find_all("form")) \
         or "同意" in str(soup.find_all("form")) \
             or "プライバシーポリシー" in str(soup.find_all("form")) == 1:
                 
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
         ws1.update_cell(k, lastcol+1, "同意")         
#         break
#nameのみ存在
       elif len(SELECT_list3) == 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[0])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")
       elif len(SELECT_list3) > 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")
#         break
#      except:
#       pass   


#ラジオボタン
      element5 = soup.find_all("input",type="radio")
      print(element5)
      element6 = soup.find_all("input",class_="questionTypeRadio")
      print(element6)
      element7 = soup.find_all("input",attrs={"name":"questioner_type","type":"radio"})
      print(element7)
      
      SELECT_list1 = []
      SELECT_list2 = []
      SELECT_list3 = []
      SELECT_list4 = []

      for elem in element5: 
        SELECT_list1.append(elem.get("value"))
#        print(SELECT_list1)

      for elem in element5:
        SELECT_list2.append(elem.get("id"))
#        print(SELECT_list2)

      for elem in element6: 
        SELECT_list3.append(elem.get("id"))
#        print(SELECT_list3)

      for elem in element7: 
        SELECT_list4.append(elem.get("id"))
        print(SELECT_list4)

#value値のみ、id値なしの場合
      if len(SELECT_list1) > 0 \
          and len(SELECT_list2) == 0 \
              and len(SELECT_list3) == 0 \
                  and len(SELECT_list4) == 0:
       print(len(SELECT_list1))
       print(len(SELECT_list2))
       print(len(SELECT_list3))
       print(len(SELECT_list4))

#（種別）
       if len([i for i in SELECT_list1 if "その他" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='その他']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "その他")
           print(radiobutton.is_selected())

#（連絡方法）
       if len([i for i in SELECT_list1 if "メール" in i]) == 1:
         radiobutton = driver.find_element_by_css_selector("[value='メール']")
         driver.execute_script("arguments[0].click();", radiobutton)
         print(radiobutton.is_selected())
         if radiobutton.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, "メール")
           print(radiobutton.is_selected())

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



#指定のタグが存在しない場合
     else:
      element1 = soup.find_all("form")
      list_1 = []   
      for list_ in element1:
        if "企業名" in list_.getText() \
            or "貴社名" in list_.getText() \
                or "会社名" in list_.getText() \
                    or "御社名" in list_.getText() \
                        or "ふりがな" in list_.getText() \
                            or "フリガナ" in list_.getText() \
                                or "カナ" in list_.getText() \
                                    or "担当者" in list_.getText() \
                        or "郵便番号" in list_.getText() \
                            or "都道府県" in list_.getText() \
                                or "市区町村" in list_.getText() \
                                    or "番地" in list_.getText() \
                                        or "建物名" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "氏名" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
                                                    or "Email" in list_.getText() \
                                                        or "種別" in list_.getText() \
                                                            or "業種" in list_.getText() \
                                                                or "題名" in list_.getText() \
                                                                    or "本文" in list_.getText() \
                                                                        or "詳細" in list_.getText() \
                                                                            or "連絡方法" in list_.getText() \
                                                                                or "用件" in list_.getText() \
                                                                                    or "ご意見" in list_.getText() \
                                                                                        or "返信方法" in list_.getText():
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
         
      print(items_1)
      items_2 = []
      items_3 = []
      items_4 = []
      
#inputタグの各要素を取得
      element2 = soup.find_all("input",type="text")
      print(element2)
      list_2 = []

      element3 = soup.find_all("input",type="email")
      print(element3)
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []


#type属性：text
      for name in element2:
       list_2.append(name.get("name"))
       print(list_2)
      
      list_2d = []
      for name in element2:
        list_2d.append(name.get("data-name"))
        print(list_2d)
       
      for elem in element2:
#       items_1.append(name.get("placeholder"))
       items_2.append(elem.get("id"))
       print(items_2)

      list_2c = []
      for elem in element2:
#       items_1.append(name.get("placeholder"))
       list_2c.append(elem.get("class"))
       print(items_2)

#type属性：email
      for name in element3:
       list_3.append(name.get("name"))
       print(list_3)
      
      list_3d = []
      for name in element3:
        list_3d.append(name.get("data-name"))
        print(list_3d)
 
      for elem in element3:
#       items_1.append(name.get("placeholder"))
       items_3.append(elem.get("id"))
       print(items_3)

      list_3c = []
      for elem in element3:
#       items_1.append(name.get("placeholder"))
       list_3c.append(elem.get("class"))
       print(items_3)
       
#type属性：tel
      for name in element4:
       list_4.append(name.get("name"))
       print(list_4)
       
      for elem in element4:
#       items_1.append(name.get("placeholder"))
       items_4.append(elem.get("id"))
       print(items_4)


#リストにNoneが含まれていると「TypeError: argument of type 'NoneType' is not iterable」
#が発生するので、リスト内包表記で処理

#name値
      if not len(list_2) == 0:
       list_2 = [i for i in list_2 if i is not None]
       print(list_2)
      if not len(list_3) == 0:
       list_3 = [j for j in list_3 if j is not None]
       print(list_3)

#data-name値       
      if not len(list_2d) == 0:
       list_2d = [i for i in list_2d if i is not None]
       print(list_2d)
      if not len(list_3d) == 0:
       list_3d = [j for j in list_3d if j is not None]
       print(list_3d)
       
#id値
      print(items_2)
      print(items_3)
      print(items_4)

#id値
      print(list_2c)
      print(list_3c)
      
#会社名
#      try:
      if not len([i for i in items_1 if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or "your-company" in i \
                         or "company-name" in i \
                             or "name" in i]
        print(Cell_list1)
#テキスト入力          
        driver.find_element_by_name(Cell_list1[0]).send_keys(ws2.cell(2, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)
        ws1.update_cell(k, lastcol+1, "会社名")
#      except:
#       pass

#会社名ふりがな         
#      try:
      if len([i for i in str(soup.find_all("form")) if "ふりがな（カナ）" in i]) > 1:
       Cell_list2 = [i for i in list_2 if "企業名ふりがな（カナ）" in i]
       print(Cell_list2)
#テキスト入力
       driver.find_element_by_name(Cell_list2[0]).send_keys(ws2.cell(3, 2).value)
       lastcol = len(list(ws1.row_values(k)))       
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "会社名カナ")
#      except:
#       pass

#フルネーム（姓＋名）
#      try:
      Cell_list3 = [i for i in list_2 if "姓" == i \
                      or "名" == i]
      print(Cell_list3)
      for j in range(1,len(Cell_list3)+1):
         print(Cell_list3[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list3[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)
#      except:
#       pass

#フルネーム（氏名）
      if not len(list_2d) == 0:
       Cell_list3 = [i for i in list_2d if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                                 or "name" == i]
       print(Cell_list3)
       driver.find_element_by_id(items_2[0]).send_keys(ws2.cell(6, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "氏名")
      elif not len(list_2) == 0:
       Cell_list3 = [i for i in items_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "f4a6f2b" in i \
                                 or "name" == i]
       print(Cell_list3)
       driver.find_element_by_id(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1) 
       ws1.update_cell(k, lastcol+1, "氏名")

      elif not len(list_2c) == 0:
       driver.find_elements_by_class_name(list_2c[0])[0].send_keys(ws2.cell(6, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "氏名")

#フルネームふりがな
#      try:
      Cell_list5 = [i for i in list_2 if "せい" == i \
                      or "めい" == i]
      print(Cell_list5)
      for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(7, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(7, 2+j).value)
#      except:
#       pass


#フルネームカタカナ（セイ＋メイ）
#      try:
      Cell_list5 = [i for i in list_2 if "セイ" == i or "メイ" == i]
      print(Cell_list5)
      for j in range(1,len(Cell_list5)+1):
         print(Cell_list5[j-1])

#テキスト入力
         driver.find_element_by_name(Cell_list5[j-1]).send_keys(ws2.cell(8, 2+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(8, 2+j).value)

      try:
#フルネームカタカナ（セイメイ）
       Cell_list5 = [i for i in list_2 if "your-kana" in i]
       print(Cell_list5)

#テキスト入力
       driver.find_element_by_name(Cell_list5[0]).send_keys(ws2.cell(8, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "氏名フリガナ")
      except:
       pass


#住所（郵便番号＋都道府県＋市町村＋建物名）
      try:
#       Cell_list6 = []    
       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i]
#       if "ハイフンなし" in items_1:
       print(Cell_list6)
       driver.find_element_by_name(Cell_list6[0]).send_keys("1600022")
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "郵便番号")
      except:
        pass
    
#      try:
#       Cell_list6 = []
      Cell_list6 = [i for i in list_2 if "都道府県" in i \
                     or "your-address" in i]
      print(Cell_list6)

      if len([i for i in Cell_list6 if "0" in i or "1" in i]) > 1:
        Cell_list7 =[i for i in Cell_list6 if "01" in i \
                     or "02" in i \
                         or "03" in i \
                             or "04" in i]
        print(Cell_list7)
        for j in range(1,len(Cell_list7)+1):
         driver.find_element_by_name(Cell_list7[j-1]).send_keys(ws2.cell(5, 1+j).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, ws2.cell(5, 1+j).value)
         
      elif "都道府県" in Cell_list6: 
        pref = driver.find_element_by_name(Cell_list6[0])
        pref.clear()
        pref.send_keys("東京都")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "都道府県")
#      except:
#        pass

#      try:
        Cell_list6 = [i for i in list_2 if "市町村" in i]
        print(Cell_list6)
        Municipal = driver.find_element_by_name(Cell_list6[0])
        Municipal.clear()   
        Municipal.send_keys("新宿区新宿5-4-1")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "市区町村")
#      except:
#        pass

#      try:
        Cell_list6 = [i for i in list_2 if "アパート" in i]
        print(Cell_list6)
        build = driver.find_element_by_name(Cell_list6[0])
        build.send_keys("新宿Qフラットビル8F")
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "アパート")       
#      except:
#        pass
                           

#メールアドレス
      if not len(list_3d) == 0:
       Cell_list8 = [i for i in list_3d if "mail" in i \
                     or "メール" in i]
       print(Cell_list8)
       if len([i for i in Cell_list8 if "メール" in i]) > 0 \
          and len(items_3) > 0:
        for j in range(1,len(Cell_list8)+1):
         driver.find_element_by_id(items_3[j-1]).send_keys(ws2.cell(17, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1) 
         ws1.update_cell(k, lastcol+1, "メール")


      elif not list_3 == []:
        Cell_list8 = [i for i in list_3 if "mail" in i \
                     or "メール" in i]
#テキスト入力
        for j in range(1,len(Cell_list8)+1):          
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8[j-1])
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
         ws1.update_cell(k, lastcol+1, "メールアドレス")
         
      elif list_3 == []:
        Cell_list8 = [i for i in list_2 if "mail" in i \
                     or "メール" in i]
#テキスト入力      
        driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(17, 2).value)
        print(Cell_list8)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)
        ws1.update_cell(k, lastcol+1, "メールアドレス")

      elif not list_3c == []:
        driver.find_element_by_class_name(list_3c[0]).send_keys(ws2.cell(17, 2).value)
        print(list_3c)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)
        ws1.update_cell(k, lastcol+1, "メールアドレス")


#ホームページアドレス
      try:
#       if not list_2 == []:
       Cell_list8 = [i for i in list_2 if "url" in i]
#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(16, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "URL")
      except:
       pass

#業種
      try:
#       if not list_2 == []:
       Cell_list8 = [i for i in list_2 if "industry" in i]
#テキスト入力
       driver.find_element_by_name(Cell_list8[0]).send_keys(ws2.cell(10, 2).value)
       print(Cell_list8)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)
       ws1.update_cell(k, lastcol+1, "業種")
      except:
       pass

         
#電話番号
#「type属性：tel」が存在する
      if not len(list_4) == 0 :
#       Cell_list7 = [i for i in list_4 if "tel" in i \
#                     or "電話" in i \
#                         or "your-phone" in i]
#       print(Cell_list7)
#       if len(Cell_list7) > 0 and len(items_3) > 0:

        driver.find_element_by_id(items_4[0]).send_keys(ws2.cell(14, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")

#「type属性：tel」が存在しない
      elif not len(list_2d) == 0:
       Cell_list7 = [i for i in list_2d if "tel" in i \
                     or "電話" in i \
                         or "your-phone" in i]
       print(Cell_list7)
       if len(Cell_list7) > 0 and len(items_3) > 0:

        driver.find_element_by_id(items_2[1]).send_keys(ws2.cell(14, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")

      elif not len(list_2c) == 0:
        driver.find_elements_by_class_name(list_2c[0])[1].send_keys(ws2.cell(14, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")


#textareaタグのname値を取得
      TEXTAREA_list1 = []
      TEXTAREA_list2 = []
      TEXTAREA_list3 = []
      element3 = soup.find_all("textarea")
      print(element3)
       
      for textarea in element3:
        TEXTAREA_list1.append(textarea.get("id"))
#       for elem3 in element3: 
#        items_1.append(name.get("placeholder"))
#        print(items_1)
        driver.find_element_by_id(TEXTAREA_list1[0]).send_keys(ws3.cell(1, 1).value)
        print(TEXTAREA_list1[0])
        lastcol = len(list(ws1.row_values(k)))
        ws1.update_cell(k, lastcol+1, "本文")        

        if len(TEXTAREA_list1) == 0:
         for textarea in element3:
          TEXTAREA_list2.append(textarea.get("name"))   
          print(textarea.get("name"))
       
          driver.find_element_by_name(TEXTAREA_list2[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list2[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")
          
        elif len(TEXTAREA_list1) == 0 \
            and len(TEXTAREA_list2) == 0:
         for textarea in element3:
          TEXTAREA_list3.append(textarea.get("class"))
          print(textarea.get("name"))
       
          driver.find_element_by_name(TEXTAREA_list3[0]).send_keys(ws3.cell(1, 1).value)
          print(TEXTAREA_list3[0])
          lastcol = len(list(ws1.row_values(k)))
          ws1.update_cell(k, lastcol+1, "本文")         
#      else:

  
#プルダウンメニュー
#      import select_type
      list_6 = []
      for element5 in soup.find_all("select"):
       list_6.append(element5.get("name"))

#（お問い合わせ内容）
#      try:
#       Cell_11 = select_type.Cell_11
      SELECT_list1 = []
      SELECT_list2 = []
#      element2 = soup.find("select")
      for element in soup.find_all("option"): 
        SELECT_list1.append(element.get("value"))
        print(SELECT_list1)
      
      SELECT_list2 = [i for i in SELECT_list1 if "お問い合わせ" in i \
                      or "その他" in i \
                          or "営業" in i \
                              or "宣伝" in i]
      print(SELECT_list2)
      if len(list_6) == 1 \
           or len(list_6) > 1:
#        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[len(SELECT_list2)-1])
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, SELECT_list2[len(SELECT_list2)-1])
#      except:
#       pass

#プルダウンメニュー（連絡方法）
      try:
#       import select_type
#       Cell_12 = select_type.Cell_12
#       print(Cell_12.value)
#       SELECT_list1 = []
       SELECT_list2 = []       
       SELECT_list2 = [i for i in SELECT_list1 if "メール" in i]
       print(SELECT_list2)
       
       if len(list_6) > 1:       
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
#        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[j-1])
         dropdown = driver.find_element_by_name(list_6[1])
         print(list_6[1])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
      except:
       pass    


#チェックボックス
      element6 = soup.find_all("input",type="checkbox")
      list_6 = []
      
#（お問い合わせ内容）
#      try:          
      SELECT_list3 = []
      for elem1 in element6: 
       SELECT_list3.append(elem1.get("data-name"))

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

      
      if not "お問い合わせ内容" in str(soup.find_all("form")) == 0:
          
#両リスト内が1個必ず存在する場合において、更にリスト内包表記で処理
         if len(SELECT_list3) > 0 \
             and len(SELECT_list4) > 0:
          SELECT_list4 = [i for i in SELECT_list3 if "その他" in i]
          print(SELECT_list4)
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:           
            lastcol = len(list(ws1.row_values(k)))    
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list4)-1])
            print(checkbox.is_selected())
#           break
      else:
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list3)-2])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list3)-2])
           print(checkbox.is_selected())


      if not "返信方法" in str(soup.find_all("form")) == 0:
         
#両リスト内が1個必ず存在する場合において、更にリスト内包表記で処理
         if len(SELECT_list3) > 0 \
             and len(SELECT_list4) > 0:
          SELECT_list4 = [i for i in SELECT_list3 if "メール" in i]
          print(SELECT_list4)
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list4)-1])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:           
            lastcol = len(list(ws1.row_values(k)))    
            time.sleep(1)             
            ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list4)-1])
            print(checkbox.is_selected())
#           break
      else:
          checkbox = driver.find_element_by_id(SELECT_list4[len(SELECT_list3)-2])
          driver.execute_script("arguments[0].click();", checkbox)
          if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list4[len(SELECT_list3)-2])
           print(checkbox.is_selected())
        
#（個人情報取り扱いに関する同意）
      if "個人情報" in str(soup.find_all("form")) \
         or "同意" in str(soup.find_all("form")) \
             or "プライバシーポリシー" in str(soup.find_all("form")) == 1:
                 
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
         ws1.update_cell(k, lastcol+1, "同意")         
#         break
#nameのみ存在
       elif len(SELECT_list3) == 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[0])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")
       elif len(SELECT_list3) > 1 \
            and len(SELECT_list4) == 0:
         checkbox = driver.find_element_by_name(SELECT_list3[len(SELECT_list3)-1])
         driver.execute_script("arguments[0].click();", checkbox)
         lastcol = len(list(ws1.row_values(k)))    
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "同意")
#         break
#      except:
#       pass   


#ラジオボタン（連絡方法）
#      try:
      element5 = soup.find_all("input",type="radio")
      print(element5)
#       list_5 = []
      SELECT_list1 = []
#      SELECT_list2 = []
#      element2 = soup.find("select")
#      for element5 in soup.find_all("select"):
#       print(element5.get("name"))
      for elem in element5: 
        SELECT_list1.append(elem.get("id"))
        print(SELECT_list1)
      
      if "種別" in str(soup.find_all("form")):
       radiobutton = driver.find_element_by_id(SELECT_list1[len(SELECT_list1)-1])
       driver.execute_script("arguments[0].click();", radiobutton)
       print(SELECT_list1[len(SELECT_list1)-1])
       if radiobutton.is_selected() is True:
          print(radiobutton.is_selected())
          lastcol = len(list(ws1.row_values(k)))                
          ws4.update_cell(k, lastcol+1, SELECT_list1[len(SELECT_list1)-1])
#      except:
#       pass


    else:
     ws1.update_cell(k, 9, "フォーム要素取得不可")
 except:
  ws1.update_cell(k, 9, "無限ページロードによりスキップしました。")
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