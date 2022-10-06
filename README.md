# vocab
command line vocab training quiz tool written in python

# usage
needs a csv file of vocabulary to generate the quiz from, which should be formatted with the words to learn in the first column with an arbitrary number of additional columns containing definitions of the word on that line.

the .csv included in the repo gives a short working example of some basic toki pona vocabulary.

when run in the command line the program interactively prompts for a file to generate the quiz from.

## sample output

```
Welcome to Rowan's vocab test tool!
type 'help' for a detailed help, or enter the name of the vocab file to use
vocab

how many rounds do you want to try?
5

starting test!
==============
Question 1
what's the definition of "suwi"?
sweet
Correct!

Question 2
what's the definition of "waso"?
bird
Correct!

Question 3
what's the definition of "waso"?
dog
oops! the definitions are actually: 
	bird
	flying creature
	winged animal
```

# todo
add support for config directory location with universally accessible vocab files
