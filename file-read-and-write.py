

# Step 1: Read the original file
with open("file-test.txt", "r") as infile:
    data = infile.read()

# Step 2: Modify the content (append a string)
modified = data + "\nThis is appended to the file" 

# Step 3: Write the modified content into a new file
with open("file-test-modified.txt", "w") as outfile:
    outfile.write(modified)
    print(modified)