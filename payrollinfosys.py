class Employee():
    def __init__(self):
        pass
    basicPay=None
    def getData(self):
    
      self.empNo=input("Enter employee number ")
      self.empName=input("Enter employee name ")
      self.empDesignation=input("Enter employee designation ")
      self.empAddress=input("Enter employee address ")
      self.empPhone=input("Enter emplyeee phoneno ")

    def putData(self):
        print(f"\nEmployee No is {self.empNo} ")
        print(f"Name of employee {self.empName} ")
        print(f"Designation of  {self.empName} is {self.empDesignation}")
        print(f"Addree of {self.empName} is {self.empAddress}")
        print(f"Phone No of {self.empName} is {self.empPhone}")

class Salary(Employee):

    def getData1(self):
        self.getData()
        self.basicPay=int(input("\nEnter the employee basic pay "))

    def calculate(self):
        self.DA=self.basicPay*.08
        self.hra=self.basicPay*.15
        self.pf=self.basicPay*.10
        
        self.tax=int(input("\nEnter the tax "))

        self.grossPay=self.basicPay+self.DA+self.hra+self.pf+self.tax

        self.netPay=self.grossPay-self.tax-self.pf

        print(f"\nBasic pay of Employee {self.empName} is {self.basicPay}")
        print(f"DA of Employee {self.empName} is {self.DA}")
        print(f"HRA of Employee {self.empName} is {self.hra}")
        print(f"PF of Employee {self.empName} is {self.pf}")
        print(f"Gross pay of Employee {self.empName} is {self.grossPay}")
        print(f"Net pay of Employee {self.empName} is {self.netPay}")



    def display(self):
        self.getData1()
        self.putData()
        self.calculate()


sal=Salary()
sal.display()


