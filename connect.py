import psycopg2
from configparser import RawConfigParser

def connect():
    db_config = RawConfigParser()
    db_config.read('connection.properties')
    db_config = db_config['DEFAULT']
    return psycopg2.connect(
    host=db_config.get('host'),
    port=db_config.get('port'),
    dbname=db_config.get('dbname'),
    user=db_config.get('user'),
    password=db_config.get('password'))


def main():
    db_conn = connect()


if __name__ == '__main__':
    main()
