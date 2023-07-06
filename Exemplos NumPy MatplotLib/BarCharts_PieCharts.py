import numpy as np
import matplotlib.pyplot as plt

# .zeros((arrays, rows, columns))
a = np.zeros((3, 6, 4)) 
b = np.full((3,4,2), 4)
c = np.linspace(0,1000, 100)
#print(a)
#print(b)
#print(c)
print(b.sum())
print(np.median(b))

x = [5,8,10] 
y = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.grid()  # creates a grid
plt.show()


python = (45, 67, 23, 50)
java = (50, 50, 23, 14)
networking = (60, 20, 56, 22)
machine_learning = (45, 23, 40, 22)

people = ["Bob", "Anna", "John", "Mark"]

index = np.arange(4)

plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="java")
plt.bar(index + 0.4, networking, width=0.2, label="networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="machine_learning")

plt.title("IT Skill Levels")
plt.xlabel("Person")
plt.ylabel("Skill level")
plt.xticks(index + 0.2, people)
plt.legend(loc='upper left')
plt.ylim(0, 120)

plt.show()

nationalities = ["American", "German", "French", "Other"]
students = [60, 23, 21, 34]

pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)

plt.pie(students, labels=nationalities, autopct="%2.f%%", counterclock=False,
        startangle=90)
plt.title("Student Nationality")

plt.show()