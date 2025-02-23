#!/usr/bin/env python3

# Requirement for Python Upload 01 about lists and lambda and for each and ...:
# 
# Susanne Peer SWD21
#    

from functools import reduce


def longestWord_with_loop(words): 
    result = ""

    for word in words:
        if len(word) > len(result):
            result = word 
    return result
           
def longestWord_with_recursion(words):
    if len(words) == 1:
        return words[0]
    else:
        differentResult = longestWord_with_recursion(words[1:])
        return words[0] if len(words[0]) > len(differentResult) else differentResult


def longestWord_with_reduce(words):
    result = reduce(lambda x, y: x if len(x) > len(y) else y, words)
    return result


def longestWord_with_max(words):
    result = max(words, key = len)
    return result


#------------------------------------------------------------------- 
#Just for testing.
# The printed output is NOT relevant for grading.
# Evaluation calls functions above and analyses the values returned.
#-------------------------------------------------------------------


quotes = """The Scandal of education is that every time 
you teach something, you deprive a student of the pleasure 
and benefit of discovery.
(Seymour Papert, born February 29, 1928 died July 31 2016)

If debugging is the process of removing bugs, then programming 
must be the process of putting them in.
(Edsger W. Dijkstra)
"""
import re 
# \W to substitute non-word-chars
quotes = re.sub(r'\W',' ',quotes) 
words = quotes.split()


print( longestWord_with_loop( words ) )
print( longestWord_with_recursion( words ) )
print( longestWord_with_reduce( words ) )
print( longestWord_with_max( words ) )

