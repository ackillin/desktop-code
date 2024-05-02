from datetime import datetime
from functools import reduce

def main_runner(filename):
    file = open(filename)
    dicty = {}
    for x in open(filename):
        bef,aft = x.strip().split(';')
        aft = float(aft)
        if bef in dicty.keys():
            dicty[bef].append(aft)
        else:
            dicty.update({bef:[aft]})
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
    open('times.txt','a').write(f"{finish_time.date()}, {str(diff_time)[5:]}\n")

    
