# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.2 LTS"

# Attention
Before installing MySQL (version 8.0), you need to uninstall the mysql dependency package and remove the mysql deployment file.
* If you do not follow this order, socket errors and apt-get dependencies will not be resolved! !

# MySQL installation failure example
`dpkg: dependency problems prevent configuration of mysql-server:`
` mysql-server depends on mysql-server-8.0; however:`
`  Package mysql-server-8.0 is not configured yet.`

`dpkg: error processing package mysql-server (--configure):`
` dependency problems - leaving unconfigured
Processing triggers for man-db (2.10.2-1) ...
No apport report written because the error message indicates its a followup error from a previous failure.`

`Warning: Unable to start the server.
Job for mysql.service failed because the control process exited with error code.
See "systemctl status mysql.service" and "journalctl -xeu mysql.service" for details.
invoke-rc.d: initscript mysql, action "start" failed.
● mysql.service - MySQL Community Server`
`     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)`
`     Active: activating (auto-restart) (Result: exit-code) since Sun 2023-05-07 23:17:47 JST; 12ms ago`
`    Process: 6421 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCESS)`
`    Process: 6429 ExecStart=/usr/sbin/mysqld (code=exited, status=1/FAILURE)`
`   Main PID: 6429 (code=exited, status=1/FAILURE)`
`     Status: "Server shutdown complete"`
`      Error: 22 (Invalid argument)`
`        CPU: 663ms`

`Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)`

`The following packages are only half configured, probably due to problems
configuring them the first time.  The configuration should be retried using
dpkg --configure <package> or the configure menu option in dselect:`
` mysql-server-8.0     MySQL database server binaries and system database setup`

`dpkg: error processing package mysql-server-8.0 (--configure):`
` installed mysql-server-8.0 package post-installation script subprocess returned error exit status 1
dpkg: dependency problems prevent configuration of mysql-server:`
` mysql-server depends on mysql-server-8.0; however:`
`  Package mysql-server-8.0 is not configured yet.`

`needrestart is being skipped since dpkg has failed`

`Cannot create redo log files because data files are corrupt or the database was not shut down cleanly after creating the data files.`

# If then Failed to start MySQL Community Server, check the error log (var/log/mysql/error.log). 
**・`[InnoDB] Multiple files found for the same tablespace ID`**
**・`[InnoDB] Scanned file '/var/lib/mysql/test_db/hello_post_1.ibd' for tablespace formsales_db/accounts_post_1 cannot be opened because it is not in a sub-directory named for the schema.`**
**・`Mysql2::Error: Tablespace is missing for table`**
 
*Permissions must be restored!!*
**`[Warning] World-writable config file '/etc/my.cnf' is ignored.`**
`chmod 644 /etc/my.cnf`
 
