import doctor
import teacher
import student

Tuan = doctor.Doctor(name="Tuan", yob=2000, specialist="Nurse")

Ngoc = teacher.Teacher(name="Ngoc", yob=1998, subject="Math")

Hieu = student.Student(name="Hieu", yob=2005, grade=9)


print(Tuan.describe())
