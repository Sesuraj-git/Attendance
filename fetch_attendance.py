import sqlite3
import PyQt5


# opening database
def ececute_file(path):
    atten_conn = sqlite3.connect('student.db')
    atten = atten_conn.cursor()

    fetch_names = ("SELECT rollno, profile_Name, name FROM Attendance")
    atten.execute(fetch_names)
    temp_names = atten.fetchall()

    db_names = []
    per_names = []
    for t in temp_names:
        db_names.append(str(t[1]).upper())
        per_names.append([str(t[0]).upper(), str(t[1]).upper(),str(t[2]).upper()])

    # open file
    file1 = open(path[0], "r+")
    names_today = file1.readlines()
    file1.close()

    names_to_update = []
    present_today = []

    for name in names_today:
        name = name.split('\n')[0].upper()
        if name.upper() in db_names:
            id = db_names.index(name)
            if len(per_names[id]) > 3:
                per_names[id][3] = 'P'
                # print('yes')
            elif len(per_names[id]) == 3:
                per_names[id].append('P')
                # print('no', per_names[id])
            else:
                print('Something is not well for index of per_names \n call developer @ 8943627235')
                return False
            present_today.append(name)

        else:
            names_to_update.append(name)

    # print(names_to_update)
    # print(present_today)
    retext = ['', '']
    retext[0] = names_to_update
    retext[1] = per_names
    return retext

    '''print('Couldnt match names for ', len(names_to_update), 'Enter your response')
    print('1. Assign roll numbers \n2. Ignore all')
    c = input()

    rollnos = []
    if c == '1':
        for name in names_to_update:
            print('0 or Enter: to ignore \nRoll number for ', name)
            rollnos.append([input(), name])
    print(rollnos)
    print(present_today)

    file1 = open('Present.txt', 'w+')
    file2 = open('Abscent.txt', 'w+')
    print('Todays absentiees ')

    for i in per_names:

        if len(i) <= 2 or i[2] != 'P':
            file1.writelines(i[0] + '\n')
            print(i[0])
        elif len(i) == 3 and i[2] == 'P':
            file2.writelines(i[0] + '\n')
            print(i[0])
    return True
'''
