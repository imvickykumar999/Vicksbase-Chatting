from crud import Vicks as vix
# print(help(h))
from datetime import datetime

obj = vix('https://chatting-c937e-default-rtdb.firebaseio.com/')

# f = obj.pull()
# print(f)

f = obj.push('Hello', 'Group/Chat')
print(f)

dt = datetime.now()
print(help(dt))

# obj.remove('Hello')
