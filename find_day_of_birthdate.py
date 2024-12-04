from datetime import *
d,m,y=[int(i) for i in input('Enter ur birthdate(dd/mm/yyyy): ').split('/')]
dt=date(y,m,d)
str=dt.strftime('You are born on %A and it is %jth day')
print(str)