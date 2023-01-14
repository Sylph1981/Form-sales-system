# private
System to automatically send emails from the inquiry form.


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