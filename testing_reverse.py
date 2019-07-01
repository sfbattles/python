def reverse_string(input):
    output = ""
    for index, letter in enumerate(input):
        print(f"this is the index {index} of letter  {letter}")

        output = letter + output
        print(f"this is output --> {output}")
    return output


print(reverse_string("nowis the time"))
