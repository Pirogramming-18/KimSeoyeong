import random

#사용자정의함수부
def brGame():
    num=0
    player = 'player'
    while num<31:
        if player=='computer':
            cnt=random.randint(1,3)

        else:
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
            print('{0}: {1}'.format(player,num))

            if num==31:
                if player=='player':
                    print('computer win!')
                elif player=='computer':
                    print('player win!')
                break

        if player=='player':
            player='computer'
        elif player=='computer':
            player='player'

#주프로그램부
brGame()