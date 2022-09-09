# Spelling Corrector

Your friend is studying Journalism at university as well as working freelance
for some online outlets, and has to write tons of articles every week. 

They seemed stressed, and so you asked to help out. After some brainstorming,
you came up with the idea of making a program to automatically correct the
spelling of the articles your friend writes.

## Instructions

Write a function `fix_file_spelling` to correct the spelling of a word in a file.

Your function should take in as arguments the name of a file, a misspelled word,
and its replacement. It should find all of the words in the file that match the
misspelled word, replace them with the correct spelling, and then rewrite the
file with the fully corrected version.

## Testing

Test your function manually by running it for some specific files with
misspellings and corrections. 

## Extensions

* Add an optional boolean argument `no_write`, which makes the function print
    the fixed version to standard output instead of rewriting the file.
* Write a function `fix_spellings` that works like `fix_file_spelling`, but
    fixes a list of pairs of words, instead of a single pair of misspelling and
    correction.
