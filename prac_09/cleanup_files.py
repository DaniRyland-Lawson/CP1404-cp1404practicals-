"""
CP1404/CP5632 Practical
Cleanup song lyrics file names

Not complete. Can not figure out
"""
import os


def main():
    """Clean up song lyric filenames."""
    os.chdir('Lyrics')
    try:
        os.mkdir("temp_lyrics")
    except FileExistsError:
        pass

    file_names = [name for names in os.listdir('.') if names.endswith('.TXT')]
    print(file_names)

    for name in file_names:
        new_name = name[:name.find(".")] + ".txt"
        print(new_name)
    # Change to desired directory

    for directory_name, subdirectories, filenames in os.walk("."):
        print("Directory: ", directory_name)
    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in filenames:
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, get_fixed_filename(filename))
        os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    return new_name


main()
