# coding:cp949
def my_sum1(num1, num2) :   # 입력, 출력을 모두 지정ㅇ하는 케이스
    result = num1 + num2
    return result           # 연산, 비즈니스 로직에만 집중

def my_sum2(num1, num2) :
    result = num1 + num2
    print("%d + %d = %d"%(num1,num2,result))

def my_sum3() :
    num1 = int(input("첫 번째 수를 입력하세요 : "))
    num2 = int(input("두 번째 수를 입력하세요 : "))
    result = num1 + num2
    return result

def my_sum4() :
    num1 = int(input("첫 번째 수를 입력하세요 : "))
    num2 = int(input("두 번째 수를 입력하세요 : "))
    result = num1 + num2
    print("%d+%d=%d"%(num1, num2, result))


num1 = int(input("첫 번째 수를 입력하세요."))
num2 = int(input("두 번째 수를 입력하세요."))

result = my_sum1(num1,num2)
print("%d+%d=%d"%(num1, num2, result))

num1 = int(input("첫 번째 수를 입력하세요."))
num2 = int(input("두 번째 수를 입력하세요."))
my_sum2(num1,num2)

print(my_sum3())


