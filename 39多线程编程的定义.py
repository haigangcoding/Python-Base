# import threading
# import time
# from threading import current_thread
#
#
# def myThread(arg1, arg2):
#     print(current_thread().getName(), 'start')
#     print('%s %s' %(arg1, arg2))
#     time.sleep(5)
#     print(current_thread().getName(), 'stop')
#
#
# for i in range(1, 6, 1):
#     # t1 = myThread(i, i + 1)
#     t1 = threading.Thread(target=myThread, args=(i, i + 1))
#     t1.start()
#
# print(current_thread().getName(), 'end')

import threading
from threading import current_thread

class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')

t1 = Mythread()
t1.start()
t1.join()

print(current_thread().getName(), 'end')
