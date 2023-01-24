class Student: 
 def __init__(self,full_name="", subject=0, progress=[]): 
    self.full_name = full_name 
    self.group_number = subject
    self.progress = progress 
 def __str__(self): 
    txt = 'Ученик: ' + self.full_name + ' Предмет: ' + self.group_number 
    txt += ' Оценки:'
    for x in self.progress: 
        txt += ' ' + str(x) 
        return txt 

def SortParam(st):
    return st.full_name 

st_size = 5 
students = [] 
for i in range(st_size): 
    print("Введите полное имя студента: ") 
    full_name = input() 
    print("Введите предмет: ") 
    subject = input() 
    n=3 
    print('Введите ',n,' оценок в столбик: ') 
    progress = [] 
    for i in range(n): 
        score = int(input()) 
        progress.append(score) 
 
    st = Student(full_name, subject, progress) 
    students.append(st) 

print("Список учеников:") 
for st in students: 
    print(st) 
students = sorted(students, key=SortParam) 


 
 


     


