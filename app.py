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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"営業支援ツール", pos = wx.DefaultPosition, size = wx.Size( 476,657 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainBox = wx.BoxSizer( wx.VERTICAL )

		hbox4 = wx.BoxSizer( wx.VERTICAL )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn1 = wx.Button( self.main_panel, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		gSizer11.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.Button( self.main_panel, wx.ID_ANY, u"Exit", wx.Point( 1,-1 ), wx.DefaultSize, 0 )
		self.btn2.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		gSizer11.Add( self.btn2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		hbox4.Add( gSizer11, 1, wx.EXPAND, 5 )

		self.m_panel16 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel16.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		hbox4.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( hbox4, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		bSizer19.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( bSizer19, 1, wx.EXPAND, 5 )

		hbox5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		hbox5.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( hbox5, 1, wx.EXPAND, 5 )


		self.main_panel.SetSizer( mainBox )
		self.main_panel.Layout()
		mainBox.Fit( self.main_panel )
		mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.create_button )
		self.btn2.Bind( wx.EVT_BUTTON, self.quit_button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def create_button( self, event ):
		event.Skip()

	def quit_button( self, event ):
		event.Skip()


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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"リスト作成", pos = wx.DefaultPosition, size = wx.Size( 613,687 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainBox = wx.BoxSizer( wx.VERTICAL )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel22 = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel22.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		bSizer30.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )


		mainBox.Add( bSizer30, 1, wx.EXPAND, 5 )

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

		self.dbtn1 = wx.Button( self.main_panel, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dbtn1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Meiryo UI" ) )

		mainBox.Add( self.dbtn1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.main_panel.SetSizer( mainBox )
		self.main_panel.Layout()
		mainBox.Fit( self.main_panel )
		mainSizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.dbtn1.Bind( wx.EVT_BUTTON, self.quit_button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def quit_button( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


