def gradingStudents(grades):
    # Write your code here
    list1 = []
    for i in grades:
        if (i%5>=3) and i>=38:
            new = i+(5-i%5)
            list1.append(new)
        else:
            list1.append(i)
    return list1