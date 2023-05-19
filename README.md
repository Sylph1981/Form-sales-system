# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.2 LTS"

# Attention
Before installing MySQL (version 8.0), you need to uninstall the mysql dependency package and remove the mysql deployment file.
* If you do not follow this order, socket errors and apt-get dependencies will not be resolved! !

# MySQL installation failure example
dpkg: dependency problems prevent configuration of mysql-server:
 mysql-server depends on mysql-server-8.0; however:
  Package mysql-server-8.0 is not configured yet.

dpkg: error processing package mysql-server (--configure):
 dependency problems - leaving unconfigured
Processing triggers for man-db (2.10.2-1) ...
No apport report written because the error message indicates its a followup error from a previous failure.

Warning: Unable to start the server.
Job for mysql.service failed because the control process exited with error code.
See "systemctl status mysql.service" and "journalctl -xeu mysql.service" for details.
invoke-rc.d: initscript mysql, action "start" failed.
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: activating (auto-restart) (Result: exit-code) since Sun 2023-05-07 23:17:47 JST; 12ms ago
    Process: 6421 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCESS)
    Process: 6429 ExecStart=/usr/sbin/mysqld (code=exited, status=1/FAILURE)
   Main PID: 6429 (code=exited, status=1/FAILURE)
     Status: "Server shutdown complete"
      Error: 22 (Invalid argument)
        CPU: 663ms

Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)

The following packages are only half configured, probably due to problems
configuring them the first time.  The configuration should be retried using
dpkg --configure <package> or the configure menu option in dselect:
 mysql-server-8.0     MySQL database server binaries and system database setup

dpkg: error processing package mysql-server-8.0 (--configure):
 installed mysql-server-8.0 package post-installation script subprocess returned error exit status 1
dpkg: dependency problems prevent configuration of mysql-server:
 mysql-server depends on mysql-server-8.0; however:
  Package mysql-server-8.0 is not configured yet.

needrestart is being skipped since dpkg has failed

Cannot create redo log files because data files are corrupt or the database was not shut down cleanly after creating the data files.

# [Sakura VPS] API for obtaining server status and operating power

# Get server information list
PS C:\Users\*****> curl.exe -X GET 'https://secure.sakura.ad.jp/vps/api/v7/servers' -H 'Authorization: Bearer {API key}'

# Get sever power state
PS C:\Users\*****> curl.exe -X GET 'https://secure.sakura.ad.jp/vps/api/v7/servers/{sever_id}/power_status' -H 'Authorization: Bearer {API key}'

# Start the sever
PS C:\Users\*****> curl.exe -X POST 'https://secure.sakura.ad.jp/vps/api/v7/servers/{sever_id}/power_on' -H 'Authorization: Bearer {API key}'

# Don't forget to start Gunicorn (application server)!!
$ sudo systemctl start formsales.socket
$ sudo systemctl start formsales.service
$ sudo systemctl status formsales
formsales.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/formsales.service; disab>
     Active: active (running) since Wed 2023-05-10 00:32:47 JST; >
TriggeredBy: ● formsales.socket
   Main PID: 25290 (gunicorn)
      Tasks: 4 (limit: 1026)
     Memory: 97.3M
        CPU: 6.105s
     CGroup: /system.slice/formsales.service
             ├─25290 /var/www/winbridge.biz/html/djangovenv/bin/p>
             ├─25337 /var/www/winbridge.biz/html/djangovenv/bin/p>
             ├─25345 /var/www/winbridge.biz/html/djangovenv/bin/p>
             └─25346 /var/www/winbridge.biz/html/djangovenv/bin/p>

May 10 00:33:28 os3-365-15569 gunicorn[25311]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25290]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25290]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25309]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25310]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25337]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25345]: [2023-05-10 00:33:>
May 10 00:33:29 os3-365-15569 gunicorn[25346]: [2023-05-10 00:33:>
May 10 00:34:47 os3-365-15569 systemd[1]: /etc/systemd/system/for>
lines 1-23

* If you forget it, you will get an error "502 bad gateway"!!

 
# System to automatically send emails from the inquiry form.

**・Only older versions of Python Selenium (3.141.0) are supported.**

**・Google account is required to use Google Spreadsheets.**

**・Please set up the private key generation etc. on "Google Cloud Platform".**

**・If you import the library with the latest version of pandas, an error will occur in matplotlib, so be sure to downgrade to "1.2.4" before using pandas!!**
*https://github.com/pyinstaller/pyinstaller/issues/5994#issuecomment-877765057*

# **・PyInstaller uses version 4.1.0.**
**Don't upgrade to the latest version!!**
*https://pypi.org/project/pyinstaller/4.10/*

**Cause:**
**1.Because the size of the executable file becomes large**
**2.When trying to display the graph, it will be "UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure."**

# **・wxPython uses version 4.1.1(No update required:pip install -U wxPython)**

**Cause:**
**1."UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: encoding error"**
**2.Repeated processing is not possible. (ends only once)**
 
# **・Other error handling**
**"Grid.SetCellValue(): arguments did not match any overloaded call:"**
**The cells used in the spreadsheet don't have any values filled in and need to be populated with data. (A hyphen is also acceptable)**

 
*Unauthorized reproduction of this code is strictly prohibited!!*
