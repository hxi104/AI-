# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:02:29 2025

@author: qpy23cmu
"""
from employee import Employee

class Lecturer(Employee):
    def __init__(self, name, salary, modules=None):
        super().__init__(name, salary)
        
        self.modules = modules if modules is not None else []
    
    def add_module(self, module_name):
        if module_name not in self.modules:
            self.modules.append(module_name)
            pass
            
    def remove_module(self, module_name):
        if module_name in self.modules:
            self.modules.remove(module_name)
            pass
            
    def get_module(self):
        return self.modules
        
    def __str__(self):
        base_str = super().__str__()
        modules_str = ", ".join(self.modules) if self.modules else "None"
        return f"{base_str}, Modules: {modules_str}"
        
def tester():
    lec1 = Lecturer("Dr. Smith", 70000, ["CMP6045A"])
    lec1.add_module("CMP7045A")
    lec1.remove_module("CMP6045A")
    print(lec1)


if __name__ == "__main__":
    tester()