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
#driver.set_page_load_timeout(60)

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
for k in tqdm(range(25, 26)):
    
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
# print(html)
    soup = BeautifulSoup(html, 'html.parser')
#    print(soup.find("form"))

#フォーム送信ＮＧ
    if "営業のご連絡" in html \
        or "営業のお問い合わせ" in html:
     ws1.update_cell(k, 9, "営業お断り！！")
    elif "recaptcha" in html:
     ws1.update_cell(k, 9, "reCAPTCHA")
    elif "予算" in str(soup.find_all("form")) \
        or "納期" in str(soup.find_all("form")):
     ws1.update_cell(k, 9, "サービスに関する専用フォーム")
#自動送信対象     
    elif "確認" in str(soup.find_all("form")) \
        or "送信" in str(soup.find_all("form")):
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
#      name = soup.input["name"]

      element3 = soup.find_all("input",type="email")
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []

      element5 = soup.find_all("input",type="radio")
      list_5 = []


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
#      try:
      if not len([i for i in items_1 if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i \
                       or "貴社名" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or r"your-company" in i \
                         or "company" in i]
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
                                 or "yourname" in i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)             
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
                           

#メールアドレス
#「import email」はライブラリ参照のコマンドなので使用不可
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
        for j in range(1,len(Cell_list8)+1):           
         driver.find_element_by_name(Cell_list8[j-1]).send_keys(ws2.cell(17, 2).value)
         print(Cell_list8)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(3)
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
        for j in range(1, len(SELECT_list2)+1):
         time.sleep(1)          
         dropdown = driver.find_element_by_name(list_6[0])
         print(list_6[0])
#        dropdown.click()
         select = Select(dropdown)
         select.select_by_value(SELECT_list2[j-1])
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
      try:
       import select_type
       Cell_11 = select_type.Cell_11
       SELECT_list1 = []
       SELECT_list2 = []
#      element2 = soup.find("select")
#      for element5 in soup.find_all("select"):
#       print(element5.get("name"))
       for elem in element5: 
        SELECT_list1.append(elem.get("id"))
        print(SELECT_list1)
      
       SELECT_list2 = [i for i in SELECT_list1 if "mail" in i \
                      or "その他" in i]
       print(SELECT_list2)
       
       for i in range(1, len(SELECT_list2)+1):
        time.sleep(1)
        ws4.update_cell(Cell_11.row, Cell_11.col+1, SELECT_list2[i-1])
        radio = driver.find_element_by_id(ws4.cell(Cell_11.row, Cell_11.col+1).value)
        driver.execute_script("arguments[0].click();", radio)
      except:
       pass


#pタグのテキストを取得
     elif "お問い合せ" in str(soup.find_all("p")):
      element1 = soup.find_all("p")
      list_1 = []
      for list_ in element1:
        if "企業名" in list_.getText() \
            or "ふりがな" in list_.getText() \
                or "フリガナ" in list_.getText() \
                    or "担当者" in list_.getText() \
                        or "住所" in list_.getText() \
                            or "お問い合わせ" in list_.getText() \
                                or "お問い合せ" in list_.getText() \
                                    or "名前" in list_.getText() \
                                        or "電話" in list_.getText() \
                                            or "連絡先" in list_.getText() \
                                                or "メールアドレス" in list_.getText() \
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
                                                for i in list_1]
      for j in range(1,len(items_1)+1):
        lastrow = len(ws4.col_values(1))
        time.sleep(1)
        ws4.update_cell(lastrow+1, 1, items_1[j-1])
        print(ws4.cell(lastrow+1, 1).value)

        

#inputタグのname値を取得
      element2 = soup.find_all("input",type="text")
      list_2 = []
      name = soup.input["name"]

      element3 = soup.find_all("input",type="email")
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []

      element5 = soup.find_all("input",type="radio")
      list_5 = []

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


#会社名・ふりがな
      try:
       Cell_1 = ws4.find("企業名")       
       Cell_list1 = [i for i in list_2 if Cell_1.value in i]
       for j in range(1,len(Cell_list1)+1):
         time.sleep(1)          
         ws4.update_cell(Cell_1.row, Cell_1.col+1, Cell_list1[j-1])
         print(ws4.cell(Cell_1.row, Cell_1.col+1).value)

