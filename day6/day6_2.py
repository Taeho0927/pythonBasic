#함수 연습 2(입력값이 없는 함수)
#1)hello()라고 함수를 실행하면 "hello python!"이라고 출력되는 함수를 구현하라
def hello():
    print('"hello python!"')
hello()
#2)print(hello())라고 실행하면 "hello python!"이라고 출력되는 함수를 구현하라
def hello():
    return '"hello python!"'
print(hello())