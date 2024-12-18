# Python script to write and read a text file

# Write to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python scripting is fun!")

# Read from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
