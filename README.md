#  Logs Analysis Project

This is Udacity's Full Stack Web Developer Nanodegree's first project **[Logs Analysis](#)** .
In the project, I have created a program where _Analyzer_ can view commands' result instead of typing query in **database**.

### Project Requirements
* Reporting tool should answer the following questions:
 	* What are the most popular three articles of all time?
 	* Who are the most popular article authors of all time?
 	* On which days did more than 1% of requests lead to errors?

* Project follows good SQL coding practices: Each question should be answered with a single database query.
* The code is error free and conforms to the   [pycodestyle](https://pypi.org/project/pycodestyle/) style recommendations.
* The code presents its output in clearly formatted _plain text_ .

### Dependencies.
This program requires some other software programs to run properly .

* **Python** Programming Language version 3 [click here](https://www.python.org/) to download .
* **PostgreSQL** Database [click here](https://www.postgresql.org/) to download .
* **Virtual Box** to manage virtual machines [click here ](https://www.virtualbox.org/wiki/Downloads) to download .
* **Vagrant** development environment [click here](https://www.vagrantup.com/) to download .
* **News** database schema [click here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to download

##### After installing all dependencies make sure it's all ok .
Write `python --version` into your terminal if you have output like `python 3.X.X` then it's ok, to check the vagrant type `vagrant --version` the output must be like `Vagrant 2.X.X`, type `virtualbox` into your terminal then you will find it open up if your Installation process was ok and finally type `psql --version` to your terminal if you had something like `psql (PostgreSQL) 9.5.14` now i can tell you _"you'r good to go ."_


### Quick Start
After downloading the **news database schema** extract it, you will find **_newsdata.sql_** file add it to your project directory.
* Open your shell terminal
* run `vagrant up` to start the virtual machine .
* then `vagrant ssh` to login to virtual machine .
* `cd` into your preferred directory to download the project
* Clone this repo by typing `git clone https://github.com/EngDiesel/log-analysis.git`
* Then go to the project directory by typing `cd log-analysis/` in your terminal .

Now time to use the **PostgreSQL Database** .
* Type `psql -d news -f newsdata.sql` into your terminal to prepare the _database_.

Now time to use our **Log Analysis Program** .
* Type `python3 log.py` in your terminal to run the program.

this will give you the **OUTPUT.txt** file modified with the output.


### Output

this is an example for how output must be

  [Click here](https://github.com/EngDiesel/log-analysis/blob/master/output.txt) to see output.txt file .

  	---------------- 1) Most popular three articles of all time ? ----------------

  	1 ) 'Candidate is jerk, alleges rival' -- 338647 Views

  	2 ) 'Bears love berries, alleges bear' -- 253801 Views

  	3 ) 'Bad things gone, say good people' -- 170098 Views

  	---------------- 2) Most popular article authors of all time ? ---------------

  	1 ) 'Ursula La Multa' -- 507594 Views

  	2 ) 'Rudolf von Treppenwitz' -- 423457 Views

  	3 ) 'Anonymous Contributor' -- 170098 Views

  	-------- On which days did more than 1% of requests lead to error ? ----------

  	1 ) 'July 17, 2016' -- 2.3 %


### Queries Used

* 1) Most popular three articles of all time ?
```sql
select articles.title, count(log.ip) as views
from log join articles
on log.path = concat('/article/', articles.slug)
group by articles.title
order by views desc limit 3;
```


* 2) Most popular article authors of all time ?
```sql
select authors.name, count(log.ip) as views
from log, authors, articles
where articles.author = authors.id
and CONCAT('/article/',articles.slug) = log.path
group by authors.name order by views desc limit 3;
```

* On which days did more than 1% of requests lead to error ?
```sql
select to_char(date, 'FMMonth FMDD, YYYY'),
        (err/total) * 100 as ratio
from (select time::date as date, count(*) as total,
        sum((status != '200 OK')::int)::float as err
from log group by date) as errors
where err/total > 0.01;
```

### Contributors

* Mostafa Yasin
	 * [Github](https://github.com/EngDiesel)
	 * [Facebook](https://fb.com/mostafa.yasin.2013)
	 * [Twitter](https://twitter.com/_mostafayasin_)
