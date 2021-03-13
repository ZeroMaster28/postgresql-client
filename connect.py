import psycopg2
import pandas as pd
from configparser import RawConfigParser


def connect():
    db_config = RawConfigParser()
    db_config.read('connection.properties')
    db_config = db_config['DEFAULT']
    connection = psycopg2.connect(
    host=db_config.get('host'),
    port=db_config.get('port'),
    dbname=db_config.get('dbname'),
    user=db_config.get('user'),
    password=db_config.get('password'))
    if connection != None:
        print("Connection successfully instantiated to host",
         db_config.get('host'), "and database", db_config.get('dbname'))
    return connection


def read_query_from_file(file_name):
    query = ''
    with open(file_name, encoding='utf8') as f:
        for line in f:
            query += line.strip() + ' '
    return query


def save_query_results(query_results, file_name):
    if not query_results is None:
        query_results.to_csv(file_name)
        print('Saved query results to file', file_name)
    else:
        print('Nothing to save')


def main():
    db_conn = connect()
    query_results = None
    print('Type \'exit\' to disconnect')
    while db_conn != None:
        query = input('query>')
        if query == 'exit':
            db_conn.close()
            db_conn = None
            break
        if query.startswith("save"):
            query_components = query.split()
            if len(query_components) > 1:
                save_query_results(query_results, query_components[1])
            continue 
        if query.startswith("read"):
            query_components = query.split()
            if len(query_components) > 1:
                query = read_query_from_file(query_components[1])
            else:
                continue
        query_results = pd.read_sql(query, db_conn)
        print(query_results)


if __name__ == '__main__':
    main()
