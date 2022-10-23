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

from MyProject1MyDialog import MyProject1MyDialog
from MyProject1MyDialog3 import MyProject1MyDialog3
from MyProject1MyDialog4 import MyProject1MyDialog4
from MyProject1MyDialog5 import MyProject1MyDialog5
from MyProject1MyDialog7 import MyProject1MyDialog7
from MyProject1MyDialog8 import MyProject1MyDialog8
from MyProject1MyFrame6 import MyProject1MyFrame6

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"お問い合わせフォーム投稿アプリ", pos = wx.DefaultPosition, size = wx.Size( 600,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

#Setting up the menu on menubar.
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()

#メニュー追加の場合は以下のコメントアウト解除
#		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
#		self.m_menu1.Append( self.m_menuItem1 )

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

		self.m_menu3 = wx.Menu()
#		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Create", wx.EmptyString, wx.ITEM_NORMAL )
#		self.m_menu3.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Inquiry", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem7 )

		self.m_menubar1.Append( self.m_menu3, u"List" )

		self.m_menu4 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem8 )

#		self.m_menuItem9 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"For administrators", wx.EmptyString, wx.ITEM_NORMAL )
#		self.m_menu4.Append( self.m_menuItem9 )

		self.m_menubar1.Append( self.m_menu4, u"Help" )
		self.SetMenuBar( self.m_menubar1 )


#Connect Events
		self.Bind( wx.EVT_MENU, self.quit_button, self.m_menuItem2 )
		self.Bind( wx.EVT_MENU, self.Configuration, self.m_menuItem3 )
		self.Bind( wx.EVT_MENU, self.Profile, self.m_menuItem4 )
		self.Bind( wx.EVT_MENU, self.Send_email_body, self.m_menuItem5 )
#		self.Bind( wx.EVT_MENU, self.create_button, self.m_menuItem6 )
		self.Bind( wx.EVT_MENU, self.inquiry_button, self.m_menuItem7 )
		self.Bind( wx.EVT_MENU, self.Creator_info, self.m_menuItem8 )
#		self.Bind( wx.EVT_MENU, self.Status_info, self.m_menuItem9 )
		self.Bind(wx.EVT_CLOSE, self.quit_button) 


	def inquiry_button(self, event):
	   adid = MyProject1MyDialog3(self)
        
	   if adid.m_comboBox6.GetValue() == '' \
           or not 'json' in adid.m_textCtrl11.GetValue():
	      adid.m_comboBox6.SetBackgroundColour('#f56cbe')
	      adid.m_textCtrl11.SetBackgroundColour('#f56cbe')
#	      self.m_textCtrl111.SetForegroundColour('#f56cbe')
	      wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
	   elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
	      adid.m_textCtrl111.SetForegroundColour('#f56cbe')
	      wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)
	   elif not adid.m_comboBox6.GetValue() == '' \
           and 'json' in adid.m_textCtrl11.GetValue() \
               and 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
	      adid.m_comboBox6.SetBackgroundColour('#FFFFFF')
	      adid.m_textCtrl11.SetBackgroundColour('#FFFFFF')
	      adid.m_textCtrl111.SetBackgroundColour('#FFFFFF')

#例外処理開始
	      try:
              
#秘密鍵（JSONファイル）のファイル名を入力
	        credentials = ServiceAccountCredentials.from_json_keyfile_name(adid.m_textCtrl11.GetValue(), scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
	        gc = gspread.authorize(credentials)

#存在するワークシートの情報を全て取得
	        wb = gc.open_by_key(adid.m_comboBox6.GetValue())
	        worksheets = wb.worksheets()

#メインフレーム作成
	        mainSizer = wx.BoxSizer( wx.VERTICAL )

	        self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        mainBox = wx.BoxSizer( wx.VERTICAL )

	        bSizer19 = wx.BoxSizer( wx.VERTICAL )

	        self.m_panel6 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        self.m_panel6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"Processing related to inquiry form" ), wx.VERTICAL )

	        bSizer15 = wx.BoxSizer( wx.VERTICAL )

#機能追加のため此処からコーディング変更（2022.01.12）
	        gSizer43 = wx.GridSizer( 0, 2, 0, 0 )

#2021.12.06機能追加（お問い合わせフォーム投稿前に営業リストをプレビュー表示）

	        self.m_panel85 = wx.Panel( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        sbSizer75 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel85, wx.ID_ANY, u"The created sales list" ), wx.VERTICAL )

