# coding:cp949
def my_sum1(num1, num2) :   # �Է�, ����� ��� �������ϴ� ���̽�
    result = num1 + num2
    return result           # ����, ����Ͻ� �������� ����

def my_sum2(num1, num2) :
    result = num1 + num2
    print("%d + %d = %d"%(num1,num2,result))

def my_sum3() :
    num1 = int(input("ù ��° ���� �Է��ϼ��� : "))
    num2 = int(input("�� ��° ���� �Է��ϼ��� : "))
    result = num1 + num2
    return result

def my_sum4() :
    num1 = int(input("ù ��° ���� �Է��ϼ��� : "))
    num2 = int(input("�� ��° ���� �Է��ϼ��� : "))
    result = num1 + num2
    print("%d+%d=%d"%(num1, num2, result))


num1 = int(input("ù ��° ���� �Է��ϼ���."))
num2 = int(input("�� ��° ���� �Է��ϼ���."))

result = my_sum1(num1,num2)
print("%d+%d=%d"%(num1, num2, result))

num1 = int(input("ù ��° ���� �Է��ϼ���."))
num2 = int(input("�� ��° ���� �Է��ϼ���."))
my_sum2(num1,num2)

print(my_sum3())


