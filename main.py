import zlib
from interface import *
from getpass import getpass


def mainLoop():
    os.system("clear")
    print("Enter Master Password")
    masterPassEntry = getpass()
    masterPassInBytes = str.encode(masterPassEntry)
    if zlib.adler32(masterPassInBytes) == <ADLER32 HASHED PASSWORD>:
        interface()
    else:
        os.system("clear")
        print('''
 .'"'.        ___,,,___        .'``.
: (\  `."'"```         ```"'"-'  /) ;
 :  \                         `./  .'
  `.                            :.'
    /        _         _        \ 
   |         0}       {0         |
   |         /         \         |
   |        /           \        |
   |       /             \       |
    \     |      .-.      |     /
     `.   | . . /   \ . . |   .'
       `-._\.'.(     ).'./_.-'
           `\'  `._.'  '/'
             `. --'-- .'
               `-...-' 
   You're not supposed to be here''')



mainLoop()
