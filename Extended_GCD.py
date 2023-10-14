
def extended_GCD(a, b):
    UserInput_A = a
    UserInput_B = b

    Non_modified_A = a
    Non_modified_B = b
    Q = Non_modified_A // Non_modified_B
    Index = 0
######################## START OF simpleGCD ########################
    Q_list = []
    while b > 0:
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
######################## END OF simpleGCD ########################

    # just for testing purpose.
    print("")
    print("Q-list reversed:", Q_list[::-1])
    Q_listREVERSE = Q_list[::-1]
    print("")
    ######################## START OF EXTENDED PART (x, y) ########################
    x = 1
    y = 0
    Index = 0
    i = 0
    while Index <= 5:
        if Index == 0:
            # x = 1, y = 0
            print(
                f"{Index} | x = {x} | y = {y} |")
            Index += 1  # index 1
            x_new = y  # xnew = 0
            y_new = x - (Q_listREVERSE[0] * x_new)
        x_new = y  # xnew = 0
        y_new = x - (Q_listREVERSE[(Index-1)] * x_new)
        x, y = x_new, y_new
        print(
            f"{Index} | x = {x_new} | y = {y_new} | Q_listReverse[{Index-1}]: {Q_listREVERSE[Index-1]}")
        Index += 1
    print(
        f"\na*x + b*y = GCD(a,b)\na= {UserInput_A}, b= {UserInput_B}, GCD(a,b)={b}\n--> {UserInput_A}*({x_new}) + {UserInput_B}*({y_new}) = {b}\n--> {UserInput_A*x_new} + {UserInput_B*y_new} = {(UserInput_A*x_new) + (UserInput_B*y_new)}")


extended_GCD(a=int(input("a= ")), b=int(input("b= ")))

'''after testing with different inputs, it does need some fixes.
   - one of the issues is the looping, or indexing IN THE SECOND, EXTENDED PART. -> right now it works for numbers like (240, 46) (333, 56) (112, 33) (208, 128)
   - second part needs fix, for looping thru everything. it throws IndexErrors. So because it didnt went thru all of it, the last print() statement, where it does multiplication, its wrong'''
