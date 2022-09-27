

class Employee:

    def __init__(self, name, idnum, department, title, msalary):
        self.__name = name
        self.__idnum = idnum
        self.__department = department
        self.__title = title
        self.__msalary = msalary

    def set_name(self, name):
        self.__name = name

    def set_idnum(self, idnum):
        self.__idnum = idnum

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    def self_msalary(self, msalary):
        self.__msalary = msalary 

    def get_name(self):
        return self.__name

    def get_idnum(self):
        return self.__idnum

    def get_department(self): 
        return self.__department 

    def get_title(self):
        return self.__title

    def get_msalary(self):
        return self.__msalary

