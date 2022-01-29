# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:14:04 2021

@author: iorin
"""

import wx
import json
import codecs
#import app
from MyProject1MyFrame2Child_rev4 import MyProject1MyFrame2
from MyProject1MyFrame2Child_rev4 import MyProject1MyDialog3

# Implementing MyDialog2
class MyProject1MyDialog2( wx.Dialog ):
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"User Authentication", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel23.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Please enter your account information." ), wx.VERTICAL )

		self.m_panel20 = wx.Panel( sbSizer17.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel20.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel20, wx.ID_ANY, u"Username" ), wx.VERTICAL )

		self.m_textCtrl4 = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		sbSizer15.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel20.SetSizer( sbSizer15 )
		self.m_panel20.Layout()
		sbSizer15.Fit( self.m_panel20 )
		sbSizer17.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel21 = wx.Panel( sbSizer17.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21, wx.ID_ANY, u"Password" ), wx.VERTICAL )

		self.m_textCtrl5 = wx.TextCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		sbSizer16.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel21.SetSizer( sbSizer16 )
		self.m_panel21.Layout()
		sbSizer16.Fit( self.m_panel21 )
		sbSizer17.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel23.SetSizer( sbSizer17 )
		self.m_panel23.Layout()
		sbSizer17.Fit( self.m_panel23 )
		bSizer17.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button10 = wx.Button( self.m_panel24, wx.ID_OK, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		gSizer7.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button11 = wx.Button( self.m_panel24, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		gSizer7.Add( self.m_button11, 0, wx.ALL, 5 )


		self.m_panel24.SetSizer( gSizer7 )
		self.m_panel24.Layout()
		gSizer7.Fit( self.m_panel24 )
		bSizer17.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )

#		bSizer21 = wx.BoxSizer( wx.VERTICAL )

#		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Remember Me", wx.DefaultPosition, wx.DefaultSize, 0 )
#		bSizer21.Add( self.m_checkBox1, 0, wx.ALL, 5 )


#		bSizer17.Add( bSizer21, 1, wx.EXPAND, 5 )

		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )


#設定情報（json）読み込み
#文字コードをUTF-8に変換しないとエラーが発生するため注意！！
		with codecs.open('setting.json','r',encoding='utf-8') as f:
#「JSONDecodeError: Invalid control character at」が返さないようにする。
#strictがfalse（デフォルトはTrue）の場合、制御文字を文字列に含めることができます。
#ここで言う制御文字とは、'\t'（タブ）、'\n'、'\r'、'\0'を含む0-31の範囲のコードを持つ文字のことです。
		    j = json.load(f,strict=False)
#            print(j)
		    f.close()
		    if j['remember'] == True:
		      self.m_textCtrl4.SetValue(j['user'])
		      self.m_textCtrl5.SetValue(j['password'])


	def GetUser(self):
		return self.m_textCtrl4.GetValue()

	def GetPasswd(self):
		return self.m_textCtrl5.GetValue()
    

class MyApp(wx.App):
    def OnInit(self):
#        self.frm = wx.Frame(None, -1, 'Main Window')

        login = MyProject1MyDialog2(None)
        loggedIn = False
        while not loggedIn:
            dlg = login.ShowModal()
            if dlg == wx.ID_OK:
                uname = login.GetUser()
                passwd = login.GetPasswd()
                adid = MyProject1MyDialog3(None)
                if (uname, passwd) == (adid.m_textCtrl4.GetValue(), adid.m_textCtrl5.GetValue()):
                    loggedIn = True
                else:
                  wx.MessageBox(u'Please enter the correct account information!!'
                                , u'Login error', wx.ICON_ERROR)
                    
            elif dlg == wx.ID_CANCEL:
                self.Destroy()
                return False

#        self.frm.Show()

#ログインに成功した後の画面遷移
        frame = MyProject1MyFrame2(None)
        frame.Show(True)
        return True


if __name__ == '__main__':
     app = MyApp(False)
     app.MainLoop()
 
#if __name__ == '__main__':
#    app = wx.App(False)
#    frame = MyProject1MyFrame2(None)
#    frame.Show(True)
#    app.MainLoop()