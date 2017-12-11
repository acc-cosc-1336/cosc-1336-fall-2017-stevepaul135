#Stephen Paul's 12th homework assignment

class Person:
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name

    def displayPerson(self):
        print("This persons name is", self.name)
        
    

class Student(Person):
    def __init__(self, student_id, first_name, last_name, enroll_date):
        self.student_id = student_id
        self.__enrollDate = enroll_date
        Person.__init__(self, first_name, last_name)

    def displayStudentInfo(self):
        print(self.student_id, self.name, self.__enrollDate)


class Professor(Person):
    def __init__(self, professor_id, first_name, last_name, hire_date):
        self.hire = hire_date
        self.professor_id = professor_id
        Person.__init__(self, first_name, last_name)

    def displayProfessoInfo(self):
        print(self.professor_id, self.name, self.hire)
    

class Course:
    def __init__(self, course_id, title, credit_hours, professor):
        self.course_id = course_id
        self.title = title
        self.hours = credit_hours
        self.professor = professor  #Should be a professor object

    def displayCourseInfo(self):
        print(self.course_id, self.title, self.hours, self.professor.name)
    

class Enrollment:
    def __init__(self, enrollment_id, student, course, grade):
        self.enrollment_id = enrollment_id
        self.course = course   #should be a course object
        self.student = student #should be a student object
        self.grade = grade

    def displayEnrollment(self): 
        print(format(self.enrollment_id, '3'),"        ", format(self.course.title, '17'), format(self.course.hours,'12'), '  ', format(self.student.name,'24'), format(self.grade, '10'))

    def changeGrade(self,new_grade):
        self.grade = new_grade




class Transcript:
    def __init__(self, student):
        self.student_enrollments = {}
        self.student = student  #Should be a student object 
        
    def addEnrollments(self, enrollment):  #enrollment should be an enrollment object
        self.student_enrollments[enrollment.enrollment_id] = enrollment

    def displayTranscript(self):
        print("Name ", self.student.name)
        print("Class          ", "Credit Hours", "Credit Points", "Grade Points", "Grade")
        creditpoint = ' '
        gradepoint = ' '
        Total_Credit_hours = 0 
        Total_Grade_Point = 0
        for entry in self.student_enrollments:
            if self.student_enrollments[entry].grade == 'A':
                creditpoint = 4
            elif self.student_enrollments[entry].grade == 'B':
                creditpoint = 3
            elif self.student_enrollments[entry].grade == 'C':
                creditpoint = 2
            elif self.student_enrollments[entry].grade == 'D':
                creditpoint = 1
            elif self.student_enrollments[entry].grade == 'F':
                creditpoint = 0
            elif self.student_enrollments[entry].grade == "I":
                creditpoint  = " "
            elif self.student_enrollments[entry].grade == 'W':
                creditpoint  = " "
            else:
                creditpoint = " "  #Case only when the Grade in an Enrollment hasn't been Updated

            if creditpoint != " ":
                gradepoint = creditpoint * self.student_enrollments[entry].course.hours
                Total_Credit_hours += self.student_enrollments[entry].course.hours
                Total_Grade_Point += gradepoint
                print(format(self.student_enrollments[entry].course.title, '15'), format(self.student_enrollments[entry].course.hours, "11"), format(creditpoint, '12'), format(gradepoint, '13'),"     ", format(self.student_enrollments[entry].grade,'5'))
            else:
                gradepoint = " "
                print(format(self.student_enrollments[entry].course.title, '15'), format(self.student_enrollments[entry].course.hours, "11"), format(creditpoint, '12'), format(gradepoint, '13'),"     ", format(self.student_enrollments[entry].grade,'5'))

        print('-' * 60)
        print(format(Total_Credit_hours, "26"), format(Total_Grade_Point, "25"))
        print( "GPA :", Total_Grade_Point/Total_Credit_hours)
            
        
        
class Gradebook:
    def __init__(self):
        self.students = {}

        #add to student dictionary
        s = Student(1, "Carson", "Alexander", "09012005")
        self.students[s.student_id] = s
        s = Student(2, "Meredith", "Alonso", "09022002")
        self.students[s.student_id] = s
        s = Student(3, "Arturo", "Anand", "09032003")
        self.students[s.student_id] = s
        s = Student(4, "Gytis", "Barzdukas", "09012001")
        self.students[s.student_id] = s
        s = Student(5, "Peggy", "Justice", "09012001")
        self.students[s.student_id] = s
        s = Student(6, "Laura", "Norman", "09012003")
        self.students[s.student_id] = s
        s = Student(7, "Nino", "Olivetto", "09012005")
        self.students[s.student_id] = s
           
        self.professors = {}

        #professor_id   first_name   last_name  hire_date
        p = Professor(1, "Kim", "Abercrombie", "1995-03-11") 
        self.professors[p.professor_id] = p

        p = Professor(2, "Fadi", "Fakhouri", "2002-07-06") 
        self.professors[p.professor_id] = p

        p = Professor(3, "Roger", "Harui", "1998-07-01") 
        self.professors[p.professor_id] = p

        p = Professor(4, "Candace", "Kapoor", "2001-01-15")
        self.professors[p.professor_id] = p

        p = Professor(5, "Roger", "Zheng", "2004-02-12") 
        self.professors[p.professor_id] = p
        

        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3, self.professors[1])
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3, self.professors[2])
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3, self.professors[3])
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3, self.professors[5])
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4, self.professors[5])
        self.courses[c.course_id] = c


        self.enrollments = {}

        #add enrolled students into courses
        enroll_id = 11050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050]," ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045], " ")
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141], " ")
        self.enrollments[enroll_id] = enrollment


