import argparse
import ast
import subprocess
import random
from sqlalchemy.orm import sessionmaker
import time
from db_connect import get_conn

parser = argparse.ArgumentParser()
parser.add_argument('E',
                    type=int,
                    help='number of exchange transactions in a process')
parser.add_argument('P', type=int, help='number of processes')
parser.add_argument('I', help='isolation level')
args = parser.parse_args()

processes = []
for i in range(0, args.P):

    processes.append(
        subprocess.Popen(['python3', 'run_exchanges.py',
                          str(args.E), args.I],
                         stdout=subprocess.PIPE))

for process in processes:
    process.wait()

time = []
for process in processes:
    # print(process.communicate()[0])
    a = process.communicate()[0].decode()

    time.append(ast.literal_eval(a))

# print(time)
print(float(sum(time)) / len(time))
