# def extended_GCD(a, b):  # a, b is the number which user will input
#
#    UserInput_A = a
#    UserInput_B = b
#
#    Non_modified_A = a  # for saving the user inputs, for print(f"").
#    Non_modified_B = b
#    Q = Non_modified_A // Non_modified_B
#    x = 1  # not used yet
#    y = 0  # not used yet
#    Index = 0
#
#    listforXY = list()
#    while b > 0:
#        if Index == 0:
#            print(f"{Index}: {a} ")
#            listforXY.append(a)
#            Index += 1
#        if Index == 1:
#            print(f"{Index}: {b} ")
#            listforXY.append(b)
#        R = a % b
#        if b > R:
#            Index += 1
#            if R == 0:  # needed this if-statement, or else there will be "ZeroDivisionError: integer division or modulo by zero"
#                print(
#                    f"{Index} | {Non_modified_A} / {Non_modified_B} = {Q} | Rest = {R} | ")
#
#                print(
#                    f"{Index+1} | Because Rest = 0 -> No Zero Division (example: x / 0) | We found the GCD({UserInput_A}, {UserInput_B}) = {b}")
#                break
#            a = b
#            b = R
#        print(f"{Index} | {Non_modified_A} / {Non_modified_B} = {Q} | Rest = {R} | ")
#        print(listforXY)
#        Non_modified_A = Non_modified_B
#        Non_modified_B = R
#        Q = Non_modified_A // Non_modified_B
#
#    print("")
#    while Index >= 0:
#        x_new = y
#        y_new = x - (Q * y)
#        print(f"{Index} | x = {x_new} | y = {y_new} ")
#        Index -= 1
#
#
# extended_GCD(a=int(input("a= ")), b=int(input("b= ")))


#####################################################
def extended_GCD(a, b):
    UserInput_A = a
    UserInput_B = b

    Non_modified_A = a
    Non_modified_B = b
    Q = Non_modified_A // Non_modified_B
    Index = 0

    Q_list = []
    while b > 0:
        '''if Index == 0:
            print(f"{Index}: {a} ")
            Index += 1
        if Index == 1:
            print(f"{Index}: {b} ")'''
        R = a % b
        if b > R:
            Index += 1
            if R == 0:
                print(
                    f"{Index} | {Non_modified_A} / {Non_modified_B} = {Q} | Rest = {R} ")
                Index += 1
                Q_list.append(Q)
                print(
                    f"{Index} | {Non_modified_B} / 0 = __| --> We found GCD({UserInput_A}, {UserInput_B}) = {b})")
                break
            a = b
            b = R
        print(
            f"{Index} | {Non_modified_A} / {Non_modified_B} = {Q} | Rest = {R} ")
        Q_list.append(Q)
        Non_modified_A = Non_modified_B
        Non_modified_B = R
        Q = Non_modified_A // Non_modified_B

    # print(Rest_list)  # just for testing purpose.
    print("")
    print("Q-list reversed:", Q_list[::-1])
    print("")
    x = 1
    y = 0
    Index = 0
    while Index <= 6:  # index = 6
        if Index == 0:
            print(f"{Index} | x = {x} | y = {y}")  # x = 1, y = 0
            Index += 1  # index 5 lesz
        x_new = y  # xnew = 0
        y_new = x - (Q_list[(Index-2)] * x_new)
        print(f"{Index} | x = {x_new} | y = {y_new}")
        Index += 1
        x, y = x_new, y_new

    '''while Index >= 1:   
        if (Index+1) == 6:
            print(f"{Index} | x = {x} | y = {y}")
            Index -= 1
            x_new = y
            y_new = x - (Q * y)
        x_new = y
        y_new = x - (Q * y)
        print(f"{Index} | x = {x_new} | y = {y_new}")
        Index -= 1'''


extended_GCD(a=int(input("a= ")), b=int(input("b= ")))
