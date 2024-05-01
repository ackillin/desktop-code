from datetime import datetime

def main_runner(filename):
    file = open(filename)
    dicty = {}
    for x in file:
        bef,aft = x.strip().split(';')
        if bef in dicty.keys():
            dicty[bef].append(aft)
        else:
            dicty.update({bef:[aft]})
    print(len(dicty['London']))

if __name__ == '__main__':
    cur_time = datetime.now()
    print("Starting", cur_time)
    main_runner('measurements.txt')
    finish_time = datetime.now()
    print("Finished", finish_time)
    diff_time = finish_time - cur_time
    print(diff_time)
    open('times.txt','a').write(f"{finish_time.date()}, {str(diff_time.time())[6:]}\n")

    
