# 취미 개발용 문법

# 프로그래밍

# - 컴퓨터에게 명령 을 내리는 것 그 언어를 파이썬으로 하는 것 뿐임.
# - 컴퓨터는 지능이 0임 
# - 생각 추론을 못함

# 1. 출력명령
# 	print

# 2. 변수 
# 	a = 1
# 	글자 일부만 떼어네기 
# 	'안녕하세요'[0] ===> '안'
# 	'안녕하세요'[0:2] ===> '안녕'
# 	일명 인덱싱


# List라는 자료 저장법
car = ['bmw','white',8000] 

# 원하는 자료만 출력하자
print(car[0])



# 자료 수정
car[1] = 'black'
print(car[1])

# 정렬
car.sort()
# List의 순서를 뒤집기
car.reverse()
# 맨 뒷자리
car.pop()


# Dictionary 자료형 특) 중괄호임 / 이름(key)도 써야함
car2 = {
    'brand' : 'bmw',  
    'model' : '520d', 
    'price' : 5000
    }
car2['brand'] = 123 # 수정 
print(car2['brand'])
