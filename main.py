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

def decode(password="12345678"):
    password_list = []
    updated_password_list = []
    decoded_password = ""

    for i in password:
        password_list.append(i)

    for y in password_list:
        if y.isdigit() == True:
            if int(y) == 0:
                updated_password_list.append("7")
            elif int(y) == 1:
                updated_password_list.append("8")
            elif int(y) == 2:
                updated_password_list.append("9")
            else:
                updated_password_list.append(str(int(y) - 3))

    decoded_password = "".join(updated_password_list)

    return decoded_password

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
            print(f"The encoded password is {password}, and the original password is {decode(password=password)}.")
        if menu_option == 3:
            break



