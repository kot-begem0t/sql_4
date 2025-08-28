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

def processing_name(name):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    name_s = str(name)
    res = []
    for l in name_s:
        if (l in lower) or (l in upper):
            res.append(l.lower())
        else:
            return 'need use only english letters'
    n = res[0].upper()
    res[0] = n
    return ''.join(res)

def processing_email(email):
    email_s = str(email)
    res = []
    i = 0
    a = '@'
    for e in email_s:
        if e == a:
            i += 1
            if i >= 2:
                return 'symbol "@" should only one'
        res.append(e)
    if a not in res:
        return 'email have to symbol "@" '
    return ''.join(res)


number = '+7(902)-723-8535'
name = 'BOGDAN'
email = 'mail@.com'

print(proc_phone(number))
print(processing_name(name))
print(processing_email(email))