PPP_Scraper
===========

Web scraping application for UN Peacekeeping contributions database.

Dependancies
------------
*	[Pymongo](http://api.mongodb.org/python/current/ "Pymongo") - MongoDB interface
*	[Request](http://docs.python-requests.org/en/latest/ "Requests") - Python HTTP library
*	Pulls data from [Morph.io](https://morph.io/ "Morph.io") API
*	Scraper pulls data from the [DPKO contribution documents](http://api.mongodb.org/python/current/ "DPKO")
*	Scraper uses [ScraperWiki](https://blog.scraperwiki.com/ "ScraperWiki") library to convert pdf's to xml and parse into Morph SQLLiteDB



-init
bash init.sh

~./boto touch with the following content
[Credentials]
aws_access_key_id = <aws access key>
aws_secret_access_key = <aws secret key>