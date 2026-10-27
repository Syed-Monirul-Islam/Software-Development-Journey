from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC","Dhaka")

eight = ClassRoom("Eight")
nine  = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student
moni = Student("Moni",eight)
toni = Student("Toni",nine)
boni = Student("Boni",ten)
soni = Student("Soni",eight)

school.student_admission(moni)
school.student_admission(toni)
school.student_admission(boni)
school.student_admission(soni)

# adding teacher
rahim = Teacher("Rahim")
karim = Teacher("Karim")
jobber = Teacher("Jobber")

# adding subject
bangla = Subject("Bangla",rahim)
physics = Subject("Physics",karim)
math = Subject("math",jobber)
english = Subject("English",rahim)


eight.add_subject(bangla)
eight.add_subject(math)
eight.add_subject(english)

nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(physics)
nine.add_subject(english)

ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(physics)
ten.add_subject(english)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)
