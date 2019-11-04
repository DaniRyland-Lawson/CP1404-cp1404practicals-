"""CP1404 Programming II Prac 9 Sorting files."""

import os


def main():
    """Move files from user input based on extension."""
    extension_choices = {}
    os.chdir("FilesToSort.old")
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        file_extension = file_name.split('.')[-1]
        if file_extension not in extension_choices:
            choice = input("What file type would you like to sort {] files into? ".format(file_extension))
            extension_choices[file_extension] = choice
            try:
                os.mkdir(choice)
            except FileExistsError:
                pass

        os.rename(file_name, "{}/{}".format(extension_choices[file_extension], file_name))


main()
