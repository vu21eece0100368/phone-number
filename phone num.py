import re
n=input('Enter Mobile number :')  
r=re.fullmatch('[+91][6-9][0-9]{11}',n) 
if r!=None: 
     print('Valid Number')
else:
     print('Not a valid number')
