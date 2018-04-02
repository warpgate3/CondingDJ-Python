a = input('input version ==> ')

args = a.split(" ")
v1_list = args[0].split('.')
v2_list = args[1].split('.')

def com(v1 , v2):
    i = 0
    for v in v1_list:
        if v > v2_list[i]:
            return '.'.join(v1)+' > '+'.'.join(v2)
        elif v < v2_list[i]:
            return '.'.join(v1)+' < '+'.'.join(v2)
        i = i + 1

    return '.'.join(v1)+'='+'.'.join(v2)


print(com(v1_list, v2_list))



