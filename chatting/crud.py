
# pip install imvickykumar999
# C:\Users\Vicky\anaconda3\Lib\site-packages\vicksbase

import json
from datetime import datetime

dt = datetime.now()
d = str(dt).split()[0]
t = str(dt).split()[1].split('.')[0]

class Vicks:
    def __init__(self,
                link = 'https://chatting-c937e-default-rtdb.firebaseio.com/',
                name = 'anonymous'):

        try:
            from vicksbase import firebase as f
            self.link = link
            self.firebase_obj = f.FirebaseApplication(self.link, None)
            # print(self.pull(child = '/'))

        except Exception as e:
            print(e)
            print('try: pip install imvickykumar999')

    def show(self):
        return self.link

    def pull(self, child = 'Group/Chat'):
        result = self.firebase_obj.get(f'{child}', None)
        return result

    def push(self, data = 1, child = 'Group/Chat'):
        self.firebase_obj.put('/', child, data)
        return self.pull(child = '/')

    def remove(self, child = 'A/B/C/led2'): # danger to run... loss of data.
        data = self.firebase_obj.delete('/', child)
        return self.pull(child = '/')

    def save(self, child = 'Group/Chat'):
        with open('data.json', 'w', encoding ='utf8') as json_file:
            json.dump(self.pull(child), json_file, ensure_ascii = False)



# link = 'https://chatting-c937e-default-rtdb.firebaseio.com/'
# obj = Vicks(link)

# f = obj.show()
# f = obj.pull()
# f = obj.push(1)
# f = obj.remove()

# print(f)
# input('Press Enter to Exit...')
