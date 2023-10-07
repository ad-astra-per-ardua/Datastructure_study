def solution(spell, dic):
    for word in dic:
        found = False
        for char in spell:
            if char not in word:
                found = False
                break
            found = True
            
        if found:
            return 1
        
    return 2

spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]

# spell = ["p", "o", "s"]
# dic = ["sod", "eocd", "qixm", "adio", "soo"]

result = solution(spell, dic)
print(result)
