
import subject_module
import student_module

# Creating objects of Subject class
subject1 = subject_module.Subject("Math", 90)
subject2 = subject_module.Subject("Science", 85)
subject3 = subject_module.Subject("History", 95)

student1 = student_module.Student("John", 18, "New York")
student2 = student_module.Student("Emma", 17, "London")
student3 = student_module.Student("Michael", 19, "Paris")


student1.add_mark(85)
student1.add_mark(92)

student2.add_mark(78)
student2.add_mark(89)
student2.add_mark(91)

student3.add_mark(95)
student3.add_mark(88)
student3.add_mark(93)


average1 = student1.calc_average()
average2 = student2.calc_average()
average3 = student3.calc_average()

print("Average for", student1.name, ":", average1)
print("Average for", student2.name, ":", average2)
print("Average for", student3.name, ":", average3)