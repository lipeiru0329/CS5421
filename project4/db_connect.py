from sqlalchemy import create_engine


## Create a connection to the postgres database server.
def get_conn():
    server = 'localhost'
    dbname = 'cs4221_p4'
    username = 'postgres'
    password = '123456'

    engine = create_engine('postgres://%s:%s@localhost:5432/%s' %
                           (username, password, dbname))

    return engine
