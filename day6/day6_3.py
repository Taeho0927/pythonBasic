#함수 연습3 (출력값이 없는 함수)
#아래 오름차순 정렬 프로그램을 함수로 변형하고,lst를 키보드로 입력받아 오름차순으로 정렬하라
#lst=[93,45,21,30,20,94,66,71,45]
#오름차순
# for a in range(0,len(lst)-1):
#     for b in range(a+1,len(lst)):
#         if lst[a] > lst [b]:
#             (lst[a],lst[b]) = (lst[b],lst[a])
# print(lst)
#------------------------------------------------------#
def orum(arg):
    for a in range(0,len(arg)-1):
        for b in range(a+1,len(arg)):
            if arg[a] > arg [b]:
                (arg[a],arg[b]) = (arg[b],arg[a])
    return arg

num_list = list(map(int,input('오름차순으로 정렬할 수를 입력하세요 :').split(',')))
print(orum(num_list))