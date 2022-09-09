# Implement the spelling correction function here
def fix_file_spelling(file, misspelling, correction):
    pass



# This code will run your function and pass in arguments from the command line
# If you run the program like this:
#
# python3 main.py article.txt teh the
#
# Then it will call `fix_file_spelling` with arguments "article.txt", "teh", and "the"
if __name__ == "__main__":
    try:
        _, file, misspelling, correct = sys.argv
    except:
        print("Usage: python3 main.py [file] [misspelling] [correction]")
        exit()

    fix_file_spelling(file, misspelling, correction)
