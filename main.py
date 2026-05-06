import sys

# Implement the spelling correction function here
def fix_file_spelling(filename, wrong_word, correct_word):
    # Read file
    with open(filename, "r") as f:
        content = f.read()

    # Fix spelling
    # Fix spelling
    fixed_content = content

    fixed_content = fixed_content.replace(wrong_word.lower(), correct_word.lower())
    fixed_content = fixed_content.replace(wrong_word.capitalize(), correct_word.capitalize())
    fixed_content = fixed_content.replace(wrong_word.upper(), correct_word.upper())

    # Write back to file
    with open(filename, "w") as f:
        f.write(fixed_content)

# This code will run your function and pass in arguments from the command line
# If you run the program like this:
#
# python3 main.py article.txt teh the
#
# Then it will call `fix_file_spelling` with arguments "article.txt", "teh", and "the"
if __name__ == "__main__":
    print(sys.argv)
    try:
        _, file, misspelling, correction = sys.argv
    except:
        print("Usage: python3 main.py [file] [misspelling] [correction]")
        exit()

    fix_file_spelling(file, misspelling, correction)
