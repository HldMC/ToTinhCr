import time
from random import randint
for i in range(1,45):
    print('')
s = ''
for i in range(1,1000):
    count = randint(1,100)
    while (count > 0):
        s += ' '
        count -= 1
    if (i % 10 ==0):
        print(s + 'yeu NTP')
    else:
        print(s + '<3')
    s = ''
    time.sleep(0.2)