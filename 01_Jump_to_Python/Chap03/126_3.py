# coding:cp949
print("<SW ��Ű��ó Ŀ�����Ǳ� Ver 1.0>")
coffee_number = 10
money = 300

menu = """
<MENU>
1. Ŀ�Ǳ���
2. Ŀ�� �ܷ�Ȯ��
3. ���α׷� ���� """

while True :   
    print(menu,end='')
    check = int(input("�޴��� �����ϼ���.: "))
    
    if check == 1 :
        money = int(input("���� �־��ּ���.: "))
    
        if money == 300 :
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee_number = coffee_number - 1
        elif money > 300 :
            print("�Ž����� %d�� �ְ� Ŀ�Ǹ� �ݴϴ�." %(money-300))
            coffee_number = coffee_number -1
        else :
            print("�ݾ��� %d ���ڶ��ϴ�." %(300-money))

    elif check == 2 :
        print("���� Ŀ���� ���� %d�� �Դϴ�." %coffee_number)
    elif check == 3 :
        print("�����մϴ�.")
        break

    if not coffee_number :
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break

    print(" ")
    print(" ")
