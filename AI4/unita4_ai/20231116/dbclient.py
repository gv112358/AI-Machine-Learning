from configparser import ConfigParser
import psycopg2

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

conn = None


def connect():
    """ Connect to the PostgreSQL database server """
    global conn
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        return cur

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def write_in_db(cur,sql_insert):
    global conn
    try:
        cur.execute(sql_insert)
        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur = None
        conn = None

def read_in_db(cur,sql_select):
    try:
        cur.execute(sql_select)
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur = None
        conn = None



def close(cur):
    global conn
    try:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur = None
        conn = None


#usage
if __name__ == '__main__':
    cur = connect()
    sql_insert = "insert into your_table values "
    dati = "(1200,'10489434', '85048', '15CM CHRISTMAS GLASS BALL 20 LIGHTS', 12, TO_DATE('2009/12/03','YYYY/MM/DD'), 6.95, 13085, 'United Kingdom', '07:45');"
    sql_insert += dati
    write_in_db(cur, sql_insert)
    read_in_db(cur, "select * from ordini;")
    close(cur)
