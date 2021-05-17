


def main():
    user_input = int(input("How old are you? "))
    if user_input < 16:
        print("You cannot vote in Peturksbouipo, Stanlau and Mayengua.")
    if user_input >= 16 and user_input < 25:
        print("You can vote in Peturksbouipo where the voting age is 16.")
        print("You cannot vote in Stanlau where the voting age is 25. ")
        print("You cannot vote in Mayengua where the voting age is 48.")
    if user_input >= 25 and user_input < 48:
        print("You can vote in Peturksbouipo where the voting age is 16.")
        print("You can vote in Stanlau where the voting age is 25. ")
        print("You cannot vote in Mayengua where the voting age is 48.")
    if user_input >= 48:
        print("You can vote in Peturksbouipo where the voting age is 16.")
        print("You can vote in Stanlau where the voting age is 25. ")
        print("You can vote in Mayengua where the voting age is 48.")
if __name__ == '__main__':
    main()
