from datetime import datetime
startTime = datetime.now()

import time
from progress.bar import IncrementalBar

n = int(input('Введите число '))
a=0
i=0

##mylist = range(1,n-1)

#bar = IncrementalBar('Countdown', max = len(mylist))

#for item in mylist:
#    bar.next()
 #   time.sleep(1)

#bar.finish()


for i in range(1,n-1):
  for j in range(1,i):
    if i%j==0:
      a=a+j
    if a==i and j==i-1:
      print(i)
  a=0

print(datetime.now() - startTime)