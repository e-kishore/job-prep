if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        students.append([name,score])
        
    sort_stud = students.sort(key = lambda x:(x[0],x[1]))
    second_low = sorted(set([student[1] for student in students]))[1]
    for student in students:
        if student[1] == second_low:
            print(student[0])
    