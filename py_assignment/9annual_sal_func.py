def annual_sal(msal):
    asal=msal*12
    return asal
def prov_fund():
    msal=float(input("Enter monthly salary: "))
    asal=annual_sal(msal)
    print("Annual salary is %.2f" %asal)
    fund=asal*(12.5/100)
    return fund
pfund=prov_fund()
print("Provident fund is %.2f" %pfund)