from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox



root = Tk()
root.title('Ultimate Tic Tac Toe')
heightWindow = root.winfo_screenheight()
widthWindow = root.winfo_screenwidth()
root.geometry(f'{widthWindow}x{heightWindow}')
root.resizable(False, False)

   



#initialization of global variables
#BG and FG are for background foreground color
BG = ''
FG = ''
turn = 'X'
#gg is to measure if the game is winnable or not i.e. for TIE
gg = 0
arr = [[' ' for i in range(9)] for j in range(9)]
checkarr = [' ' for i in range(9)]
permaDis = [' ' for i in range(9)]

ph = PhotoImage(file='play (1).png')

def mainWindow():
    global player2Box,player1Box

    #Creating and Placing Main Frame
    main = Frame(root, width=widthWindow, height=heightWindow, bg="#BDB76B").place(
        x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    Frame(main, width=700, height=700, bg="#556B2F").place(
        x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

    #Creating and Placing Game Board Frame
    Frontframe = Frame(main, width=660, height=660, bg="#2E8B57").place(
        x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

    # Creating the Button for PLAY
    Button(Frontframe, image=ph, bg="#2E8B57", command=playScreen).place(
        x=0, y=120, relx=0.5, rely=0.5, anchor=CENTER)

    # Creating the Title and Entry Box of Player 2 to input his/her name 
    player2 = Label(Frontframe, bg="#2E8B57", padx=30, pady=10, width=15, height=1, text="Enter Player 2 name :",
                            font=("BankGothic Md BT ", 16, "bold"))
    player2.place(x=-160, y=-80, relx=0.5, rely=0.5, anchor=CENTER)
    player2Box = Entry(Frontframe, font=(
        "BankGothic Md BT", 18, "bold"), bg="#2E8B57")
    player2Box.place(y=-80, x=110, relx=0.5, rely=0.5,
                     anchor=CENTER, width=300, height=50)

    # Creating the Title and Entry Box of Player 1 to input his/her name
    player1 = Label(Frontframe, bg="#2E8B57", padx=30, pady=10, width=15, height=1, text="Enter Player 1 name :",
                    font=("BankGothic Md BT ", 16, "bold")).place(
        x=-160, y=-180, relx=0.5, rely=0.5, anchor=CENTER)
    player1Box = Entry(Frontframe, font=(
        "BankGothic Md BT", 18, "bold"), bg="#2E8B57")
    player1Box.place(y=-180, x=110, relx=0.5, rely=0.5,
                    anchor=CENTER, width=300, height=50)
    


def state_change():
    global State,permaDis
    flag = 1
    for i in State:
        #if the state is active then to change every other boxes state to disabled flag variable is used
        if i == 'active':
            flag = 0
            break
    if flag == 1:
        for i in range(9):
            if permaDis[i]=='disabled':
                State[i] = permaDis[i]
            else:
                State[i] = 'active'



def Box1():
    global State,permaDis
    #to change box1 State to disabled if permaDis is disabled
    State[0] = 'active' if permaDis[0]==' ' else permaDis[0]
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'disabled'
    State[8] = 'disabled'
    state_change()
    
def Box2():
    global State, permaDis
    #to change box2 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'active' if permaDis[1] == ' ' else permaDis[1]
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'disabled'
    State[8] = 'disabled'
    state_change()

def Box3():
    global State, permaDis
    # to change box3 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'active' if permaDis[2] == ' ' else permaDis[2]
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'disabled'
    State[8] = 'disabled'
    state_change()
    
def Box4():
    global State, permaDis
    #to change box4 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'active' if permaDis[3] == ' ' else permaDis[3]
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'disabled'
    State[8] = 'disabled'
    state_change()
    
def Box5():
    global State, permaDis
    #to change box5 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'active' if permaDis[4] == ' ' else permaDis[4]
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'disabled'
    State[8] = 'disabled'
    # print(f'before state_change {State}')
    state_change()

def Box6():
    global State, permaDis
    # to change box6 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'active' if permaDis[5] == ' ' else permaDis[5]
    State[6] = 'disabled' 
    State[7] = 'disabled'
    State[8] = 'disabled'
    state_change()

def Box7():
    global State, permaDis
    # to change box7 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'active' if permaDis[6] == ' ' else permaDis[6]
    State[7] = 'disabled'
    State[8] = 'disabled'
    state_change()
    
def Box8():
    global State, permaDis
    # to change box8 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'active' if permaDis[7] == ' ' else permaDis[7]
    State[8] = 'disabled'
    state_change()

def Box9():
    global State, permaDis
    # to change box9 State to disabled if permaDis is disabled
    State[0] = 'disabled'
    State[1] = 'disabled'
    State[2] = 'disabled'
    State[3] = 'disabled'
    State[4] = 'disabled'
    State[5] = 'disabled'
    State[6] = 'disabled'
    State[7] = 'disabled'
    State[8] = 'active' if permaDis[8] == ' ' else permaDis[8]
    state_change()

def t1(BoardFrame, State):

    global b11, b12, b13, b14, b15, b16, b17, b18, b19, BG, arr, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box1 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box1 is active to Black and White
        FG = 'black'
        BG = 'white'

    # Creating and Placing Box1's 9 buttons
    b11 = Button(BoardFrame, text=arr[0][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b11, 1, 1))
    b12 = Button(BoardFrame, text=arr[0][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b12, 2, 1))
    b13 = Button(BoardFrame, text=arr[0][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b13, 3, 1))
    b14 = Button(BoardFrame, text=arr[0][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b14, 4, 1))
    b15 = Button(BoardFrame, text=arr[0][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b15, 5, 1))
    b16 = Button(BoardFrame, text=arr[0][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b16, 6, 1))
    b17 = Button(BoardFrame, text=arr[0][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b17, 7, 1))
    b18 = Button(BoardFrame, text=arr[0][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b18, 8, 1))
    b19 = Button(BoardFrame, text=arr[0][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b19, 9, 1))

    b11.place(x=-373, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b12.place(x=-281, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b13.place(x=-189, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b14.place(x=-373, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b15.place(x=-281, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b16.place(x=-189, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b17.place(x=-373, y=-187, relx=0.5, rely=0.5, anchor=CENTER)
    b18.place(x=-281, y=-187, relx=0.5, rely=0.5, anchor=CENTER)
    b19.place(x=-189, y=-187, relx=0.5, rely=0.5, anchor=CENTER)

def t2(BoardFrame, State):
    global b21, b22, b23, b24, b25, b26, b27, b28, b29, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box2 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box2 is active to Black and White
        FG = 'black'
        BG = 'white'

    # Creating and Placing Box2's 9 buttons
    b21 = Button(BoardFrame, text=arr[1][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b21, 1,2))
    b22 = Button(BoardFrame, text=arr[1][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b22, 2,2))
    b23 = Button(BoardFrame, text=arr[1][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b23, 3,2))
    b24 = Button(BoardFrame, text=arr[1][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b24, 4,2))
    b25 = Button(BoardFrame, text=arr[1][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b25, 5,2))
    b26 = Button(BoardFrame, text=arr[1][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b26, 6,2))
    b27 = Button(BoardFrame, text=arr[1][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b27, 7,2))
    b28 = Button(BoardFrame, text=arr[1][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b28, 8,2))
    b29 = Button(BoardFrame, text=arr[1][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b29, 9,2))

    b21.place(x=-92, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b22.place(x=0, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b23.place(x=92, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b24.place(x=-92, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b25.place(x=0, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b26.place(x=92, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b27.place(x=-92, y=-187, relx=0.5, rely=0.5, anchor=CENTER)
    b28.place(x=0, y=-187, relx=0.5, rely=0.5, anchor=CENTER)
    b29.place(x=92, y=-187, relx=0.5, rely=0.5, anchor=CENTER)

def t3(BoardFrame, State):
    global b31, b32, b33, b34, b35, b36, b37, b38, b39, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box3 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box3 is active to Black and White

        FG = 'black'
        BG = 'white'
    # Creating and Placing Box3's 9 buttons
    b31 = Button(BoardFrame, text=arr[2][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b31, 1,3))
    b32 = Button(BoardFrame, text=arr[2][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b32, 2,3))
    b33 = Button(BoardFrame, text=arr[2][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b33, 3,3))
    b34 = Button(BoardFrame, text=arr[2][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b34, 4,3))
    b35 = Button(BoardFrame, text=arr[2][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b35, 5,3))
    b36 = Button(BoardFrame, text=arr[2][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b36, 6,3))
    b37 = Button(BoardFrame, text=arr[2][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b37, 7,3))
    b38 = Button(BoardFrame, text=arr[2][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b38, 8,3))
    b39 = Button(BoardFrame, text=arr[2][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b39, 9,3))

    b33.place(x=373, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b32.place(x=281, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b31.place(x=189, y=-369, relx=0.5, rely=0.5, anchor=CENTER)
    b36.place(x=373, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b35.place(x=281, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b34.place(x=189, y=-278, relx=0.5, rely=0.5, anchor=CENTER)
    b39.place(x=373, y=-187, relx=0.5, rely=0.5, anchor=CENTER)
    b38.place(x=281, y=-187, relx=0.5, rely=0.5, anchor=CENTER)
    b37.place(x=189, y=-187, relx=0.5, rely=0.5, anchor=CENTER)

def t4(BoardFrame, State):
    global b41, b42, b43, b44, b45, b46, b47, b48, b49, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box4 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box4 is active to Black and White

        FG = 'black'
        BG = 'white'
    # Creating and Placing Box4's 9 buttons
    b41 = Button(BoardFrame, text=arr[3][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b41, 1,4))
    b42 = Button(BoardFrame, text=arr[3][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b42, 2,4))
    b43 = Button(BoardFrame, text=arr[3][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b43, 3,4))
    b44 = Button(BoardFrame, text=arr[3][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b44, 4,4))
    b45 = Button(BoardFrame, text=arr[3][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b45, 5,4))
    b46 = Button(BoardFrame, text=arr[3][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b46, 6,4))
    b47 = Button(BoardFrame, text=arr[3][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b47, 7,4))
    b48 = Button(BoardFrame, text=arr[3][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b48, 8,4))
    b49 = Button(BoardFrame, text=arr[3][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b49, 9,4))

    b41.place(x=-373, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b42.place(x=-281, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b43.place(x=-189, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b44.place(x=-373, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b45.place(x=-281, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b46.place(x=-189, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b47.place(x=-373, y=91, relx=0.5, rely=0.5, anchor=CENTER)
    b48.place(x=-281, y=91, relx=0.5, rely=0.5, anchor=CENTER)
    b49.place(x=-189, y=91, relx=0.5, rely=0.5, anchor=CENTER)

def t5(BoardFrame, State):
    global b51, b52, b53, b54, b55, b56, b57, b58, b59, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box5 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box5 is active to Black and White

        FG = 'black'
        BG = 'white'
    # Creating and Placing Box5's 9 buttons
    b51 = Button(BoardFrame, text=arr[4][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b51, 1,5))
    b52 = Button(BoardFrame, text=arr[4][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b52, 2,5))
    b53 = Button(BoardFrame, text=arr[4][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b53, 3,5))
    b54 = Button(BoardFrame, text=arr[4][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b54, 4,5))
    b55 = Button(BoardFrame, text=arr[4][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b55, 5,5))
    b56 = Button(BoardFrame, text=arr[4][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b56, 6,5))
    b57 = Button(BoardFrame, text=arr[4][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b57, 7,5))
    b58 = Button(BoardFrame, text=arr[4][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b58, 8,5))
    b59 = Button(BoardFrame, text=arr[4][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b59, 9,5))

    b51.place(x=-92, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b52.place(x=0, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b53.place(x=92, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b54.place(x=-92, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b55.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b56.place(x=92, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b57.place(x=-92, y=91, relx=0.5, rely=0.5, anchor=CENTER)
    b58.place(x=0, y=91, relx=0.5, rely=0.5, anchor=CENTER)
    b59.place(x=92, y=91, relx=0.5, rely=0.5, anchor=CENTER)

def t6(BoardFrame, State):
    global b61, b62, b63, b64, b65, b66, b67, b68, b69, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box6 is disabled to Grey and white
        FG = 'white'
        BG = 'grey'
    else:
        # to change BG and FG if the state of box6 is active to Black and White

        FG = 'black'
        BG = 'white'
    # Creating and Placing Box6's 9 buttons
    b61 = Button(BoardFrame, text=arr[5][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b61, 1,6))
    b62 = Button(BoardFrame, text=arr[5][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b62, 2,6))
    b63 = Button(BoardFrame, text=arr[5][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b63, 3,6))
    b64 = Button(BoardFrame, text=arr[5][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b64, 4,6))
    b65 = Button(BoardFrame, text=arr[5][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b65, 5,6))
    b66 = Button(BoardFrame, text=arr[5][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b66, 6,6))
    b67 = Button(BoardFrame, text=arr[5][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b67, 7,6))
    b68 = Button(BoardFrame, text=arr[5][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b68, 8,6))
    b69 = Button(BoardFrame, text=arr[5][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b69, 9,6))

    b63.place(x=373, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b62.place(x=281, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b61.place(x=189, y=-91, relx=0.5, rely=0.5, anchor=CENTER)
    b66.place(x=373, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b65.place(x=281, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b64.place(x=189, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    b69.place(x=373, y=91, relx=0.5, rely=0.5, anchor=CENTER)
    b68.place(x=281, y=91, relx=0.5, rely=0.5, anchor=CENTER)
    b67.place(x=189, y=91, relx=0.5, rely=0.5, anchor=CENTER)

def t7(BoardFrame, State):
    global b71, b72, b73, b74, b75, b76, b77, b78, b79, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box7 is disabled to Grey and white
        FG = 'white'
        BG = 'grey'
    else:
        # to change BG and FG if the state of box7 is active to Black and White

        FG = 'black'
        BG = 'white'
    # Creating and Placing Box7's 9 buttons
    b71 = Button(BoardFrame, text=arr[6][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b71, 1,7))
    b72 = Button(BoardFrame, text=arr[6][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b72, 2,7))
    b73 = Button(BoardFrame, text=arr[6][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b73, 3,7))
    b74 = Button(BoardFrame, text=arr[6][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b74, 4,7))
    b75 = Button(BoardFrame, text=arr[6][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b75, 5,7))
    b76 = Button(BoardFrame, text=arr[6][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b76, 6,7))
    b77 = Button(BoardFrame, text=arr[6][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b77, 7,7))
    b78 = Button(BoardFrame, text=arr[6][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b78, 8,7))
    b79 = Button(BoardFrame, text=arr[6][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b79, 9,7))

    b77.place(x=-373, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b78.place(x=-281, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b79.place(x=-189, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b74.place(x=-373, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b75.place(x=-281, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b76.place(x=-189, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b71.place(x=-373, y=187, relx=0.5, rely=0.5, anchor=CENTER)
    b72.place(x=-281, y=187, relx=0.5, rely=0.5, anchor=CENTER)
    b73.place(x=-189, y=187, relx=0.5, rely=0.5, anchor=CENTER)

def t8(BoardFrame, State):
    global b81, b82, b83, b84, b85, b86, b87, b88, b89, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box8 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box8 is active to Black and White

        FG = 'black'
        BG = 'white'
    # Creating and Placing Box8's 9 buttons
    b81 = Button(BoardFrame, text=arr[7][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b81, 1,8))
    b82 = Button(BoardFrame, text=arr[7][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b82, 2,8))
    b83 = Button(BoardFrame, text=arr[7][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b83, 3,8))
    b84 = Button(BoardFrame, text=arr[7][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b84, 4,8))
    b85 = Button(BoardFrame, text=arr[7][4], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b85, 5,8))
    b86 = Button(BoardFrame, text=arr[7][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b86, 6,8))
    b87 = Button(BoardFrame, text=arr[7][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b87, 7,8))
    b88 = Button(BoardFrame, text=arr[7][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b88, 8,8))
    b89 = Button(BoardFrame, text=arr[7][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b89, 9,8))

    b87.place(x=-92, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b88.place(x=0, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b89.place(x=92, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b84.place(x=-92, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b85.place(x=0, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b86.place(x=92, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b81.place(x=-92, y=187, relx=0.5, rely=0.5, anchor=CENTER)
    b82.place(x=0, y=187, relx=0.5, rely=0.5, anchor=CENTER)
    b83.place(x=92, y=187, relx=0.5, rely=0.5, anchor=CENTER)

def t9(BoardFrame, State):
    global b91, b92, b93, b94, b95, b96, b97, b98, b99, BG, FG
    if (State == 'disabled'):
        # to change BG and FG if the state of box9 is disabled to Grey and white
        BG = 'grey'
        FG = 'white'
    else:
        # to change BG and FG if the state of box9 is active to Black and White
        FG = 'black'
        BG = 'white'
    # Creating and Placing Box9's 9 buttons
    b91 = Button(BoardFrame, text=arr[8][0], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b91, 1,9))
    b92 = Button(BoardFrame, text=arr[8][1], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b92, 2,9))
    b93 = Button(BoardFrame, text=arr[8][2], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b93, 3,9))
    b94 = Button(BoardFrame, text=arr[8][3], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b94, 4,9))
    b95 = Button(BoardFrame, text=arr[8][4], font='Trattatello 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b95, 5,9))
    b96 = Button(BoardFrame, text=arr[8][5], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b96, 6,9))
    b97 = Button(BoardFrame, text=arr[8][6], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b97, 7,9))
    b98 = Button(BoardFrame, text=arr[8][7], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b98, 8,9))
    b99 = Button(BoardFrame, text=arr[8][8], font='helvetica 20',
                 bg = BG , disabledforeground = FG, height=2, width=5, state=State, command=lambda: clicked(b99, 9,9))

    b99.place(x=373, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b98.place(x=281, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b97.place(x=189, y=369, relx=0.5, rely=0.5, anchor=CENTER)
    b96.place(x=373, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b95.place(x=281, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b94.place(x=189, y=278, relx=0.5, rely=0.5, anchor=CENTER)
    b93.place(x=373, y=187, relx=0.5, rely=0.5, anchor=CENTER)
    b92.place(x=281, y=187, relx=0.5, rely=0.5, anchor=CENTER)
    b91.place(x=189, y=187, relx=0.5, rely=0.5, anchor=CENTER)



def check():
    global permaDis,checkarr
    #To Check if any of the Box is won by Player 1 or Player 2
    for i in range(9):
        if (checkarr[i]==' ' and (arr[i][0] == arr[i][1] == arr[i][2] == 'X') or (arr[i][3] == arr[i][4] == arr[i][5] == 'X') or (arr[i][6] == arr[i][7] == arr[i][8] == 'X') or (arr[i][0] == arr[i][3] == arr[i][6] == 'X') or (arr[i][1] == arr[i][4] == arr[i][7] == 'X') or (arr[i][8] == arr[i][5] == arr[i][2] == 'X') or (arr[i][0] == arr[i][4] == arr[i][8] == 'X') or (arr[i][6] == arr[i][4] == arr[i][2] == 'X')):
            checkarr[i]='X'
            permaDis[i]='disabled' 
        elif (checkarr[i] == ' ' and (arr[i][0] == arr[i][1] == arr[i][2] == 'O') or (arr[i][3] == arr[i][4] == arr[i][5] == 'O') or (arr[i][6] == arr[i][7] == arr[i][8] == 'O') or (arr[i][0] == arr[i][3] == arr[i][6] == 'O') or (arr[i][1] == arr[i][4] == arr[i][7] == 'O') or (arr[i][8] == arr[i][5] == arr[i][2] == 'O') or (arr[i][0] == arr[i][4] == arr[i][8] == 'O') or (arr[i][6] == arr[i][4] == arr[i][2] == 'O')):
            checkarr[i]='O'
            permaDis[i] = 'disabled'

    #To check if the main Box is Won by Player 1 or Player 2          
    if((checkarr[0]==checkarr[1]==checkarr[2]=='X') or (checkarr[3]==checkarr[4]==checkarr[5]=='X') or (checkarr[6]==checkarr[7]==checkarr[8]=='X') or (checkarr[0]==checkarr[3]==checkarr[6]=='X') or (checkarr[1]==checkarr[4]==checkarr[7]=='X') or (checkarr[2]==checkarr[5]==checkarr[8]=='X') or (checkarr[0]==checkarr[4]==checkarr[8]=='X') or (checkarr[6]==checkarr[4]==checkarr[2]=='X') ):
        return 'X'
    elif((checkarr[0]==checkarr[1]==checkarr[2]=='O') or (checkarr[3]==checkarr[4]==checkarr[5]=='O') or (checkarr[6]==checkarr[7]==checkarr[8]=='O') or (checkarr[0]==checkarr[3]==checkarr[6]=='O') or (checkarr[1]==checkarr[4]==checkarr[7]=='O') or (checkarr[2]==checkarr[5]==checkarr[8]=='O') or (checkarr[0]==checkarr[4]==checkarr[8]=='O') or (checkarr[6]==checkarr[4]==checkarr[2]=='O') ):
        return 'O'
    else:
        for i in range(len(checkarr)):
            if checkarr[i] == ' ':
                return NONE
        # To check if the game tied or not
        return -1



def clicked(btn, n, i):
    global player2Box, player1Box, turn, gg,mainFrame, BoardFrame

    #Taking Name values from Entry box of player 1 and player 2
    p1 = player1Box.get()
    p2 = player2Box.get()

    gg += 1
    # print(gg)
    #If turn is X ten to change the turn to O and vice versa
    #To Store value of turn in array
    if turn == "X":
        if btn['text'] == ' ':
            arr[i-1][n-1] = 'X'
            turn = 'O'
        else:
            return

    elif turn == 'O':
        if btn['text'] == ' ':
            arr[i-1][n-1] = 'O'
            turn = 'X'
        else:
            return
    Chk = check()

    #To show state(active and disabled) of the 9 boxes
    if n == 1:
        Box1()
    elif n == 2:
        Box2()
    elif n == 3:
        Box3()
    elif n == 4:
        Box4()
    elif n == 5:
        Box5()
    elif n == 6:
        Box6()
    elif n == 7:
        Box7()
    elif n == 8:
        Box8()
    elif n == 9:
        Box9()
    state_change()

    #if the game is not tie or not won by anyone then to continue the game
    if Chk == NONE:
        playScreen()
    else:
        #To show the winner or if the Game is tie
        if Chk=='X':
            messagebox.showinfo(f"{p1} WON", f"Congratulation {p1}, You Won the Ultimate TIC TAC TOE")
            destroy()
        elif Chk=='O':
            messagebox.showinfo(f"{p2} WON", f"Congratulation {p2}, You Won the Ultimate TIC TAC TOE")
            destroy()
        else:
            messagebox.showinfo(f"Tie", f"Better Luck Next Time")



def destroy():
    #when the game ends destroy is called to initialize all the global values 
    global mainFrame, BoardFrame,turn,gg,arr,checkarr,permaDis
    turn = 'X'
    gg = 0
    arr = [[' ' for i in range(9)] for j in range(9)]
    checkarr = [' ' for i in range(9)]
    permaDis = [' ' for i in range(9)]
    BoardFrame.destroy()
    mainFrame.destroy()
    mainWindow()



def playScreen():
    global mainFrame, BoardFrame,player1Box,player2Box,turn
    #Taking Name values from Entry box of player 1 and player 2
    p1 = player1Box.get()
    p2 = player2Box.get()
    #To show whose turn is in play
    if turn == 'X':
        t = p1 + "'s turn"
    else:
        t = p2 + "'s turn"
    
    # Creating and Placing Main and Board Frame 
    mainFrame = LabelFrame(root, bg="#715726", width=widthWindow, height=heightWindow)
    mainFrame.place(
        x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

    BoardFrame = LabelFrame(mainFrame, bg="#6C3602", width=1005, height=1005,
                            highlightbackground="black", highlightthickness=3)
    BoardFrame.place(
        x=0, y=0, relx=0.5, rely=0.48, anchor=CENTER)
    
    turnLabel = Label(mainFrame, bg="#715726", padx=30, pady=10, width=7, height=2, text=t,
                      font=("BankGothic Md BT ", 25, "bold")).place(
        x=650, y=0, relx=0.5, rely=0.5, anchor=CENTER)
    

    #To show which player is X and who is O
    p1Label = Label(mainFrame, bg="#715726", padx=30, pady=10, width=7, height=2, text=p1+' - X',
                              font=("BankGothic Md BT ", 25, "bold")).place(
        x=-650, y=100, relx=0.5, rely=0.5, anchor=CENTER)
    p2Label = Label(mainFrame, bg="#715726", padx=30, pady=10, width=7, height=2, text=p2+' - O',
                    font=("BankGothic Md BT ", 25, "bold")).place(
        x=-650, y=-100, relx=0.5, rely=0.5, anchor=CENTER)
    global gg, State
    #Initial state where all the box will be active to play
    if gg == 0:
        State = ['active', 'active', 'active', 'active',
                 'active', 'active', 'active', 'active', 'active']
        
    # Displaying all the 9 box
    t1(BoardFrame, State[0])

    t2(BoardFrame, State[1])

    t3(BoardFrame, State[2])

    t4(BoardFrame, State[3])

    t5(BoardFrame, State[4])

    t6(BoardFrame, State[5])

    t7(BoardFrame, State[6])

    t8(BoardFrame, State[7])

    t9(BoardFrame, State[8])
    


mainWindow()
root.mainloop()
