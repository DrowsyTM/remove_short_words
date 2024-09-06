file_name = input("Enter file name: ")
cutoff_length = int(input("Enter cutoff length: "))
print("Processing file...")

file = open(file_name, "r")
edited_file = open("edited.txt", "w")
for line in file:
    if len(line) > cutoff_length:
        edited_file.write(line)

print("Completed. Look at \"edited.txt\"")

file.close()
edited_file.close()