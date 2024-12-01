# function to calculate annual salary
def annual_sal(msal):
    asal=msal*12
    return asal

# function to calculate provident fund
def prov_fund():
    msal=float(input("Enter monthly salary: "))
    asal=annual_sal(msal)    # here i have called annual_sal func to get the annual salary 
    print("Annual salary is %.2f" %asal)
    fund=asal*(12.5/100)
    return fund
pfund=prov_fund()       # prov_fund func is called 
print("Provident fund is %.2f" %pfund)