#2022.01.08機能追加（リストプレビュー時の必要項目選択）
	        self.m_panel87 = wx.Panel( sbSizer75.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        gSizer41 = wx.GridSizer( 0, 2, 0, 0 )

	        self.m_checkBox1 = wx.CheckBox( self.m_panel87, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0 )
	        gSizer41.Add( self.m_checkBox1, 0, wx.ALL, 5 )

	        self.m_checkBox2 = wx.CheckBox( self.m_panel87, wx.ID_ANY, u"Tel number", wx.DefaultPosition, wx.DefaultSize, 0 )
	        gSizer41.Add( self.m_checkBox2, 0, wx.ALL, 5 )

	        self.m_checkBox3 = wx.CheckBox( self.m_panel87, wx.ID_ANY, u"Corporate site", wx.DefaultPosition, wx.DefaultSize, 0 )
	        gSizer41.Add( self.m_checkBox3, 0, wx.ALL, 5 )

	        self.m_checkBox4 = wx.CheckBox( self.m_panel87, wx.ID_ANY, u"Inquiry url", wx.DefaultPosition, wx.DefaultSize, 0 )
	        gSizer41.Add( self.m_checkBox4, 0, wx.ALL, 5 )

	        self.m_checkBox5 = wx.CheckBox( self.m_panel87, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
	        gSizer41.Add( self.m_checkBox5, 0, wx.ALL, 5 )
	        self.m_checkBox5.SetValue(True)

	        self.m_checkBox6 = wx.CheckBox( self.m_panel87, wx.ID_ANY, u"Date and time", wx.DefaultPosition, wx.DefaultSize, 0 )
	        gSizer41.Add( self.m_checkBox6, 0, wx.ALL, 5 )
	        self.m_checkBox6.SetValue(True)

	        self.m_panel87.SetSizer( gSizer41 )
	        self.m_panel87.Layout()
	        gSizer41.Fit( self.m_panel87 )
	        sbSizer75.Add( self.m_panel87, 1, wx.EXPAND |wx.ALL, 5 )

	        self.m_panel86 = wx.Panel( sbSizer75.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

#ここまで機能追加のコーディング

	        gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

	        self.m_staticText612 = wx.StaticText( self.m_panel86, wx.ID_ANY, u"sheet title", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText612.Wrap( -1 )


	        gSizer8.Add( self.m_staticText612, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

#現在のワークシートのタイトルをリストへ格納
	        m_comboBox12Choices = [worksheet.title for worksheet in worksheets]
	        self.m_comboBox12 = wx.ComboBox( self.m_panel86, wx.ID_ANY, u"選択して下さい", wx.DefaultPosition, wx.DefaultSize, m_comboBox12Choices, wx.CB_DROPDOWN )
	        gSizer8.Add( self.m_comboBox12, 0, wx.ALL, 5 )

	        self.btn32 = wx.Button( self.m_panel86, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.btn32.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        gSizer8.Add( self.btn32, 0, wx.ALL, 5 )

	        self.m_panel86.SetSizer( gSizer8 )
	        self.m_panel86.Layout()
	        gSizer8.Fit( self.m_panel86 )
	        sbSizer75.Add( self.m_panel86, 1, wx.EXPAND |wx.ALL, 5 )

	        self.m_panel85.SetSizer( sbSizer75 )
	        self.m_panel85.Layout()
	        sbSizer75.Fit( self.m_panel85 )
	        gSizer43.Add( self.m_panel85, 1, wx.EXPAND |wx.ALL, 5 )

	        self.m_panel27 = wx.Panel( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        self.m_panel27.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel27, wx.ID_ANY, u"Extraction of inquiry page" ), wx.VERTICAL )

	        self.m_panel5 = wx.Panel( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        bSizer16 = wx.BoxSizer( wx.VERTICAL )

	        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

	        self.m_staticText5 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText5.Wrap( -1 )

	        self.m_staticText5.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        gSizer5.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

	        self.row1 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
	        gSizer5.Add( self.row1, 0, wx.ALL, 5 )
#	      self.row1.Disable()

	        self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"last", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText6.Wrap( -1 )

	        gSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

	        self.row2 = wx.SpinCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 10000, 0 )
	        gSizer5.Add( self.row2, 0, wx.ALL, 5 )
#	      self.row2.Disable()

	        self.m_staticText61 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"sheet title", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText61.Wrap( -1 )

	        gSizer5.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

#現在のワークシートのタイトルをリストへ格納
	        m_comboBox1Choices = [worksheet.title for worksheet in worksheets]
#	      print(m_comboBox1Choices)
	        self.m_comboBox1 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"選択して下さい", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, wx.CB_DROPDOWN )
	        gSizer5.Add( self.m_comboBox1, 0, wx.ALL, 5 )

#（お問い合わせページの抽出：機能未完成によりドロップボックスを無効）
#	      self.m_comboBox1.Enable(False)
	        self.m_comboBox1.Enable(True)

	        self.btn3 = wx.Button( self.m_panel5, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.btn3.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
#	      self.btn3.Disable()
          
	        gSizer5.Add( self.btn3, 0, wx.ALL, 5 )

	        gSizer62 = wx.GridSizer( 0, 2, 0, 0 )


	        gSizer5.Add( gSizer62, 1, wx.EXPAND, 5 )


	        bSizer16.Add( gSizer5, 1, wx.EXPAND, 5 )


	        self.m_panel5.SetSizer( bSizer16 )
	        self.m_panel5.Layout()
	        bSizer16.Fit( self.m_panel5 )
	        sbSizer20.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


	        self.m_panel27.SetSizer( sbSizer20 )
	        self.m_panel27.Layout()
	        sbSizer20.Fit( self.m_panel27 )
	        gSizer43.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )


	        bSizer15.Add( gSizer43, 1, wx.EXPAND, 5 )

	        self.m_panel28 = wx.Panel( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        self.m_panel28.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel28, wx.ID_ANY, u"Automatic form posting" ), wx.VERTICAL )

	        self.m_panel51 = wx.Panel( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        bSizer17 = wx.BoxSizer( wx.VERTICAL )

	        gSizer6 = wx.GridSizer( 0, 2, 0, 0 )


#以下、機能追加のためコーディング変更（2022.01.10）
	        self.m_panel88 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        self.m_panel88.SetBackgroundColour( wx.Colour( 183, 255, 111 ) )
	        sbSizer78 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel88, wx.ID_ANY, u"Setting" ), wx.VERTICAL )

	        gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

	        self.m_staticText51 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText51.Wrap( -1 )
	        self.m_staticText51.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        gSizer61.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

	        self.row11 = wx.SpinCtrl( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 1000, 0 )
	        self.row11.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
	        self.row11.SetForegroundColour( wx.Colour( 0, 128, 0 ) )
	        self.row11.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )

	        gSizer61.Add( self.row11, 0, wx.ALL, 5 )
#	      self.row11.Disable()
          
	        self.m_staticText62 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"last", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText62.Wrap( -1 )
	        self.m_staticText62.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

	        gSizer61.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

	        self.row21 = wx.SpinCtrl( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 1000, 0 )
	        self.row21.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
	        self.row21.SetForegroundColour( wx.Colour( 0, 128, 0 ) )
	        self.row21.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )

	        gSizer61.Add( self.row21, 0, wx.ALL, 5 )
