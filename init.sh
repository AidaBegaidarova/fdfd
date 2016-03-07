sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/django.py /etc/gunicorn.d/django.py
sudo ln -s /home/box/web/etc/test /etc/nginx/sites-available/test
sudo ln -s /home/box/web/etc/test /etc/nginx/sites-enabled/test
sudo rm -f /etc/nginx/sites-enabled/default
sudo /etc/init.d/mysql restart
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/nginx restart
sudo git config --global user.email "atlantis.blackdragon@gmail.com"                              
sudo git config --global user.name "AbiGeuS2"