*This statement cannot be used because it produces an error!!*
**[RENAME TABLE](https://dev.mysql.com/doc/refman/8.0/ja/rename-table.html)**

**・`ERROR 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 102`**
**・`ERROR 2013 (HY000) at line : Lost connection to MySQL server during query`**

*I found a solution on this site, but it didn't work…*
**・[MySQLである程度大きいダンプファイルのインポートを行った際のERROR 2013 (HY000) at line : Lost connection to MySQL server during queryエラーの解決策](https://qiita.com/shy_azusa/items/9f6ba519cfda626db52b)**
**・[MySQL タイムアウトの値を取得する](https://mebee.info/2022/04/26/post-49850/)**
 
# Discard the table you want to replace.
`mysql> use formsales_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed
mysql> ALTER TABLE accounts_post DISCARD TABLESPACE;
Query OK, 0 rows affected (0.08 sec)
mysql> ALTER TABLE auth_group DISCARD TABLESPACE;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails ()
mysql> SET FOREIGN_KEY_CHECKS = 0;
Query OK, 0 rows affected (0.04 sec)
mysql> SET FOREIGN_KEY_CHECKS = 1;
Query OK, 0 rows affected (0.01 sec)`

# Tell InnoDB to use the new .ibd file for the table.
`mysql> ALTER TABLE formsales_db.accounts_user IMPORT TABLESPACE;
ERROR 1812 (HY000): Tablespace is missing for table 'formsales_db'.'accounts_user'.`
 **[mysql - InnoDB_ Tablespace is missing for table - Database Administrators Stack Exchange](https://dba.stackexchange.com/questions/56849/innodb-tablespace-is-missing-for-table)**
 
`chmod 777 /var/lib/mysql/formsales_db/accounts_user.ibd
mysql> ALTER TABLE formsales_db.accounts_user IMPORT TABLESPACE;
Query OK, 0 rows affected, 1 warning (0.11 sec)
mysql> CREATE TABLE test_db.hello_user SELECT * FROM formsales_db.accounts_user;
Query OK, 2 rows affected (0.12 sec)
Records: 2  Duplicates: 0  Warnings: 0`

`mysql> show tables;
+-------------------+
| Tables_in_test_db |
+-------------------+
| hello_user        |
+-------------------+
1 row in set (0.08 sec)`

`mysql> show columns from hello_user;
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| id                | int          | YES  |     | NULL    |       |
| password          | varchar(128) | YES  |     | NULL    |       |
| is_superuser      | int          | YES  |     | NULL    |       |
| username          | varchar(50)  | YES  |     | NULL    |       |
| email             | varchar(50)  | YES  |     | NULL    |       |
| is_active         | int          | YES  |     | NULL    |       |
| is_staff          | int          | YES  |     | NULL    |       |
| icon              | varchar(50)  | YES  |     | NULL    |       |
| account           | varchar(50)  | YES  |     | NULL    |       |
| build             | varchar(50)  | YES  |     | NULL    |       |
| bussiness_content | varchar(50)  | YES  |     | NULL    |       |
| company_hira      | varchar(50)  | YES  |     | NULL    |       |
| company_kata      | varchar(50)  | YES  |     | NULL    |       |
| companyname       | varchar(50)  | YES  |     | NULL    |       |
| department        | varchar(50)  | YES  |     | NULL    |       |
| domain            | varchar(50)  | YES  |     | NULL    |       |
| firstname_hira    | varchar(50)  | YES  |     | NULL    |       |
| firstname_kata    | varchar(50)  | YES  |     | NULL    |       |
| industry          | varchar(50)  | YES  |     | NULL    |       |
| lastname_hira     | varchar(50)  | YES  |     | NULL    |       |
| lastname_kata     | varchar(50)  | YES  |     | NULL    |       |
| municipality      | varchar(50)  | YES  |     | NULL    |       |
| phone_1           | varchar(3)   | YES  |     | NULL    |       |
| phone_2           | varchar(4)   | YES  |     | NULL    |       |
| phone_3           | varchar(4)   | YES  |     | NULL    |       |
| position          | varchar(50)  | YES  |     | NULL    |       |
| postal_code_1     | varchar(3)   | YES  |     | NULL    |       |
| pref_code         | int          | YES  |     | NULL    |       |
| prefecture        | varchar(50)  | YES  |     | NULL    |       |
| street_name       | varchar(50)  | YES  |     | NULL    |       |
| first_name        | varchar(50)  | YES  |     | NULL    |       |
| last_name         | varchar(50)  | YES  |     | NULL    |       |
| url               | varchar(50)  | YES  |     | NULL    |       |
| postal_code_2     | varchar(4)   | YES  |     | NULL    |       |
| last_login        | datetime     | YES  |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
35 rows in set (0.02 sec)`

**For your reference**
**・[新規作成したDBでテーブルをCREATEしようとした時に、エラーが出た場合の対処方法](https://tech.kurojica.com/archives/31631/)**
**`[InnoDB] Unable to import tablespace 'test_db'.'hello_user' because it already exists.  Please DISCARD the tablespace before IMPORT.`**
`# rm -v /var/lib/mysql/test_db/hello_user.ibd`
`removed '/var/lib/mysql/test_db/hello_user.ibd'`
 
**・[【MySQL】ALTER TABLE を使って ibd ファイルを置き換える手順](https://www.hiskip.com/pg-notes/database/mysql/1130.html)**

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
