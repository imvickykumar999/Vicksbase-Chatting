
import os

os.system('pip install -r requirements.txt')

os.system('python setup.py sdist')

os.system('twine upload dist/*')
