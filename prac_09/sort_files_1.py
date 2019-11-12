"""CP1404 - Programming II Prac 9- Sorting files """

import os


def main():
    """Sort files into folders with the same file extension."""
    os.chdir("FilesToSort")
    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        file_extension = file_name.split('.')[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass

        print("{}/{}".format(file_extension, file_name))
        os.rename(file_name, "{}/{}".format(file_extension, file_name))


main()
