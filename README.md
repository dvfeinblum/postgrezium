# postgrezium
Simple postgres/debezium project

Why?
====
If you know even the slightest thing about any of these technologies, you're probably confused why this is so... manual and janky.
And that's a good question.
Indeed, debezium has some marvelous dockerfiles and containers that you could use to spin all this stuff up for ya.
I worked through this the way I did to see what it's like manually configuring a postgres db for debezium so I could take learnings back to my day job.

And it was fun.

How to Run
==========
First, get yourself a venv and install requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Next, you're gonna need to spin up the infrastructure
```bash
make build
```
This gives you postgres, zookeeper, kafka, and debezium.
It'll also run a python script that creates a database to play with and some tables.

Finally, it's time to write some data into the db so we can capture it with debezium.
You can do this by running
```bash
make dml
```
which will execute the sql located in `/resources/dml.sql`.