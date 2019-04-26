def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    initials = ""
    names = fullname.split()
    for name in names:
        initials += name[0]
    return initials.upper()


def main():
    user_input = input("What is your full name? ")
    print("The initials of", user_input, "are:", get_initials(user_input))

if __name__ == '__main__':
    main()