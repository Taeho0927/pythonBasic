#함수 연습4
#[1,4,6]의 값으로 구성된 리스트가 있다
#index(a) 함수는 a가 몇번째에 있는지 찾는 내장함수다.
#해당 내장함수를 쓰지 말고, for 문을 사용하여 같은 역할을 하는 find라는 함수를 구현하라

list_a=[1,4,6]
def find(a):
    co=0
    for i in list_a:
        co += 1
        if i == a:
            return '입력하신 수 {}는 리스트의 {}번째의 존재합니다'.format(a,co)
    return '입력하신 수 {}은(는) 리스트에 존재하지 않습니다'.format(a)
print(find(5))
