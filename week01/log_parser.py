
def main(log: list[str]) -> None:
    print(f"Found {len(find_error_lines(read_log(log)))} ERROR lines:")
    for error in find_error_lines(read_log(log)):
        print(error)

def read_log(log: str) -> list[str]:
    with open(log, "r", encoding="utf-8") as f:
        return f.readlines()

def find_error_lines(log: list[str]) -> list[str]:
    error_lines = []
    for line in log:
        split_line = line.split()
        if len(split_line) <= 2: 
            continue
        if split_line[2] == "ERROR":
            error_lines.append(line.rstrip())
    return error_lines


if __name__ =="__main__":
    main("app.log")