class Ractangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
    def circum(self):
        return (self.width + self.height) * 2
w=int(input('가로 :'))
h=int(input('세로 :'))
sagak=Ractangle(w,h)
print('='*20)
print('넓이 :',sagak.area())
print('둘레 :',sagak.circum())
print('='*20)