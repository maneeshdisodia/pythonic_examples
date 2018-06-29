#import multiprocessing
from pymongo import MongoClient
import pandas as pd
import numpy as np
import string
import re
from multiprocessing import Lock, Process
from datetime import datetime

def process_data(maxx,l):
    pass



def process_cursor(skip_n, limit_n,l):
    print('Starting process', skip_n // limit_n, '...')
    client = MongoClient(uri)
    db = client.cs_ml
    max = db.coll.find({}).skip(skip_n).limit(limit_n)

    max_list = list(max)
    status = process_data(max_list,l)
    print('job done for partitions', skip_n // limit_n, status)

    print('Completed process', skip_n // limit_n, '...')


if __name__ == '__main__':
    n_cores = 1  # number of splits (logical cores of the CPU-1)
    # collection_size = 5284733-13  5284720 for 16core # your collection size in mongo
    collection_size = 5781408
    batch_size = round(collection_size / n_cores)
    skips = range(0, n_cores * batch_size, batch_size)
    print(collection_size, batch_size, skips, len(skips))

    l= Lock()

    processes = [Process(target=process_cursor, args=(skip_n, batch_size,l)) for skip_n in skips]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
