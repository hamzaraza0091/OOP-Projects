from abc import ABC, abstractmethod

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def get_name(self):
        return
    
    def get_age(self):
        return
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Emplooye(Person,ABC):
    def __init__(self,name,age,employe):
        super().__init__(name,age)
        self.employe = employe

    @abstractmethod
    def calculate_salary(self):
        pass

class Doctor(Emplooye):
    def __init__(self,name,age,employe,specialization,patients):
        super().__init__(name,age,employe)
        self.specialization = specialization
        self.patients = patients

    def calculate_salary(self):
        base_salary = 500000
        return base_salary 
    
    def doctor_info(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Employe_Id: {self.employe}\n specialization: {self.specialization}\n Patients: {self.patients}\n Salary: {self.calculate_salary()}")
        
D = Doctor(name="Hamza",
          age=22,
           employe=2,
           specialization="Cardiologist",
           patients=5
           )
D.doctor_info()