from employee_parent import Employee

class Permanent(Employee):
    def __init__(self,name,emptype,money,bouns):
        super().__init__(name,emptype)
        self.pay=money+bouns

class Temporary(Employee):
    def __init__(self,name,emptype,time,t_money):
        super().__init__(name,emptype)
        self.pay=time*t_money

while True:
    port=input('고용형태 선택(정규직<P>,비정규직<T>)')
    if port =='p' or port =='P'or port =='t'or port =='T':
        break
    else:
        print("지원하지않는 고용형태,입력오류")
        continue
name=input('이름 :')   
if port=='p' or port =='P':
    print('고용형태 :정규직')
    while True:
        try:
            money=int(input('월급 :'))
            bouns=int(input('보너스 :'))
            break
        except:
            print('숫자가 아닙니다.다시입력하세요!')
            continue
    class1=Permanent(name,port,money,bouns)
    print('급여 :',class1.pay)
    print('='*20)
elif port =='t' or port=='T':
    print('고용형태 :비정규직')
    while True:
        try:
            time=int(input('업무시간 :'))
            t_money=int(input('시급 :'))
            break
        except:
            print('숫자가 아닙니다.다시입력하세요!')
            continue
    class1=Temporary(name,port,time,t_money)
    print('급여 :',class1.pay)
    print('='*20)