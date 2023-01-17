#from secrets1 import username, password
from decouple import config



print("hello world")
#print(username, password)


USER1= config('user1')
PASSWORD1= config('password1')

print(USER1)
print(PASSWORD1)