#テキスト入力
       if "企業名" in Cell_1.value:
        driver.find_element_by_name(ws4.cell(Cell_1.row, Cell_1.col+1).value).send_keys(ws2.cell(2, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)      
        ws1.update_cell(k, lastcol+1, "会社名")

      except:
       pass
         
      try:
       Cell_2 = ws4.find("ふりがな（カナ）")
#       if len(Cell_2) > 0:
       Cell_list2 = [i for i in list_2 if Cell_2.value in i]
       for j in range(1,len(Cell_list2)+1):
         time.sleep(1)
         ws4.update_cell(Cell_2.row, Cell_2.col+1, Cell_list2[j-1])
         print(ws4.cell(Cell_2.row, Cell_2.col+1).value)

#テキスト入力         
       if "カナ" in Cell_2.value:
        driver.find_element_by_name(ws4.cell(Cell_2.row, Cell_2.col+1).value).send_keys(ws2.cell(3, 2).value)
        lastcol = len(list(ws1.row_values(k)))       
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "会社名カナ")
         
      except:
       pass

#     except gspread.exceptions.CellNotFound:
#      continue

#フルネーム（姓＋名）
      try:
       Cell_3 = ws4.find("担当者氏名")
       Cell_list3 = [i for i in list_2 if "姓" == i]
       print(Cell_list3)
       for j in range(1,len(Cell_list3)+1):
         lastcol = len(list(ws4.row_values(Cell_3.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_3.row, lastcol+Cell_3.col, Cell_list3[j-1])
         print(ws4.cell(Cell_3.row, lastcol+Cell_3.col).value)
         
       Cell_list3 = [i for i in list_2 if "名" == i]
       print(Cell_list3)
       for j in range(1,len(Cell_list3)+1):
         lastcol = len(list(ws4.row_values(Cell_3.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_3.row, lastcol+Cell_3.col, Cell_list3[j-1])
         print(ws4.cell(Cell_3.row, lastcol+Cell_3.col).value)

#テキスト入力
       if "姓" in ws4.cell(Cell_3.row, Cell_3.col+1).value:
        driver.find_element_by_name(ws4.cell(Cell_3.row, Cell_3.col+1).value).send_keys(ws2.cell(6, 3).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "姓")
        driver.find_element_by_name(ws4.cell(Cell_3.row, Cell_3.col+2).value).send_keys(ws2.cell(6, 4).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "名")
       
      except:
       pass

#フルネーム（氏名）
      try:
       import fullname   
       Cell_4 = fullname.Cell_4
       Cell_list4 = [i for i in list_2 if "your-name" in i \
                     or "名前" in i]
       for j in range(1,len(Cell_list4)+1):
         lastcol = len(list(ws4.row_values(Cell_4.row)))
         time.sleep(1)           
         ws4.update_cell(Cell_4.row, Cell_4.col+lastcol, Cell_list4[j-1])
         print(ws4.cell(Cell_4.row, Cell_4.col+lastcol).value)
           
#テキスト入力          
       driver.find_element_by_name(ws4.cell(Cell_4.row, Cell_4.col+1).value).send_keys(ws2.cell(6, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "氏名")
      except:
       pass


#フルネーム振り仮名（せい＋めい）
      try:
       Cell_5 = ws4.find("ふりがな（かな）")         
       Cell_list5 = [i for i in list_2 if "せい" == i]
       print(Cell_list5)
       for j in range(1,len(Cell_list5)+1):
         lastcol = len(list(ws4.row_values(Cell_5.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_5.row, lastcol+Cell_5.col, Cell_list5[j-1])
         print(ws4.cell(Cell_5.row, lastcol+Cell_5.col).value)
         
       Cell_list5 = [i for i in list_2 if "めい" == i]
       print(Cell_list5)
       for j in range(1,len(Cell_list5)+1):
         lastcol = len(list(ws4.row_values(Cell_5.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_5.row, lastcol+Cell_5.col, Cell_list5[j-1])
         print(ws4.cell(Cell_5.row, lastcol+Cell_5.col).value)         
   
#テキスト入力
       if "せい" in ws4.cell(Cell_5.row, Cell_5.col+1).value:
        driver.find_element_by_name(ws4.cell(Cell_5.row, Cell_5.col+1).value).send_keys(ws2.cell(7, 3).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "せい")
        driver.find_element_by_name(ws4.cell(Cell_5.row, Cell_5.col+2).value).send_keys(ws2.cell(7, 4).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "めい")
    
      except:
       pass

#フルネーム（セイメイ）
      try:
       import K_fullname   
       Cell_5 = K_fullname.Cell_5
       Cell_list5 = [i for i in list_2 if "your-kana" in i \
                     or "フリガナ" in i]
       for j in range(1,len(Cell_list5)+1):
         lastcol = len(list(ws4.row_values(Cell_5.row)))
         time.sleep(1)           
         ws4.update_cell(Cell_5.row, Cell_5.col+lastcol, Cell_list5[j-1])
         print(ws4.cell(Cell_5.row, Cell_5.col+lastcol).value)
           
#テキスト入力          
       driver.find_element_by_name(ws4.cell(Cell_5.row, Cell_5.col+1).value).send_keys(ws2.cell(8, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "氏名フリガナ")
      except:
       pass
   
    
#住所（郵便番号＋都道府県＋市町村＋建物名）
#      try:
#       Cell_6 = ws4.find("住所")
#       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
#                     and "都道府県" in i and "市町村" in i \
#                         and "アパート" in i]
#       for j in range(1,len(Cell_list6)+1):
#         lastcol = len(list(ws4.row_values(Cell_6.row)))
#         time.sleep(1)         
#         ws4.update_cell(Cell_6.row, lastcol+Cell_6.col, Cell_list6[j-1])
#         print(ws4.cell(Cell_6.row, lastcol+Cell_6.col).value)                  
#      except:
#        pass

      try:
       Cell_6 = ws4.find("住所")
       Cell_list6 = [i for i in list_2 if "郵便番号" in i]
       for j in range(1,len(Cell_list6)+1):
         lastcol = len(list(ws4.row_values(Cell_6.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_6.row, lastcol+Cell_6.col, Cell_list6[j-1])
         print(ws4.cell(Cell_6.row, lastcol+Cell_6.col).value)                  
#テキスト入力
       postcode = driver.find_element_by_name(ws4.cell(Cell_6.row, Cell_6.col+1).value)      
       if "郵便番号" in ws4.cell(Cell_6.row, Cell_6.col+1).value:
        postcode.send_keys(ws2.cell(4, 3).value + ws2.cell(4, 4).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "郵便番号")
      except:
        pass
         
      try:
       Cell_6 = ws4.find("住所")
       Cell_list6 = [i for i in list_2 if "都道府県" in i]
       for j in range(1,len(Cell_list6)+1):
         lastcol = len(list(ws4.row_values(Cell_6.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_6.row, lastcol+Cell_6.col, Cell_list6[j-1])
         print(ws4.cell(Cell_6.row, lastcol+Cell_6.col).value)                  
#テキスト入力       
       pref = driver.find_element_by_name(ws4.cell(Cell_6.row, Cell_6.col+2).value) 
       if "都道府県" in ws4.cell(Cell_6.row, Cell_6.col+2).value: 
        pref.clear()       
        pref.send_keys(ws2.cell(5, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "都道府県")
      except:
        pass

      try:
       Cell_6 = ws4.find("住所")
       Cell_list6 = [i for i in list_2 if "市町村" in i]
       for j in range(1,len(Cell_list6)+1):
         lastcol = len(list(ws4.row_values(Cell_6.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_6.row, lastcol+Cell_6.col, Cell_list6[j-1])
         print(ws4.cell(Cell_6.row, lastcol+Cell_6.col).value)                  
#テキスト入力       
       Municipal = driver.find_element_by_name(ws4.cell(Cell_6.row, Cell_6.col+3).value)       
       if "市町村" in ws4.cell(Cell_6.row, Cell_6.col+3).value:
        Municipal.clear()   
        Municipal.send_keys(ws2.cell(5, 3).value + ws2.cell(5, 4).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "市町村")
      except:
        pass

      try:
       Cell_6 = ws4.find("住所")
       Cell_list6 = [i for i in list_2 if "アパート" in i]
       for j in range(1,len(Cell_list6)+1):
         lastcol = len(list(ws4.row_values(Cell_6.row)))
         time.sleep(1)         
         ws4.update_cell(Cell_6.row, lastcol+Cell_6.col, Cell_list6[j-1])
         print(ws4.cell(Cell_6.row, lastcol+Cell_6.col).value)                  
#テキスト入力       
       build = driver.find_element_by_name(ws4.cell(Cell_6.row, Cell_6.col+4).value)       
       if "アパート" in ws4.cell(Cell_6.row, Cell_6.col+4).value: 
        build.send_keys(ws2.cell(5, 5).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)             
        ws1.update_cell(k, lastcol+1, "アパート")       
      except:
        pass


#メールアドレス
#「import email」はライブラリ参照のコマンドなので使用不可
      try:
       import email_addr
       Cell_8 = email_addr.Cell_8
       Cell_list8 = [i for i in list_3 if "mail" in i \
                     or "メール" in i]
       for j in range(1,len(Cell_list8)+1):
         lastcol = len(list(ws4.row_values(Cell_8.row)))
         time.sleep(1)           
         ws4.update_cell(Cell_8.row+j-1, Cell_8.col+1, Cell_list8[j-1])
         print(ws4.cell(Cell_8.row+j-1, Cell_8.col+1).value)
           
#テキスト入力
#       if "mail" in ws4.cell((Cell_8.row+1, Cell_8.col+1).value):
         driver.find_element_by_name(ws4.cell(Cell_8.row+j-1, Cell_8.col+1).value).send_keys(ws2.cell(17, 2).value)
         lastcol = len(list(ws1.row_values(k)))
         time.sleep(1)             
         ws1.update_cell(k, lastcol+1, "メールアドレス")
      except:
       pass
                           
    
#電話（ハイフンなし）
      try:
       import telephone   
       Cell_7 = telephone.Cell_7
       Cell_list7 = [i for i in list_4 if "tel" in i \
                     or "電話" in i]
       for j in range(1,len(Cell_list7)+1):
         lastcol = len(list(ws4.row_values(Cell_7.row)))
         time.sleep(1)           
         ws4.update_cell(Cell_7.row, Cell_7.col+lastcol, Cell_list7[j-1])
         print(ws4.cell(Cell_7.row, Cell_7.col+lastcol).value)
           
#テキスト入力          
       driver.find_element_by_name(ws4.cell(Cell_7.row, Cell_7.col+1).value).send_keys(ws2.cell(14, 2).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)             
       ws1.update_cell(k, lastcol+1, "電話（ハイフン）")
      except:
       pass
   
 
#textareaタグのname値を取得
      TEXTAREA_list = []
      element3 = soup.find_all("textarea")
      textarea = soup.textarea["name"]
      for textarea in element3:
       TEXTAREA_list.append(textarea.get("name"))   
       print(textarea.get("name"))

#件名
      try:
       Cell_9 = ws4.find("お問い合わせ件名")
       Cell_list9 = [i for i in TEXTAREA_list if Cell_9.value in i]
       for j in range(1,len(Cell_list9)+1):
         time.sleep(1)          
         ws4.update_cell(Cell_9.row, Cell_9.col+1, Cell_list9[j-1])
         print(ws4.cell(Cell_9.row, Cell_9.col+1).value)        
#テキスト入力
       if "題名" in Cell_9.value:
        driver.find_element_by_name(ws4.cell(Cell_9.row, Cell_9.col+1).value).send_keys(ws2.cell(1, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1)            
        ws1.update_cell(k, lastcol+1, "タイトル")
      except:
       pass

      
#詳細
      time.sleep(1)
      try:
       import textarea     
       Cell_10 = textarea.Cell_10
#       Cell_list10 = [i for i in TEXTAREA_list if Cell_10.value in i]
#       for j in range(1,len(Cell_list10)+1):
       time.sleep(1)          
       ws4.update_cell(Cell_10.row, Cell_10.col+1, TEXTAREA_list[0])
       print(ws4.cell(Cell_10.row, Cell_10.col+1).value)        
           
#テキスト入力          
       driver.find_element_by_name(ws4.cell(Cell_10.row, Cell_10.col+1).value).send_keys(ws3.cell(1, 1).value)
       lastcol = len(list(ws1.row_values(k)))
       time.sleep(1)            
       ws1.update_cell(k, lastcol+1, "本文")        
      except:
       pass

#プルダウンメニューの選択
       SELECT_list1 = []
#      element2 = soup.find("select")
#      for element5 in soup.find_all("select"):
#       print(element5.get("name"))
       for element in soup.find_all("option"): 
        SELECT_list1.append(element.get("value"))
        print(SELECT_list1)
        
      try:        
       Cell_11 = ws4.find("お問い合わせ事業")
       SELECT_list2 = [i for i in SELECT_list1 if "お問い合わせ" in i \
                      or "その他" in i] 
       for i in range(1, len(SELECT_list2)+1):
        time.sleep(1)          
        ws4.update_cell(Cell_11.row, Cell_11.col+1, SELECT_list2[i-1])
        dropdown = driver.find_element_by_name(ws4.cell(Cell_11.row, Cell_11.col).value)
#        dropdown.click()
        select = Select(dropdown)
        select.select_by_value(ws4.cell(Cell_11.row, Cell_11.col+1).value)
      except:
       pass
  
#ラジオボタン
       SELECT_list1 = []
#      element2 = soup.find("select")
#      for element5 in soup.find_all("select"):
#       print(element5.get("name"))
       for elem in element5: 
        SELECT_list1.append(elem.get("id"))
        print(SELECT_list1)
        
      try:
       Cell_12 = ws4.find("連絡方法")      
       SELECT_list2 = [i for i in SELECT_list1 if "mail" in i \
                      or "その他" in i] 
       for i in range(1, len(SELECT_list2)+1):
        time.sleep(1)
        ws4.update_cell(Cell_12.row, Cell_12.col+1, SELECT_list2[i-1])
        radio = driver.find_element_by_id(ws4.cell(Cell_12.row, Cell_12.col+1).value)
        driver.execute_script("arguments[0].click();", radio)
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
                                                                or "連絡方法" in list_.getText() \
                                                                    or "用件" in list_.getText() \
                                                                        or "ご相談"in list_.getText():
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

      element5 = soup.find_all("input",type="radio")
      list_5 = []


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
#      try:
      if not len([i for i in items_1 if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or "your-company" in i \
                         or "company-name" in i\
                             or "会社名" in i]
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
      if len([i for i in items_1 if "ふりがな（カナ）" in i]) > 1:
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
#      try:
      if not len([i for i in items_1 if "名前" in i \
               or "担当者" in i \
                   or "氏名" in i]) == 0:
        Cell_list3 = [i for i in list_2 if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "name" == i]
        print(Cell_list3)    
#テキスト入力            
        driver.find_element_by_name(Cell_list3[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(3)             
        ws1.update_cell(k, lastcol+1, "氏名")
#      except:
#       pass


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
      if len([i for i in items_1 if "住所" in i]) == 1:
#      try:
#       Cell_list6 = []    
       Cell_list6 = [i for i in list_2 if "郵便番号" in i \
                     or "your-post" in i \
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
         print(len(SELECT_list3))
         print(len(SELECT_list4))
         print(list_6[len(list_6)-1])
         print([len(list_6)-1])
#        for i in range(1, len(list_6)+1):
         checkbox = driver.find_element_by_css_selector("[value='その他']")
#         checkbox.click()
         driver.execute_script("arguments[0].click();", checkbox)
         print(checkbox.is_selected())         
         if checkbox.is_selected() is True:
           lastcol = len(list(ws1.row_values(k)))    
           time.sleep(1)             
           ws1.update_cell(k, lastcol+1, SELECT_list3[len(SELECT_list3)-1])
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


#ラジオボタン（連絡方法）
      try:
       import select_type
       Cell_11 = select_type.Cell_11
       SELECT_list1 = []
       SELECT_list2 = []
#      element2 = soup.find("select")
#      for element5 in soup.find_all("select"):
#       print(element5.get("name"))
       for elem in element5: 
        SELECT_list1.append(elem.get("id"))
        print(SELECT_list1)
      
       SELECT_list2 = [i for i in SELECT_list1 if "mail" in i \
                      or "その他" in i]
       print(SELECT_list2)
       
       for i in range(1, len(SELECT_list2)+1):
        time.sleep(1)
        ws4.update_cell(Cell_11.row, Cell_11.col+1, SELECT_list2[i-1])
        radio = driver.find_element_by_id(ws4.cell(Cell_11.row, Cell_11.col+1).value)
        driver.execute_script("arguments[0].click();", radio)
      except:
       pass


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
      
#inputタグの各要素を取得
      element2 = soup.find_all("input",type="text")
      print(element2)
      list_2 = []

      element3 = soup.find_all("input",type="email")
      print(element3)
      list_3 = []

      element4 = soup.find_all("input",type="tel")
      list_4 = []

      element5 = soup.find_all("input",type="radio")
      list_5 = []


#type属性：text
      for name in element2:
       list_2.append(name.get("name"))
       print(list_2)
      
      list_2d = []
      for name in element2:
        list_2d.append(name.get("data-name"))
        print(list_2d)
       
      for elem3 in element2:
#       items_1.append(name.get("placeholder"))
       items_2.append(elem3.get("id"))
       print(items_2)
       
#type属性：email
      for name in element3:
       list_3.append(name.get("name"))
       print(list_3)
      
      list_3d = []
      for name in element3:
        list_3d.append(name.get("data-name"))
        print(list_3d)
 
      for elem3 in element3:
#       items_1.append(name.get("placeholder"))
       items_3.append(elem3.get("id"))
       print(items_3)
       
#type属性：tel
      for name in element4:
       list_4.append(name.get("name"))
       print(list_4)

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

      
#会社名
#      try:
      if not len([i for i in str(soup.find_all("form")) if "御社名" in i \
               or "企業名" in i \
                   or "会社名" in i]) == 0:
        Cell_list1 = [i for i in list_2 if "facility" in i \
                     or "your-company" in i \
                         or "company-name" in i]
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
#      try:
#      if not len([i for i in items_1 if "名前" in i \
#               or "担当者" in i \
#                   or "氏名" in i]) == 0:
      if not len(list_2d) == 0:
       Cell_list3 = [i for i in list_2d if r"user_name" in i \
                     or r"your-name" in i \
                         or "名前" in i \
                             or "name" == i]
       print(Cell_list3)
       if len([i for i in Cell_list3 if "名前" in i]) > 0 \
          and len(items_2) > 0:
        driver.find_element_by_id(items_2[0]).send_keys(ws2.cell(6, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "氏名")
#      except:
#       pass


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
      if not len(list_2d) == 0:
       Cell_list7 = [i for i in list_2d if "tel" in i \
                     or "電話" in i \
                         or "your-phone" in i]
       print(Cell_list7)
       if len([i for i in Cell_list7 if "電話" in i]) > 0 \
          and len(items_2) > 0:
        driver.find_element_by_id(items_2[1]).send_keys(ws2.cell(14, 2).value)
        lastcol = len(list(ws1.row_values(k)))
        time.sleep(1) 
        ws1.update_cell(k, lastcol+1, "電話（ハイフンあり）")



#textareaタグのname値を取得
      TEXTAREA_list = []
      element3 = soup.find_all("textarea")
      print(element3)
       

      for textarea in element3:
        TEXTAREA_list.append(textarea.get("id"))
#       for elem3 in element3: 
#        items_1.append(name.get("placeholder"))
#        print(items_1)
        driver.find_element_by_id(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
        print(TEXTAREA_list[0])
        lastcol = len(list(ws1.row_values(k)))
        ws1.update_cell(k, lastcol+1, "本文")        

      if len(TEXTAREA_list) == 0:
       for textarea in element3:
        TEXTAREA_list.append(textarea.get("name"))   
        print(textarea.get("name"))
       
        driver.find_element_by_name(TEXTAREA_list[0]).send_keys(ws3.cell(1, 1).value)
        print(TEXTAREA_list[0])
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
      try:
       import select_type
       Cell_11 = select_type.Cell_11
       SELECT_list1 = []
       SELECT_list2 = []
#      element2 = soup.find("select")
#      for element5 in soup.find_all("select"):
#       print(element5.get("name"))
       for elem in element5: 
        SELECT_list1.append(elem.get("id"))
        print(SELECT_list1)
      
       SELECT_list2 = [i for i in SELECT_list1 if "mail" in i \
                      or "その他" in i]
       print(SELECT_list2)
       
       for i in range(1, len(SELECT_list2)+1):
        time.sleep(1)
        ws4.update_cell(Cell_11.row, Cell_11.col+1, SELECT_list2[i-1])
        radio = driver.find_element_by_id(ws4.cell(Cell_11.row, Cell_11.col+1).value)
        driver.execute_script("arguments[0].click();", radio)
      except:
       pass


    else:
     ws1.update_cell(k, 9, "フォーム要素取得不可")   
except:
 pass
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
