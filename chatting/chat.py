from crud import Vicks as vix
# print(help(h))

from datetime import datetime
# import time

obj = vix('https://chatting-c937e-default-rtdb.firebaseio.com/', 'vicks')

# f = obj.pull()
# print(f)

# dt = datetime.now()
# d = str(dt).split()[0]
# t = str(dt).split()[1].split('.')[0]

# print(f'A/{dt}')

obj.save('Group/Chat/2021-05-28')

while True:
    dt = datetime.now()
    d = str(dt).split()[0]
    t = str(dt).split()[1].split('.')[0]

    # name = input('\nEnter your name : ')
    message = input('Enter your message : ')
    # name = 'Vicks'

    f = obj.push(f'{message}', f"Group/Chat/{d}/{t}@{name}")
    # print(f)
    obj.save()


# print(obj.pull('Group/Chat'))
# obj.save()
# obj.remove(f"Group/Chat/{d}/23:50:45@{name}")

# while(1):
#     print(datetime.now())
#     time.sleep(1)
