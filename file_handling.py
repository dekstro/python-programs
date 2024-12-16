with open('test.bin','w+b') as f:
    n=f.tell() #show current pos of f 0
    print(n)
    f.write(b'Core Python')  #writing operation
    n=f.tell() #show current pos of f 11
    print(n)
    f.seek(0,0) #move f to 0th position
    n=f.tell() #show current pos of f 0
    print(n)
    data=f.read(4) #read the file now f is at 4th pos
    print(data.decode())
    f.seek(1,1) #move f to 5th position
    n=f.tell() #show current pos of f 5th
    print(n)