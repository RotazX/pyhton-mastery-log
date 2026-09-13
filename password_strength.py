
while True:
    pas = input("Enter a password: ")
    if len(pas)>=8 and any(c.isdigit() for c in pas) and any(c.isupper() for c in pas):
        print("Your password is safe.")
        break
    else:
        print("Your password is too weak. Try again.")