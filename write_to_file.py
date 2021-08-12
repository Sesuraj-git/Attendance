import sqlite3

atten_conn = sqlite3.connect('student.db')
atten = atten_conn.cursor()

fetch_names = ("SELECT rollno, profile_Name FROM Attendance")
atten.execute(fetch_names)
temp_names = atten.fetchall()


def write_file(updated_names, per_names, out_dir_path):
    print(per_names)
    for i in updated_names:
        for j in per_names:
            if i[0] == j[0]:
                print(i, j)
                j[1] = i[1]
                j.append('P')
    # per_names.index('B19286')
    print(per_names)

    file1 = open(str(out_dir_path) + '/Absent.txt', 'w+')
    file2 = open(str(out_dir_path) + '/Present.txt', 'w+')
    print('Today\'s absentees ')

    for i in per_names:

        if len(i) <= 3 or i[3] != 'P':
            file1.writelines(i[0] + ' ' + i[2] + '\n')
            # print(i[0])
        elif len(i) == 4 and i[3] == 'P':
            file2.writelines(i[0] + ' ' + i[2] + '\n')
            # print(i[0])
    return True
