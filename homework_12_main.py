#homework 12 main
import home_work_12
from home_work_12 import Student
from home_work_12 import Professor
from home_work_12 import Course
from home_work_12 import Enrollment
from home_work_12 import Gradebook

student_record = home_work_12.Gradebook()

keep_going = input('enter y to update a grade for a course or type display to print a transcript')

while keep_going == 'y' or keep_going == "display" :
    if keep_going == 'y':
        enrollment_id = int(input("please input an enrollemnt id"))
        Grade = input("please input a letter grade for this enrollment")
        while Grade.upper() != "A" and Grade.upper() != "B" and Grade.upper() != "C" and Grade.upper() != "D" and Grade.upper() != "F" and Grade.upper() != "I" and Grade.upper() != "W":
            Grade = input("Please input a valid letter Grade A,B,C,D,F,I,W")
        if enrollment_id in student_record.enrollments:
            student_record.enrollments[enrollment_id].changeGrade(Grade.upper())
        else:
            print("This enrollment is not in our records")
        keep_going = input(" enter y to update a grade ,display to print a transcript, or anything else to stop")  
    else:
        student_ID = int(input("please enter a student id"))
        if student_ID in student_record.students:
            student_transcript =home_work_12.Transcript(student_record.students[student_ID])
            for entry in student_record.enrollments:
                if student_record.enrollments[entry].student.student_id == student_ID:
                   student_transcript.addEnrollments(student_record.enrollments[entry])
                else:
                    nada = 'nada'  #Do nothing
            student_transcript.displayTranscript()
        else:
            print("This student id is not in our records")
        keep_going = input(" enter y to update a grade ,display to print a transcript, or anything else to stop")     

    
