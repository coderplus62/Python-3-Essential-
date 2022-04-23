init = 0

'''
Dictionary
there is keyword, value, item
'''


student1 = {"ID": 221,
            "Name":"Sastra",
            "Semester":6,
            "Organization":"KMHD"
            }

student2 = {"ID": 323,
            "Name":"Yogi",
            "Semester":3,
            "Organization":"SYIC"
            }
'''Taking data based on the keyword'''
print('\n '+10*'#'+' Taking data based on the keyword '+10*'#'+'\n')


print(student1["Name"])
print(student1.keys())
print(student1.values())
print(student1.items())


'''Dictionary in dictionary: for Database'''
'''Taking data based from previous list'''
print('\n '+10*'#'+' Taking data based from previous list '+10*'#'+'\n')

studentList = {1:student1, 2:student2}
print(studentList[1])