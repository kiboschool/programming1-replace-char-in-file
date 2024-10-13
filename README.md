# Spelling Corrector

Your friend is studying Journalism at university as well as working freelance
for some online outlets, and has to write tons of articles every week. 

They seemed stressed, and so you asked to help out. After some brainstorming,
you came up with the idea of making a program to automatically correct the
spelling of the articles your friend writes.

## Steps

Write a function `fix_file_spelling` to correct the spelling of a word in a file.

Your function should take in 3 arguments: the name of a file, a misspelled word,
and its replacement. It should find all of the words in the file that match the
misspelled word, replace them with the correct spelling, and then rewrite the
file with the fully corrected version.

## Starter Code

`main.py` starts with an empty function `fix_file_spelling`, which you need to
fill in. The code at the end of the file parses the arguments to the program and
passes them as arguments to your function.

That way, you can run the program this way:

```
python3 main.py article.txt Teh The
```

and it will pass `"article.txt"`, `"Teh"`, and `"Teh"` as arguments to your
`fix_file_spelling`.

## Testing

Test your function manually by running it for some specific files with
misspellings and corrections. 

The file `article.txt` has several misspellings ('Teh' for 'The', 'bcame' for
'became', and 'smoe' for 'some'). You can try fixing each of these.

## Bonus Task

* Make your function respect case, so that it works to fix 'Teh' -> 'The' and 'teh' -> 'the', if either version is passed in as the misspelling.
* Add an optional boolean argument `no_write`, which makes the function print
    the fixed version to standard output instead of rewriting the file.
* Write a function `fix_spellings` that works like `fix_file_spelling`, but
    fixes a list of pairs of words, instead of a single pair of misspelling and
    correction.
