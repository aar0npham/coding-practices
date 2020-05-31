'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def isString(string):
    poped = [string[0]]
    for c in string[1:]:
        if (c ==')' and poped[-1]=='(') or (c==']' and poped[-1]=='[') or (c=='}' and poped[-1]=='{'):
            poped.pop()
        else:
            poped.append(c)
    if poped:
        return False
    else:
        return True

s1 = "([])[]({})"
s2 = "([)]"
s3 = "((()"
print(isString(s1))
print(isString(s2))
print(isString(s3))
