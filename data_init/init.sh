#! /bin/bash

echo "Please enter your Mongo username: "
read user

echo "Please enter you Mongo password: "
read password


mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_1.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_2.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_3.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_4.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_5.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_6.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_7.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_8.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_9.json
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_10.json


mongoimport --jsonArray --collection countries --db pppDB --username $user --password $password --file collection_2.json
mongoimport --jsonArray --collection missions --db pppDB --username $user --password $password --file collection_3.json