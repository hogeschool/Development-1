
def de_tafel_van(input2):
    output = ""

    for i in range(1, 4):
        output += str(i * input2)
        if i < 3:
            output += ", "
    return output


for i in range(1, 3):
    print(de_tafel_van(i))
