# **************** WELCOME ************************


print("Welcome to Bank program! \n******************************")
print()


def bank_program():
    is_running = True
    bale = 0.0
    while is_running:
        print()
        print("1. Balance Check\n2. Deposite Amount\n3. Withdraw Amount\n4. Exit")

        usr_inpt = int(input("Enter a choice (1-4): "))

        def inpt_check():
            nonlocal is_running
            inpt = int(input("Back (1)\nQuit (2)\n => "))

            if inpt == 2:
                print("Have a Nice Day!\nExiting......")
                is_running = False

        def balance():
            print(f"\n\nYour Balance is ${bale:.2f}\n")
            inpt_check()

        def deposite():
            nonlocal bale
            amnt = float(input("Enter the amount you want to deposite: $"))
            if amnt > 0 and amnt < 1000000000:
                bale += amnt
                print(f"${amnt} Was sucessfully added\n")
            else:
                print("Invalid Amount Entered!")
            inpt_check()

        def withdraw():
            nonlocal bale
            amnt = float(input("Enter the amount you want to Withdraw: $"))
            if amnt > 0 and amnt > bale:
                bale -= amnt
                print(f"${amnt} was sucessfully withdrawn")
            elif amnt < 0:
                print("Insufficient Fund")
            else:
                print("Invalid Amount Entered")
            inpt_check()

        match usr_inpt:
            case 1:
                balance()
            case 2:
                deposite()
            case 3:
                withdraw()
            case 4:
                print("Have a Nice Day!\nExiting......")
                is_running = False


bank_program()
