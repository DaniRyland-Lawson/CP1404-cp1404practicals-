"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# This section gets a test score from the user and shows them their grade status.
# I added a little more to this just to play around with the output.
def main():
    test_score = int(input("Please enter you test score: "))
    print("Your grade is: ", test_score, "out of 100, which is:", grade_status(test_score))

# Used for the user to get their grade status from their test score

def grade_status(test_score):
    if test_score < 0 or test_score >100:
        return("Invalid score")
    elif test_score >= 90:
        return("Excellent")
    elif test_score >= 50:
        return("Passable")
    else:
        return("Bad")
main()