
def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def reverse_string(s: str) -> str:
    # letter = []
    # rw = ""
    # for i in s:
    #     letter.append(i)
    # letter.reverse()
    # return rw.join(letter)
    return "".join(reversed(s))

def flatten(list_of_lists: list[list]) -> list:
    flatten_list = []
    for list in list_of_lists:
        for item in list:
            flatten_list.append(item)
    return flatten_list

def most_common_words(text: str) -> dict[str, int]: 
    common_words = {}
    for word in text.lower().split():
        if word not in common_words:
            common_words[word] = 1
        else:
            common_words[word] = common_words[word] + 1
    return max(common_words, key=common_words.get)

if __name__ == "__main__":
    print(is_prime(2))
    print(reverse_string("hello"))
    print(flatten([[1, 2, 3], [4, 5], [6]]))
    print(most_common_words("I like to like cats because I like cats cats"))