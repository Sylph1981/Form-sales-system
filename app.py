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

#from MyProject1MyDialog import MyProject1MyDialog
from MyProject1MyDialog10 import MyProject1MyDialog10
from MyProject1MyDialog3 import MyProject1MyDialog3
from MyProject1MyDialog4 import MyProject1MyDialog4
from MyProject1MyDialog6 import MyProject1MyDialog6
from MyProject1MyDialog7 import MyProject1MyDialog7
from MyProject1MyDialog8 import MyProject1MyDialog8
from MyProject1MyDialog9 import MyProject1MyDialog9
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"お問い合わせフォーム投稿アプリ", pos = wx.DefaultPosition, size = wx.Size( 400,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

#メニューバー追加によりコーディング変更（2022.8.23）
		self.m_menu3 = wx.Menu()
#		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Create", wx.EmptyString, wx.ITEM_NORMAL )
#		self.m_menu3.Append( self.m_menuItem6 )

		self.m_menu11 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"URL extraction", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem7 )

		self.m_menuItem8 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Posting and sending", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem8 )

		self.m_menu3.AppendSubMenu( self.m_menu11, u"Inquiry" )

		self.m_menuItem9 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Preview", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem9 )

		self.m_menubar1.Append( self.m_menu3, u"List" )

#ここまでが変更分

		self.m_menu4 = wx.Menu()
		self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.Append( self.m_menuItem10 )

#		self.m_menuItem11 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"For administrators", wx.EmptyString, wx.ITEM_NORMAL )
#		self.m_menu4.Append( self.m_menuItem11 )

		self.m_menubar1.Append( self.m_menu4, u"Help" )
		self.SetMenuBar( self.m_menubar1 )


#Connect Events
		self.Bind( wx.EVT_MENU, self.quit_button, self.m_menuItem2 )
		self.Bind( wx.EVT_MENU, self.Configuration, self.m_menuItem3 )
		self.Bind( wx.EVT_MENU, self.Profile, self.m_menuItem4 )
		self.Bind( wx.EVT_MENU, self.Send_email_body, self.m_menuItem5 )
#		self.Bind( wx.EVT_MENU, self.create_button, self.m_menuItem6 )
		self.Bind( wx.EVT_MENU, self.inquiry_url, self.m_menuItem7 )
		self.Bind( wx.EVT_MENU, self.inquiry_button, self.m_menuItem8 )
		self.Bind( wx.EVT_MENU, self.list_view, self.m_menuItem9 )
		self.Bind( wx.EVT_MENU, self.Creator_info, self.m_menuItem10 )
#		self.Bind( wx.EVT_MENU, self.Status_info, self.m_menuItem11 )
		self.Bind(wx.EVT_CLOSE, self.quit_button) 


	def inquiry_url( self, event ):
		adid = MyProject1MyDialog3(self)
		if adid.m_comboBox6.GetValue() == '' \
			or not 'json' in adid.m_textCtrl11.GetValue():
			wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
		else:
			try:
				adid = MyProject1MyDialog10(self)
				adid.ShowModal()
				adid.Destroy()
			except gspread.exceptions.APIError as e:
				print("error:", e)
				wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)


	def inquiry_button(self, event):
		adid = MyProject1MyDialog3(self)
        
		if adid.m_comboBox6.GetValue() == '' \
			or not 'json' in adid.m_textCtrl11.GetValue():
			wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
		elif not adid.m_comboBox6.GetValue() == '' \
			and 'json' in adid.m_textCtrl11.GetValue():
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

