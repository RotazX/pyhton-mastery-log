
def validate_password(pw) -> list[str]: # an annotation that pw returns a list of strings.
    errors = []
    if len(pw) < 8:
        errors.append("Password must be 8 characters or more")
    if not any(c.isdigit() for c in pw):
        errors.append("Password must include a number!")
    if not any(c.isupper() for c in pw):
        errors.append("Password must include an uppercase!")

    return errors

if __name__ == "__main__":
    while True:
        pw = input("Enter a password: ")
        problems = validate_password(pw)

        if not problems:
            print("Your password is safe!")
            break

        for p in problems:
            print(f" - {p}")
