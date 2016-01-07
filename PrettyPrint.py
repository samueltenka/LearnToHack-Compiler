def pretty_print(string, minlen=10):
    if type(string)==type(0.0) or ' ' not in string:
        string = str(round(float(string),4))
    else:
        string = string[:3] + ';'.join(string.split(' ')[1:])
    return string+' '*(minlen-len(string))
