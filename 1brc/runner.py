from datetime import datetime
from functools import reduce
import multiprocessing
from multiprocessing import Queue
import re
import os


def children(start=0, stop, filename)
    dicty = {}
    my_pid = os.getpid()
    chunk_count = 0
    with open(filename,'r') as file:
        file.seek(start)
        data = file.read(stop - start)
        dicty = {}
        for line in data:
            bef,aft = line.strip().split(';')
            aft = int(re.search(r'(-*\d+)',aft)+aft[-1])
            if bef in dicty.keys():
                dicty[bef].append(aft)
            else:
                dicty.update({bef:[aft]})
        return dicty



def main_runner(filename):
    POOL_SIZE = 10
    CHUNK_COUNT = 10000
    TOTAL_LINES = 10_000_000
    CHUNK_SIZE_LINES = TOTAL_LINES // CHUNK_COUNT
    SLEEP_SECONDS = 0.1


    dicty = {}
    with multiprocessing.Manager() as manager:
        chunk_queue: manager.Queue() = manager.Queue()
        #Creates a pool of 10 workers

        print(f"Creating pool of {POOL_SIZE} workers")
        pool = multiprocessing.Pool(POOL_SIZE)
        

        pool.close()
        pool.join()
    print(len(dicty['London']))
    print("Max:", reduce(lambda a,b: a if a>b else b, dicty['London']) )
    print("Min:", reduce(lambda a,b: a if a<b else b, dicty['London']) )
    print("Avg:", sum(dicty['London'])/len(dicty['London']) )


if __name__ == '__main__':
    cur_time = datetime.now()
    print("Starting", cur_time)
    main_runner('measurements.txt')
    finish_time = datetime.now()
    print("Finished", finish_time)
    diff_time = finish_time - cur_time
    print(str(diff_time)[5:])
    #open('times.txt','a').write(f"{finish_time.date()}, {str(diff_time)[5:]}\n")

    
