
Student = dict[str, str | int] # a dict whose keys are strings and whose values are either strings or ints.

STUDENTS: list[Student] = [
    {"name": "Anna", "score": 78},
    {"name": "Bogdan", "score": 92},
    {"name": "Clara", "score": 65},
    {"name": "Dmitri", "score": 92},
    {"name": "Eva", "score": 54},
    {"name": "Fedor", "score": 88},
    {"name": "Greta", "score": 71},
]

# def main(students):
#     print(top_score(sort(students)))
#     print(sort(students))
#     print(average_score(students))

# def average_score(students: list[student]) -> int:
#     scores = []
#     for student in students:
#         scores.append(student["score"])
#     return sum(scores)/len(scores)

# def top_score(students):
#     return students[0]["score"]

# def sort(students):
#     s_students = sorted(students, key=lambda student: student["score"], reverse=True)
#     return s_students

# if __name__ == "__main__":
#     main(STUDENTS)


def average_score(students: list[Student]) -> float:
    if not students:
        raise ValueError("cannot average an empty list of students")
    return sum(s["score"] for s in students) / len(students)


def top_scorer(students: list[Student]) -> Student:
    if not students:
        raise ValueError("no students to pick a top scorer from")
    return max(students, key=lambda s: s["score"])


def sort_by_score_desc(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda s: s["score"], reverse=True)


def main(students: list[Student]) -> None:
    print(f"Average: {average_score(students):.2f}")
    print(f"Top scorer: {top_scorer(students)['name']}")
    for student in sort_by_score_desc(students):
        print(f"{student['name']:<10} {student['score']}")


if __name__ == "__main__":
    main(STUDENTS)