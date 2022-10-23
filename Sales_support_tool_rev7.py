# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:14:04 2021

@author: iorin
"""

import wx
#import app
from form_post_rev11 import MyProject1MyFrame2
from MyProject1MyDialog3 import MyProject1MyDialog3
from MyProject1MyDialog2 import MyProject1MyDialog2

# Implementing MyDialog2
#class MyProject1MyDialog2( wx.Dialog ):
#	def __init__( self, parent ):
    
class MyApp(wx.App):
    def OnInit(self):
#        self.frm = wx.Frame(None, -1, 'Main Window')
        try:
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

        except:
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