# **************** WELCOME ************************

is_running = True
print("Welcome to Bank program! \n******************************")
print()


def bank_program():
    bale = 0.0
    while is_running:
        print()
        print("1. Balance Check\n2. Deposite Amount\n3. Withdraw Amount\n4. Exit")

        usr_inpt = int(input("Enter a choice (1-4): "))

        def balance():
            print(f"\n\nYour Balance is ${bale:.2f}\n")
            bank_program()

        def deposite():
            nonlocal bale
            amnt = float(input("Enter the amount you want to deposite: $"))
            bale += amnt
            print(f"${amnt} Was sucessfully added")

        def withdraw():
            nonlocal bale
            amnt = float(input("Enter the amount you want to Withdraw: $"))
            bale -= amnt
            print(f"${amnt} was sucessfully withdrawn")

        match usr_inpt:
            case 1:
                balance()
            case 2:
                deposite()
            case 3:
                withdraw()
            case 4:
                break


bank_program()
