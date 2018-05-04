def many(choice, *args) :
    result = args[0]
    if choice == "sum" :
        for i in args :
            result += i
    elif choice == "sub" :
        for i  in args :
            result -= i
    elif choice == "mul" :
        for i in args :
            result *= i
    elif choice == "div" :
        for i in args :
            result /= i
    return result;


op = input("operation :")

print("result = %d"%(many(op,1,2,3,4,5)))
