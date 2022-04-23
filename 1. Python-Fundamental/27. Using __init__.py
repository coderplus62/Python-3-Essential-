class student():

    def __init__(self, input_name, student_id, cohort_year):
        # print('Init function is working')
        self.name = input_name
        self.id = student_id
        self.cohort = cohort_year

    def data(self):
        print(f'Student name: {self.name}')
        print(f'Student id: {self.id}')
        print(f'Student cohort: {self.cohort}')

# data1 = ['sastra',201911,2019]
# data2 = ['yogi',201912,2019]

sastra = student('sastra','201911','2019')
sastra.data()
