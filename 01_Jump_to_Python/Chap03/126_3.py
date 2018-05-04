# coding:cp949
print("<SW 아키텍처 커피자판기 Ver 1.0>")
coffee_number = 10
money = 300

menu = """
<MENU>
1. 커피구매
2. 커피 잔량확인
3. 프로그램 종료 """

while True :   
    print(menu,end='')
    check = int(input("메뉴를 선택하세요.: "))
    
    if check == 1 :
        money = int(input("돈을 넣어주세요.: "))
    
        if money == 300 :
            print("커피를 줍니다.")
            coffee_number = coffee_number - 1
        elif money > 300 :
            print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
            coffee_number = coffee_number -1
        else :
            print("금액이 %d 모자랍니다." %(300-money))

    elif check == 2 :
        print("남은 커피의 양은 %d개 입니다." %coffee_number)
    elif check == 3 :
        print("종료합니다.")
        break

    if not coffee_number :
        print("커피가 다 떨여졌습니다. 판매를 중지합니다.")
        break

    print(" ")
    print(" ")
