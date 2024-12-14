try:
    print('Open files')
    a,b=[int(i) for i in input('Enter two no: ').split()]
    c=a/b
    print(c)
except Exception as obj:
    print(obj)
finally:
    print('Close files')
