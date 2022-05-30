class Calculator:
    def setdata(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.result=0
    def add(self):
        self.result=self.num1 + self.num2
        return self.result
    def sub(self):
        self.result=self.num1 - self.num2
        return self.result
    def mul(self):
        self.result=self.num1 * self.num2
        return self.result
    def div(self):
        self.result=self.num1 / self.num2
        return self.result

class1=Calculator()
class1.setdata(10,20)
result=class1.add()
print(result)