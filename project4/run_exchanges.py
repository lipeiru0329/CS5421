import argparse
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import time
from random import randrange
from db_connect import get_conn

## Argument parser to take the parameters from the command line
## Example on how to run: python run_sums.py 10 READ_COMMITTED
parser = argparse.ArgumentParser()
parser.add_argument('E', type=int, help='number of exchanges')
parser.add_argument('I', help='isolation level')
args = parser.parse_args()


## Execute a sum query and return the results
def sum_balance(sess, A1, A2):
    V1 = sess.execute(
        "SELECT ACCOUNT.BALANCE FROM ACCOUNT WHERE ACCOUNT.ID = :mv", {
            'mv': A1
        }).fetchone()[0]
    V2 = sess.execute(
        "SELECT ACCOUNT.BALANCE FROM ACCOUNT WHERE ACCOUNT.ID = :mv", {
            'mv': A2
        }).fetchone()[0]

    sess.execute("UPDATE ACCOUNT SET BALANCE =:ml WHERE ACCOUNT.ID =:mv", {
        'mv': A1,
        'ml': V2
    })
    sess.execute("UPDATE ACCOUNT SET BALANCE =:ml WHERE ACCOUNT.ID =:mv", {
        'mv': A2,
        'ml': V1
    })

    sess.commit()

    return 1


## Create E exchanges operations
def S_exchanges(sess, E):
    start = time.time()
    A1 = randrange(0, 100000)
    A2 = randrange(0, 100000)
    for i in range(0, E):
        while True:
            try:
                sum = sum_balance(sess, A1, A2)
            except Exception as e:
                sess.rollback()
                continue
            break
    stop = time.time()
    return stop - start


## Create the engine and run the exchanges
engine = get_conn()
Session = sessionmaker(bind=engine.execution_options(isolation_level=args.I))
sess = Session()
time = S_exchanges(sess, args.E)
print(time)