#	      self.row21.Disable()
          
	        self.m_staticText611 = wx.StaticText( sbSizer78.GetStaticBox(), wx.ID_ANY, u"sheet title", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.m_staticText611.Wrap( -1 )

	        gSizer61.Add( self.m_staticText611, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


	        m_comboBox11Choices = [worksheet.title for worksheet in worksheets]
#	      print(m_comboBox1Choices)
	        self.m_comboBox11 = wx.ComboBox( sbSizer78.GetStaticBox(), wx.ID_ANY, u"選択して下さい", wx.DefaultPosition, wx.DefaultSize, m_comboBox11Choices, wx.CB_DROPDOWN )
	        self.m_comboBox11.SetForegroundColour( wx.Colour( 0, 128, 0 ) )
	        self.m_comboBox11.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )

	        gSizer61.Add( self.m_comboBox11, 0, wx.ALL, 5 )

#（お問い合わせページの自動入力：機能未完成によりドロップボックスを無効）        
#	      self.m_comboBox11.Enable(False)
	        self.m_comboBox11.Enable(True)


	        self.btn4 = wx.Button( sbSizer78.GetStaticBox(), wx.ID_ANY, u"Posting", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.btn4.SetDefault()
	        self.btn4.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
#	      self.btn31.Disable()
          
	        gSizer61.Add( self.btn4, 0, wx.ALL, 5 )


	        sbSizer78.Add( gSizer61, 1, wx.EXPAND, 5 )


	        self.m_panel88.SetSizer( sbSizer78 )
	        self.m_panel88.Layout()
	        sbSizer78.Fit( self.m_panel88 )
	        gSizer6.Add( self.m_panel88, 1, wx.EXPAND |wx.ALL, 5 )

	        self.m_panel89 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        sbSizer76 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel89, wx.ID_ANY, u"Graph drawing" ), wx.VERTICAL )

	        self.m_panel90 = wx.Panel( sbSizer76.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
	        bSizer20 = wx.BoxSizer( wx.VERTICAL )

	        self.m_radioBtn1 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Number of executions", wx.DefaultPosition, wx.DefaultSize, 0 )
	        bSizer20.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

	        self.m_radioBtn2 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Number of send completely", wx.DefaultPosition, wx.DefaultSize, 0 )
	        bSizer20.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
#	        self.m_radioBtn2.Disable()

	        self.m_radioBtn3 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Breakdown of errors", wx.DefaultPosition, wx.DefaultSize, 0 )
	        bSizer20.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
#	        self.m_radioBtn3.Disable()
            
	        self.btn5 = wx.Button( self.m_panel90, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
	        self.btn5.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

	        bSizer20.Add( self.btn5, 0, wx.ALL, 5 )

	        gSizer42 = wx.GridSizer( 0, 2, 0, 0 )


	        bSizer20.Add( gSizer42, 1, wx.EXPAND, 5 )


	        self.m_panel90.SetSizer( bSizer20 )
	        self.m_panel90.Layout()
	        bSizer20.Fit( self.m_panel90 )
	        sbSizer76.Add( self.m_panel90, 1, wx.EXPAND |wx.ALL, 5 )


	        self.m_panel89.SetSizer( sbSizer76 )
	        self.m_panel89.Layout()
	        sbSizer76.Fit( self.m_panel89 )
	        gSizer6.Add( self.m_panel89, 1, wx.EXPAND |wx.ALL, 5 )


#以上、ここまでが機能追加のためのコーディング変更分

	        bSizer17.Add( gSizer6, 1, wx.EXPAND, 5 )


	        self.m_panel51.SetSizer( bSizer17 )
	        self.m_panel51.Layout()
	        bSizer17.Fit( self.m_panel51 )
	        sbSizer21.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )


	        self.m_panel28.SetSizer( sbSizer21 )
	        self.m_panel28.Layout()
	        sbSizer21.Fit( self.m_panel28 )
	        bSizer15.Add( self.m_panel28, 1, wx.EXPAND |wx.ALL, 5 )


#	        bSizer15.Add( gSizer8, 1, wx.EXPAND, 5 )
#	        bSizer15.Add( gSizer43, 1, wx.EXPAND |wx.ALL, 5 )


	        sbSizer5.Add( bSizer15, 1, wx.EXPAND, 5 )


	        self.m_panel6.SetSizer( sbSizer5 )
	        self.m_panel6.Layout()
	        sbSizer5.Fit( self.m_panel6 )


	        bSizer19.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


	        mainBox.Add( bSizer19, 1, wx.EXPAND, 5 )


	        self.main_panel.SetSizer( mainBox )
	        self.main_panel.Layout()
	        mainBox.Fit( self.main_panel )        
	        mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )

	        self.SetSizer( mainSizer )
	        self.Layout()

	        self.Centre( wx.BOTH )


