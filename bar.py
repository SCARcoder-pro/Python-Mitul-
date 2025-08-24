import matplotlib.pyplot as plt

students_names = ['John', 'Emily', 'Michael', 'Sarah', 'David'] 
students_marks = [85, 92, 78, 90, 88]
 
marks_perc = []
for x in students_marks:
    res = (x / 50) * 100
    marks_perc.append(res)

print(marks_perc)

def line_chart_of_students_and_marks():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graphs")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

line_chart_of_students_and_marks()

def percentage_bar_chart():
    plt.plot(students_names, students_marks)
    plt.title("Students Percentage Graphs")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

percentage_bar_chart()