#!/usr/bin/env python3

import sys
import random
import os.path

def get_entry(line):
    entry = line.split(",")
    i = 0
    while i < len(entry):
        item = entry[i]
        entry[i] = item.strip()
        i += 1
    return entry

def test(rounds, material):
    i = 0
    score = 0
    lines = material.readlines()
    while i < rounds:
        line_num = random.randrange(0, len(lines))
        entry = get_entry(lines[line_num])
        print("Question " + str(i + 1))
        answer = input("what's the definition of \"" + entry[0] + "\"?\n")
        if answer in entry[1:]:
            print("Correct!\n")
            score += 1
        else:
            print("oops! the definitions are actually: ")
            for item in entry[1:]:
                print("\t" + item)
            print("")
        i += 1
    print("test complete!")
    print("you scored: " + str(score) + " out of " + str(rounds))

def main():
    print("\nWelcome to Rowan's vocab test tool!")
    print("type 'help' for a detailed help, or enter the name of the vocab file to use")
    input1 = input().strip()
    match str(input1):
        case "help" | "Help":
            print("\nRowan's vocab test tool:\n\n\tgenerates a random quiz from a csv.\n\n\tcsv should have format:\n\t\t word,definition,[definitions, ...]\n\n\tsee https://github.com/gender-delenda-est/vocab for details\n")
            return 0
        case _:
            if os.path.exists(str(input1)):
                filename = str(input1)
            elif os.path.exists(str(input1) + ".csv"):
                filename = str(input1) + ".csv"
            else:
                print("oops, i couldn't find that file!")
                return 0
    rounds = input("\nhow many rounds do you want to try?\n")
    rounds = int(rounds)
    vocab = open(filename)
    print("\nstarting test!")
    print("==============")
    test(rounds, vocab)

main()
