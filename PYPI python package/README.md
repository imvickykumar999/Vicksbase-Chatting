# New feature Added : [Now you can Upload Your Custom package on Python Package Index using Above Project](https://www.c-sharpcorner.com/article/firebase-crud-operations-using-python/) !!!

    import crud

    obj1 = crud.vicks('passwprd', name = 'Vicky')
    obj1.push('kaisa hai tu ?')

    obj2 = crud.vicks('password')
    obj2.push()

    obj2.save()
    obj2.pull()

    
    # Firebase-CRUD
      Home Automation using my firebase package and kivy Android App, finally display output on my website.

    ## Create new file in cmd
      type nul > led.py

    ## crud.py

        from imvickykumar999 import firebase

        firebase_obj = firebase.FirebaseApplication('https://your_project_name.firebaseio.com/', None)

        # update data
        firebase_obj.put('/parant/','child', data)

        # fetch data
        result = firebase_obj.get('/parent/child', None)
        print (result)

    [![image](https://user-images.githubusercontent.com/50515418/116424009-cd519480-a85e-11eb-943f-e566d49bad09.png)](https://github.com/imvickykumar999/Firebase-CRUD/blob/bdeb5b7a0b703b2f86719ee2da0d06505ee00ceb/main.py#L16)

    ## CMD...

        C:\Users\Vicky\Desktop\Repository\firebase\Firebase-CRUD>python
        Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
        >>> import crud as f

        >>> f.push({"Cost": 250, "Name": "LED 1", "Switch": "ON", "Value": 1})
        'updated'
        >>> f.pull()
        ('Value fetched = ', {'Cost': 250, 'Name': 'LED 1', 'Switch': 'ON', 'Value': 1})

        >>> f.push({"Cost": 250, "Name": "LED 1", "Switch": "ON", "Value": 1}, fan)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'fan' is not defined

        >>> f.push({"Cost": 250, "Name": "Fan", "Switch": "ON", "Value": 1}, 'fan')
        'updated'
        >>> f.pull('fan')
        ('Value fetched = ', {'Cost': 250, 'Name': 'Fan', 'Switch': 'ON', 'Value': 1})

        >>> f.push({"Cost": 250, "Name": "LED", "Switch": "OFF", "Value": 0})
        'updated'
        >>> f.pull()
        ('Value fetched = ', {'Cost': 250, 'Name': 'LED', 'Switch': 'OFF', 'Value': 0})

        >>> c.insert()
        {'name': '-MZPZc4g5Aq_tqp7Z15x'}
        >>> c.remove()
        (('Value fetched = ', {'fan': {'Name': 'Fan', 'Switch': 'OFF'}}), '...is present')
        >>> c.pull()
        ('Value fetched = ', None)
        >>> c.insert()
        {'name': '-MZPZoeNKI0vWr2ZhX4Q'}
        >>> c.push()
        'updated'
        >>> c.remove()
        (('Value fetched = ', {'fan': {'Name': 'Fan', 'Switch': 'OFF'}}), '...is present')
        >>>
