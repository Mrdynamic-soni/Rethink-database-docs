-#*Rethink DATABASE DOCS*
-Rethinkdb is an open source database.

-The best thing about the rethinkdb is that it always keeps  connect the backend to the database to exchange of information as soon as you will update anything in databsee it will automartically and immediately will be shown on frontend with no delay 

RethinkDB is the first open-source, scalable JSON database built from the ground up for the realtime web. It inverts the traditional database architecture by exposing an exciting new access model – instead of polling for changes, the developer can tell RethinkDB to continuously push updated query results to applications in realtime. RethinkDB’s realtime push architecture dramatically reduces the time and effort necessary to build scalable realtime apps.

In addition to being designed from the ground up for realtime apps, RethinkDB offers a flexible query language, intuitive operations and monitoring APIs, and is easy to setup and learn.

-##Here aree some steps to follow to start using rethink database 

-##*FOR WINDOWS*
-To get started rethink database with windows you need to first dockerise your windows <a href = "https://blog.sixeyed.com/how-to-dockerize-windows-applications/">HOW TO DOCKERISE</a>
-Or follow <a href = "https://rethinkdb.com/docs/install/windows/#:~:text=Running%20RethinkDB&text=You'll%20need%20to%20start%20the%20Windows%20command%20shell.&text=Use%20the%20cd%20command%20to,you%20unpacked%20rethinkdb.exe%20in.&text=Then%2C%20you%20can%20start%20RethinkDB%20with%20its%20default%20options.&text=You%20can%20also%20use%20any,as%20specify%20a%20configuration%20file).">these steps</a> for complete guidelines

-##*FOR UBUNTU*
-To get started rethink databsase with ubuntu follow below listed steps 

-To install the server, you have to add the RethinkDB repository to your list of repositories and install via apt-get. To do this, paste the following lines into your terminal:
*source /etc/lsb-release && echo "deb https://download.rethinkdb.com/repository/ubuntu-$DISTRIB_CODENAME $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/repository/raw/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install rethinkdb*


-after installing rethink databse in ubuntu you need to start rethik databse 

-rethink databse provides a GUI interface to perform all the actions

-To start GUI interface of rethink database 
-just after installing rethink datbase  type code #rethinkdb
-It will ask you to bind all the connections so just type  #rethinkdb --bind all
-Now GUI interface of rethink dtabase has been started at port *8080* to head to that go to browser type *localhost/808* on searchbasr  you are ready to create databse with rethibkdb GUI

##To use rethink database with python follow steps listed below on unbuntu
-install the dependencies  *pip3 install
