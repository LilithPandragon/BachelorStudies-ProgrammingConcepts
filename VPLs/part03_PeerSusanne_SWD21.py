#!/usr/bin/env python3

# Requirement for Part 04 Python: multithreading
# Susanne Peer SWD21
#

from threading import Thread, Lock
import time

class Sum(object):
    val = 0
    lck = Lock()

     
class Down(Thread):
    no = 0

    def __init__(self, safe = None, mb = 0):
        Thread.__init__(self)
        self.safe = safe
        self.mb = mb
        Down.no += 1
        self.no = Down.no

    def run(self):
        print(f"{self.no} starts downloading {self.mb} MB of data.")
        
        with self.safe.lck:
            time.sleep(2) 
            self.safe.val += self.mb
        print(f"{self.no} finished the download of {self.mb} MB." )

def main(no_of_concurrent_downloads,mb_each):
    result = None
    
    sum = Sum()
    
 
    threads = []

    for _ in range(no_of_concurrent_downloads):
        thread = Down(safe = sum, mb = mb_each)
        threads.append(thread)


    for thread in threads:
        thread.start()


    for thread in threads:
        thread.join()


    result = f"Downloaded {sum.val} MB."

    
    return result


# Just for testing. The printed output is NOT relevant for grading.
# Evaluation calls function 'main' and analyses the values returned.
print( main(no_of_concurrent_downloads = 11, mb_each = 3))
print( main(no_of_concurrent_downloads = 7, mb_each = 2))