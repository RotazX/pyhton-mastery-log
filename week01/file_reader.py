
def main(path: str) -> None:
    lines = read_lines(path)
    print("Total lines:", len(lines))
    print("Total words:", count_words(lines))
    print("Longest line:", longest_line(lines))

def read_lines(lines: str) -> list[str]:
    with open(lines, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def count_words(lines: list[str]) -> int:
    words = 0
    for line in lines:
        words += len(line.split())
    return words
    


def longest_line(lines: list[str]) -> str:
    if not lines:
        raise ValueError("no lines to compare")
    return max(lines, key=len)

if __name__ == "__main__":
    main("types-and-io.md")

# f.read() pulls the entire file into one string. f.readlines() gives you a list of lines.