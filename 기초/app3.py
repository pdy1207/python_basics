# def
# 함수 잘쓰는 법
# 1.긴 코드를 짧은 단어로 축약할때.

def hi() :
    print('Hi my name is... your name?')

hi()

# 2. 마법의 모자 만들기 
# 파라미터 문법 뭔가 집어 넣으면 다른게 나오는 변환기
def hat(test) : 
    print(test + 1)

hat(1)

# 두개 뚫어도 됨
def hat2(test,abc) : 
    print(test + abc)

hat2(1,2)

# 함수 특 위에서 만들어 놔야 밑에가서 함수쓸 수 있음
# 실행 후 가죽을 남기고 싶을때
# return 남길자료 (옵션임)

def ham() :
    return 10

print(ham() + 10)


# 1. 긴코드 축약? 
# 2. 마법모자 ? 
