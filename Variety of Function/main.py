def format(f_name, l_name):
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    print(f"{formatted_f} {formatted_l}")


format("usan", "zaman")


def format(f_name, l_name):
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    return f"{formatted_f} {formatted_l}"


formatted_name = format("lional", "messi")
print(formatted_name)


def format(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"You didn't prvide valid inputs"
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    return f"name:{formatted_f} {formatted_l}"


print(format(input("What is your first name ?  "), input("what is your last name ?")))
