# About Django admin screen
## Error "django.db.utils.OperationalError: (1054, "Unknown column 'hello_user.date_joined' in 'field list'")." when trying to edit a Users model.

**Solved by adding a field when defining a custom user.**

```python
class User(AbstractBaseUser, PermissionsMixin):
    from .py_app import Choices
    Industry_Choices = Choices.Industry_Choices
    Prefecture_Choices = Choices.Prefecture_Choices
    Prefcode_Choices = Choices.Prefcode_Choices
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField("姓名", max_length=15, blank=True)
    last_name = models.CharField("名前", max_length=15, blank=True)
    # gendar = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, blank=True)
    firstname_hira = models.CharField("姓名ひらがな", max_length=15, blank=True)
    lastname_hira = models.CharField("名前ひらがな", max_length=15, blank=True)
    firstname_kata = models.CharField("姓名カタカナ", max_length=15, blank=True)
    lastname_kata = models.CharField("名前カタカナ", max_length=15, blank=True)
    companyname = models.CharField("会社名", max_length=30, blank=True)
    company_hira = models.CharField("会社名ひらがな", max_length=30, blank=True)
    company_kata = models.CharField("会社名カタカナ", max_length=30, blank=True)
    industry = models.CharField("業種", max_length=30, choices = Industry_Choices, blank=True)
    bussiness_content = models.CharField("事業内容", max_length=30, blank=True)
    department = models.CharField("部署", max_length=15, blank=True)
    position = models.CharField("役職", max_length=15, blank=True)
    postal_code_1 = models.CharField("〒（地域番号）", max_length=3, blank=True, null=True)
    postal_code_2 = models.CharField("〒（局番号）", max_length=4, blank=True, null=True)
    prefecture = models.CharField("都道府県", max_length=15, choices=Prefecture_Choices, blank=True)
    pref_code = models.IntegerField("都道府県番号", blank=True, null=True)
    municipality = models.CharField("市区町村", max_length=30, blank=True)
    street_name = models.CharField("番地名", max_length=15, blank=True)
    build = models.CharField("建物名", max_length=30, blank=True)
    account = models.CharField("メールアカウント", max_length=100, blank=True)
    domain = models.CharField("ドメイン", max_length=100, blank=True)
    phone_1 = models.CharField("市外局番", max_length=3, blank=True, null=True)
    phone_2 = models.CharField("市内局番", max_length=4, blank=True, null=True)
    phone_3 = models.CharField("加入者番号", max_length=4, blank=True, null=True)
    url = models.URLField("ホームページ", max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

# Add here
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    icon = models.ImageField(blank=True, null=True)  
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 

    objects = UserManager()
   
    def get_absolute_url(self):
        return reverse_lazy('accounts:home')
```
```sql
mysql> show columns from hello_user;
+-------------------+--------------+------+-----+---------+----------------+
| Field             | Type         | Null | Key | Default | Extra          |
+-------------------+--------------+------+-----+---------+----------------+
| id                | bigint       | NO   | PRI | NULL    | auto_increment |
| password          | varchar(128) | YES  |     | NULL    |                |
| is_superuser      | int          | YES  |     | NULL    |                |
| username          | varchar(50)  | YES  |     | NULL    |                |
| email             | varchar(50)  | YES  |     | NULL    |                |
| is_active         | int          | YES  |     | NULL    |                |
| is_staff          | int          | YES  |     | NULL    |                |
| icon              | varchar(50)  | YES  |     | NULL    |                |
| account           | varchar(50)  | YES  |     | NULL    |                |
| build             | varchar(50)  | YES  |     | NULL    |                |
| bussiness_content | varchar(50)  | YES  |     | NULL    |                |
| company_hira      | varchar(50)  | YES  |     | NULL    |                |
| company_kata      | varchar(50)  | YES  |     | NULL    |                |
| companyname       | varchar(50)  | YES  |     | NULL    |                |
| department        | varchar(50)  | YES  |     | NULL    |                |
| domain            | varchar(50)  | YES  |     | NULL    |                |
| firstname_hira    | varchar(50)  | YES  |     | NULL    |                |
| firstname_kata    | varchar(50)  | YES  |     | NULL    |                |
| industry          | varchar(50)  | YES  |     | NULL    |                |
| lastname_hira     | varchar(50)  | YES  |     | NULL    |                |
| lastname_kata     | varchar(50)  | YES  |     | NULL    |                |
| municipality      | varchar(50)  | YES  |     | NULL    |                |
| phone_1           | varchar(3)   | YES  |     | NULL    |                |
| phone_2           | varchar(4)   | YES  |     | NULL    |                |
| phone_3           | varchar(4)   | YES  |     | NULL    |                |
| position          | varchar(50)  | YES  |     | NULL    |                |
| postal_code_1     | varchar(3)   | YES  |     | NULL    |                |
| pref_code         | int          | YES  |     | NULL    |                |
| prefecture        | varchar(50)  | YES  |     | NULL    |                |
| street_name       | varchar(50)  | YES  |     | NULL    |                |
| first_name        | varchar(50)  | YES  |     | NULL    |                |
| last_name         | varchar(50)  | YES  |     | NULL    |                |
| url               | varchar(50)  | YES  |     | NULL    |                |
| postal_code_2     | varchar(4)   | YES  |     | NULL    |                |
| last_login        | datetime     | YES  |     | NULL    |                |
| date_joined       | datetime     | YES  |     | NULL    |                |
+-------------------+--------------+------+-----+---------+----------------+
36 rows in set (0.00 sec)
```
### Since the error is still displayed, add the missing table.
```bash
1146, "Table 'test_db.hello_user_groups' doesn't exist"
```
```sql
mysql> create table test_db.hello_user_groups(id bigint auto_increment not null primary key);
Query OK, 0 rows affected (4.28 sec)
```
```bash
Unknown column 'hello_user_groups.user_id' in 'where clause'
```
```bash
Unknown column 'hello_user_groups.group_id' in 'on clause'
```
```sql
mysql> show columns from test_db.hello_user_groups;
+----------+--------+------+-----+---------+----------------+
| Field    | Type   | Null | Key | Default | Extra          |
+----------+--------+------+-----+---------+----------------+
| id       | bigint | NO   | PRI | NULL    | auto_increment |
| user_id  | bigint | NO   |     | NULL    |                |
| group_id | bigint | NO   |     | NULL    |                |
+----------+--------+------+-----+---------+----------------+
3 rows in set (0.30 sec)
```
```sql
mysql> create table test_db.hello_user_user_permissions(id bigint auto_increment not null primary key);
Query OK, 0 rows affected (3.14 sec)

mysql> show columns from test_db.hello_user_user_permissions;
+---------------+--------+------+-----+---------+----------------+
| Field         | Type   | Null | Key | Default | Extra          |
+---------------+--------+------+-----+---------+----------------+
| id            | bigint | NO   | PRI | NULL    | auto_increment |
| user_id       | bigint | NO   |     | NULL    |                |
| permission_id | bigint | NO   |     | NULL    |                |
+---------------+--------+------+-----+---------+----------------+
3 rows in set (0.02 sec)
```
## For your reference
**[【Django】カスタムユーザー（独自のユーザー）の作り方【AbstractBaseUser編】](https://daeudaeu.com/django-abstractbaseuser/)**

# Precautions when installing MySQL
*Before installing MySQL (version 8.0), you need to uninstall the mysql dependency package and remove the mysql deployment file.*
*If you do not follow this order, socket errors and apt-get dependencies will not be resolved!!*

<details>
<summary>cat /etc/lsb-release</summary>

```bash
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.2 LTS"
```
</details>

# MySQL installation failure example

```shell
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
```

# If then Failed to start MySQL Community Server, check the error log (var/log/mysql/error.log). 

```bash
[InnoDB] Multiple files found for the same tablespace ID
```
```bash
[InnoDB] Scanned file '/var/lib/mysql/test_db/hello_post_1.ibd' for tablespace formsales_db/accounts_post_1 cannot be opened because it is not in a sub-directory named for the schema.
```
```bash
Mysql2::Error: Tablespace is missing for table
```
 
## Permissions must be restored!!
```bash
[Warning] World-writable config file '/etc/my.cnf' is ignored.
```
```shell
chmod 644 /etc/my.cnf
```

## This statement cannot be used because it produces an error!!

**~~[RENAME TABLE](https://dev.mysql.com/doc/refman/8.0/ja/rename-table.html)~~**

```sql
ERROR 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 102
```
```sql
ERROR 2013 (HY000) at line : Lost connection to MySQL server during query
```

*I found a solution on this site, but it didn't work…*

**・[MySQLである程度大きいダンプファイルのインポートを行った際のERROR 2013 (HY000) at line : Lost connection to MySQL server during queryエラーの解決策](https://qiita.com/shy_azusa/items/9f6ba519cfda626db52b)**

**・[MySQL タイムアウトの値を取得する](https://mebee.info/2022/04/26/post-49850/)**
 
# Discard the table you want to replace.
```sql
mysql> use formsales_db;
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
Query OK, 0 rows affected (0.01 sec)
```

# Tell InnoDB to use the new .ibd file for the table.
```sql
mysql> ALTER TABLE formsales_db.accounts_user IMPORT TABLESPACE;
ERROR 1812 (HY000): Tablespace is missing for table 'formsales_db'.'accounts_user'.
```
## For your reference

 **・[mysql - InnoDB_ Tablespace is missing for table - Database Administrators Stack Exchange](https://dba.stackexchange.com/questions/56849/innodb-tablespace-is-missing-for-table)**

```shell
chmod 777 /var/lib/mysql/formsales_db/accounts_user.ibd
```
```mysql
mysql> ALTER TABLE formsales_db.accounts_user IMPORT TABLESPACE;
Query OK, 0 rows affected, 1 warning (0.11 sec)
mysql> CREATE TABLE test_db.hello_user SELECT * FROM formsales_db.accounts_user;
Query OK, 2 rows affected (0.12 sec)
Records: 2  Duplicates: 0  Warnings: 0
```
```sql
mysql> show tables;
+-------------------+
| Tables_in_test_db |
+-------------------+
| hello_user        |
+-------------------+
1 row in set (0.08 sec)
```
```sql
mysql> show columns from hello_user;
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| id                | int          | YES  |     | NULL    |       |
| password          | varchar(128) | YES  |     | NULL    |       |
| is_superuser      | int          | YES  |     | NULL    |       |
| username          | varchar(50)  | YES  |     | NULL    |       |
| email             | varchar(50)  | YES  |     | NULL    |       |
| last_login        | datetime     | YES  |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
35 rows in set (0.02 sec)
```
## For your reference

**・[新規作成したDBでテーブルをCREATEしようとした時に、エラーが出た場合の対処方法](https://tech.kurojica.com/archives/31631/)**
```shell
[InnoDB] Unable to import tablespace 'test_db'.'hello_user' because it already exists.  Please DISCARD the tablespace before IMPORT.
```
```bash
rm -v /var/lib/mysql/test_db/hello_user.ibd
removed '/var/lib/mysql/test_db/hello_user.ibd'
``` 
**・[【MySQL】ALTER TABLE を使って ibd ファイルを置き換える手順](https://www.hiskip.com/pg-notes/database/mysql/1130.html)**

# About implementing social authentication
```shell
pip install social-auth-app-django
```
## Why does it fail when I try to migrate?
```bash
Referencing column 'user_id' and referenced column 'id' in foreign key constraint 'social_auth_usersocialauth_user_id_17d28448_fk_hello_user_id' are incompatible.
```
### Cause: The data type does not match due to foreign key constraint settings.
```sql
mysql> show columns from social_auth_usersocialauth;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| provider   | varchar(32)  | NO   | MUL | NULL    |                |
| uid        | varchar(255) | NO   |     | NULL    |                |
| extra_data | longtext     | NO   |     | NULL    |                |
| user_id    | bigint       | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
5 rows in set (0.02 sec)
```
## By the way, even if you set the type again from the middle, the migration will not go well, so be careful!!
```bash
Internal Server Error: /social-auth/complete/google-oauth2/
Traceback (most recent call last):
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/db/backends/mysql/base.py", line 75, in execute
    return self.cursor.execute(query, args)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/MySQLdb/cursors.py", line 206, in execute
    res = self._query(query)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/MySQLdb/cursors.py", line 319, in _query
    db.query(q)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/MySQLdb/connections.py", line 254, in query
    _mysql.connection.query(self, query)
MySQLdb.OperationalError: (1054, "Unknown column 'social_auth_usersocialauth.created' in 'field list'")
```
*This method did not help!!*

**~~[Exception Value: (1054, "Unknown column 'social_auth_usersocialauth.created' in 'field list'")](https://stackoverflow.com/questions/63213190/exception-value-1054-unknown-column-social-auth-usersocialauth-created-in)~~**

### Migration solution (not recommended for begginers)
**・Delete the record that migrate returns.**
```sql
mysql> DELETE FROM test_db.django_migrations WHERE session_data LIKE 'social';
```
**・Delete the following files and migrate again.**
```bash
├── 0001_initial.py
├── 0002_add_related_name.py
├── 0003_alter_email_max_length.py
├── 0004_auto_20160423_0400.py
├── 0005_auto_20160727_2333.py
├── 0006_partial.py
├── 0007_code_timestamp.py
├── 0008_partial_timestamp.py
├── 0009_auto_20191118_0520.py
├── 0010_uid_db_index.py
├── 0011_alter_id_fields.py
├── __init__.py
└── __pycache__
1 directory, 25 files

python manage.py makemigrations social_django

python manage.py showmigrations social_django
 [X] 0001_initial

python manage.py migrate social_django
```
### An error message appears again, but there is no particular need to fix it.
```bash
Referencing column 'user_id' and referenced column 'id' in foreign key constraint 'social_auth_usersocialauth_user_id_17d28448_fk_hello_user_id' are incompatible.
```
```bash
python manage.py migrate social_django --fake
```
・Confirm that the issue of missing fields has been resolved
```sql
mysql> show columns from social_auth_usersocialauth;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | bigint       | NO   | PRI | NULL    | auto_increment |
| provider   | varchar(32)  | NO   | MUL | NULL    |                |
| uid        | varchar(255) | NO   |     | NULL    |                |
| extra_data | longtext     | NO   |     | NULL    |                |
| created    | datetime(6)  | NO   |     | NULL    |                |
| modified   | datetime(6)  | NO   |     | NULL    |                |
| user_id    | bigint       | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
7 rows in set (0.02 sec)

mysql> SELECT * FROM django_migrations;
+----+---------------+-----------------------------------------------------------+----------------------------+
| id | app           | name                                                      | applied                    |
+----+---------------+-----------------------------------------------------------+----------------------------+
| 15 | hello         | 0001_initial                                              | 2023-06-08 08:39:19.068324 |
| 18 | sessions      | 0001_initial                                              | 2023-06-08 08:39:19.083360 |
| 19 | admin         | 0001_initial                                              | 2023-06-08 09:49:14.447154 |
| 20 | admin         | 0002_logentry_remove_auto_add                             | 2023-06-08 09:49:14.475310 |
| 21 | admin         | 0003_logentry_add_action_flag_choices                     | 2023-06-08 09:49:14.479678 |
| 42 | hello         | 0002_send_preset_class_alter_post_date_time_and_more      | 2023-06-10 17:12:30.551351 |
| 43 | hello         | 0003_alter_post_date_time_alter_post_1_date_time_and_more | 2023-06-10 17:52:51.692500 |
| 49 | social_django | 0001_initial                                              | 2023-06-11 11:12:41.183683 |
+----+---------------+-----------------------------------------------------------+----------------------------+
```
### Error handling for social authentication login.
```bash
Traceback (most recent call last):
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/db/backends/mysql/base.py", line 75, in execute
    return self.cursor.execute(query, args)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/MySQLdb/cursors.py", line 206, in execute
    res = self._query(query)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/MySQLdb/cursors.py", line 319, in _query
    db.query(q)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/MySQLdb/connections.py", line 254, in query
    _mysql.connection.query(self, query)
MySQLdb.IntegrityError: (1364, "Field 'id' doesn't have a default value")
```
```bash
ValueError: The database backend does not accept 0 as a value for AutoField.
```
**・Since NULL is included after the 3rd row of the table column "id", give an appropriate definition.**
```sql
mysql> SELECT * FROM hello_user;
+------+----------------------------------------------------------------------------+--------------+---------------------------+-----------------------------+-----------+----------+-----------------------+---------------+-------+-------------------+--------------+--------------+--------------------------+--------------------------+---------------+----------------+----------------+-----------------------------------+---------------+---------------+--------------+---------+---------+---------+--------------------+---------------+-----------+------------+----------------------+------------+-----------+------+---------------+---------------------+
| id   | password                                                                   | is_superuser | username                  | email                       | is_active | is_staff | icon                  | account       | build | bussiness_content | company_hira | company_kata | companyname              | department               | domain        | firstname_hira | firstname_kata | industry                          | lastname_hira | lastname_kata | municipality | phone_1 | phone_2 | phone_3 | position           | postal_code_1 | pref_code | prefecture | street_name          | first_name | last_name | url  | postal_code_2 | last_login          |
+------+----------------------------------------------------------------------------+--------------+---------------------------+-----------------------------+-----------+----------+-----------------------+---------------+-------+-------------------+--------------+--------------+--------------------------+--------------------------+---------------+----------------+----------------+-----------------------------------+---------------+---------------+--------------+---------+---------+---------+--------------------+---------------+-----------+------------+----------------------+------------+-----------+------+---------------+---------------------+
|    1 | bcrypt_sha256$$2b$12$6aPS4T84uQL2soms.PuYGO/43srylCRDjeNpwBjQqybGPyrt/zM.2 |            1 | winbridge                 | account@domain.com |         1 |        1 | Sample_01_QwQWMGq.jpg | account |       | 人材紹介          |              |              | 株式会社○○○○             | マーケティング部         | account.com |                | オオタ         | スポーツ・フィットネス            |               | イオリ        | 新宿区       | 03      | 1234     | 5678    | マネージャー       | 160           |        12 | 東京都     | 西新宿○-○○-○       | 太田       |  伊織      |      | 0023           | 2023-06-11 10:04:06 |
|    2 | bcrypt_sha256$$2b$12$ftrkgb6ni9eOCAOATapx4OGO40HXqPnhu9AxqSePTmC6UpYFUrG4S |            0 | iorioota                  | otoiawase@domain.jp     |         1 |        0 |                       |               |       |                   |              |              |                          |                          |               |                |                |                                   |               |               |              | NULL    | NULL    | NULL    |                    | NULL          |      NULL |            |                      |            |           |      | NULL          | NULL                |
| NULL | !1ADVXqifgXy6iIqd8MF1XLjtG38kcJYfhnyCF7iI                                  |            0 | i12345678                 | i12345678@gmail.com         |         1 |        0 |                       |               |       |                   |              |              |                          |                          |               |                |                |                                   |               |               |              | NULL    | NULL    | NULL    |                    | NULL          |      NULL |            |                      |            |           |      | NULL          | NULL                |
| NULL | !gzKP4BFCzYxWY7tXoe555d3Mmf2sDa1JIgwGeRhg                                  |            0 | i123456783115954a7e1944df | i12345678@gmail.com         |         1 |        0 |                       |               |       |                   |              |              |                          |                          |               |                |                |                                   |               |               |              | NULL    | NULL    | NULL    |                    | NULL          |      NULL |            |                      |            |           |      | NULL          | NULL                |
| NULL | !Q7VXd9oEbu6jfMv89z4h0RH8blTACRdIgJTZq6ss                                  |            0 | i12345678336390e551334290 | i12345678@gmail.com         |         1 |        0 |                       |               |       |                   |              |              |                          |                          |               |                |                |                                   |               |               |              | NULL    | NULL    | NULL    |                    | NULL          |      NULL |            |                      |            |           |      | NULL          | NULL                |
| NULL | !6HauwQM1qhkzhoTXPczU1LeeSOftWrcCHk1wACib                                  |            0 | i123456785c257b0fee44496b | i12345678@gmail.com         |         1 |        0 |                       |               |       |                   |              |              |                          |                          |               |                |                |                                   |               |               |              | NULL    | NULL    | NULL    |                    | NULL          |      NULL |            |                      |            |           |      | NULL          | NULL                |
+------+----------------------------------------------------------------------------+--------------+---------------------------+-----------------------------+-----------+----------+-----------------------+---------------+-------+-------------------+--------------+--------------+--------------------------+--------------------------+---------------+----------------+----------------+-----------------------------------+---------------+---------------+--------------+---------+---------+---------+--------------------+---------------+-----------+------------+----------------------+------------+-----------+------+---------------+---------------------+
12 rows in set (0.06 sec)
```
**・Delete rows where table column 'id' is NULL.**
```sql
mysql> SELECT * FROM test_db.hello_user WHERE id is not null;
2 rows in set (0.07 sec)
```
**・Add "PRIMARY KEY" to "auto_increment" field.**
```sql
mysql> ALTER TABLE test_db.hello_user MODIFY id bigint NOT NULL AUTO_INCREMENT PRIMARY KEY;
Query OK, 2 rows affected (1.74 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> show columns from hello_user;
+-------------------+--------------+------+-----+---------+----------------+
| Field             | Type         | Null | Key | Default | Extra          |
+-------------------+--------------+------+-----+---------+----------------+
| id                | bigint       | NO   | PRI | NULL    | auto_increment |
| password          | varchar(128) | YES  |     | NULL    |                |
| is_superuser      | int          | YES  |     | NULL    |                |
| username          | varchar(50)  | YES  |     | NULL    |                |
| email             | varchar(50)  | YES  |     | NULL    |                |
| last_login        | datetime     | YES  |     | NULL    |                |
+-------------------+--------------+------+-----+---------+----------------+
35 rows in set (0.01 sec)
```

### How to resolve session errors
```bash
Traceback (most recent call last):
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/utils/deprecation.py", line 136, in __call__
    response = self.process_response(request, response)
  File "/usr/share/nginx/html/djangovenv/lib/python3.10/site-packages/django/contrib/sessions/middleware.py", line 61, in process_response
    raise SessionInterrupted(
django.contrib.sessions.exceptions.SessionInterrupted: The request's session was deleted before the request completed. The user may have logged out in a concurrent request, for example.
```
**・Declare session data to be cached in session engine without registering it in database.**
```python
INSTALLED_APPS = [
    'hello.apps.HelloConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # comment out
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
```

### For your reference

**・[【決定版】爆速でDjangoソーシャル認証を実装する(Google認証）](https://sinyblog.com/django/social-auth-app-django/)**

**・[Django のプロジェクトにおいて、 migrate した DB を元に戻す方法](https://gb-j.com/column/django-migrate/)**

**・[登録フォームでデータが登録できない　SQLSTATE[HY000]: General error: 1364 Field 'id' doesn't have a default value](https://teratail.com/questions/296888)**

**・[Fix MySQL ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key](https://www.tutorialspoint.com/fix-mysql-error-1075-42000-incorrect-table-definition-there-can-be-only-one-auto-column-and-it-must-be-defined-as-a-key)**

**・[djangoのキャッシュを使ったセッションの設定](https://torajirousan.hatenadiary.jp/entry/2020/12/27/005409)**

# Enabling SSL for Django Projects
```shell
vi /etc/nginx/sites-available/form_marketing.conf
```
```conf
server {
        # Override port number to 443.
		listen 443 ssl;
        server_name domain-name.jp;

        # Key file storage location required for SSL settings.
        ssl_certificate /etc/letsencrypt/live/domain-name.jp/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/domain-name.jp/privkey.pem;
...
}
```
```shell
systemctl restart nginx
```
**・Let's take measures against cross-site request forgery (CSRF) verification!!**
```py
ALLOWED_HOSTS = ['domain-name', '***.***.**.**', 'localhost', '127.0.0.1']

# add this
CSRF_TRUSTED_ORIGINS = ['https://domain-name']
```
# How to start Gunicorn without sockets (without systemd service file)
**1. Show systemd service file status.**
```shell
systemctl status formsales
● formsales.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/formsales.service; enabled; vendor preset: enabled)
     Active: active (exited) since Tue 2023-06-27 00:23:22 JST; 1min 6s ago
TriggeredBy: ● formsales.socket
    Process: 490 ExecStart=/usr/share/nginx/html/djangovenv/bin/gunicorn --config /usr/share/nginx/html/djang>
   Main PID: 490 (code=exited, status=0/SUCCESS)
      Tasks: 6 (limit: 1011)
     Memory: 184.5M
        CPU: 2.539s
     CGroup: /system.slice/formsales.service
             ├─593 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn>
             ├─594 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn>
             ├─595 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn>
             ├─596 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn>
             ├─597 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn>
             └─598 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn>
```
**2. Show all services at system startup.**
```shell             
systemctl list-unit-files -t service | grep formsales
formsales.service                          enabled         enabled
```
**3. Disable automatic startup of systemd service file.**
```shell
systemctl disable formsales
Removed /etc/systemd/system/multi-user.target.wants/formsales.service.
```
**4. Check autostart disable in systemd service file.**
```shell
systemctl list-unit-files -t service | grep formsales
formsales.service                          disabled         enabled
```
**5. Stop starting systemd service file.**
```shell
systemctl stop formsales
Warning: Stopping formsales.service, but it can still be activated by:
  formsales.socket
```
**6. Check systemd service file status.**
```shell
systemctl status formsales
○ formsales.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/formsales.service; disabled; vendor preset: enabled)
     Active: inactive (dead) since Tue 2023-06-27 01:17:38 JST; 56s ago
TriggeredBy: ● formsales.socket
   Main PID: 490 (code=exited, status=0/SUCCESS)
        CPU: 3.746s

Jun 27 00:23:22 os3-365-15569 systemd[1]: Started gunicorn daemon.
Jun 27 01:17:38 os3-365-15569 systemd[1]: Stopping gunicorn daemon...
Jun 27 01:17:38 os3-365-15569 systemd[1]: formsales.service: Deactivated successfully.
Jun 27 01:17:38 os3-365-15569 systemd[1]: Stopped gunicorn daemon.
Jun 27 01:17:38 os3-365-15569 systemd[1]: formsales.service: Consumed 3.746s CPU time.
```
**7. After switching to the virtual environment, move to the directory where "manage.py" is located and run gunicorn in daemon mode.**
```shell
gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
```
**8. Check if the gunicorn process is running.**
```shell
ps ax | grep gunicorn
   1047 ?        S      0:00 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
   1048 ?        S      0:00 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
   1049 ?        S      0:00 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
   1050 ?        S      0:00 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
   1051 ?        S      0:00 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
   1052 ?        S      0:00 /usr/share/nginx/html/djangovenv/bin/python3 /usr/share/nginx/html/djangovenv/bin/gunicorn --bind 127.0.0.1:8000 test_app.wsgi -D
   1055 pts/1    S+     0:00 grep --color=auto gunicorn
```
### For your reference
**・[DjangoプロジェクトのSSL化](https://view-s.co.jp/product/webapp/ssl/)**

**・[【AmazonLinux2でDjangoの本番環境構築】Python3.8,Nginx,Gunicorn,PostgreSQL](https://tomato-develop.com/amazon-linux-2-django-python-nginx-gunicorn-postgresql/)**

# [Sakura VPS] API for obtaining server status and operating power

### Get server information list
```shell
PS C:\Users\*****> curl.exe -X GET 'https://secure.sakura.ad.jp/vps/api/v7/servers' -H 'Authorization: Bearer {API key}'
```

### Get sever power state
```shell
PS C:\Users\*****> curl.exe -X GET 'https://secure.sakura.ad.jp/vps/api/v7/servers/{sever_id}/power_status' -H 'Authorization: Bearer {API key}'
```

### Start the sever
```shell
PS C:\Users\*****> curl.exe -X POST 'https://secure.sakura.ad.jp/vps/api/v7/servers/{sever_id}/power_on' -H 'Authorization: Bearer {API key}'
```

# [Sakura VPS] How to use public key authentication



# Windows Desktop app version
**[Bad news!!] The system was rendered unusable by a malicious party, so development will end at the end of the year...**

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
