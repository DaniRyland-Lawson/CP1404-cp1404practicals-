"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# In this section, it took me a little while to realise it is best in order. Highest to lowest.

score = float(input("Enter score: "))
if score < 0 or score >100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")