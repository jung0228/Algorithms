import string

def solution(new_id):
    answer = ''
    n = len(new_id)
    #1
    list_lower = list(string.ascii_lowercase)
    list_upper = list(string.ascii_uppercase)
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special = ['-', '_', '.']
    for i in range(n):
        if new_id[i] in list_upper:
            index = list_upper.index(new_id[i])
            l = list(new_id)
            l[i] = list_lower[index]
            new_id = "".join(l)
    #2 
    l = list(new_id)
    for i in range(len(l)):
        if l[i] not in list_lower and l[i] not in num and l[i] not in special:
            l[i] = ""
    new_id = "".join(l)

    #3
    l = list(new_id)
    for i in range(len(l)-1):
        if l[i] == '.' and l[i+1] == '.':
            l[i] = ""
    new_id = "".join(l)

    #4
    l = list(new_id)
    if l[0] == '.':
        l[0] = "" 
    
    if l[-1] == '.':
        l[-1] = ""
    new_id = "".join(l)
    
    #5
    l = list(new_id)
    if len(l) == 0:
        l.append("a")
    new_id = "".join(l)

    #6
    l = list(new_id)
    l = l[:15]
    if l[-1] == '.':
        l[-1] = ""
    new_id = "".join(l)

    #7
    l = list(new_id)
    if len(l) == 1:
        l.append(l[0])
        l.append(l[0])
    if len(l) == 2:
        l.append(l[1])
    new_id = "".join(l)

    answer = new_id
    return answer