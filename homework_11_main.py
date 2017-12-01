#homework 11 main
import homework_11
from homework_11 import Student
from homework_11 import Course
from homework_11 import Enrollment
from homework_11 import Gradebook

student_record = homework_11.Gradebook()

keep_going = 'y'

while keep_going == 'y':
    enrollment_id = int(input("please input an enrollemnt id"))
    Grade = input("please input a letter grade for this enrollment")
    while Grade.upper() != "A" and Grade.upper() != "B" and Grade.upper() != "C" and Grade.upper() != "D" and Grade.upper() != "F" and Grade.upper() != "I" and Grade.upper() != "W":
                        Grade = input("Please input a valid letter Grade A,B,C,D,F,I,W")
    if enrollment_id in student_record.enrollments:
        student_record.enrollments[enrollment_id].changeGrade(Grade)
    else:
        print("This enrollment is not in our records")
    keep_going = input(" enter y to keep going or anything else to stop")

print("enrollment_id  ", "course title    ", "credit hours  ", "student name         ", "grade  ")
for entry in student_record.enrollments:
    student_record.enrollments[entry].displayEnrollment()





        
        
    
