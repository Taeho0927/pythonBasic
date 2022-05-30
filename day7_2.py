class Calculator:
    def __init__(self):
        self.result=0
    def sum(self,startNum):
        self.result += startNum

a=int(input('몇 까지 더할래? :'))
sumA=Calculator()
i=0
while i<=a:
    sumA.sum(a-i)
    i+=1
print(sumA.result)