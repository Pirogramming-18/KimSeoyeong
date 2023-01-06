num=0
player = True

while num<31:
    while True:
        try:
            cnt=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): '))
            if not(1<=cnt<=3):
                raise Exception()
        except ValueError:
            print('정수를 입력하세요')          
        except Exception:
            print('1,2,3중 하나를 입력하세요')
        else:
            break
    
    for i in range(cnt):
        num+=1
        if player==True:
            print('playerA: {0}'.format(num))
        elif player==False:
            print('playerB: {0}'.format(num))

        if num==31:
            break

    player = not player
