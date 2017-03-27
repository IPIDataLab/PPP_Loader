#! /bin/bash

echo "Please enter your Mongo username: "
read user

echo "Please enter you Mongo password: "
read password

# Set current month and year
cur_mon=$(date +%m)
cur_year=$(date +%y)

if [[ $cur_mon -eq 1 ]]; then
	let "cur_year-=1"

fi

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    sudo apt-get install python-dev
	sudo apt-get install python-pip
	sudo apt-get install r-base-core
	sudo apt-get install r-base-dev
	sudo apt-get update
fi

sudo pip install requests
sudo pip install pymongo
sudo pip install boto
sudo pip install rpy2


echo "Loading contributions (part 1 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_1.json
echo "Loading contributions (part 2 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_2.json
echo "Loading contributions (part 3 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_3.json
echo "Loading contributions (part 4 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_4.json
echo "Loading contributions (part 5 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_5.json
echo "Loading contributions (part 6 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_6.json
echo "Loading contributions (part 7 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_7.json
echo "Loading contributions (part 8 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_8.json
echo "Loading contributions (part 9 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_9.json
echo "Loading contributions (part 10 of 10)"
mongoimport --jsonArray --collection contributions --db pppDB --username $user --password $password --file collection_1_10.json

echo "Loading missions"
mongoimport --jsonArray --collection missions --db pppDB --username $user --password $password --file collection_2.json
echo "Loading countries"
mongoimport --jsonArray --collection countries --db pppDB --username $user --password $password --file collection_3.json

# update data apprpriately
# if [[ $cur_year -eq 14 ]]; then
# 	for m in `seq 3 $cur_mon`;
# 		do
# 			echo $m/$cur_year
# 			sudo python ../python/main.py $user $password $m/$cur_year
# 		done
# 	exit
# fi

for y in `seq 14 17`;
	do
		if [[ $y -eq 14 ]]; then
			for m in `seq 4 12`;
				do
					echo $m/$y
					sudo python ../python/main.py $user $password $m/$y
				done
			exit
		fi
		if [[ $y -ne 15 ]]; then
			for m in `seq 1 12`;
				do
					echo $m/$y
					sudo python ../python/main.py $user $password $m/$y
				done
			exit
		fi
		if [[ $y -ne 16 ]]; then
			for m in `seq 1 12`;
				do
					echo $m/$y
					sudo python ../python/main.py $user $password $m/$y
				done
			exit
		fi
		if [[ $y -ne 17 ]]; then
			for m in `seq 1 12`;
				do
					echo $m/$y
					sudo python ../python/main.py $user $password $m/$y
				done
			exit
		fi
	done
