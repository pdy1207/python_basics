# if 조건문 해보기
# 어떤 코드를 조건이 맞을 때만 실행 시키고 싶을 때

product = 10

# 꼭 인덴트가 들어가야함 띄어쓰기
if product > 1 : 
    print('available to order')


carlist = ['k5', 'bmw' , 'benz']

# in 문법도 있음
if 'k6' in carlist :
    print('Buy? Y/N')
else :
    print('No')


# elif? else if임 차례차례 조건을 여러개 검사할때 

# ===

# for 반복문  

# 1. 코드 단순 반복
# 2. List에서 자료 하나씩 뽑을때


# for 변수 in 범위 indent들어간것은 10번반복해줘라는것.
# 노가다 줄일때

# print('benz')
# print('benz')
# print('benz')
# print('benz')
# print('benz')

for i in range(0,10) :
    print('benz')

    

# List 에서 자료 하나씩 뽑을때
fruit = ['apple', 'banana', 'pineapple']

# print (fruit[0])
# print (fruit[1])
# print (fruit[2])

for i in fruit :
    print(i)
