import sys

def main(path: str) -> None:
    ...

def read_file(path: list[str]) -> list[str]:
    ...

def average_score_calc(path: list[str]) -> int:
    ...

def top_students(path: list[str]) -> list[str]:
    ...

def sorted_scores(path: list[str]) -> list[str]:
    ...



if __name__ == "__main__":
    print("Please insert scoreboard: ")
    main(sys.argv[0])

