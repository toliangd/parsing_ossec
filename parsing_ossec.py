# dict = {'id': {'Name':[], 'IP':[], 'Condition':[]}}
dct = {}
lst = ['ID: 10, Name: ss-n-02, IP: 0.6.9.4, Active',\
        'ID: 11, Name: Sds, IP: 1.6.1.5, Active',\
        'ID: 12, Name: Sps-01, IP: 1.6.9.6, Active',\
        'ID: 14, Name: vm-2, IP: 0.9.8.5, Active',\
        'ID: 16, Name: node-1, IP: 0.9.9.0, Active',\
        'ID: 15, Name: acs34-1, IP: 2.1.3.8, Active',\
        'ID: 17, Name: vm-2, IP: 2.1.4.4, Active]']


def param(lst):
    for i in lst:
        blank_1 = i.split(", ")
        for j in blank_1:
            blank_2 = j.split(": ")
            if blank_2[0] == 'ID':
                id = blank_2[1]
            if blank_2[0] == 'Name':
                name = blank_2[1]
            if blank_2[0] == 'IP':
                ip = blank_2[1]
            if blank_2[0] == 'Active':
                condition = blank_2[0]
        dict1(id, name, ip, condition)


def dict1(a,b,c,d):
    dct[a] = {'Name':[],'IP':[],'Condition':[]}
    dct[a]['Name'].append(b)
    dct[a]['IP'].append(c)
    dct[a]['Condition'].append(d)

def all_id(lst):
    param(lst)
    return(list(dct.keys()))

def all_ip(lst):
    param(lst)
    list_ip = []
    for i in list(dct.keys()):
        list_ip.append(dct[i]['IP'])
    return list_ip

def all_name(lst):
    param(lst)
    list_name = []
    for i in list(dct.keys()):
        list_name.append(dct[i]['Name'])
    return list_name

all_ip(lst)