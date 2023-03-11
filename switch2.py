ch=input("Enter any number in between a-e:")
match ch.lower():
    case 'a':
        print("A")
    case 'b':
        print("B")
    case 'c':
        print("C")
    case 'd':
        print("D")
    case 'e':
        print("E")
    case _:
        print("Invalid choice")
