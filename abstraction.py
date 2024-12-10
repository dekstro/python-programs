 # 9. Bank class with a private variable 'loan'. 
class Bank: 
    def __init__(self): 
        self.accno=1001 
        self.name='Ganesh' 
        self.bal = 5000.0 
        self.__loan = 1500000.00 
  
    def display_to_clerk(self): 
        print('Accno= ', self.accno) 
        print('Name= ', self.name) 
        print('Balance= ', self.bal)        
     
# create instance to the class 
b = Bank() 
b.display_to_clerk() 
print(b.accno) 
print(b.name) 
print(b.bal) 
print(b._Bank__loan)  # name mangling 