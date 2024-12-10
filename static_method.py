 # 7. understanding static methods 
# to count the number of objects created for a class 
class Myclass: 
    # this is class var or static var 
    n=0    
    # constructor that increments n when an instance is created 
    def __init__(self): 
        Myclass.n +=1 
    # this is a static method to display the no. of instances 
    @staticmethod 
    def noObjects(): 
        print('No. of instances created: ', Myclass.n)  
# create 3 instances 
obj1 = Myclass()  # this will call default constructor 
obj2 = Myclass() 
obj3 = Myclass()  
Myclass.noObjects() 