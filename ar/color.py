# Neat color function
red = "31"
yellow = "33"
green = "32"
def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"
