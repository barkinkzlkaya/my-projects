#! /bin/bash
yum update -y
yum install python3 -y
pip3 install flask
yum install git -y
cd /home/ec2-user
wget -P templates https://raw.githubusercontent.com/barkinkzlkaya/my-projects/main/Python/flask-05-Handling-SQL-with-Flask-Web-Application/templates/add-email.html
wget -P templates https://raw.githubusercontent.com/barkinkzlkaya/my-projects/main/Python/flask-05-Handling-SQL-with-Flask-Web-Application/templates/emails.html
wget https://raw.githubusercontent.com/barkinkzlkaya/my-projects/main/Python/flask-05-Handling-SQL-with-Flask-Web-Application/app-with-mysql.py
python3 app.py
