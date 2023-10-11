def extended_GCD(a, b):  # a, b is the number which user will input

    UserInput_A = a
    UserInput_B = b

    Non_modified_A = a  # for saving the user inputs, for print(f"").
    Non_modified_B = b
    Q = Non_modified_A // Non_modified_B
    x = 1  # not used yet
    y = 0  # not used yet
    Index = 0

    while b > 0:
        if Index == 0:
            print(f"{Index}: {a} ")
            Index += 1
        if Index == 1:
            print(f"{Index}: {b} ")
        R = a % b
        if b > R:
            Index += 1
            if R == 0:  # needed this if-statement, or else there will be "ZeroDivisionError: integer division or modulo by zero"
                print(
                    f"{Index} | {Non_modified_A} / {Non_modified_B} = {Q} | Rest = {R} | ")
                print(
                    f"{Index+1} | Because Rest = 0 -> No Zero Division (example: x / 0) | We found the GCD({UserInput_A}, {UserInput_B}) = {b}")
                break
            a = b
            b = R
        print(f"{Index} | {Non_modified_A} / {Non_modified_B} = {Q} | Rest = {R} | ")
        Non_modified_A = Non_modified_B
        Non_modified_B = R
        Q = Non_modified_A // Non_modified_B


extended_GCD(240, 46)
