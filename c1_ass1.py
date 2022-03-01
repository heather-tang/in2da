import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    result = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+(?=:\sB)", grades)
    return result
    print(result)
grades()



import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()

    # YOUR CODE HERE
    pattern = '''
    (?P<host>\d+\.\d+\.\d+\.\d+)
    (\ -\ )
    (?P<user_name>\S+)
    (\ \[)
    (?P<time>\d+\S*\s\S*\d)
    (\]\ \")
    (?P<request>[A-Z]+\s\S*\s\S*\d)'''
    lst = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        lst.append(item.groupdict())
        #print(list)
        #print(item.groupdict())
    return lst
