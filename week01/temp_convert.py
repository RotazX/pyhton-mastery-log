
temp = input("What is the temperature?").strip()

if temp[-1].upper() == "C":
    F = int(temp[0]) * 9/5 + 32
    print(f"Tempereture in fahrenheit is {F} F.")
elif temp[-1].upper() == "F":
    C = (int(temp[0]) - 32) * 5/9 
    print(f"Temperature in celsius is {C} C.")
else:
    print("Please enter a temperature ending in C or F.")