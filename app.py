# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import gspread
import requests
import json
import codecs

# from MyProject1MyDialog import MyProject1MyDialog
from MyProject1MyDialog10 import MyProject1MyDialog10
from MyProject1MyDialog11 import MyProject1MyDialog11
from MyProject1MyDialog3 import MyProject1MyDialog3
from MyProject1MyDialog4 import MyProject1MyDialog4
from MyProject1MyDialog5 import MyProject1MyDialog5
from MyProject1MyDialog7 import MyProject1MyDialog7
from MyProject1MyDialog8 import MyProject1MyDialog8
from MyProject1MyDialog9 import MyProject1MyDialog9
# from MyProject1MyFrame6 import MyProject1MyFrame6

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
       wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"お問い合わせフォーム投稿アプリ", pos = wx.DefaultPosition, size = wx.Size( 400,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

       self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

#Setting up the menu on menubar.
       self.m_menubar1 = wx.MenuBar( 0 )
       self.m_menu1 = wx.Menu()

#メニュー追加の場合は以下のコメントアウト解除
#       self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
#       self.m_menu1.Append( self.m_menuItem1 )

       self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu1.Append( self.m_menuItem2 )

       self.m_menubar1.Append( self.m_menu1, u"File" )

       self.m_menu2 = wx.Menu()
       self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Configuration", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu2.Append( self.m_menuItem3 )

       self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Profile", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu2.Append( self.m_menuItem4 )

       self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Send text creation", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu2.Append( self.m_menuItem5 )

       self.m_menubar1.Append( self.m_menu2, u"Setting" )

#メニューバー追加によりコーディング変更（2022.12.25）
       self.m_menu3 = wx.Menu()
       # self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Create", wx.EmptyString, wx.ITEM_NORMAL )
       # self.m_menu3.Append( self.m_menuItem6 )

       self.m_menu11 = wx.Menu()
       self.m_menuItem7 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"URL extraction", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu11.Append( self.m_menuItem7 )

       self.m_menuItem8 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Posting and sending", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu11.Append( self.m_menuItem8 )

       self.m_menu3.AppendSubMenu( self.m_menu11, u"Inquiry" )

       self.m_menu12 = wx.Menu()
       self.m_menuItem9 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"Target info", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu12.Append( self.m_menuItem9 )

       self.m_menuItem13 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"Report", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menuItem13.Enable(False)
       self.m_menu12.Append( self.m_menuItem13 )

       self.m_menu3.AppendSubMenu( self.m_menu12, u"Preview" )

#ここまでが変更分

       self.m_menubar1.Append( self.m_menu3, u"List" )

       self.m_menu4 = wx.Menu()
       self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
       self.m_menu4.Append( self.m_menuItem10 )

#       self.m_menuItem11 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"For administrators", wx.EmptyString, wx.ITEM_NORMAL )
#       self.m_menu4.Append( self.m_menuItem11 )

       self.m_menubar1.Append( self.m_menu4, u"Help" )
       self.SetMenuBar( self.m_menubar1 )


#Connect Events
       self.Bind( wx.EVT_MENU, self.quit_button, self.m_menuItem2 )
       self.Bind( wx.EVT_MENU, self.Configuration, self.m_menuItem3 )
       self.Bind( wx.EVT_MENU, self.Profile, self.m_menuItem4 )
       self.Bind( wx.EVT_MENU, self.Send_email_body, self.m_menuItem5 )
       # self.Bind( wx.EVT_MENU, self.create_button, self.m_menuItem6 )
       self.Bind( wx.EVT_MENU, self.inquiry_url, self.m_menuItem7 )
       self.Bind( wx.EVT_MENU, self.inquiry_button, self.m_menuItem8 )
       self.Bind( wx.EVT_MENU, self.list_view, self.m_menuItem9 )
       self.Bind( wx.EVT_MENU, self.report, self.m_menuItem13 )
       self.Bind( wx.EVT_MENU, self.Creator_info, self.m_menuItem10 )
#       self.Bind( wx.EVT_MENU, self.Status_info, self.m_menuItem11 )
       self.Bind(wx.EVT_CLOSE, self.quit_button) 


    def listbox_select(self, event):
       import filter
       adid3 = MyProject1MyDialog3(self)
       adid8 = MyProject1MyDialog8(self)
       listbox_1 = event.GetEventObject()
       n = listbox_1.GetSelections()
       print(n)
       try:
              if n == []:
                     self.m_listBox2.Clear()
                     self.m_listBox3.Clear()
                     self.m_listBox4.Clear()
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [0]:
                     self.m_listBox2.SetItems(filter.bussiness_ban)
                     self.m_listBox3.Clear()
                     self.m_listBox4.Clear()
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [1]:
                     self.m_listBox3.SetItems(filter.dedicated_form)
                     self.m_listBox2.Clear()
                     self.m_listBox4.Clear()
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [2]:
                     self.m_listBox4.SetItems(filter.other)
                     self.m_listBox2.Clear()
                     self.m_listBox3.Clear()
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [0, 1]:
                     self.m_listBox2.SetItems(
                            filter.bussiness_ban
                            )
                     self.m_listBox3.SetItems(
                            filter.dedicated_form
                            )
                     self.m_listBox4.Clear()
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [0, 1, 2]:
                     self.m_listBox2.SetItems(
                            filter.bussiness_ban
                            )
                     self.m_listBox3.SetItems(
                            filter.dedicated_form
                            )
                     self.m_listBox4.SetItems(
                            filter.other
                            )
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [1, 2]:
                     self.m_listBox2.Clear()
                     self.m_listBox3.SetItems(
                            filter.dedicated_form
                            )
                     self.m_listBox4.SetItems(
                            filter.other
                            )
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')
              elif n == [0, 2]:
                     self.m_listBox2.SetItems(
                            filter.bussiness_ban
                            )
                     self.m_listBox3.Clear()
                     self.m_listBox4.SetItems(
                            filter.other
                            )
                     with open('setting.json','w',encoding='utf-8') as f:
                            w_data = {}
                            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                            w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                            w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                            w_data['user'] = adid3.m_textCtrl4.GetValue()
                            w_data['password'] = adid3.m_textCtrl5.GetValue()
                            w_data['remember'] = adid3.m_checkBox1.GetValue()
                            w_data['date'] = adid8.m_textCtrl52.GetValue()
                            w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                           w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                           w_data['sheetname2'] = self.m_comboBox1.GetValue()
                            w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                           w_data['row1'] = self.row1.GetValue()
#                           w_data['row2'] = self.row2.GetValue()
                            w_data['row11'] = self.row11.GetValue()
                            w_data['row21'] = self.row21.GetValue()
                            w_data['key1'] = self.m_listBox2.GetCount()
                            w_data['key2'] = self.m_listBox3.GetCount()
                            w_data['key3'] = self.m_listBox4.GetCount()

                            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                            print('WRITE:')

       except Exception as e:
              print(e)
              wx.MessageBox(f'{e}', u'error', wx.ICON_ERROR)

    def inquiry_url( self, event ):
       adid = MyProject1MyDialog3(self)
       if adid.m_comboBox6.GetValue() == '' \
               or not 'json' in adid.m_textCtrl11.GetValue():
#                   or not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
             wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
#          elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
#             wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)          
       else:
           
#例外処理開始
            try:
              adid = MyProject1MyDialog10(self)
              adid.ShowModal()
              adid.Destroy()
           
#エラーメッセージ表示
            except gspread.exceptions.APIError as e:
              print("error:", e)
              wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)


    def inquiry_button(self, event):
       import filter
       adid = MyProject1MyDialog3(self)
        
       if adid.m_comboBox6.GetValue() == '' \
           or not 'json' in adid.m_textCtrl11.GetValue():
