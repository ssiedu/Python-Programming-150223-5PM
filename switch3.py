ch=input("Enter any charcter:")
match ch.lower():
    case 'a'|'e'|'o'|'i'|'u':
        print("Vowel")
    case _:
        print("consonant")
        
