PPP_Loader
===========
This app pulls data collected with the PPP_Scraper from the Morph.io API for processing and is built to run on a server or locally. The app asks for user verification of mongodb username and password, as well as the target month to update. This can be entered at the prompt or as arguments. 

JSON data is requested from the Morph.io API and user is notified if no data exists or if returned data is already int he database. JSON is normalized to load into mongodb. JSON is also converted to CSV to update full_data.csv, full_gender_data.csv, and current_month.csv and added to archive folder within the ppp_files directory. The program runs an R script to create monthly reporting and to update all the various time series charts within the PPP_files directory. Finally, all of this is uploaded to an s3 bucket to serve on the web.


## Dependencies

Python
-	[Request](http://docs.python-requests.org/en/latest/ "Requests") - Python HTTP library to pull from API
-	[Pymongo](http://api.mongodb.org/python/current/ "Pymongo") - MongoDB interface
-	[boto](https://boto.readthedocs.org/en/latest/ "boto") - AWS interface used here to access and update S3 bucket
-	[rpy2](http://rpy.sourceforge.net/ "rpy2") - Library to run R scripts natively within Python
-	python modules: `json`, `csv`, `datetime`, `calendar`, `time`, `re`, `os`, `sys`, `subprocess`, `traceback`


R packages
-	[reshape2](https://github.com/hadley/reshape "reshape2") - An R package to flexible rearrange, reshape and aggregate data.
-	[ggplot2](http://ggplot2.org/ "ggplot2") - Nice R charting.
-	[plyr](https://github.com/hadley/plyr "plyr") - A R package for splitting, applying and combining.  Used here for aggregation.
-	[scales](https://github.com/hadley/scales "scales") - Graphical scales
-	[RColorBrewer](http://cran.r-project.org/web/packages/RColorBrewer/index.html "RColorBrewer") - Provides chloropleth palettes
-	[reldist](http://cran.r-project.org/web/packages/reldist/index.html "reldist") - R functions for the comparison of distributions. Used here for gini and quintile calculations.


Other
-	Pulls data from [Morph.io](https://morph.io/ "Morph.io") API
-	Relies on [PPP_Scraper]() to get data from [DPKO contribution documents](http://api.mongodb.org/python/current/ "DPKO")

## UNIX (Mac OS X and Linux) install notes

Clone the application from GitHub:
```
	git clone https://github.com/IPIDataLab/PPP_Loader.git
```

#### Setting up MongoDB
This application relies on a working MongoDB install. To install MongoDB follow their updated install [instructions](http://docs.mongodb.org/manual/installation/).

Run:
```
pgrep mongod
```
to check if mongod is running. If a mumber is returned you should be good to go. If not, run:
```
mongod
```

Start up MongoDB interface and initiate DB settings by runing the following commands:
```
mongo
>use pppDB
>db.addUser("<username>","<password>")
```
### setting up boto
Boto is a python package to manage connections to a variety AWS services. To make this work boto needs access to the secret and access keys of an AWS IAM acct with read and write access on S3. You can either pass these into the boto connect funciton as arguments or you can set up a boto registry. To create and add a registry locally, run:
```
key="<aws access key>";
secret="<aws secret key>";

cat > ~./boto << EOL
[Credentials]
aws_access_key_id = ${key}
aws_secret_access_key = ${secret}
EOL
```

### Initializing data
Run:
```
bash /path/to/PPP_Loader/data_init/init.sh
```
This will run the initilization shell commands. Data up to 2/14 is contained in json files. The script also calls a series up updates from 3/14 to 8/14.

#####Note: 
This shell scripts also run `sudo pip install` commands for all the dependancies. You will be asked for your root user password.

## To Run from Command-line
There are two options fro running the validation for loading data. 
##### Option 1: pass as arguments
```
bash /path/to/PPP_Loader/python/main.py mongo_username mongo_password target_date[mm/yyyy]
```

##### Option 2: on prompt
```
bash /path/to/PPP_Loader/python/main.py
```
This command will be followed by prompts for the relvant data.

#####Note: 
The script normalizes data input so there is some latitude. Alternate options include m/yy, m/yyyy, and mm/yy


## TODO



