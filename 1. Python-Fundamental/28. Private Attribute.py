class student():
    __score = 0 # private attribute
    def __init__(self, input_name, student_id, cohort_year):
        # print('Init function is working')
        self.name = input_name  # public variable
        self.id = student_id
        self.cohort = cohort_year

    def data(self):
        print(f'Student name: {self.name}')
        print(f'Student id: {self.id}')
        print(f'Student cohort: {self.cohort}')

    def mid(self,mid_score):
        print(self.name,'has mid score:',mid_score)
        mid_score += self.__score
        return mid_score

    def final(self,final_score):
        print(self.name,'has mid score:',final_score)
        final_score += self.__score
        return final_score
    def status(self,mid,final):
        final_score = (mid+final)/2
        if final_score < 70:
            print(self.name,'is not pass')
        else:
            print(self.name,'is pass\n')

data1 = ['sastra',201911,2019]
data2 = ['yogi',201912,2019]

sastra = student('sastra','201911','2019')
sastra_mid = sastra.mid(80)
sastra_final = sastra.final(60)
sastra_status = sastra.status(sastra_mid,sastra_final)

yogi = student('yogi',201912,2019)
yogi_mid = yogi.mid(40)
yogi_final = yogi.final(80)
yogi_status = yogi.status(yogi_mid,yogi_final)


