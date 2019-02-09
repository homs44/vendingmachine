import os


balance = 0

def clear():
    os.system('cls')

def printMainMenu():
    global balance
    print("자판기 서비스 입니다.")
    print("현재 잔돈 : {0}".format(balance))
    print("="*20)
    print("1. 음료수 선택")
    print("2. 잔돈 추가")
    print("3. 잔돈 반환")
    print("0. 종료")
    print("="*20)


def addBalance():
    global balance
    print("현재 잔돈 : {0}".format(balance))
    
    temp = input("입금할 금액 : ")

    try:
        # 숫자를 입력하면 잔돈 +
        balance = balance + int(temp)

    except Exception:
        # 숫자외의 값을 입력하면 잘못된 입력입니다.
        print("잘못된 입력 값입니다.")

    finally:
        # 아무거나 누르시면 메뉴로 이동합니다
        input("아무거나 누르시면 메뉴로 이동합니다")
    
def returnBalance():
    global balance
    # 자판기의 잔돈을 준다라고 출력
    print("잔돈은 {0} 입니다.".format(balance))
    #자판기 금액 초기화
    balance = 0
    # 아무거나 누르시면 메뉴로 이동합니다
    input("아무거나 누르시면 메뉴로 이동합니다")


def selectDrink():
    global balance
    print("현재 잔돈 : {0}".format(balance))
    print("="*20)
    print("1. 사이다 700원")
    print("2. 암바사 800원")
    print("3. 코카콜라 600원")
    drink = input("원하는 음료수를 선택하세요 : ")


    if drink == "1":
        if balance >= 700:
            balance = balance - 700
            print("사이다가 나왔습니다.") 
        else:
            print("잔돈이 부족합니다.")
            
    elif drink == "2":
        if balance >= 800:
            balance = balance - 800
            print("암바사가 나왔습니다.")
        else:
            print("잔돈이 부족합니다.")

    elif drink == "3":
        if balance >= 600:
            balance = balance - 600
            print("코카콜라가 나왔습니다.")
        else:
            print("잔돈이 부족합니다.")
        
    else:
        print("잘못된 입력 값입니다.")
    
    input("아무거나 누르시면 메뉴로 이동합니다")


def run():
    
    while True:
        clear()

        printMainMenu()

        selected = input("메뉴를 선택하세요 : ")
        
        clear()
        
        if selected == "1":
            # 음료수 선택
            
            selectDrink()
        elif selected == "2":
            #잔돈 입력
            addBalance()
        elif selected == "3":
            #잔돈 반환
            returnBalance()
        elif selected =="0":
            print("프로그램이 종료되었습니다.")
            break
        else:
            print("잘못된 입력입니다.")
            input("아무거나 입력하시면 돌아갑니다.")



run()