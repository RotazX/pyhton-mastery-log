
l = input("Enter a list of items. ").split()

def dedupe(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

# list(set(l)) - here the duplicates are gone but the order is wrecked

def dedupe_fast(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(dedupe(l))
print(dedupe_fast(l))