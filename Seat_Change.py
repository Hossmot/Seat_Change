import random as rd
from turtle import goto

Class_Seat = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
CS_Storage = []
HMSP_StudentSeatNum = []
HMSP_StudentNumber = []




def Show_CS():
    for v in range(5):
        for h in range(5):
            print(Class_Seat[v][h], end='  ')
            if (Class_Seat[v][h] // 10 == 0):
                print(' ', end='')
        print('\n')


def Seat_Shuffle():
    i = int(0)
    for v in range(5):
        for h in range(5):
            CS_Storage.append(Class_Seat[v][h])
            rd.shuffle(CS_Storage)
    for v in range(5):
        for h in range(5):
            Class_Seat[v][h] = CS_Storage[i]
            i += 1


def CSReset():
    for v in range(5):
        for h in range(5):
            Class_Seat[v][h] = 0


def SetStudentSeat():
    Numinsert = int(0)
    CSReset()
    print('고정할 자리의 개수를 선택하여 주십시오.')
    HMSP = int(input())
    if HMSP != 0:
        print('고정할 자리의 번호를 입력하여 주십시오.(중복X)(순서대로)')
        for i in range(HMSP):
            HMSP_StudentSeatNum.append(int(input()))
        print('고정할 학생의 번호를 선택하여 주십시오.(중복 X)')
        for i in range(HMSP):
            HMSP_StudentNumber.append(int(input()))
        for i in range(HMSP):
            Class_Seat[(HMSP_StudentSeatNum[i] - 1) // 5][(HMSP_StudentSeatNum[i] - 1) % 5] = HMSP_StudentNumber[i]
        for i in range(25):
            CS_Storage.append(i+1)
        for i in range(25):
            if (CS_Storage[i] in HMSP_StudentNumber) == True:
                CS_Storage[i] = 0
        rd.shuffle(CS_Storage)
        for v in range(5):
            for h in range(5):
                while (CS_Storage[Numinsert] == 0 and Numinsert != 24):
                    Numinsert += 1
                if (CS_Storage[Numinsert] != 0 and Class_Seat[v][h] == 0):
                    Class_Seat[v][h] = CS_Storage[Numinsert]
                    Numinsert += 1
    else:
        Seat_Shuffle()
        Show_CS()
    Numinsert = int(0)




def VerticalShuffle(j):
    VerticalElementStorage = []
    for a in range(5):
        VerticalElementStorage.append(Class_Seat[a][j-1])
    rd.shuffle(VerticalElementStorage)
    for a in range(5):
        Class_Seat[a][j-1] = VerticalElementStorage[a]




def Main_1(i):
    if i == 1:
        Seat_Shuffle()
        Show_CS()
    elif i == 2:
        SetStudentSeat()
        Show_CS()
    elif i == 3:
        pass
    else:
        print('올바른 수를 입력하여 주세요.')
        Main_1(i=int(input("자리를 바꾸시려면 1, 고정 후 바꾸시려면 2를, 다음으로 넘어가시려면 3을 눌러주세요.")))

def Main_2(i):
    if i == 1:
        ChangeNumQuantity = int(input("몇 개의 가로줄을 섞을지 입력하여 주십시오."))
        for k in range(ChangeNumQuantity):
            j = int(input('몇 번 줄을 섞으시겠습니까?'))
            rd.shuffle(Class_Seat[j-1])
        Show_CS()
    if i == 2:
        ChangeNumQuantity = int(input("몇 개의 세로줄을 섞을지 입력하여 주십시오."))
        for k in range(ChangeNumQuantity):
            j = int(input('몇 번 줄을 섞으시겠습니까?'))
            VerticalShuffle(j)
        Show_CS()
    if i == 3:
        pass
    if i == 4:
        Engine = 0
    else:
        print('올바른 수를 입력하여 주세요.')  
        Main_2(i=int(input("가로줄을 섞으시려면 1을, 세로줄을 섞으시려면 2를, 다음으로 넘어가시리면 3을,  프로그램을 끝내시려면 4을 눌러주세요.")))  



Engine = int(1)
while (Engine == 1):

    Main_1(i=int(input("자리를 바꾸시려면 1, 고정 후 바꾸시려면 2를, 다음으로 넘어가시려면 3을 눌러주세요.")))
    Main_2(i=int(input("가로줄을 섞으시려면 1을, 세로줄을 섞으시려면 2를, 다음으로 넘어가시리면 3을,  프로그램을 끝내시려면 4을 눌러주세요.")))
    CS_Storage = []
    HMSP_StudentSeatNum = []
    HMSP_StudentNumber = []
