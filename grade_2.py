
def letter_grade(grade: int) -> str:
    if not 0 <= grade <= 100:
        raise ValueError("grade must be between 0 and 100")

    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    grade = int(input("Enter your grade on scale of 0-100: "))
    letter = letter_grade(grade)
    article = "an" if letter in ("A", "F") else "a"
    print(f"You got {article} {letter}!")