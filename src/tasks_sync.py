import mysql.connector
import time
import sys
import requests


def store_address(address, connection):
    cur = connection.cursor()
    cur.execute("insert into Places(street_name) values('{address}');".format(address=address.replace("'", '')))
    connection.commit()
    cur.close()


def geocode(address, connection, session):
    session.post('http://localhost:8000/', data=address)
    store_address(address, connection)


def read_addresses_from(file, connection, session):
    with open(file, 'r') as addresses:
        for address in addresses:
            geocode(address, connection=connection, session=session)


def main(file_name):
    session = requests.Session()
    connection = mysql.connector.connect(host='127.0.0.1', port=3306,
                                         user='sa', password='caju3253',
                                         db='addresses')

    print(f"started at {time.strftime('%X')}")
    read_addresses_from(file_name, connection=connection, session=session)
    print(f"finish at {time.strftime('%X')}")
    connection.close()
    session.close()


if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)
