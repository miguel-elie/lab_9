#Name: Miguel Elie
#Collaborator: Parker Grimes
#Lab 9
def encode(old_password):
    old_pass_list = []
    for i in old_password:
        if int(i) >= 7:
            if int(i) == 7:
                old_pass_list.append("0")
            elif int(i) == 8:
                old_pass_list.append("1")
            else:
                old_pass_list.append("2")
        else:
            old_pass_list.append(str(int(i) + 3))
    new_password = "".join(old_pass_list)
    return new_password

def decode():
    print()

if __name__ == "__main__":
    password = None
    while True:
        menu_option = int(input("\nMenu\n"
                                "-------------\n"
                                "1. Encode\n"
                                "2. Decode\n"
                                "3. Quit\n"
                                "\n"
                                "Pleaser enter an option: "))
        #ENCODER
        if menu_option == 1:
            temp_password = (input("Please enter your password to encode: "))
            password = encode(temp_password)
            print("Your password has been encoded and stored!")
        #DECODER
        if menu_option == 2:
            continue
        if menu_option == 3:
            break



