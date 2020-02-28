#!/usr/bin/python

import sys
import math

def print_99bottles_lyrics(howmany=99):
    ''' this program prints lyrics of '99bottles' poem
    ...
    99 bottles of beer on the wall, 99 bottles of beer.
    Take one down and pass it around, 98 bottles of beer on the wall.
    ..
    '''
    stanza1 = lambda x : (str(x) if x > 0 else "no more")+" bottle"+ \
            ('' if x == 1 else 's')+" of beer"
    stanza2 = " on the wall"
    stanza3 = "\nTake one down and pass it around, "

    for i in reversed(range( 1, howmany+1 )) :
        print(stanza1(i)+stanza2+", "+stanza1(i)+"." +      \
              stanza3+stanza1(i-1)+stanza2+".\n\n")
    print(stanza1(0).capitalize()+stanza2+", "+stanza1(0)+  \
          ".\nGo to the store and buy some more, " +        \
          stanza1(howmany)+ stanza2+".\n\n")             

def main():

    args=sys.argv[1:]

    
    print_99bottles_lyrics(5)

    
if __name__ =='__main__' :
    main()
