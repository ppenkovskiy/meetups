Project "MEETUPS" preview:
https://drive.google.com/file/d/1Dknxil2GpMMrL_dW99R-gmgn1dlchI_M/view?usp=sharing

Installing "Bookstore" project on Linux:

git clone git@github.com:ppenkovskiy/meetups_app.git

cd meetups_app

sudo apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver
