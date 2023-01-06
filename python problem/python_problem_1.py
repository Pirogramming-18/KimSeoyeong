num=0

while True:
    try:
        cntA=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): '))
        if not(1<=cntA<=3):
            raise Exception()
    except ValueError:
        print('정수를 입력하세요')          
    except Exception:
        print('1,2,3중 하나를 입력하세요')
    else:
        break

for i in range(cntA):
    num+=1
    print('playerA: {0}'.format(num))

while True:
    try:
        cntB=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): '))
        if not(1<=cntB<=3):
            raise Exception()
    except ValueError:
        print('정수를 입력하세요')          
    except Exception:
        print('1,2,3중 하나를 입력하세요')
    else:
        break

for i in range(cntB):
    num+=1
    print('playerB: {0}'.format(num))