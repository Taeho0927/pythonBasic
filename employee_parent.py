class Employee:
    def __init__(self,name,emptype):
        self.name = name
        self.emptype = emptype

    def printprofile(self):
        print('이름 :',self.name)
        print('이름 :',self.emptype)