The steps for running the Lite Twitter:
(I am using Mac for implementation this project, the installation of the apps are based on Mac's command. However, the processes are very similiar for a PC)

1. Go to https://www.python.org/downloads/ to download Python (I am using Python3.8.2 64-bit)
2. Go to https://code.visualstudio.com/Download to download Visual Studio Code (Herein after VSC)
3. After installed VSC, open the file folder that you downloaded
4. Go to View menu of VSC to choose Terminal

In the terminal: (Setup environment)
5. Ensure python version: which python3
6. Create virtual environment: type python3 -m venv venv
7. Click the lower left VSC to choose the corresponding python version with venv that you just created
8. Activate virtual environment: source venv/bin/activate
9. Install Linter pylint: pip install pylint
10. Install Flask: pip install Flask
11. Install mysql-client: pip install mysql-client
12. Install mysql for flask: pip install flask-mysql
13. Install mysqldb for Flask: pip install flask-mysqldb
14. Install pymysql for connection mysql for python: pip install pymysql
15. Install wtforms for validator input field: pip install flask-wtf

For running the app: (You can watch the demo on youtube: https://youtu.be/xBI3G0nzxEM)
16. Click the Run button on the very left of VSC, and choose Flask as the running environment

Notice:
For the line 13, 14, and 15 in the app.py, plese feel free to change to your mysql setting respectively. However, please MAKE SURE keep the SAME of the line 16 of the database name. Otherwise, the app will not run correctly.