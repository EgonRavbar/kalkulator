print("Zdravo, dobrodosel v kalkulatorju!")

x = int(raw_input("Vpisi stevilo"))
y = raw_input("Vpisi operacijo (+,-,*,/)")
z = int(raw_input("Vpisi stevilo"))

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)

odgovor = "da"
while odgovor == "da":
    odgovor = raw_input("Ponovno racunanje?(da/ne)")
    if odgovor == "ne":
        print("Hvala in nasvidenje")
        break
    else:
        x = int(raw_input("Vpisi stevilo"))
        y = raw_input("Vpisi operacijo (+,-,*,/")
        z = int(raw_input("Vpisi stevilo"))

        if y == "+":
            print(x + z)
        elif y == "-":
            print(x - z)
        elif y == "*":
            print(x * z)
        elif y == "/":
            print(x / z)