# Connect Events
	        self.btn3.Bind( wx.EVT_BUTTON, self.inquiry_url )
	        self.btn4.Bind( wx.EVT_BUTTON, self.inquiry_post )
	        self.btn5.Bind( wx.EVT_BUTTON, self.graph_start )
	        self.btn32.Bind( wx.EVT_BUTTON, self.list_view )


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
	          self.m_comboBox12.SetValue(j['sheetname1'])
	          self.m_comboBox1.SetValue(j['sheetname2'])
	          self.m_comboBox11.SetValue(j['sheetname3'])
	          self.row1.SetValue(j['row1'])
	          self.row2.SetValue(j['row2'])
	          self.row11.SetValue(j['row11'])
	          self.row21.SetValue(j['row21'])

#エラーメッセージ表示
	      except requests.exceptions.ConnectionError as e:
	        print("error:", e)
	        wx.MessageBox(f'{e}', u'Server error', wx.ICON_ERROR)

#エラーメッセージ表示
	      except gspread.exceptions.APIError as e:
	        print("error:", e)
	        wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)

#設定情報（json）書き出し
	def quit_button(self, event):
	        adid3 = MyProject1MyDialog3(self)
	        adid8 = MyProject1MyDialog8(self)

#文字コードをUTF-8に変換しないとエラー発生がするため注意！！
	        with open('setting.json','w',encoding='utf-8') as f:
	            w_data = {}
	            w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
	            w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
	            w_data['webdriver'] = adid3.m_textCtrl111.GetValue()
	            w_data['user'] = adid3.m_textCtrl4.GetValue()
	            w_data['password'] = adid3.m_textCtrl5.GetValue()
	            w_data['remember'] = adid3.m_checkBox1.GetValue()
	            w_data['date'] = adid8.m_textCtrl52.GetValue()
	            w_data['posts'] = adid8.m_textCtrl53.GetValue()
	            w_data['sheetname1'] = self.m_comboBox12.GetValue()
	            w_data['sheetname2'] = self.m_comboBox1.GetValue()
	            w_data['sheetname3'] = self.m_comboBox11.GetValue()
	            w_data['row1'] = self.row1.GetValue()
	            w_data['row2'] = self.row2.GetValue()
	            w_data['row11'] = self.row11.GetValue()
	            w_data['row21'] = self.row21.GetValue()                
                
	            json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
	            print('WRITE:')
