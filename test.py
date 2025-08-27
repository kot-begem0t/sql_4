import string

def proc_phone(number: str):
    allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = '+7'
    res = []
    number_s = str(number)
    for n in number_s:
        if n in allowed:
            res.append(n)
    if len(res) != 11:
        return 'incorrect number of digits'
    if res[1] != '9':
        return 'code should start with 9, for example: 902, 920, 923'
    if res[0] == '7' or res[0] == '8':
        res[0] = num
        return ''.join(res)
    else:
        return 'incorrect format of number phone, it should start 7 or 8'


def check_name(name):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    name_s = str(name)
    for n in name:
        if (n in lower) or (n in upper):
            pass
        else:
            return 'need use only english letters'
    return True

number = '+7(902)-723-8535'
name = 'Bogdan'

allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(proc_phone(number))
print(check_name(name))

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)