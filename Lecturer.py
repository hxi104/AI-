# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:02:29 2025

@author: qpy23cmu
"""

class Lecturer(Employee):
    def __init__(self, name, salary, modules=None):
        super().__init__(name, salary)
        
        self.modules = modules if modules is not None else []
    
        