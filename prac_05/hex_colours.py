""" Please choose a colour name and we will tell you the hexadecimal colour code."""

HEX_COLOURS = {"black": "#000000", "blue1": "#0000ff",
               "darkgreen": "#006400", "darkorange": "#ff8c00",
               "darkturquoise=": "#00ced1", "deeppink": "#ff1493",
               "darkviolet": "#9400d3", "firebrick1": "#ff3030",
               "forestgreen": "#228b22", "deepskyblue1": "#00bfff"}
# print(HEX_COLOURS)


colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print("The code for \"{}\" is {}".format(colour_name, HEX_COLOURS[colour_name]))
    else:
        print("Invalid entry")
    colour_name = input("Enter colour name: ")