#                print(w_data)
	            self.Destroy()


	def list_view( self, event ):
	        adid = MyProject1MyDialog3(self)
	        credentials = ServiceAccountCredentials.from_json_keyfile_name(adid.m_textCtrl11.GetValue(), scope)
	        gc = gspread.authorize(credentials)                   

	        if self.m_comboBox12.GetValue() == '選択して下さい':
	         self.m_comboBox12.SetBackgroundColour("#ff0000")
	         wx.MessageBox(u'Please select the Worksheet title!!', u'Setting value error', wx.ICON_ERROR)
#	        elif self.m_comboBox12.GetValue() == '完成例':
#	         self.m_comboBox12.SetBackgroundColour("#FFFFFF")
#	         wx.MessageBox(u'The selected sheet name is not valid.!!', u'Setting value error', wx.ICON_ERROR)
		# Set cell values.
	        else:
	         wb = gc.open_by_key(adid.m_comboBox6.GetValue())
	         ws3 = wb.worksheet(self.m_comboBox12.GetValue())
	         lastrow = len(ws3.col_values(1))         
	         self.m_comboBox12.SetBackgroundColour("#FFFFFF")
             
#住所＋電話番号不要
	         if self.m_checkBox1.GetValue() is False \
                and self.m_checkBox2.GetValue() is False \
                    and self.m_checkBox3.GetValue() is True \
                       and self.m_checkBox4.GetValue() is True \
                           and self.m_checkBox5.GetValue() is True \
                              and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame5に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 6)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "ホームページ")
       		   adid.grid.SetColLabelValue(2, "お問い合わせページ")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(4, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(5, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list5 = ws3.range(1, 5, lastrow, 5)
	           cell_list6 = ws3.range(1, 6, lastrow, 6)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)               
             
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list5[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list6[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 5, cell_list9[i].value)                 
                
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()

#住所＋電話番号＋ホームページＵＲＬ＋お問い合わせページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is False \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame5に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 4)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(2, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(3, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#電話番号＋ホームページＵＲＬ＋お問い合わせページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is True \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 5)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "住所")                  
       		   adid.grid.SetColLabelValue(2, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(4, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list3 = ws3.range(1, 3, lastrow, 3)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list3[i].value)                 
	             adid.grid.SetCellValue(row, 2, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()

#電話番号＋ホームページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is True \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is True \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 6)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "住所")
       		   adid.grid.SetColLabelValue(2, "お問い合わせページ")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(4, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(5, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list3 = ws3.range(1, 3, lastrow, 3)
	           cell_list6 = ws3.range(1, 6, lastrow, 6)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list3[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list6[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 5, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()

#住所＋ホームページＵＲＬ＋お問い合わせページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is False \
                 and self.m_checkBox2.GetValue() is True \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 5)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "電話番号")                  
       		   adid.grid.SetColLabelValue(2, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(4, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list4 = ws3.range(1, 4, lastrow, 4)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list4[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#住所＋電話番号＋お問い合わせページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is False \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is True \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 5)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "ホームページ")                  
       		   adid.grid.SetColLabelValue(2, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(4, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list5 = ws3.range(1, 5, lastrow, 5)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list5[i].value)                 
	             adid.grid.SetCellValue(row, 2, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#住所＋電話番号＋ホームページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is False \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is True \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 5)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "お問い合わせページ")
       		   adid.grid.SetColLabelValue(2, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(4, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list6 = ws3.range(1, 6, lastrow, 6)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list6[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#ホームページＵＲＬ＋お問い合わせページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is True \
                 and self.m_checkBox2.GetValue() is True \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 6)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "住所")
       		   adid.grid.SetColLabelValue(2, "電話番号")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(4, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(5, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list3 = ws3.range(1, 3, lastrow, 3)
	           cell_list4 = ws3.range(1, 4, lastrow, 4)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list3[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list4[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 5, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#電話番号＋お問い合わせページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is True \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is True \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 6)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "住所")
       		   adid.grid.SetColLabelValue(2, "ホームページ")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(4, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(5, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list3 = ws3.range(1, 3, lastrow, 3)
	           cell_list5 = ws3.range(1, 5, lastrow, 5)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list3[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list5[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 5, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#住所＋会社ホームページＵＲＬ不要
	         elif self.m_checkBox1.GetValue() is False \
                 and self.m_checkBox2.GetValue() is True \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is True \
                             and self.m_checkBox5.GetValue() is True \
                                and self.m_checkBox6.GetValue() is True:

#MyDialogの各設定値をMyFrame6に受け渡し
	           adid = MyProject1MyFrame6(self)
	           adid.grid.ClearGrid()
       		   adid.grid.CreateGrid(10000, 6)
       		   adid.grid.SetColLabelValue(0, "法人名称")
       		   adid.grid.SetColLabelValue(1, "電話番号")
       		   adid.grid.SetColLabelValue(2, "お問い合わせページ")
       		   adid.grid.SetColLabelValue(3, "結果・エラー情報等（１）")
       		   adid.grid.SetColLabelValue(4, "結果・エラー情報等（２）")
       		   adid.grid.SetColLabelValue(5, "投稿日時")

	           dlg = wx.ProgressDialog(
	             title="リスト取得中",
	             message="0/100",
	             maximum=100,
	             style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME )
	         
# ダイアログ表示
	           dlg.Show()
	           rate = 0

	           cell_list2 = ws3.range(1, 2, lastrow, 2)
	           cell_list4 = ws3.range(1, 4, lastrow, 4)
	           cell_list6 = ws3.range(1, 6, lastrow, 6)
	           cell_list7 = ws3.range(1, 7, lastrow, 7)
	           cell_list8 = ws3.range(1, 8, lastrow, 8)
	           cell_list9 = ws3.range(1, 9, lastrow, 9)
               
	           i = 0
	           for row in range(lastrow):
	             adid.grid.SetCellValue(row, 0, cell_list2[i].value)
	             adid.grid.SetCellValue(row, 1, cell_list4[i].value)
	             adid.grid.SetCellValue(row, 2, cell_list6[i].value)
	             adid.grid.SetCellValue(row, 3, cell_list7[i].value)
	             adid.grid.SetCellValue(row, 4, cell_list8[i].value)
	             adid.grid.SetCellValue(row, 5, cell_list9[i].value)
                 
	             i += 1
	             rate += 1/(lastrow+1)*100
                 
	             # 値の更新
	             dlg.Update(value=rate, newmsg="%d/100" % rate + "%")
	           
	           dlg.Destroy()
	            
	           adid.grid.AutoSize()
	           adid.Show()


#「結果・エラー情報等」及び「投稿日時」のチェックは必須
	         elif self.m_checkBox5.GetValue() is False \
                 and self.m_checkBox6.GetValue() is False \
                     or self.m_checkBox5.GetValue() is False \
                        or self.m_checkBox6.GetValue() is False:
	           wx.MessageBox(u'Please check the required items!!', u'Extraction error', wx.ICON_ERROR)
                     

#チェック項目が１個も選択されていない
	         elif self.m_checkBox1.GetValue() is False \
                 and self.m_checkBox2.GetValue() is False \
                     and self.m_checkBox3.GetValue() is False \
                         and self.m_checkBox4.GetValue() is False \
                             and self.m_checkBox5.GetValue() is False \
                                 and self.m_checkBox6.GetValue() is False:

	           wx.MessageBox(u'No check items have been selected!!', u'Extraction error', wx.ICON_ERROR)


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
               or not 'json' in adid.m_textCtrl11.GetValue() \
                   or not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
	      wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
	   elif not 'chromedriver.exe' in adid.m_textCtrl111.GetValue():
	      wx.MessageBox(u'The web driver file is not set or the file path does not pass!!', u'Setting value error', wx.ICON_ERROR)          
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
           
	def quit_button( self, event ):
		# TODO: Implement quit_button
		self.Destroy()
		wx.Exit()
		return

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame5
###########################################################################

#class MyFrame5 ( wx.Frame ):

#	def __init__( self, parent ):
#		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 873,573 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

#		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


#		self.Centre( wx.BOTH )

#	def __del__( self ):
#		pass


###########################################################################
## Class MyDialog
###########################################################################

#class MyDialog ( wx.Dialog ):

#	def __init__( self, parent ):
#		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"リスト作成", pos = wx.DefaultPosition, size = wx.Size( 517,600), style = wx.DEFAULT_DIALOG_STYLE )

#		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

#		mainSizer = wx.BoxSizer( wx.VERTICAL )

#		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#		mainBox = wx.BoxSizer( wx.VERTICAL )

#		hbox1 = wx.BoxSizer( wx.VERTICAL )

#		self.m_panel6 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#		self.m_panel6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

#		hbox1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


#		mainBox.Add( hbox1, 1, wx.EXPAND, 5 )

#		hbox4 = wx.BoxSizer( wx.VERTICAL )

#		self.m_panel15 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
#		self.m_panel15.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

#		hbox4.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


#		mainBox.Add( hbox4, 1, wx.EXPAND, 5 )


#		self.main_panel.SetSizer( mainBox )
#		self.main_panel.Layout()
#		mainBox.Fit( self.main_panel )
#		mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )


#		self.SetSizer( mainSizer )
#		self.Layout()

#		self.Centre( wx.BOTH )

#	def __del__( self ):
#		pass


###########################################################################
## Class MyFrame4
###########################################################################

#class MyFrame4 ( wx.Frame ):

#	def __init__( self, parent ):
#		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,594 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

#		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


#		self.Centre( wx.BOTH )

#	def __del__( self ):
#		pass


###########################################################################
## Class MyDialog2
###########################################################################

#class MyDialog2 ( wx.Dialog ):

#	def __init__( self, parent ):


###########################################################################
## Class MyDialog3
###########################################################################

#class MyDialog3 ( wx.Dialog ):

#	def __init__( self, parent ):
#		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting", pos = wx.DefaultPosition, size = wx.Size( 498,540 ), style = wx.DEFAULT_DIALOG_STYLE )

#		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


#		self.Centre( wx.BOTH )

#	def __del__( self ):
#		pass


###########################################################################
## Class MyDialog4
###########################################################################

#class MyDialog4 ( wx.Dialog ):

#	def __init__( self, parent ):
#		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting of transmission contents", pos = wx.DefaultPosition, size = wx.Size( 853,464 ), style = wx.DEFAULT_DIALOG_STYLE )

#		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


#		self.Centre( wx.BOTH )

#	def __del__( self ):
#		pass


###########################################################################
## Class MyDialog5
###########################################################################

#class MyDialog5 ( wx.Dialog ):

#	def __init__( self, parent ):
#		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Email body creation", pos = wx.DefaultPosition, size = wx.Size( 670,655 ), style = wx.DEFAULT_DIALOG_STYLE )

#		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


#		self.Centre( wx.BOTH )

#	def __del__( self ):
#		pass


###########################################################################
## Class MyDialog7
###########################################################################

#class MyDialog7 ( wx.Dialog ):
    
#	def __init__( self, parent ):