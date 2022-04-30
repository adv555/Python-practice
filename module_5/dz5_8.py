grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    list=[]
    length=0
    for student, grade in students.items():
        length+=1
        list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(length,student,students[student], grades[grade]))
    
    return list

   
    # length=0

    # for student in students:
    #     length+=1
    #     # print(student, students[student])
    #     print("{:>4}|{:<10}|{:^5}|{:^5}".format(length,student,students[student],grades[students[student]]))
    
    

# print(formatted_grades(students))
for el in formatted_grades(students):
    print(el)