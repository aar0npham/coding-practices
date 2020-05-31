'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''

test1 = ['dog', 'deer', 'deal']
test2 = ['facebook', 'twitter', 'compromise', 'testcar']

def prefix(list_string, pre):
    filtered = []
    for i in list_string:
        if pre in i:
            filtered.append(i)
    return filtered

print(prefix(test1, 'de'))
print(prefix(test2, 'face'))
