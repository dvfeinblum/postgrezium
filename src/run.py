from os import environ
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_cursor():
    conn = connect(host='localhost',
                   port='5432',
                   user='postgres',
                   database='greenhouse')
    conn.autocommit = True
    return conn.cursor()


def execute_ddl():
    with connect(host='localhost',
                 port='5432',
                 user='postgres') as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE greenhouse;')
        cursor.close()

    cur = get_cursor()
    ddl = open('resources/ddl.sql').read()
    for command in ddl.split(';'):
        if command != '':
            cur.execute(command)
    cur.close()


def execute_dml():
    cur = get_cursor()
    dml = open('resources/dml.sql').read()
    for command in dml.split(';'):
        if command != '':
            cur.execute(command)
    cur.close()


if __name__ == '__main__':
    mode = environ.get('MODE')
    if mode == 'DDL':
        execute_ddl()
    elif mode == 'DML':
        execute_dml()
    elif mode == 'ALL':
        execute_ddl()
        execute_dml()
    else:
        raise RuntimeError('Invalid run mode. Run this script with either "MODE=DML" or "MODE=DDL".')
