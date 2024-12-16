empdata = [(1001, 'Ganesh Rao', 10000.00, '10-10-2000'), 
(1002, 'Anil Kumar', 23000.50, '3-20-2002'), 
(1003, 'Gaurav Gupta', 18000.33, '03-03-2002'), 
(1004, 'Hema Chandra', 16500.50, '10-09-2000'), 
(1005, 'Laxmi Prasanna', 12000.75, '08-10-2000'), 
(1006, 'Anant Nag', 9999.99, '09-09-1999')] 
import pandas as pd
df=pd.DataFrame(empdata, columns=['eno','ename','salary','doj'])
print(df)