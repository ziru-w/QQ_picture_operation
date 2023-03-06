

# filepath=""
# for 

from datetime import datetime
import os


import time
def getTimeStamp(datetime='2023-4-06 00:00'):
    s_t = time.strptime(datetime, "%Y-%m-%d %H:%M")  # 返回元祖
    mkt = time.mktime(s_t)
    print(mkt)
    return mkt

def isTime(resource)->float:
    mtime = os.path.getmtime(resource) #修改时间
    print(mtime)
    # mtime_string = datetime.fromtimestamp(int(mtime))
    return mtime
getTimeStamp('2023-4-06 00:00')
getTimeStamp('2023-4-06 00:00')
# print(isTime("main.py"))
# print(datetime)