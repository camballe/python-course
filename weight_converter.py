weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted_weight = weight * 0.45
    print(f"You are {converted_weight} kilos")
elif unit.upper() == "K":
    converted_weight = weight / 0.45
    print(f"You are {converted_weight} pounds")
else:
    print("Please enter valid input!")
