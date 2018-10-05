# Udacity's Logs Analysis Project
###  _Version Control with Git_

This is the repo for [Udacity's Logs Analysis Project](). In the project, I have created a program where analyzer can view commands' result instead of typing query in database.

This repo contains the source code of a Logs Analysis project.

## Table of Contents

* [Instructions](#instructions)
* [Creator](#creators)

## Instructions

* ### Set-up Instructions
	1. Create the news database in PostgreSQL
		* From the command line, launch the psql console by typing: psql
		* Check to see if a _news database already exists_ by listing all databases with the command: ``` \l ```
		* If a news database already exists, drop it with the command: ``` DROP DATABASE news; ```
		* Create the _news_ database with the command: ``` CREATE DATABASE news; ```
		* exit the console by typing: ``` \q ``` or press ``` ctrl + d ```
	2. Download the schema and data for the _news_ database:
		* [Click here to download it](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	3. Unzip the downloaded file. ``` unzip newsdata.zip ```.
		* You should now have an sql script file with the name _newsdata.sql_.
	4. From the command line, navigate to the directory containing _newsdata.sql_ using ``` cd ``` command.
	5. Import the schema and data in _newsdata.sql_ to the news database by typing: ``` psql -d news -f newsdata.sql ```


* ### Installation (Run program)
 >* clone the project
 >* open terminal in project directory
 >* go in news directory. using ``` cd news ``` in terminal
 >* run ``` python newsdb.py ``` or ``` python3 news.py ```

## Output

 * [Click here to see output.txt file]().

## Developer

* Mostafa Yasin
    - [Github](https://github.com/EngDiesel)
    - [Facebook](https://fb.com/mostafa.yasin.2013)

Required software:

* Python
* PostgreSQL