#ここからコーディング変更（2022.8.23）
				bSizer15 = wx.BoxSizer( wx.VERTICAL )

				self.m_panel28 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
				self.m_panel28.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )

				sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel28, wx.ID_ANY, u"Automatic form submission" ), wx.VERTICAL )

				self.m_panel51 = wx.Panel( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
				bSizer17 = wx.BoxSizer( wx.VERTICAL )

#				gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

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

				self.row11 = wx.SpinCtrl( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 10000, 1 )
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

				self.row21 = wx.SpinCtrl( sbSizer78.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 1, 10000, 1 )
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
#			print(m_comboBox1Choices)
				self.m_comboBox11 = wx.ComboBox( sbSizer78.GetStaticBox(), wx.ID_ANY, u"選択して下さい", wx.DefaultPosition, wx.Size( 300,-1 ), m_comboBox11Choices, wx.CB_DROPDOWN )
				self.m_comboBox11.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
				self.m_comboBox11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
				self.m_comboBox11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

				bSizer27.Add( self.m_comboBox11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

				sbSizer78.Add( bSizer27, 1, wx.EXPAND, 5 )

				self.btn4 = wx.Button( sbSizer78.GetStaticBox(), wx.ID_ANY, u"Posting", wx.DefaultPosition, wx.DefaultSize, 0 )

				self.btn4.SetDefault()
				self.btn4.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )

				sbSizer78.Add( self.btn4, 0, wx.ALL, 5 )

				self.m_panel88.SetSizer( sbSizer78 )
				self.m_panel88.Layout()
				sbSizer78.Fit( self.m_panel88 )
				bSizer17.Add( self.m_panel88, 1, wx.EXPAND |wx.ALL, 5 )

				self.m_panel89 = wx.Panel( self.m_panel51, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
				sbSizer76 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel89, wx.ID_ANY, u"Graph drawing" ), wx.VERTICAL )

				self.m_panel90 = wx.Panel( sbSizer76.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
				bSizer20 = wx.BoxSizer( wx.VERTICAL )

				self.m_radioBtn1 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Number of executions", wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_radioBtn1.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
				self.m_radioBtn1.Enable()

				bSizer20.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

				self.m_radioBtn2 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Number of send completely", wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_radioBtn2.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
				self.m_radioBtn2.Enable()

				bSizer20.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

				self.m_radioBtn3 = wx.RadioButton( self.m_panel90, wx.ID_ANY, u"Breakdown of errors", wx.DefaultPosition, wx.DefaultSize, 0 )
				self.m_radioBtn3.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )
				self.m_radioBtn3.Enable()

				bSizer20.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

				self.m_panel90.SetSizer( bSizer20 )
				self.m_panel90.Layout()
				bSizer20.Fit( self.m_panel90 )
				sbSizer76.Add( self.m_panel90, 1, wx.EXPAND |wx.ALL, 5 )

				self.btn5 = wx.Button( sbSizer76.GetStaticBox(), wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
				self.btn5.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Meiryo UI" ) )
				self.btn5.Enable()

				sbSizer76.Add( self.btn5, 0, wx.ALL, 5 )


				self.m_panel89.SetSizer( sbSizer76 )
				self.m_panel89.Layout()
				sbSizer76.Fit( self.m_panel89 )
				bSizer17.Add( self.m_panel89, 1, wx.EXPAND |wx.ALL, 5 )


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
				self.btn5.Bind( wx.EVT_BUTTON, self.graph_start )


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
#					self.m_comboBox12.SetValue(j['sheetname1'])
#					self.m_comboBox1.SetValue(j['sheetname2'])
					self.m_comboBox11.SetValue(j['sheetname3'])
#					self.row1.SetValue(j['row1'])
#					self.row2.SetValue(j['row2'])
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


	def graph_start(self, event):
		import json
		import codecs

		adid3 = MyProject1MyDialog3(self)
		adid8 = MyProject1MyDialog8(self)

# 「AttributeError: 'int' object has no attribute 'GetValue'」
# が表示されてしまうので、try~exceptにより回避
		try:
			row11 = self.row11.GetValue()
			row21 = self.row21.GetValue()
			print(row11)
			print(row21)

#文字コードをUTF-8に変換しないとエラー発生がするため注意！！
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
#			w_data['sheetname1'] = self.m_comboBox12.GetValue()
#			w_data['sheetname2'] = self.m_comboBox1.GetValue()
				w_data['sheetname3'] = self.m_comboBox11.GetValue()
#			w_data['row1'] = self.row1.GetValue()
#			w_data['row2'] = self.row2.GetValue()

# 属性GetValue()は不要
				w_data['row11'] = row11
				w_data['row21'] = row21
                
				json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
				print('WRITE:')

		except Exception as e:
			print(e)

		with codecs.open('setting.json','r',encoding='utf-8') as f:
			j = json.load(f,strict=False)
			f.close()

			self.row11 = j["row11"]
			self.row21 = j["row21"]

# ラジオボタンが１個も選択されていない
		if self.m_radioBtn1.GetValue() is False \
            and self.m_radioBtn2.GetValue() is False \
            and self.m_radioBtn3.GetValue() is False:
			wx.MessageBox(u'No check items have been selected!!',
            u'Extraction error', wx.ICON_ERROR)

		elif j["sheetname3"] == '選択して下さい':
			wx.MessageBox(u'Please select the Worksheet title!!',
			u'Setting value error', wx.ICON_ERROR)
		elif self.row11 == 0 and self.row21 == 0:
			wx.MessageBox(u'Please set the range!!',
			u'Setting value error', wx.ICON_ERROR)
		elif self.row21 - self.row11 > 1000:
			wx.MessageBox(u'The value exceeds the configurable range!!',
			u'Setting value error', wx.ICON_ERROR)
		elif self.row21 - self.row11 < 0:
			wx.MessageBox(u'Illegal range!!',
			u'Setting value error', wx.ICON_ERROR)
		elif j["sheetname3"] == '選択して下さい' \
			and self.row11 == 0 \
			and self.row21 == 0:
			wx.MessageBox(u'Please select the Worksheet title and Illegal range!!',
			u'Setting value error', wx.ICON_ERROR)

# 件数の可視化
		elif self.m_radioBtn1.GetValue() is True:
			adid = MyProject1MyDialog3(self)
			credentials = ServiceAccountCredentials.from_json_keyfile_name(
			adid.m_textCtrl11.GetValue(), scope)
			gc = gspread.authorize(credentials)
			wb = gc.open_by_key(adid.m_comboBox6.GetValue())
			ws3 = wb.worksheet(j["sheetname3"])
			#import wx.lib
			#import wx.lib.plot as plot
#	      import matplotlib
#	      matplotlib.use('WXAgg')
			import matplotlib.pyplot as mlp

			import pandas as pd
			#import seaborn as sns

			dlg = wx.ProgressDialog(
				title="データ処理中",
				message="0/100",
				maximum=100,
				style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME)

# ダイアログ表示
			dlg.Show()
			rate = 0

			date = []
			try:
				cell_list_X = ws3.range(self.row11, 9, self.row21, 9)
#	      print(cell_list_X)

				i = 0
				j = 0
				for i in range(len(cell_list_X)):
					print(cell_list_X[i].value)

# 時刻を消して日付だけにしたいとき
# https://qiita.com/daijiro_maeyama/items/8a62fbb0741e5bad8568
					dt_str, new_time = cell_list_X[i].value.split()

# 空リスト「date」に上記の式で区切った文字列を追加
					date.append(dt_str)

					j += 1
					rate += 1/(self.row21)*100

        # 値の更新
					dlg.Update(value=rate, newmsg="%d/100" % rate + "%")

				# print(date)

# listをDataFrameに変換する
# https://qiita.com/fault/items/6d5d69d4a0c257ed39df
				df = pd.DataFrame({'Date': date})
				# print(df)

# value_counts()・・・DataFrameの特定の「列」に入っている「ユニークな要素」の「出現回数」を抽出することができる関数
# 棒グラフで時系列順に表示する（Index順にソートしてからプロット）
# https://teratail.com/questions/265731
				val = df["Date"].value_counts().sort_index()
				# print(val)

# グラフウィンドウのタイトル
				mlp.figure("Number of executions")

# X軸ラベル設定
				mlp.xlabel("件数", fontname="Yu Gothic")

# X軸目盛ラベルの文字を「游ゴシック」
				mlp.xticks(fontname="Yu Gothic")

# Y軸ラベル設定（非表示）
				mlp.ylabel("", fontname="Yu Gothic")

# Y軸目盛ラベルの文字を「游ゴシック」
				mlp.yticks(fontname="Yu Gothic")

# グラフの種類を「横棒グラフ」に設定
				val.plot(kind='barh', label='total')

				dlg.Destroy()

# プロットしたグラフを表示
				mlp.show()

			except Exception as e:
				print(e)
				wx.MessageBox(f'{e}', u'error', wx.ICON_ERROR)
				dlg.Destroy()

# 送信完了数
		elif self.m_radioBtn2.GetValue() is True:
			adid = MyProject1MyDialog3(self)
			credentials = ServiceAccountCredentials.from_json_keyfile_name(
			adid.m_textCtrl11.GetValue(), scope)
			gc = gspread.authorize(credentials)
			wb = gc.open_by_key(adid.m_comboBox6.GetValue())
			ws3 = wb.worksheet(j["sheetname3"])
			import matplotlib.pyplot as mlp
			import pandas as pd
#	      import seaborn as sns
			dlg = wx.ProgressDialog(
				title="データ処理中",
				message="0/100",
				maximum=100,
				style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME)

# ダイアログ表示
			dlg.Show()
			rate = 0

			data1 = []
			try:
				cell_list_1 = ws3.range(self.row11, 9, self.row21, 9)
#	      print(cell_list_1)

				i = 0
				j = 0
				for i in range(len(cell_list_1)):
				#	        print(cell_list_1[i].value)

				# 時刻を消して日付だけにしたいとき
				# https://qiita.com/daijiro_maeyama/items/8a62fbb0741e5bad8568
					dt_str, new_time = cell_list_1[i].value.split()

# 空リスト「data1」に上記の式で区切った文字列を追加
					data1.append(dt_str)

					j += 1
					rate += 1/(self.row21)*100
        # 値の更新
					dlg.Update(value=rate, newmsg="%d/100" % rate + "%")

				print(data1)

# 7列目（文字列のみ）
				data2 = []
				cell_list_2 = ws3.range(self.row11, 7, self.row21, 7)
#	      print(cell_list_2)

				rate = 0
				i = 0
				j = 0
				for i in range(len(cell_list_2)):
				#	        print(cell_list_2[i].value)
					data2.append(cell_list_2[i].value)

					j += 1
					rate += 1/(self.row21)*100
        # 値の更新
					dlg.Update(value=rate, newmsg="%d/100" % rate + "%")

				print(data2)
# listをDataFrameに変換する
# https://qiita.com/fault/items/6d5d69d4a0c257ed39df
				df1 = pd.DataFrame(list(zip(data1, data2)),
							   columns=['Date', 'Result'])
				print(df1)

#           Date                        Result
# 0   2021年12月22日                サービスに関する専用フォーム
# 1   2021年12月22日   x この項目 "メールアドレス" は入力が必須です。
# 2   2021年12月22日                 入力にエラーがあります。
# 3   2021年12月22日                    フォーム要素取得不可
# 4   2021年12月22日                    フォーム要素取得不可
# ..          ...                           ...
# 79  2021年12月24日                     送信完了しました。
# 80  2021年12月24日  お問い合わせを送信いたしました。ありがとうございました。
# 81  2021年12月24日                     送信完了しました。
# 82  2021年12月24日                          送信完了
# 83  2021年12月24日                          完了画面

# value_counts()・・・DataFrameの特定の「列」に入っている「ユニークな要素」の「出現回数」を抽出することができる関数
# 棒グラフで時系列順に表示する（Index順にソートしてからプロット）
# https://teratail.com/questions/265731
				val1 = df1["Date"].value_counts().sort_index()
				print(val1)

# [84 rows x 2 columns]
# 2021年12月21日    18
# 2021年12月22日    22
# 2021年12月23日    26
# 2021年12月24日    18
# Name: Date, dtype: int64

				val2 = df1["Result"].value_counts().sort_index()
				print(val2)

#	      df_str = df[['Date','Result']]
#	      print(df_str)

# x この項目 "メールアドレス" は入力が必須です。
#                                 1
# * 必須項目です* メールアドレスが正しくありません
#                                   1
# Email *
#             1
# TYPE2ERRORメールアドレスが正しくありません。
#                              1
# Thank you for your message. It has been sent.
#             1
# 【Email】は必須入力項目です。
#                         1
# 【Email】は必須項目です。
#                       1
# あなたのメッセージは送信されました。ありがとうございました。
#                                           6
# ありがとうございます。メッセージは送信されました。
#                                     15
# ありがとうございます。メッセージは送信されました。なお、自動返信メールが届かない場合は、メールア
# ドレス誤記の可能性がございますので、ご確認をお願いいたします。                              1
# お問い合わせありがとうございました。
#                               1
# お問い合わせを送信いたしました。ありがとうございました。
#                                         2
# お問い合わせメッセージを送信しました。
#                                1
# お問い合わせ頂きまして、誠に有難うございます。内容を確認後、早急にご返信させて頂きます。 もし数
# 日中に返事が無い場合は、正しく受信できなかった可能性がありますので、恐れ入りますが再度のご連絡を
# お願い致します。     1
# サービスに関する専用フォーム
#                           4
# フォーム要素取得不可
#                       5
# メッセージは送信されました。ありがとうございました。
#                                       1
# メールアドレスが入力されていません
#                              3
# メール送信終了｜エムアンドシーシステム（株）
#                                   1
# 入力にエラーがあります。
#                         1
# 営業お断り！！
#                    1
# 完了画面
#                 1
# 必須項目に入力してください。
#                           5
# 必須項目に記入もれがあります。
#                            4
# 資料請求専用フォーム
#                       6
# 送信できませんでした。入力に不備があります。
#                                   1
# 送信完了
#                 4
# 送信完了 株式会社ナガツカ
#                         1
# 送信完了しました。
#                     11
# 送信完了｜お問い合わせ
#                        1

# Result全体より指定キーワードにて抽出
# 論理積（かつ）: &演算子
# 論理和（または）: |演算子
# 否定（でない）: ~演算子
# https://note.nkmk.me/python-pandas-count-condition/
				df2 = df1[df1['Result'].str.contains("送信されました")
                      | df1['Result'].str.contains("完了")
                      | df1['Result'].str.contains("終了")
                      | df1['Result'].str.contains("送信いたしました")
                      | df1['Result'].str.contains("送信しました")
                      | df1['Result'].str.contains("ございま")
                      | df1['Result'].str.contains("Thank")]
				print(df2)

#           Date                                             Result
# 36  2021年12月21日                          ありがとうございます。メッセージは送信されました。
# 37  2021年12月21日                          ありがとうございます。メッセージは送信されました。
# 38  2021年12月21日                                               送信完了
# 39  2021年12月21日                                          送信完了しました。
# 40  2021年12月21日                       お問い合わせを送信いたしました。ありがとうございました
# 。
# 42  2021年12月21日                                          送信完了しました。
# 43  2021年12月21日                          ありがとうございます。メッセージは送信されました。
# 44  2021年12月21日                                          送信完了しました。
# 45  2021年12月21日                                               送信完了
# 46  2021年12月21日                     あなたのメッセージは送信されました。ありがとうございまし
# た。
# 47  2021年12月21日                                お問い合わせメッセージを送信しました。
# 48  2021年12月21日                                          送信完了しました。
# 49  2021年12月21日                         メッセージは送信されました。ありがとうございました。
# 50  2021年12月21日                     あなたのメッセージは送信されました。ありがとうございまし
# た。
# 51  2021年12月21日                                      送信完了 株式会社ナガツカ
# 52  2021年12月21日                                          送信完了しました。
# 53  2021年12月21日                                        送信完了｜お問い合わせ
# 54  2021年12月22日                                          送信完了しました。
# 55  2021年12月22日                                          送信完了しました。
# 56  2021年12月22日                          ありがとうございます。メッセージは送信されました。
# 57  2021年12月22日                             メール送信終了｜エムアンドシーシステム（株）
# 58  2021年12月22日                          ありがとうございます。メッセージは送信されました。
# 59  2021年12月22日                     あなたのメッセージは送信されました。ありがとうございまし
# た。
# 60  2021年12月22日                     あなたのメッセージは送信されました。ありがとうございまし
# た。
# 61  2021年12月23日                                          送信完了しました。
# 62  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 63  2021年12月23日                                               送信完了
# 64  2021年12月23日  お問い合わせ頂きまして、誠に有難うございます。内容を確認後、早急にご返信させ
# て頂きます。 も...
# 65  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 66  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 67  2021年12月23日                     あなたのメッセージは送信されました。ありがとうございまし
# た。
# 68  2021年12月23日                                 お問い合わせありがとうございました。
# 69  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 70  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 71  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 72  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 73  2021年12月23日  ありがとうございます。メッセージは送信されました。なお、自動返信メールが届か
# ない場合は、メー...
# 74  2021年12月23日                     あなたのメッセージは送信されました。ありがとうございまし
# た。
# 75  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 76  2021年12月23日                          ありがとうございます。メッセージは送信されました。
# 77  2021年12月24日                                          送信完了しました。
# 78  2021年12月24日                          ありがとうございます。メッセージは送信されました。
# 79  2021年12月24日                                          送信完了しました。
# 80  2021年12月24日                       お問い合わせを送信いたしました。ありがとうございました
# 。
# 81  2021年12月24日                                          送信完了しました。
# 82  2021年12月24日                                               送信完了
# 83  2021年12月24日                                               完了画面

#	      val3 = df[df['Result'].str.contains("送信されました")].value_counts().sort_index()
#	      print(df[df['Result'].str.contains("送信されました")].value_counts().sort_index())

				val3 = df2["Date"].value_counts().sort_index()
				print(val3)

# 2021年12月21日    17
# 2021年12月22日     7
# 2021年12月23日    16
# 2021年12月24日     7
# Name: Date, dtype: int64

# 日付別件数

# listをDataFrameに変換する
# https://qiita.com/fault/items/6d5d69d4a0c257ed39df
#	      df3 = pd.DataFrame({'Date':data1})
#	      print(df3)

# value_counts()・・・DataFrameの特定の「列」に入っている「ユニークな要素」の「出現回数」を抽出することができる関数
# 棒グラフで時系列順に表示する（Index順にソートしてからプロット）
# https://teratail.com/questions/265731
#	      val4 = df3["Date"].value_counts().sort_index()
#	      print(val4)


# グラフウィンドウのタイトル
				mlp.figure("Number of executions")

# X軸ラベル設定
				mlp.xlabel("件数", fontname="Yu Gothic")

# X軸目盛ラベルの文字を「游ゴシック」
				mlp.xticks(fontname="Yu Gothic")

# Y軸ラベル設定（非表示）
				mlp.ylabel("", fontname="Yu Gothic")

# Y軸目盛ラベルの文字を「游ゴシック」
				mlp.yticks(fontname="Yu Gothic")

# グラフの種類を「横棒グラフ」に設定
				val3.plot(kind='barh', color='cornflowerblue', label='send complete')

				dlg.Destroy()

# 凡例の表示
				mlp.legend()

# プロットしたグラフを表示
				mlp.show()

			except Exception as e:
				print(e)
				wx.MessageBox(
					f'{e}', u'error', wx.ICON_ERROR)
				dlg.Destroy()


# エラー内訳を可視化
		elif self.m_radioBtn3.GetValue() is True:
			adid = MyProject1MyDialog3(self)
			credentials = ServiceAccountCredentials.from_json_keyfile_name(
			adid.m_textCtrl11.GetValue(), scope)
			gc = gspread.authorize(credentials)
			wb = gc.open_by_key(adid.m_comboBox6.GetValue())
			ws3 = wb.worksheet(j["sheetname3"])
			#import wx.lib
			#import wx.lib.plot as plot
			import matplotlib.pyplot as mlp
			import pandas as pd
			from matplotlib import rcParams
			#import seaborn as sns

# スクリプトの最初でフォント変更の宣言
# https://qiita.com/yniji/items/3fac25c2ffa316990d0c
			rcParams['font.family'] = 'sans-serif'
			rcParams['font.sans-serif'] = ['Yu Gothic']

			dlg = wx.ProgressDialog(
			    title="データ処理中",
			    message="0/100",
			    maximum=100,
			    style=wx.PD_AUTO_HIDE | wx.PD_ELAPSED_TIME | wx.PD_ESTIMATED_TIME | wx.PD_REMAINING_TIME)

# ダイアログ表示
			dlg.Show()
			rate = 0

			data = []
			try:
				cell_list_X = ws3.range(self.row11, 7, self.row21, 7)
#	      print(cell_list_X)

				i = 0
				j = 0
				for i in range(len(cell_list_X)):
				#	        print(cell_list_X[i].value)
					data.append(cell_list_X[i].value)

					j += 1
					rate += 1/(self.row21)*100
        # 値の更新
					dlg.Update(value=rate, newmsg="%d/100" % rate + "%")

				print(data)

# listをDataFrameに変換する
# https://qiita.com/fault/items/6d5d69d4a0c257ed39df
				df1 = pd.DataFrame({'Result': data})
				print(df1)

# Result全体より指定キーワードにて抽出
# 論理積（かつ）: &演算子
# 論理和（または）: |演算子
# 否定（でない）: ~演算子
# https://note.nkmk.me/python-pandas-count-condition/
				df2 = df1[~(df1['Result'].str.contains("送信されました"))
					  & ~(df1['Result'].str.contains("完了"))
					  & ~(df1['Result'].str.contains("終了"))
					  & ~(df1['Result'].str.contains("送信いたしました"))
					  & ~(df1['Result'].str.contains("送信しました"))
					  & ~(df1['Result'].str.contains("ございま"))
					  & ~(df1['Result'].str.contains("Thank"))
					  & df1['Result'].str.contains("専用")
					  | df1['Result'].str.contains("必須")
					  | df1['Result'].str.contains("要素")
					  | df1['Result'].str.contains("メールアドレス")
					  | df1['Result'].str.contains("エラー")
					  | df1['Result'].str.contains("正しくありません")
					  | df1['Result'].str.contains("不備")
					  | df1['Result'].str.contains("営業")
					  | df1['Result'].str.contains("Email")
					  | df1['Result'].str.contains("入力")
					  | df1['Result'].str.contains("問題")
					  | df1['Result'].str.contains("不可")
					  | df1['Result'].str.contains("rror")
					  | df1['Result'].str.contains("記入")
					  | df1['Result'].str.contains("失敗")
					  | df1['Result'].str.contains("URL")
					  | df1['Result'].str.contains("RROR")]
				print(df2)


# value_counts()・・・DataFrameの特定の「列」に入っている「ユニークな要素」の「出現回数」を抽出することができる関数
# 棒グラフで時系列順に表示する（Index順にソートしてからプロット）
# https://teratail.com/questions/265731
				val = df2["Result"].value_counts()
				print(val)

# グラフウィンドウのタイトル
				mlp.figure("Breakdown of errors")

# プロットの色変更
				cmap = mlp.get_cmap("Set3")

# Qualitativeの種類（参考）
#	      ['Pastel1', 'Pastel2', 'Paired', 'Accent',
#        'Dark2', 'Set1', 'Set2', 'Set3',
#        'tab10', 'tab20', 'tab20b', 'tab20c']

				colors = [cmap(i) for i in range(len(val))]

# 円グラフを描画するための引数設定
				mlp.pie(val,
					autopct='%.d%%',
					pctdistance=0.8,
					counterclock=False,
					startangle=90,
					textprops={"fontsize": 15, 'weight': "bold"},
					wedgeprops={'width': 0.5, 'linewidth': 1,
								'edgecolor': "white"},
					colors=colors,
					radius=1.2)

# ラベルテキストのサイズ設定
#	      mlp.rcParams['font.size'] = 15

# 凡例の表示
# 微調整は「loc='lower left'」「bbox_to_anchor=(0.9,0.5)」等を引数に設定
# 参考サイト（https://www.yutaka-note.com/entry/matplotlib_legend#loc%E3%81%A7%E7%B0%A1%E5%8D%98%E4%BD%8D%E7%BD%AE%E8%AA%BF%E6%95%B4）
				mlp.legend(val.index, fancybox=True, loc='upper left',
					   bbox_to_anchor=(0.9, 0.5))

				dlg.Destroy()

# プロットしたグラフを表示
				mlp.show()

			except Exception as e:
				print(e)
				wx.MessageBox(
					f'{e}', u'error', wx.ICON_ERROR)
				dlg.Destroy()

	def list_view( self, event ):
		adid = MyProject1MyDialog3(self)
		if adid.m_comboBox6.GetValue() == '' \
			or not 'json' in adid.m_textCtrl11.GetValue():
			wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
		else:
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

	# def Send_email_body(self, event):
	# 	adid = MyProject1MyDialog5(self)
	# 	adid.ShowModal()
	# 	adid.Destroy()

	def Send_email_body(self, event):
		adid = MyProject1MyDialog6(self)
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
	# def create_button( self, event ):
	# 	adid = MyProject1MyDialog3(self)
	# 	if adid.m_comboBox6.GetValue() == '' \
	# 		or not 'json' in adid.m_textCtrl11.GetValue():
	# 		wx.MessageBox(u'The key is incorrect or does not exist!!', u'Setting value error', wx.ICON_ERROR)
	# 	else:
	# 		try:
#MyFrame2のテキストボックス及びコンボボックスの値をMyDialogに受け渡し
				# adid = MyProject1MyDialog(self)
				# adid.ShowModal()
				# adid.Destroy()
           
#エラーメッセージ表示
			# except gspread.exceptions.APIError as e:
			# 	print("error:", e)
			# 	wx.MessageBox(f'{e}', u'Setting value error', wx.ICON_ERROR)

#設定情報（json）書き出し
	def quit_button(self, event):
		adid3 = MyProject1MyDialog3(self)
		adid8 = MyProject1MyDialog8(self)

#文字コードをUTF-8に変換しないとエラー発生がするため注意！！
		with open('setting.json','w',encoding='utf-8') as f:
			w_data = {}
			w_data['verificationkey'] = adid3.m_textCtrl11.GetValue()
			w_data['spreadsheetkey'] = adid3.m_comboBox6.GetValue()
			w_data['tempfile'] = adid3.m_textCtrl111.GetValue()
#			w_data['profile_path'] = adid3.m_textCtrl112.GetValue()
			w_data['user'] = adid3.m_textCtrl4.GetValue()
			w_data['password'] = adid3.m_textCtrl5.GetValue()
			w_data['remember'] = adid3.m_checkBox1.GetValue()
			w_data['date'] = adid8.m_textCtrl52.GetValue()
			w_data['posts'] = adid8.m_textCtrl53.GetValue()
#			w_data['sheetname1'] = self.m_comboBox12.GetValue()
#			w_data['sheetname2'] = self.m_comboBox1.GetValue()
			w_data['sheetname3'] = self.m_comboBox11.GetValue()
#			w_data['row1'] = self.row1.GetValue()
#			w_data['row2'] = self.row2.GetValue()
			w_data['row11'] = self.row11.GetValue()
			w_data['row21'] = self.row21.GetValue()                
                
			json.dump(w_data, f, ensure_ascii=False, indent=1, sort_keys=True, separators=(',', ': '))
			print('WRITE:')
#                print(w_data)
			self.Destroy()


	def quit_button( self, event ):
#		# TODO: Implement quit_button
		self.Destroy()
		wx.Exit()
		return

	def __del__( self ):
		pass