'''
Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid. validBraces should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets, and open and closed curly braces. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

What is considered Valid? A string of braces is considered valid if all braces are matched with the correct brace.
For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.

Examples:
validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true
'''
#################
def validBraces(s):
	while '{}' in s or '()' in s or '[]' in s:
		s=s.replace('{}','')
        s=s.replace('[]','')
        s=s.replace('()','')
    return s==''



#################
braces = '() [] {}'.split()
def validBraces(s):
  while any(b in s for b in braces):
      for b in braces:
          s = s.replace(b, '')
  return not s



################
def validBraces(s):
    while True:
        o = s
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        if o == s:
            break
    return s == ''



#################
def validBraces(string):
	brace_map = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for brace in string:
        if brace in list(brace_map.keys()):
            stack.append(brace_map[brace])
        elif len(stack) == 0 or stack.pop() != brace:
        	return False
    return len(stack) == 0



#################
def validBraces(s, previous = ''):
	while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  	return not s


#############
def validBraces(string):
    stack = []
    for c in string:
        if c in "({[":
            stack.append(c)
        elif c in ")}]" and stack and "({[".index(stack[-1]) == ")}]".index(c):
            stack.pop()
        else:
            return False

    return len(stack) == 0



##############
def validBraces(string):
    stack = []
    for x in string:
        if stack and (stack[len(stack) - 1] + x) in {'[]': True, '{}': True, '()': True}:
            stack.pop()
        else:
            stack.append(x)
    return not stack



###############
def validBraces(string):
    _map = {'}':'{', ']':'[', ')': '('}
    red = lambda s, e: s[:-1] if s and s[-1] == _map.get(e) else s + [e]
    return reduce(red, string, []) == []



################
def validBraces(string):
    matches = [s.split() for s in ['( )', '{ }', '[ ]']]
    return not reduce(lambda a, b: a[:-1] if a and [a[-1], b] in matches else a + [b], string, [])




################
def validBraces(s):
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack.pop() + c not in ["()", "[]", "{}"]:
                return False
    return len(stack) == 0


###################
import re

def validBraces(s):
    rx = '(\(\)|{}|\[])'
    while len(s):
        if not re.search(rx, s):
            return False
        s = re.sub(rx, '', s)
    return True




