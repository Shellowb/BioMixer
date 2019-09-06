<yt-formatted-string class="content style-scope ytd-video-secondary-info-renderer" force-default-style="" split-lines="">- transforma tu raspberry pi en un servidor web !
En el vídeo de hoy les enseñamos a montar vuestro propio servidor web que funcione desde una raspberry pi. Pondremos la IP de nuestra RPI estática para nuestro router y haremos uso de apache + php + mysql para generar una pila lamp. Esto nos servirá para, en un futuro, montarte tu propia web y que esté alojada desde tu propia máquina para así tener un control total de ella. Para poder seguir aprendiendo y complementando lo aprendido en este tutorial, lo aconsejable una vez realices esto sería, instalar también phpmyadmin y otras herramientas según vuestras necesidades, que reduzcan las limitaciones de nuestro servidor apache. 
Lista de comandos utilidazos:

sudo nano /etc/network/interfaces

auto eth0
iface eth0 inet static
address 192.168.0.2
netmask 255.255.255.0
gateway 192.168.0.1

ifconfig
route

sudo groupadd www-data
sudo usermod -a -G www-data www-data

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install apache2

sudo apt-get install php5

sudo apt-get install libapache2-mod-php5 libapache2-mod-perl2 php5 php5-cli php5-common php5-curl php5-dev php5-gd php5-imap php5-ldap php5-mhash php5-mysql php5-odbc

sudo reboot

sudo nano /var/www/info.php

(menorque)?php phpinfo(); ?(mayorque)

sudo apt-get install mysql-server mysql-client php5-mysql

sudo service mysql start

mysql -u root –p



SUSCRIBETE A MI CANAL: <a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/redirect?v=V5G7mwjGvxc&amp;event=video_description&amp;redir_token=otWOURbwbywD-QVi19QnmU0Ugs18MTU2Nzg4ODc5NUAxNTY3ODAyMzk1&amp;q=http%3A%2F%2Fadf.ly%2F3738258%2Fcanal-experimentando" rel="nofollow" target="_blank">http://adf.ly/3738258/canal-experimen...</a>
GANA DINERO: <a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/redirect?v=V5G7mwjGvxc&amp;event=video_description&amp;redir_token=otWOURbwbywD-QVi19QnmU0Ugs18MTU2Nzg4ODc5NUAxNTY3ODAyMzk1&amp;q=http%3A%2F%2Fadf.ly%2F3738258%2Fconseguir-dinero" rel="nofollow" target="_blank">http://adf.ly/3738258/conseguir-dinero</a></yt-formatted-string>
