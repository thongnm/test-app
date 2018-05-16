# ssh to server 
# go to home folder (/home/ubuntu)
cd ~
# install libs
sudo apt-get install libpq-dev python-dev -y
# clone source code from git, update your [username] and [password] to access git
sudo rm -r -f test-app
git clone -b master https://github.com/thongnm/test-app.git

pkill -f "gunicorn"
# start server
cd test-app
sudo sh start.sh
 
