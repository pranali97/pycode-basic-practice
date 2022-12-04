import csv

with open("emp.csv","w",newline='') as f:
    w = csv.writer(f) #returns csv writter object pointing to f
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n = int(input("Enter Number of Employees: "))
    for i in range(n):
        eno = int(input("Enter employee number: "))
        ename = (input("Enter employee name: "))
        esalary = float(input("Enter employee salary: "))
        eaddress = input("Enter employee address: ")
        w.writerow([eno,ename,esalary,eaddress])
print("Total employee data is wriiten to csv file is successfully")  