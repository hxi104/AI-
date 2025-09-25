# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 13:26:58 2025

@author: qpy23cmu
"""

class Employee:
    
    
    empCount = 0
    
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print(f"Total Employees: {Employee.empCount}")
        
    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
def tester():
    
    emp1 = Employee("Harry", 2000)
       
    emp2 = Employee("Charlie", 1000)
        
    print(emp1)
    print(emp2)
    print (f'Total Employee is {Employee.empCount}')
if __name__ == "__main__":
        tester()
    
        
