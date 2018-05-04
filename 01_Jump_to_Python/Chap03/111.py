# coding:cp949
money = 0
#money = 1
#money = 
if money :
    print("택시를 타고 가라")
#  print("도착 했습니다") <- ikndentation 이 맞지않아 에러
#   print("목적지에 도착했습니다")
else :
    print("걸어 가라")
#    print("도착 했습니다") <- 동일 코드 중복
#                           <- 프로그램 수정시 동일 코드 로직 변경이누락 될 가능성이 있음
print("목적지 도착")        # 중복코드 제거
print("프로그램 종료합니다")
