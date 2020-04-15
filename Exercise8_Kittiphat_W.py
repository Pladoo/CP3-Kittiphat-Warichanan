UsernameInput = input("Username : ")
PasswordInput = input("password : ")
if UsernameInput == "Dream" and PasswordInput == "123" :
    print("Login success!!")
    print("--- Welcome to yumyum shop --")
    print("-----------------------------")
    print("Product..............Cost")
    print("1. Pen...............10 THB")
    print("2. Pencil............5  THB")
    print("3. Book..............30 THB")
    print("4. Bag...............50 THB")
    print("5. Ruler.............15 THB")
    print("Please select product follow by number")
    UserSelectProduct = int(input("Number is "))
    if UserSelectProduct == 1 :
        HowManyPieced = int(input("How many pieces? "))
        if HowManyPieced >= 1 :
            print("total is ", 10 * HowManyPieced , "THB")
    elif UserSelectProduct == 2 :
        HowManyPieced = int(input("How many pieces? "))
        if HowManyPieced >= 1 :
            print("total is ", 5 * HowManyPieced , "THB")
    elif UserSelectProduct == 3 :
        HowManyPieced = int(input("How many pieces? "))
        if HowManyPieced >= 1 :
            print("total is ", 30 * HowManyPieced , "THB")
    elif UserSelectProduct == 4 :
        HowManyPieced = int(input("How many pieces? "))
        if HowManyPieced >= 1 :
            print("total is ", 50 * HowManyPieced , "THB")
    elif UserSelectProduct == 5 :
        HowManyPieced = int(input("How many pieces? "))
        if HowManyPieced >= 1 :
            print("total is ", 15 * HowManyPieced , "THB")

else:
    print("Worng Username or Password!!!")
