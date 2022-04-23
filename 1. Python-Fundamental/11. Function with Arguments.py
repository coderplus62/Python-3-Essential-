# Function with simple argument
def myname(name):
    print('My name is', name)

# Function that use keyword argument
def academic_info(university,major,faculty,cohort):
    myname('Sastra')
    print(f'I am student from {university}')
    print(f'My major is {major}')
    print(f'Faculty of {faculty}.')
    print(f'I am cohort {cohort}\n')

# academic_info(university='SU',major='IE',faculty='FET',cohort='2019')
# academic_info(major='VCD',faculty='FET',cohort='2020',university='UPH')

# Function with default argument
def lecture_profile(name,course='Calculus',credits='5'):
    # This fuction just has default value only for course and credits
    # Name is mandatory to add
    print(f'Lecture name: {name}')
    print(f'Course: {course}')
    print(f'Credits weight: {credits}\n')

lecture_profile('Abidin')
lecture_profile('Wandi',course='VBA')
lecture_profile('Tika',course='Probabilities',credits=4)
lecture_profile(course='Physics',credits=4) # has error