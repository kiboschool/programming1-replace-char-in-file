import sys
from pathlib import Path

# Implement the spelling correction function here
def fix_file_spelling(file, misspelling, correction):
    txt = Path(file).read_text()
    txt = txt.replace(misspelling, correction)
    Path(file).write_text(txt)

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
