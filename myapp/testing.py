from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta



expecteddelivery=datetime.now()+timedelta(weeks=2)

x=expecteddelivery.strftime("%a,%d %B,%y")

print(x)

now=datetime.now()
