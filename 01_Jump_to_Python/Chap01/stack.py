# coding: cp949
dish_stack=[]
dish_stack.append('d1')
dish_stack.append('d2')
dish_stack.append('d3')
dish_stack.append('d4')
print("식판 현황 : " , end='')

# dish_stack=['d1','d2','d3','d4']

print("{0} 식판 설거지합니다.".format(dish_stack.pop()))
print("{0} 식판 설거지합니다.".format(dish_stack.pop()))
print("{0} 식판 설거지합니다.".format(dish_stack.pop()))
print("{0} 식판 설거지합니다.".format(dish_stack.pop()))

