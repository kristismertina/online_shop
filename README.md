# project
# Prerequisites
- **Python 3.10+ (x64).**
- **Django 4.1+.**
- **Pillow 9.4+.**
- Please check your python version with the following command. The result should be 3.10 or higher.

python3 --version
Django and Pillow can be installed via pip.

pip3 install -r requirements.txt
# Run
**From folder mysite**
- **python manage.py runserver**

# Run Dockerfile
- **"docker build -t users . "**
- **"docker mysite/online_shop:users"**
- **""docker run -d -p 8000:8000 mysite/online_shop:users"**
- **"docker stop {container id}"**
