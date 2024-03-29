import time
from GoodDog import *
from watchdog.observers import Observer
import numpy as np
import random
import os
import time
import sys

#进度条
def  process_line():
    for i in range(26):
        a = "■" * i
        b = "□" * (25 - i)
        c = (i/25) * 25 * 4
        sys.stdout.write('\r{}{:.2f}    '.format(a,c))
        sys.stdout.flush()
        time.sleep(0.2)

    #进度条1
    for i in range(25):
        a = "■" * i
        b = "□" * (25 - i)
        c = (i/25) * 25 * 4
        print('\r {}{}{:.2f}'.format(a,b,c))
        time.sleep(0.1)

    #进度条2
    for i in range(26):
        a = "■" * i
        b = "□" * (25 - i)
        c = (i/25) * 25 * 4
        sys.stdout.write('\r{} {:.2f}'.format(a,c))
        sys.stdout.flush()
        time.sleep(0.2)




def  luck_num(num_list):
    remove_str = " ".join([ str(j) for j in num_list])
    print(f"Remove: {remove_str}")
    blue = [i for i in  range(1,36)]
    red = [i for i in range(1,13)]
    for i in num_list[:len(num_list)-2]:
        if i in blue:
            blue.remove(i)
    for iii in range(3):
        jackpot = []
        for i in range(5):
            bingo = random.choice(blue)
            jackpot.append(bingo)
            blue.remove(bingo)
        for i in num_list[5:]:
            if i in red:
                red.remove(i)
        jackpot.append(":")
        for i in range(2):
            bingo = random.choice(red)
            jackpot.append(bingo)
            red.remove(bingo)
        print(jackpot)
    return


def  luck_n(num_list):
    remove_str = " ".join([ str(j) for j in num_list])
    print(f"Remove: {remove_str}")
    blue = [i for i in  range(1,36)]
    red = [i for i in range(1,13)]
    for i in num_list[:len(num_list)-2]:
        if i in blue:
            blue.remove(i)
    jackpot = []
    for n in range(5):
        blue_pix = random.choices(blue,k=5)
        red_bix = random.choices(red,k=2)
        print(blue_pix,":",red_bix)
    return



def goodDog():
    observer = Observer()
    event_handler = GoodDog()
    observer.schedule(event_handler,r"D:\\",recursive=True)
    observer.schedule(event_handler,r"E:\\",recursive=True)
    observer.schedule(event_handler,r"F:\\",recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# [24, 25, 30, 34, 8, ':', 11, 8, 5, 3]

if __name__ == "__main__":
    last = [4,6,10,24,28,6,12]
    # goodDog()
    luck_num(last)

