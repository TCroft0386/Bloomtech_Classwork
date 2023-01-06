import numpy as np
class student:
    def __init__(self,grade,passing,totalgrade):
        self.passing = passing
        self.grade = grade
        self.totalgrade = totalgrade
    def assignmentsub():
        return 'Assignment has been submitted'
    
    def gradeaftertest(grade):
        return grade/100

class BloomtechStudent(student):
    def __init__(self,grade,Name,Age,Cohort,totalgrade=100,passing=70):
        super().__init__(grade,passing,totalgrade)
        self.Cohort = Cohort
        self.Name = Name
        self.Age = Age
    
    def AmIpassing(self,grade):
        if grade >= 70:
            return 'Passing'
        else:
            return 'Not Passing'
    
    def individual(self,Name,Age,Cohort,totalgrade):
        return f'Hello {Name}, you are {Age} years old and in Cohort:{Cohort} with a grade of {totalgrade}'    
        
# Separate from class definition        
def student_generator(num):
        studentlist = []
        for i in range(num):
            studentlist.append([[student.assignmentsub(),
            student.gradeaftertest(1),
            my_student.AmIpassing(np.random.randint(0,101)),
            my_student.individual(np.random.randint(0,100),np.random.randint(0,101),np.random.randint(0,101),np.random.randint(0,101))]])  
        print(studentlist)

if __name__ == '__main__':
    my_student = BloomtechStudent('Logan',23,36,85)
    student_generator(1)
    
    