#             adid.m_comboBox6.SetBackgroundColour('#f56cbe')
#             adid.m_textCtrl11.SetBackgroundColour('#f56cbe')
#             self.m_textCtrl111.SetForegroundColour('#f56cbe')
             wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
#          elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
#             adid.m_textCtrl111.SetForegroundColour('#f56cbe')
#             wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)
       elif not adid.m_comboBox6.GetValue() == '' \
           and 'json' in adid.m_textCtrl11.GetValue():
#               and 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
#             adid.m_comboBox6.SetBackgroundColour('#FFFFFF')
#             adid.m_textCtrl11.SetBackgroundColour('#FFFFFF')
#             adid.m_textCtrl111.SetBackgroundColour('#FFFFFF')

#例外処理開始
             try:
              
#秘密鍵（JSONファイル）のファイル名を入力
               credentials = ServiceAccountCredentials.from_json_keyfile_name(adid.m_textCtrl11.GetValue(), scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
               gc = gspread.authorize(credentials)

#存在するワークシートの情報を全て取得
               wb = gc.open_by_key(adid.m_comboBox6.GetValue())
               worksheets = wb.worksheets()

# メニューバー「Report」を有効化
               self.m_menuItem13.Enable(True)

#メインフレーム作成
               mainSizer = wx.BoxSizer( wx.VERTICAL )

               self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
               mainBox = wx.BoxSizer( wx.VERTICAL )

#ここからコーディング変更（2022.8.23）
               bSizer15 = wx.BoxSizer( wx.VERTICAL )

               self.m_panel28 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
               self.m_panel28.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )

               sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel28, wx.ID_ANY, u"Automatic form submission" ), wx.VERTICAL )

               self.m_panel51 = wx.Panel( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
               bSizer17 = wx.BoxSizer( wx.VERTICAL )

#               gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

#以下、機能追加のためコーディング変更（2022.01.10）
               self.m_panel88 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
               self.m_panel88.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
               sbSizer78 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel88, wx.ID_ANY, u"Setting" ), wx.VERTICAL )

               gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

               bSizer25 = wx.BoxSizer( wx.VERTICAL )

               self.m_staticText51 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText51.Wrap( -1 )

               self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer25.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               self.row11 = wx.SpinCtrl( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 10000, 0 )
               self.row11.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
               self.row11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
               self.row11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

               bSizer25.Add( self.row11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


               gSizer61.Add( bSizer25, 1, wx.EXPAND, 5 )

               bSizer26 = wx.BoxSizer( wx.VERTICAL )
          
               self.m_staticText62 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"last", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText62.Wrap( -1 )

               self.m_staticText62.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer26.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               self.row21 = wx.SpinCtrl( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 10000, 0 )
               self.row21.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
               self.row21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
               self.row21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

               bSizer26.Add( self.row21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               gSizer61.Add( bSizer26, 1, wx.EXPAND, 5 )

               sbSizer78.Add( gSizer61, 1, wx.EXPAND, 5 )

               bSizer27 = wx.BoxSizer( wx.VERTICAL )

               self.m_staticText611 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"sheet title", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText611.Wrap( -1 )

               self.m_staticText611.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer27.Add( self.m_staticText611, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               m_comboBox11Choices = [worksheet.title for worksheet in worksheets]
#             print(m_comboBox1Choices)
               self.m_comboBox11 = wx.ComboBox( sbSizer78.GetStaticBox(), wx.ID_ANY, u"選択して下さい", wx.DefaultPosition, wx.Size( 300,-1 ), m_comboBox11Choices, wx.CB_DROPDOWN )
               self.m_comboBox11.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
               self.m_comboBox11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
               self.m_comboBox11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

               bSizer27.Add( self.m_comboBox11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
               sbSizer78.Add( bSizer27, 1, wx.EXPAND, 5 )
              #  gSizer40 = wx.GridSizer( 0, 2, 0, 0 )

# ＮＧフィルター追加（2022.12.22）
               bSizer34 = wx.BoxSizer( wx.VERTICAL )

               self.m_staticText612 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"NG filter", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText612.Wrap( -1 )

               self.m_staticText612.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer34.Add( self.m_staticText612, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               m_listBox1Choices = filter.send_exclusion
               self.m_listBox1 = wx.ListBox( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL )
               bSizer34.Add( self.m_listBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               sbSizer78.Add( bSizer34, 1, wx.EXPAND, 5 )

               bSizer35 = wx.BoxSizer( wx.VERTICAL )

               gSizer45 = wx.GridSizer( 0, 2, 0, 0 )

               gSizer41 = wx.GridSizer( 0, 2, 0, 0 )

               bSizer37 = wx.BoxSizer( wx.VERTICAL )

               self.m_staticText613 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"key 1", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText613.Wrap( -1 )

               self.m_staticText613.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer37.Add( self.m_staticText613, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               m_listBox2Choices = []
               self.m_listBox2 = wx.ListBox( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL )
               bSizer37.Add( self.m_listBox2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               gSizer41.Add( bSizer37, 1, wx.EXPAND, 5 )

               bSizer36 = wx.BoxSizer( wx.VERTICAL )

               self.m_staticText614 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"key 2", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText614.Wrap( -1 )

               self.m_staticText614.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer36.Add( self.m_staticText614, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               m_listBox3Choices = []
               self.m_listBox3 = wx.ListBox( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL )
               bSizer36.Add( self.m_listBox3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


               gSizer41.Add( bSizer36, 1, wx.EXPAND, 5 )


               gSizer45.Add( gSizer41, 1, wx.EXPAND, 5 )

               gSizer40 = wx.GridSizer( 0, 2, 0, 0 )

               bSizer341 = wx.BoxSizer( wx.VERTICAL )

               self.m_staticText615 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"key 3", wx.DefaultPosition, wx.DefaultSize, 0 )
               self.m_staticText615.Wrap( -1 )

               self.m_staticText615.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

               bSizer341.Add( self.m_staticText615, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

               m_listBox4Choices = []
               self.m_listBox4 = wx.ListBox( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL )
               bSizer341.Add( self.m_listBox4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


               gSizer40.Add( bSizer341, 1, wx.EXPAND, 5 )


               gSizer45.Add( gSizer40, 1, wx.EXPAND, 5 )


               bSizer35.Add( gSizer45, 1, wx.EXPAND, 5 )

# 以下は入れなくて不要
               # sbSizer78.Add( gSizer61, 1, wx.EXPAND, 5 )

# 追加分こここまで

               self.btn4 = wx.Button( sbSizer78.GetStaticBox(), wx.ID_ANY, u"Posting", wx.DefaultPosition, wx.DefaultSize, 0 )

               self.btn4.SetDefault()
               self.btn4.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )

               bSizer35.Add( self.btn4, 0, wx.ALL, 5 )


               sbSizer78.Add( bSizer35, 1, wx.EXPAND, 5 )

               self.m_panel88.SetSizer( sbSizer78 )
               self.m_panel88.Layout()
               sbSizer78.Fit( self.m_panel88 )
               bSizer17.Add( self.m_panel88, 1, wx.EXPAND |wx.ALL, 5 )

              #  self.m_panel89 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
              #  sbSizer76 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel89, wx.ID_ANY, u"Graph drawing" ), wx.VERTICAL )

              #  self.m_panel90 = wx.Panel( sbSizer76.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
              #  bSizer20 = wx.BoxSizer( wx.VERTICAL )

              #  self.m_radioBtn1 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Number of executions", wx.DefaultPosition, wx.DefaultSize, 0 )
              #  self.m_radioBtn1.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

              #  bSizer20.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

              #  self.m_radioBtn2 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Number of send completely", wx.DefaultPosition, wx.DefaultSize, 0 )
              #  self.m_radioBtn2.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

              #  bSizer20.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

              #  self.m_radioBtn3 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Breakdown of errors", wx.DefaultPosition, wx.DefaultSize, 0 )
              #  self.m_radioBtn3.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

              #  bSizer20.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

              #  self.m_panel90.SetSizer( bSizer20 )
              #  self.m_panel90.Layout()
              #  bSizer20.Fit( self.m_panel90 )
              #  sbSizer76.Add( self.m_panel90, 1, wx.EXPAND |wx.ALL, 5 )

              #  self.btn5 = wx.Button( sbSizer76.GetStaticBox(), wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
              #  self.btn5.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )

              #  sbSizer76.Add( self.btn5, 0, wx.ALL, 5 )


              #  self.m_panel89.SetSizer( sbSizer76 )
              #  self.m_panel89.Layout()
              #  sbSizer76.Fit( self.m_panel89 )
              #  bSizer17.Add( self.m_panel89, 1, wx.EXPAND |wx.ALL, 5 )


               self.m_panel51.SetSizer( bSizer17 )
               self.m_panel51.Layout()
               bSizer17.Fit( self.m_panel51 )
               sbSizer21.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )


               self.m_panel28.SetSizer( sbSizer21 )
               self.m_panel28.Layout()
               sbSizer21.Fit( self.m_panel28 )
               bSizer15.Add( self.m_panel28, 1, wx.EXPAND |wx.ALL, 5 )


               mainBox.Add( bSizer15, 1, wx.EXPAND, 5 )

#変更分ここまで
               self.main_panel.SetSizer( mainBox )
               self.main_panel.Layout()
               mainBox.Fit( self.main_panel )        
               mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )

               self.SetSizer( mainSizer )
               self.Layout()

               self.Centre( wx.BOTH )


# Connect Events
               self.btn4.Bind( wx.EVT_BUTTON, self.inquiry_post )
              #  self.btn5.Bind( wx.EVT_BUTTON, self.graph_start )
               self.m_listBox1.Bind(wx.EVT_LISTBOX, self.listbox_select)


#2021.12.06機能追加（'setting.json'へ設定値の書き込み）
               self.Bind( wx.EVT_BUTTON, self.quit_button )


#設定情報（json）読み込み
#文字コードをUTF-8に変換しないとエラーが発生するため注意！！
               with codecs.open('setting.json','r',encoding='utf-8') as f:
#「JSONDecodeError: Invalid control character at」が返さないようにする。
#strictがfalse（デフォルトはTrue）の場合、制御文字を文字列に含めることができます。
#ここで言う制御文字とは、'\t'（タブ）、'\n'、'\r'、'\0'を含む0-31の範囲のコードを持つ文字のことです。
                 j = json.load(f,strict=False)
#              print(j)
                 f.close()
#                 self.m_comboBox12.SetValue(j['sheetname1'])
#                 self.m_comboBox1.SetValue(j['sheetname2'])
                 self.m_comboBox11.SetValue(j['sheetname3'])
#                 self.row1.SetValue(j['row1'])
#                 self.row2.SetValue(j['row2'])
                 self.row11.SetValue(j['row11'])
                 self.row21.SetValue(j['row21'])

#エラーメッセージ表示
             except FileNotFoundError as e:
               print("error:", e)
               wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)

#エラーメッセージ表示
             except requests.exceptions.ConnectionError as e:
               print("error:", e)
               wx.MessageBox(f'{e}', u'Server error', wx.ICON_ERROR)

#エラーメッセージ表示
             except gspread.exceptions.APIError as e:
               print("error:", e)
               wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)


    def list_view( self, event ):
          adid = MyProject1MyDialog3(self)
          if adid.m_comboBox6.GetValue() == '' \
               or not 'json' in adid.m_textCtrl11.GetValue():
#                   or not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
             wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
#          elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
#             wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)          
          else:
           
#例外処理開始
            try:
#MyFrame2のテキストボックス及びコンボボックスの値をMyDialogに受け渡し
              adid = MyProject1MyDialog9(self)
              adid.ShowModal()
              adid.Destroy()
           
#エラーメッセージ表示
            except gspread.exceptions.APIError as e:
              print("error:", e)
              wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)


#各メニュー項目選択後の画面遷移
    def Configuration(self, event):
           adid = MyProject1MyDialog3(self)
           adid.ShowModal()
           adid.Destroy()

    def Profile(self, event):
           adid = MyProject1MyDialog4(self)
           adid.ShowModal()
           adid.Destroy()

    def Send_email_body(self, event):
           adid = MyProject1MyDialog5(self)
           adid.ShowModal()
           adid.Destroy()

    def Creator_info(self, event):
           adid = MyProject1MyDialog7(self)
           adid.ShowModal()
           adid.Destroy()

    def Status_info(self, event):
           adid = MyProject1MyDialog8(self)
           adid.ShowModal()
           adid.Destroy()

       # Handlers for MyFrame2 events.
    def create_button( self, event ):
          adid = MyProject1MyDialog3(self)
          if adid.m_comboBox6.GetValue() == '' \
               or not 'json' in adid.m_textCtrl11.GetValue():
#                   or not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
             wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
#          elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
#             wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)          
          else:
           
#例外処理開始
            try:
#MyFrame2のテキストボックス及びコンボボックスの値をMyDialogに受け渡し
              adid = MyProject1MyDialog(self)
              adid.ShowModal()
              adid.Destroy()
           
#エラーメッセージ表示
            except gspread.exceptions.APIError as e:
              print("error:", e)
              wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)


    def report(self, event):
          adid3 = MyProject1MyDialog3(self)
          adid8 = MyProject1MyDialog8(self)
          if adid3.m_comboBox6.GetValue() == '' \
               or not 'json' in adid3.m_textCtrl11.GetValue():
#                   or not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
             wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
#          elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
#             wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)          

# JSONファイルの更新を行ってからダイアログを表示
          else:
            try:
              with open('setting.json','w',encoding='utf-8') as f:
                   w_data = {}
                   w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
                   w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
                   w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
                   w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
                   w_data['user'] = adid3.m_textCtrl4.GetValue()
                   w_data['password'] = adid3.m_textCtrl5.GetValue()
                   w_data['remember'] = adid3.m_checkBox1.GetValue()
                   w_data['date'] = adid8.m_textCtrl52.GetValue()
                   w_data['posts'] = adid8.m_textCtrl53.GetValue()
#                   w_data['sheetname1'] = self.m_comboBox12.GetValue()
#                   w_data['sheetname2'] = self.m_comboBox1.GetValue()
                   w_data['sheetname3'] = self.m_comboBox11.GetValue()
#                   w_data['row1'] = self.row1.GetValue()
#                   w_data['row2'] = self.row2.GetValue()
                   w_data['row11'] = self.row11.GetValue()
                   w_data['row21'] = self.row21.GetValue()
                   w_data['key1'] = self.m_listBox2.GetCount()
                   w_data['key2'] = self.m_listBox3.GetCount()
                   w_data['key3'] = self.m_listBox4.GetCount()

                   json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
                   print('WRITE:')

              adid = MyProject1MyDialog11(self)
              adid.ShowModal()
              adid.Destroy()
           
            except Exception as e:
              print(e)
              wx.MessageBox(f'{e}', u'error', wx.ICON_ERROR)


#設定情報（json）書き出し
#     def quit_button(self, event):
#        adid3 = MyProject1MyDialog3(self)
#        adid8 = MyProject1MyDialog8(self)

#        try:

# #文字コードをUTF-8に変換しないとエラー発生がするため注意！！
#               with open('setting.json','w',encoding='utf-8') as f:
#                    w_data = {}
#                    w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
#                    w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
#                    w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
#                    w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
#                    w_data['user'] = adid3.m_textCtrl4.GetValue()
#                    w_data['password'] = adid3.m_textCtrl5.GetValue()
#                    w_data['remember'] = adid3.m_checkBox1.GetValue()
#                    w_data['date'] = adid8.m_textCtrl52.GetValue()
#                    w_data['posts'] = adid8.m_textCtrl53.GetValue()
# #                   w_data['sheetname1'] = self.m_comboBox12.GetValue()
# #                   w_data['sheetname2'] = self.m_comboBox1.GetValue()
#                    w_data['sheetname3'] = self.m_comboBox11.GetValue()
# #                   w_data['row1'] = self.row1.GetValue()
# #                   w_data['row2'] = self.row2.GetValue()
#                    w_data['row11'] = self.row11.GetValue()
#                    w_data['row21'] = self.row21.GetValue()                
                
#                    json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
#                    print('WRITE:')
# #                print(w_data)
#                    self.Destroy()
#                    wx.Exit()
#                    return


       # except Exception as e:
       #        print(e)
       #        wx.MessageBox(f'{e}', u'error', wx.ICON_ERROR)

    def quit_button( self, event ):
#       # TODO: Implement quit_button
         self.Destroy()
         wx.Exit()
         return

    def __del__( self ):
         pass