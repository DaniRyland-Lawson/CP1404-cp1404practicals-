# defining what the output file is
OUTPUT_FILE = "name.txt"

# open output file for writing (this creates a new file if it doesn't exist)
out_file = open(OUTPUT_FILE, 'w')

user_name = input(str("Please enter your name: "))
print("{}".format(user_name), file=out_file)
out_file.close

in_file = open("name.txt", "r")
first_line_str = in_file.readline()
first_line_str
'First line\n'

for line_str in (in_file):
    print("Name is: {} ".format(line_str))

''
in_file.close()

