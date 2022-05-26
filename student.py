class Student:
    def __init__(self):
        pass
    def getData(self):
        self.rollNo=int(input("Enter Student rollno: "))
        self.stName=input("Enter Student Name: ")
    def printData(self):
        print(f"\nRoll No={self.rollNo}")
        print(f"Student Name={self.stName}\n")

class Marks(Student):
    def inputData(self):
      self.getData()
      self.mark1=input("Enter mark1 ")
      self.mark2=input("Enter mark2 ")
      self.mark3=input("Enter mark3 ")
      self.mark4=input("Enter mark4 ")
      self.mark5=input("Enter mark5 ")
      self.mark6=input("Enter mark6 ")

    def outData(self):
        self.printData()
        print(f"Mark of subject1 for {self.stName} is {self.mark1}")
        print(f"Mark of subject2 for {self.stName} is {self.mark2}")
        print(f"Mark of subject3 for {self.stName} is {self.mark3}")
        print(f"Mark of subject4 for {self.stName} is {self.mark4}")
        print(f"Mark of subject5 for {self.stName} is {self.mark5}")
        print(f"Mark of subject6 for {self.stName} is {self.mark6}")
        totalMarks=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5+self.mark6
        avgMarks=totalMarks/6

        print(f"Total marks of 6 subject for {self.stName} is {totalMarks}")
        print(f"Average marks of 6 subject for {self.stName} is {avgMarks}")

    
  

studentMark=Marks()
studentMark.inputData()
studentMark.outData()



      


        
        