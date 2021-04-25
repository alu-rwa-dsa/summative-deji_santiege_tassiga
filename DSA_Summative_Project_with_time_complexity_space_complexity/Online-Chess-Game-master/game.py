'''
the main game
author: Serge, Adio, and Sankoh
requirements:see requirements.txt
'''

import subprocess
import sys
import get_pip

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    print("[GAME] Trying to import pygame")
    import pygame
except:
    print("[EXCEPTION] Pygame not installed")

    try:
        print("[GAME] Trying to install pygame via pip")
        import pip
        install("pygame")
        print("[GAME] Pygame has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install pygame")
            import pip
            install("pygame")
            print("[GAME] Pygame has been installed")
        except:
            print("[ERROR 1] Pygame could not be installed")


import pygame
import os
import time
from client import Network
import pickle
pygame.font.init()

board = pygame.transform.scale(pygame.image.load(os.path.join("img","board_alt.png")), (750, 750))
chessbg = pygame.image.load(os.path.join("img", "chessbg.png"))
rect = (113,113,525,525)

turn = "w"


def menu_screen(win, name):
    global bo, chessbg
    run = True
    offline = False

    while run:
        win.blit(chessbg, (0,0))
        small_font = pygame.font.SysFont("comicsans", 50)
        
        if offline:
            off = small_font.render("Server Offline, Try Again Later...", 1, (255, 0, 0))
            win.blit(off, (width / 2 - off.get_width() / 2, 500))

        pygame.display.update()
        #Time complexity(Olog2n)Logarithmic runtime complexity
        # This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
        # We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed to get from n elements to 1 element.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        #Time complexity is O(N).....A for  Loop
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(1)...color takes a constant space which is not iterable
            # if block piece takes Auxiliary space
            if event.type == pygame.MOUSEBUTTONDOWN:

                offline = False
                try:
                    bo = connect_client( )
                    run = False
                    main()
                    break
                except:
                    print("Server Offline")
                    offline = True
      #Time complexity is O(1).........
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space


    
def redraw_gameWindow(win, bo, p1, p2, color, ready):
    win.blit(board, (0, 0))
    bo.draw(win, color)
    # # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space

    formatTime1 = str(int(p1//60)) + ":" + str(int(p1%60))
    formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))
    if int(p1%60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
        #Time complexity is O(1)
        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space
    if int(p2%60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]
        # Time complexity is O(1)
        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space

    font = pygame.font.SysFont("comicsans", 30)
    try:
        txt = font.render(bo.p1Name + "\'s Time: " + str(formatTime2), 1, (255, 255, 255))
        txt2 = font.render(bo.p2Name + "\'s Time: " + str(formatTime1), 1, (255,255,255))
    except Exception as e:
        print(e)
    win.blit(txt, (520,10))
    win.blit(txt2, (520, 700))

    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (10, 20))

    if color == "s":
        txt3 = font.render("SPECTATOR MODE", 1, (255, 0, 0))
        win.blit(txt3, (width/2-txt3.get_width()/2, 10))
    # Time complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.

    if not ready:
        show = "Waiting for Player"
        if color == "s":
            show = "Waiting for Players"
        font = pygame.font.SysFont("comicsans", 80)
        txt = font.render(show, 1, (255, 0, 0))
        win.blit(txt, (width/2 - txt.get_width()/2, 300))
    # Time complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space

    if not color == "s":
        font = pygame.font.SysFont("comicsans", 30)
        # Time complexity is O(1)
        # This means that the algorithm does a fixed number of operations no matter the number of inputs.

        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space
        if color == "w":
            txt3 = font.render("YOU ARE WHITE", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))
            #  This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(1)...color takes a constant space which is not iterable
            # if block piece takes Auxiliary space
        else:
            txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))
        # Time complexity is O(1)
        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space

        if bo.turn == color:
            txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
        else:
            txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
    # Time complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space

    pygame.display.update()


def quite_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text,1, (255,0,0))
    win.blit(txt, (width / 2 - txt.get_width() / 2, 300))
    pygame.display.update()


    pygame.time.set_timer(pygame.USEREVENT+1, 3000)
    # Time complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False
#Time complexity of this O(log2n)-Logarithmic runtime complexity
#This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
#We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed to get from n elements to 1 element.



def click(pos):
    """
    :return: pos (x, y) in range 0-7 0-7
    """
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2]/8))
            j = int(divY / (rect[3]/8))
            return i, j

    return -1, -1
#
# Time complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
# Space complexity O(1)...color takes a constant space which is not iterable
# if block piece takes Auxiliary space


def connect_client():
    global n
    n = Network()
    return n.board


def main():
    global turn, bo, name

    color = bo.start_user
    count = 0

    bo = n.send("update_moves")
    bo = n.send("name " + name)
    clock = pygame.time.Clock()
    run = True

    while run:
        if not color == "s":
            p1Time = bo.time1
            p2Time = bo.time2
            if count == 60:
                bo = n.send("get")
                count = 0
            else:
                count += 1
            clock.tick(30)

        try:
            redraw_gameWindow(win, bo, p1Time, p2Time, color, bo.ready)
        except Exception as e:
            print(e)
            quite_screen(win, "Other player left")
            run = False
            break
        # Time complexity of this O(log2n)-Logarithmic runtime complexity
#This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
 #We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed to get from n elements to 1 element.



        if not color == "s":
            if p1Time <= 0:
                bo = n.send("winner b")
            elif p2Time <= 0:
                bo = n.send("winner w")
        #Time complexity of this is 0(1)
            # This means that the algorithm does a fixed number of operations no matter the number of inputs.
            # Space complexity O(1)...color takes a constant space which is not iterable
            # if block piece takes Auxiliary space

            if bo.check_mate("b"):
                bo = n.send("winner b")
            elif bo.check_mate("w"):
                bo = n.send("winner w")
        # Time complexity of this is 0(1)
        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space

        if bo.winner == "w":
            quite_screen(win, "White is the Winner!")
            run = False
        elif bo.winner == "b":
            quite_screen(win, "Black is the winner")
            run = False
        #Time complexity of this is O(1)
        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
                #Time complexity is O(n)
                # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and color != "s":
                    # quit game
                    if color == "w":
                        bo = n.send("winner b")
                    else:
                        bo = n.send("winner w")
                # Time complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

                if event.key == pygame.K_RIGHT:
                    bo = n.send("forward")
                # Time complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

                if event.key == pygame.K_LEFT:
                    bo = n.send("back")
            # Time complexity is O(1)
            # This means that the algorithm does a fixed number of operations no matter the number of inputs.

            if event.type == pygame.MOUSEBUTTONUP and color != "s":
                if color == bo.turn and bo.ready:
                    pos = pygame.mouse.get_pos()
                    bo = n.send("update moves")
                    i, j = click(pos)
                    bo = n.send("select " + str(i) + " " + str(j) + " " + color)
            #Time complexity is O(n);
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(1)...color takes a constant space which is not iterable
            # if block piece takes Auxiliary space

    n.disconnect()
    bo = 0
    menu_screen(win)


name = input("Please type your name: ")
width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alu Chess Game")
menu_screen(win, name)
