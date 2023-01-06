#함수 이름은 변경 가능합니다.
student__list = []

class StudentInfo:
    def __init__(self, name, mid__score, final__score):
        self.name=name
        self.mid__score=mid__score
        self.final__score=final__score
        self.grade='no value yet'

class Overlap(Exception):
    def __init__(self):
        super().__init__('Already exist name!')

class EmptyGrade(Exception):
    def __init__(self):
        super().__init__("There is a student who didn't get grade")

##############  menu 1
def Menu1(name, mid__score, final__score):
    student=StudentInfo(name,mid__score,final__score)
    student__list.append(student)

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in range(len(student__list)):
        avg=(int(student__list[i].mid__score) + int(student__list[i].final__score))/2

        if avg >=90:
            student__list[i].grade='A'
        elif avg>=80:
            student__list[i].grade='B'
        elif avg>=70:
            student__list[i].grade='C'
        else:
            student__list[i].grade='D'

##############  menu 3
def Menu3():
    print('\n------------------------------')
    print('name\tmid\tfinal\tgrade')
    print('------------------------------\n')
    
    for i in range(len(student__list)):
        print('{0}\t{1}\t{2}\t{3}'.format(student__list[i].name, student__list[i].mid__score,student__list[i].final__score, student__list[i].grade))

##############  menu 4
def Menu4(name):
    del student__list.name

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            #학생 정보 입력받기
            input__name, input__mid, input__final=input('Enter name mid-score final-score: ').split()
            
            for i in range(len(student__list)):
                if student__list[i].name==input__name:
                    raise Overlap

        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        except ValueError:
            print('Num of data is not 3!')
        
        except Overlap as e:
            print(e)

        else:
            try:
                if not (input__mid.isdigit() and input__final.isdigit()):
                #if (int(input__mid)<=0 or int(input__final)<=0):
                    raise ValueError
            except ValueError:
                print('Score is not positive integer!')
            else:
                Menu1(input__name, input__mid, input__final)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        try:
            if (not student__list):
                raise Exception
        except Exception:
            print('No Student Data!')

        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        else:
            Menu2()
            print("Grading to all students")

    elif choice == "3" :

        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        try: 
            if (not student__list):
                raise Exception
        except Exception:
            print('No Student Data!')

        try:
            for i in range(len(student__list)):
                if student__list[i].grade=='no value yet':
                    raise EmptyGrade

        except EmptyGrade as e:
            print(e)

        #예외사항이 아닌 경우 3번 함수 호출
        else:
            Menu3()

    elif choice == "4" :

        #예외사항 처리(저장된 학생 정보의 유무)
        try: 
            if (not student__list):
                raise Exception
        except Exception:
            print('No Student Data!')

        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력        
        else:
            delete__name = input('Enter the name to delete: ')
            if delete__name is student__list:
                Menu4(delete__name)
                print('{0} student information is deleted'.format(delete__name))
            else:
                print('Not exist name!')


    elif choice == "5":
        print('Exit Program!')
        break

    else :
        print('Wrong number. Choose again.')