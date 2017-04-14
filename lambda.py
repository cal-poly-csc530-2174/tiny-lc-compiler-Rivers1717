#################################################################
# Comments
# 
# I implemented everything and ran some trvial and slightly non trivial test cases, and it looks fine but you should probs give it closer inspection.
# The parsing aspect is pretty much done (besides println), so what ever needs to be done should just be random other stuff that doesnt take too long. 
# Im 100% sure you can write the parse function more efficiently but I was too lazy / tired, so feel free to touch it up if you want to.
#################################################################
# Bugs / Fixes
#
# TODO: println: I think he said this should evaluate to 0, im not sure, but it shouldnt be too hard to to include
# TODO: command line: The program needs to read a file from the command line if I recall correctly
# TODO: output: The program should write to a file rather than print
# TODO: JavaScript: Havent tested this yet, output looks good when I run though so this is probs fine but test it anyways
# TODO: Becuase sexpdata stuff seems to encapsuate everything in a one element list, I parse the only element of the list rather than the list itself.
#       As a result, nums and ids cannot be passed in without being parenthesized. Only really an issue when they're by themselves, you can probably just do a quick check before you parse.
# TODO: I may have missed something so double check




from sexpdata import loads, dumps
import sys


def parse(l=[]):
   fo.write('(')
   temp = dumps(l[0], str_as='symbol')
   if len(l) == 1:
      fo.write(temp)
   if len(l) == 2:
      # Println should be a subsection of this 
      if isinstance(l[0], list):
         parse(l[0])
      else:
            if temp == "println":
                  fo.write("function(x){console.log(x); return 0} ")
                  if isinstance(l[1], list):
                        parse(l[1])
            else:
                  fo.write(dumps(l[0], str_as='symbol'))
      fo.write('(')
      if isinstance(l[1], list):
         parse(l[1])
      else:
         fo.write(dumps(l[1], str_as='symbol'))
      fo.write(')') 
   if len(l) == 3:
      if temp == '+' or temp == '*':
         if isinstance(l[1], list):
            parse(l[1])
         else:
                  fo.write(dumps(l[1], str_as='symbol'))
         fo.write(" " + temp + " ")
         if isinstance(l[2], list):
            parse(l[2])
         else:
            fo.write(dumps(l[2], str_as='symbol'))
      if temp.isalpha():
         fo.write("function" + dumps(l[1], str_as='symbol') + "{ return ")
         if isinstance(l[2], list):
            parse(l[2])
         else:
            fo.write(dumps(l[2], str_as='symbol'))
         fo.write("}")
   if len(l) == 4:
      if isinstance(l[1], list):
         parse(l[1])
      else:
         fo.write(dumps(l[1], str_as='symbol'))
      fo.write(" <= 0 ? ")
      if isinstance(l[2], list):
         parse(l[2])
      else:
         fo.write(dumps(l[2], str_as='symbol'))
      fo.write(" : ")
      if isinstance(l[3], list):
         parse(l[3])
      else:
         fo.write(dumps(l[3], str_as='symbol'))
   fo.write(')')
      

with open(sys.argv[1], "r") as input:
   fo = open("output.js", "wb")
   for line in input:
      stri = loads('(' + line + ')') 
      if line[0] != '(':
            fo.write(line)
      else: 
            parse(stri[0])
      fo.write('\n')
      