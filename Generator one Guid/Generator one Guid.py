#Генерация рандомных GUID
from uuid import uuid4
from pyperclip import copy

xxx = str(uuid4())
copy(xxx)