#팩토리얼을 계산하는 재귀함수를 만들어보라.
#재귀함수-함수가 끝나면서 함수본인을 다시 호출하면된다?

#def factorial_func(x):
def factorial_func(x):
    if x == 1:      # x가 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return x * factorial_func(x - 1)    # x와 factorial 함수에 x - 1을 넣어서 반환된 값을 곱함
print(factorial_func(5))