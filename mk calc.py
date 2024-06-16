def plus(a=1,b=2): #함수 선언 및 매개변수 초기값 설정
    print(a+b)  #프린트문 선언
plus(2, 5) # 값 기입
plus() #미입력 시

def minus(a=1, b=2): # 함수 선언
    print(a-b)
minus(2, 5)
minus()

def multiply(a=1, b=2):
    print(a*b)
multiply(2, 5)
multiply()

def divide(a=1, b=2):
    print(a/b)
divide(2, 5)
divide()

def power_of(a=1, b=2):
    print(a**b)
power_of(2, 5)
power_of()

#간단한 연산자를 이용해 아주 성능 좋은 계산기를 만들어냈다