# Windows Desktop app version
**[Bad news!!] The system was rendered unusable by a malicious party, so development will end at the end of the year...**

# Change log

### 5.2.4
- **We have taken measures such as displaying a message when the following error occurs after pressing the "Posting" button.**

```shell
Traceback (most recent call last):
File "form_post_rev14.py", line 73, in inquiry_post
AttributeError: 'int' object has no attribute 'GetValue'
```

- **After pressing the "Posting" button, a confirmation message will now be displayed to confirm that the settings are correct.**

### 5.2.2
- **Compatible with Chrome driver version 115 or later.**

```shell
> pip install -U webdriver-manager
Requirement already satisfied: webdriver-manager in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (3.8.3)
Collecting webdriver-manager
  Downloading webdriver_manager-4.0.0-py2.py3-none-any.whl (27 kB)
Requirement already satisfied: python-dotenv in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from webdriver-manager) (0.20.0)
Requirement already satisfied: requests in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from webdriver-manager) (2.26.0)
Requirement already satisfied: packaging in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from webdriver-manager) (21.3)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from packaging->webdriver-manager) (2.4.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from requests->webdriver-manager) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from requests->webdriver-manager) (3.2)       
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from requests->webdriver-manager) (1.26.4)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\****\appdata\local\programs\python\python39\lib\site-packages (from requests->webdriver-manager) (2022.12.7)
Installing collected packages: webdriver-manager
  Attempting uninstall: webdriver-manager
    Found existing installation: webdriver-manager 3.8.3
    Uninstalling webdriver-manager-3.8.3:
      Successfully uninstalled webdriver-manager-3.8.3
Successfully installed webdriver-manager-4.0.0
```

# Other points to note

- **Only older versions of Python Selenium (3.141.0) are supported.**

- **Google account is required to use Google Spreadsheets.**

- **Please set up the private key generation etc. on "Google Cloud Platform".**

- **If you import the library with the latest version of pandas, an error will occur in matplotlib, so be sure to downgrade to "1.2.4" before using pandas!!**
**[ImportError: matplotlib is required for plotting when the default backend "matplotlib" is selected #5994](https://github.com/pyinstaller/pyinstaller/issues/5994#issuecomment-877765057)**

- **・PyInstaller uses version 4.1.0.**
**Don't upgrade to the latest version!!**
**[pyinstaller · PyPI](https://pypi.org/project/pyinstaller/4.10/)**

**Cause:**
**1.Because the size of the executable file becomes large**
**2.When trying to display the graph, it will be "UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure."**

- **・wxPython uses version 4.1.1(No update required:pip install -U wxPython)**

**Cause:**
**1."UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: encoding error"**
**2.Repeated processing is not possible. (ends only once)**
 
- **Other error handling**
**"Grid.SetCellValue(): arguments did not match any overloaded call:"**
**The cells used in the spreadsheet don't have any values filled in and need to be populated with data. (A hyphen is also acceptable)**
