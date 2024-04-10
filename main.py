def encoder():
    print("TEST")

if __name__ == "__main__":
    while True:
        menu_option = int(input("Menu\n"
                                "-------------\n"
                                "1. Encode\n"
                                "2. Decode\n"
                                "3. Quit\n"
                                "\n"
                                "Pleaser enter an option: "))
        password = None
        #ENCODER
        if menu_option == 1:
            old_password = (input("Please enter your password to encode: "))
            old_pass_list = []
            for i in old_password:
                old_pass_list.append(str(int(i)+3))
            password = "".join(old_pass_list)
            print("Your password has been encoded and stored!")
        #DECODER
        if menu_option == 2:
            continue
        if menu_option == 3:
            break



