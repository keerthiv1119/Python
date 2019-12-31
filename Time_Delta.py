'''
Absolute Time Difference
'''
from datetime import datetime as dt
time = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
     print(int(abs(dt.strptime(input(),time) - dt.strptime(input(),time)).total_seconds()))
