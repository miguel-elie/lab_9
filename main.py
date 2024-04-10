def encoder(old_password):
    old_pass_list = []
    for i in old_password:
        old_pass_list.append(str(int(i) + 3))
    new_password = "".join(old_pass_list)
    return new_password

def decoder():
    print()

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
            temp_password = (input("Please enter your password to encode: "))
            password = encoder(temp_password)
            print("Your password has been encoded and stored!")
        #DECODER
        if menu_option == 2:
            continue
        if menu_option == 3:
            break



