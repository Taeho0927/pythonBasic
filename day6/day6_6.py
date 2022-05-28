#함수 연습 5
#layer 변수에 별의 층수를 입력하면 각 층마다 별의 개수가 한 개씩 증가하여 출력되고, 마지막줄에
#별의 개수가 출력되도록 함수를 구현하라.
#def starCount(layer): <<함수 선언부

def starCount(layer):
    i=1
    tot=0
    while i <= layer:
        print('★'*i)
        tot+=i
        i+=1
    return'별 개수 :{}'.format(tot) 
layer=int(input('만들 별의 층 수를 입력하세요 :'))
print(starCount(layer))