class student():
    total_student = 0
    major = 'FOB'
    __score = 0 # private attribute
    def __init__(self, input_name, student_id, cohort_year):
        # print('Init function is working')
        self.name = input_name  # public variable
        self.id = student_id
        self.cohort = cohort_year
        student.total_student += 1

    # def data(self):
    #     print(f'Student name: {self.name}')
    #     print(f'Student id: {self.id}')
    #     print(f'Student cohort: {self.cohort}')

sastra = student('sastra','201911','2019')
yogi = student('yogi',201912,2019)
dewa = student('dewa',201913,2018)

# sastra.hobby = 'programming'
# sastra.major = 'FET' # override = menimpa 'FOB'

# print(student.__dict__)
# print(sastra.__dict__)
# print(yogi.__dict__)
#
# print(sastra.hobby)

print(student.total_student)

''' we can make counter using class variable '''