class student():
    name = 'name'

    def study(self, condition):
        print(self.name,'is studying', condition)
    def major(self, major):
        print(self.name,'has major:', major,'\n')

sas = student()
vip = student()

sas.name = 'sastra'
vip.name = 'vip'

# print(sas.name)
# print(vip.name)

sas.study('persistently')
sas.major('industrial engineering')

vip.study('hard')
vip.major('entrepreneur')