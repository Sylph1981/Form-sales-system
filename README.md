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


# System to automatically send emails from the inquiry form.

About "form_post_rev12.py"

・Only older versions of Python Selenium (3.141.0) are supported.

・Google account is required to use Google Spreadsheets.

・Please set up the private key generation etc. on "Google Cloud Platform".

・If you import the library with the latest version of pandas, an error will occur in matplotlib, so be sure to downgrade to "1.2.4" before using pandas!!
https://github.com/pyinstaller/pyinstaller/issues/5994#issuecomment-877765057

・PyInstaller uses version 4.1.0.
Don't upgrade to the latest version!!
https://pypi.org/project/pyinstaller/4.10/

cause:
・Because the size of the executable file becomes large
・When trying to display the graph, it will be "UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure."


*Unauthorized reproduction of this code is strictly prohibited!!*
