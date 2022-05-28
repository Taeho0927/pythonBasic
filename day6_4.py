#연습문제2 (선택적 함수 만들기)
#사칙연산을 하는 함수를 만들자. 키보드로 사칙연산을 입력받아 어떤 연산을 할 건지 선택하고
#정수 두개를 입력 받아 연산을 처리하고 결과를 돌려주는 함수를 만들어라.

def sachik(a,b,c):
    if a=='+':
        return b+c
    elif a=='-':
        return b-c        
    elif a=='*':
        return b*c        
    elif a=='/':
        return b/c        

a=input('어떤 연산을 하실래요?(ex +,-,*,/) :')
b=int(input('첫 번째 정수를 입력해주세요 :'))
c=int(input('두 번째 정수를 입력해주세요 :'))

result=sachik(a,b,c)
print('%d와%d의%s연산결과는%d입니다.'%(b,c,a,result))