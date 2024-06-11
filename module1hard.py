grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students[0] = 'Aaron'
students[1] = 'Bilbo'
students[2] = 'Johnny'
students[3] = 'Khendrik'
students[4] = 'Steve'
a = int(sum(grades[0])) / len(grades[0])
b = int(sum(grades[1])) / len(grades[1])
j = int(sum(grades[2])) / len(grades[2])
k = int(sum(grades[3])) / len(grades[3])
s = int(sum(grades[4])) / len(grades[4])
average_score = [a, b, j, k, s]
average_score_of_students = dict([[students[0],average_score[0]],[students[1],average_score[1]],[students[2],average_score[2]],[students[3],average_score[3]],[students[4],average_score[4]]])
print(average_score_of_students)