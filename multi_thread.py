import pandas as pd
import numpy as np
from threading import Thread
from multiprocessing import Queue

df = pd.DataFrame(data=np.random.rand(100).reshape(10, 10))

print(df.head())
rows = df.index
column = df.columns

que = Queue()


# long run
def long_run(row, col, pv):
    for r in row:
        for c in col:
            pv.at[r, c] = 1
    que.put(pv)
    return


threads = []


def thread_run(n, df):
    np_r = np.array_split(rows, n)
    for i in range(n):
        print(i)
        print('min =' + str(np_r[i].min()) + ' max = ' + str(np_r[i].max()))
        print()
        t = Thread(target=long_run,
                   args=(rows[np_r[i].min():np_r[i].max()], column[:], df[np_r[i].min():np_r[i].max()]))
        threads.append(t)
        t.start()


if __name__ == '__main__':
    thread_run(4, df)
    lst = []
    mydf = pd.DataFrame()
    while not que.empty():
        result = que.get()
        print('thread 1:::::>>>>>>>>')
        print(result)
        lst.append(result)

    print(lst)
    # for i in lst:
    #     mydf = pd.concat([mydf,i], axis=1)
    #     mydf.head()

# from multiprocessing.pool import ThreadPool
#
#
# def foo(bar, baz):
#     print('hello {0}'.format(bar))
#     return 'foo' + baz
#
#
# pool = ThreadPool(processes=5)
#
# async_result = pool.apply_async(foo, ('world', 'foo'))  # tuple of args for foo
#
# # do some other stuff in the main process
#
# return_val = async_result.get()  # get the return value from your function.
