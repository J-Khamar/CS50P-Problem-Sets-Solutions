import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Input: ")
        names.append(name)
    except EOFError:
        print("")
        break

print(f"Adieu, adieu, to {p.join(names)}")
