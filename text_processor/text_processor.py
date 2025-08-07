# Create input.txt with sample content
with open("input.txt", "w") as f:
    f.write("Power Learn Project is empowering Africa.\n")
    f.write("We are learning Python.\n")
    f.write("File handling is fun.\n")
    f.write("This is the fourth line.\n")
    f.write("And here comes the fifth.\n")

# Read input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Count words and convert to uppercase
word_count = len(content.split())
upper_content = content.upper()

# Write to output.txt
with open("output.txt", "w") as f:
    f.write(upper_content)
    f.write(f"\n\nWORD COUNT: {word_count}")

# Print success message
print("✅ output.txt has been created successfully!")
