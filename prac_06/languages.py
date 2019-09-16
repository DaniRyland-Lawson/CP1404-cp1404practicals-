""" CP1404 Practicals
Programming Languages"""

from prac_06.ProgrammingLanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("Dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
