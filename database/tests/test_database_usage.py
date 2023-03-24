import sys, os
import pandas as pd
import numpy as np

root_dir = os.getcwd().split('tests')[0]
sys.path.append(root_dir)

from DBClient import DBClient


# Goal: test functionality of the database. See if it can store new data and then if you can retrive it in another session.
# if you read and are able to retrive a database (i.e. it prints to the command line) then you were succesful

# Results: I tried it works. 

def write():
    df = pd.DataFrame({'a': np.linspace(0,100,100), 'b': np.random.rand(100), 'c': ['a']*100})
    db = DBClient('books')
    db.write(df, 'df')

def read():
    db = DBClient('books')
    df2 = db.query_to_df("SELECT * FROM df")
    print(df2)

def main(mode):
    if mode == 'write':
        write()
    elif mode == 'read':
        read()
    else:
        print('only "read" or "write" argument values allowed')


if __name__ == "__main__":
    try:
        mode = sys.argv[1]
        main(mode)
    except IndexError as e:
        print('You must specify one argument "read" or "write" when calling this script from the cmd.')
