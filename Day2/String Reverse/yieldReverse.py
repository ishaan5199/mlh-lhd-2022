def reverseStr(str):
    n = len(str)
    for i in range(n - 1, -1, -1):
        yield str[i]
        
str = ""

for i in reverseStr(input()):
    str += i
    
print(str)    