SHELL = /bin/sh

clean:
	docker-compose down --remove-orphans

build:
	docker-compose up -d
	MODE=DDL python src/run.py

ddl:
	MODE=DDL python src/run.py

dml:
	MODE=DML python src/run.py

clean-db:
	psql -h localhost -p 5432 -U postgres -c 'DROP DATABASE greenhouse;'
