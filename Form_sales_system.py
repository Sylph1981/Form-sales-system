# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:14:04 2021

@author: iorin
"""

import wx
#import app
from form_post_rev15 import MyProject1MyFrame2
from MyProject1MyDialog3 import MyProject1MyDialog3
from MyProject1MyDialog2 import MyProject1MyDialog2
from MyProject1MyDialog12 import MyProject1MyDialog12
from datetime import datetime
# import datetime
# from dateutil.relativedelta import relativedelta
today = datetime.now()
# dt1 = datetime.datetime.now()

# 一定期間が過ぎたら使用できなくするコードの作成
# https://qiita.com/pRaKuDam/items/1be8ce5f2428b95c5636

# Pythonで1年後や１カ月後を計算するには？
# https://xn--eckl3qmbc2cv902cnwa746d81h183l.com/instructor-blog/211103how-to-calculate-one-year-or-one-month-later-in-python/

# Implementing MyDialog2
#class MyProject1MyDialog2( wx.Dialog ):
#	def __init__( self, parent ):
    
class MyApp(wx.App):
    def OnInit(self):
#        self.frm = wx.Frame(None, -1, 'Main Window')
        start = str("2023-08-11")
        start = datetime.strptime(start, '%Y-%m-%d')
        limitdate = str("2023-11-16")
        limitdate = datetime.strptime(limitdate, '%Y-%m-%d')
        # limitdate = datetime.date.today() + relativedelta(years=1)
        # limitdate = dt1 + datetime.timedelta(hours=2)
        print("Expiration date:" + str(limitdate))
        # print(datetime.date.today())
        try:
          login = MyProject1MyDialog2(None)
          loggedIn = False
        
          while not loggedIn:
            dlg = login.ShowModal()

# 試用期間中
            if dlg == wx.ID_OK \
              and start >= today:
              uname = login.GetUser()
              passwd = login.GetPasswd()
              adid = MyProject1MyDialog3(None)
              if (uname, passwd) == (adid.m_textCtrl4.GetValue(), adid.m_textCtrl5.GetValue()):
                loggedIn = True
                wx.MessageBox(u'The paid period will start on' +
                ' ' + str(start),
                u'Infomation', wx.ICON_INFORMATION)
              else:
                wx.MessageBox(u'Please enter the correct account information!!'
                                , u'Login error', wx.ICON_ERROR)

# 有効期限切れ
            elif dlg == wx.ID_OK \
              and limitdate <= today:
              wx.MessageBox(u'This application has expired and cannot be used!!',
              u'Authentication error', wx.ICON_ERROR)
              self.Destroy()
              return False
            elif dlg == wx.ID_CANCEL:
              self.Destroy()
              return False

# 使用期間経過後～有効期限まで            
            elif dlg == wx.ID_OK \
              and limitdate >= start:
              uname = login.GetUser()
              passwd = login.GetPasswd()
              adid = MyProject1MyDialog3(None)
              if (uname, passwd) == (adid.m_textCtrl4.GetValue(), adid.m_textCtrl5.GetValue()):
                loggedIn = True
                wx.MessageBox(u'The expiration date is' +
                ' ' + str(limitdate),
                u'Infomation', wx.ICON_INFORMATION)
              else:
                wx.MessageBox(u'Please enter the correct account information!!'
                                , u'Login error', wx.ICON_ERROR)

        except Exception as e:
          wx.MessageBox(
            f'{e}', u'Startup error', wx.ICON_ERROR
            )
          return False
          
#        self.frm.Show()

#ログインに成功した後の画面遷移
        frame = MyProject1MyFrame2(None)
        frame.Show(True)
        dialog = MyProject1MyDialog12(None)
        dialog.Show(True)
        return True


if __name__ == '__main__':
     app = MyApp(False)
     app.MainLoop()
 
#if __name__ == '__main__':
#    app = wx.App(False)
#    frame = MyProject1MyFrame2(None)
#    frame.Show(True)
#    app.Ma