
# sets can be used for summing and substracting lists. It consideres duplicates.

def mutual_friends(a: list[str], b: list[str]) -> set[str]:
    return set(a) and set(b)

def frends_only_in_first(a: list[str], b: list[str]) -> set[str]:
    return set(a) - set(b)

def all_friends(a: list[str], b: list[str]) -> set[str]:
    return set(a) | set(b)

def exclusive_friends(a: list[str], b: list[str]) -> set[str]:
    return set(a) ^ set(b)

if __name__ == "__main__":
    anna_friends = ["bob", "carla", "david", "eve", "carla"]
    ben_friends = ["carla", "eve", "frank", "grace"]

    print("Anna's list:", anna_friends)
    print("Ben's list:", ben_friends)
    print()
    print("Mutual:", sorted(mutual_friends(anna_friends, ben_friends)))
    print("Only Anna's:", sorted(frends_only_in_first(anna_friends, ben_friends)))
    print("Only Ben's:", sorted(frends_only_in_first(ben_friends, anna_friends)))
    print("Exactly one list:", sorted(exclusive_friends(anna_friends, ben_friends)))