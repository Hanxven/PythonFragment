import sv
import _thread
import os
import time

th1 = _thread.start_new_thread(sv.startfuck, (1,))
th2 = _thread.start_new_thread(sv.startfuck, (2,))
th3 = _thread.start_new_thread(sv.startfuck, (3,))
th4 = _thread.start_new_thread(sv.startfuck, (4,))
th5 = _thread.start_new_thread(sv.startfuck, (5,))
th6 = _thread.start_new_thread(sv.startfuck, (6,))
th7 = _thread.start_new_thread(sv.startfuck, (7,))
th8 = _thread.start_new_thread(sv.startfuck, (8,))


while 1:
    time.sleep(1000)

