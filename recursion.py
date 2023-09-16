# Algorithm for checking pallindrome of strings

# print powerset of a string

def powset(s, i, curr):
    if i == len(s):
        print(curr)
        return
    powset(s, i + 1, curr + s[i])
    powset(s, i + 1, curr)

string = "abc"
powset(string, 0, "")

