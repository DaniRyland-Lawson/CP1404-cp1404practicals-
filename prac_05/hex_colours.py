""" Please choose a colour name and we will tell you the hexadecimal colour code."""
HEX_COLOURS = {"black": "##000000", "blue1": "#0000ff", "DarkGreen": "#006400", "DarkOrange": "#ff8c00",
               "DarkTurquoise": "#00ced1", "DeepPink1": "#ff1493", "DarkViolet": "#9400d3",
               "firebrick1": "#ff3030", "ForestGreen": "#228b22", "DeepSkyBlue1": "#00bfff"}
# print(HEX_COLOURS)


colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(colour_name, "is", HEX_COLOURS[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()

