# Function formats first and last name and returns it in title case

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Blank first or last name"

    title_f_name = f_name.title()
    title_l_name = l_name.title()
    return f"result: {title_f_name} {title_l_name}"


print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))
