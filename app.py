# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"CPU", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Memory", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"STOP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 100 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
		self.Bind( wx.EVT_TIMER, self.paint, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def m_button3OnButtonClick( self, event ):
		event.Skip()

	def m_button4OnButtonClick( self, event ):
		event.Skip()

	def paint( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"お問い合わせフォーム投稿アプリ update 3.0.1", pos = wx.DefaultPosition, size = wx.Size( 697,441 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu11 = wx.Menu()
		self.m_menuItem11 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Configuration", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem11 )

		self.m_menuItem12 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Profile", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem12 )

		self.m_menuItem13 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Send text creation", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem13 )

		self.m_menubar1.Append( self.m_menu11, u"Setting" )

		self.m_menu111 = wx.Menu()
		self.m_menuItem111 = wx.MenuItem( self.m_menu111, wx.ID_ANY, u"Create", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu111.Append( self.m_menuItem111 )

		self.m_menuItem211 = wx.MenuItem( self.m_menu111, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu111.Append( self.m_menuItem211 )

		self.m_menubar1.Append( self.m_menu111, u"List" )

		self.SetMenuBar( self.m_menubar1 )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainBox = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		bSizer19.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( bSizer19, 1, wx.EXPAND, 5 )


		self.main_panel.SetSizer( mainBox )
		self.main_panel.Layout()
		mainBox.Fit( self.main_panel )
		mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 873,573 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog
###########################################################################

class MyDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"リスト作成", pos = wx.DefaultPosition, size = wx.Size( 517,656 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainBox = wx.BoxSizer( wx.VERTICAL )

		hbox1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		hbox1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( hbox1, 1, wx.EXPAND, 5 )

		hbox4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		hbox4.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( hbox4, 1, wx.EXPAND, 5 )


		self.main_panel.SetSizer( mainBox )
		self.main_panel.Layout()
		mainBox.Fit( self.main_panel )
		mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,594 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"User Authentication", pos = wx.DefaultPosition, size = wx.Size( 417,319 ), style = wx.DEFAULT_DIALOG_STYLE )

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


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog3
###########################################################################

class MyDialog3 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting", pos = wx.DefaultPosition, size = wx.Size( 498,540 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog4
###########################################################################

class MyDialog4 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting of transmission contents", pos = wx.DefaultPosition, size = wx.Size( 853,464 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog5
###########################################################################

class MyDialog5 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Email body creation", pos = wx.DefaultPosition, size = wx.Size( 670,655 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


