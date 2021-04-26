# Author: 
1. Roheem Deji
2. Serge Tessiga
3. Santigie Sankoh

# What?: 
> Online Multiplayer Chess - High fidelity / low fidelity

# Technology Used: 
> pygame 
> python 3.x

# Required:
1. Python 3.x
+ Pygame
  
# How to Setup: 
> Once you download our game if you wish to run it from your machine, you will see a gitpod.yml file, this code once run will automatically install all necessary   files in your system. We do this, to safe you time. But if you wish to experiment it yourself, you should only install pygame.
> Also you need to add your ip address on the server.py and client.py. Please do this as it will allow your code to run. You can double run the code to be able to play by you and your friend or client. To do this, you need to run your code and then try to run the code ith another editor. Or you can run in another computer.
  
# Description: 
> An online multiplayer chess game. Supports infinite players playing against random opponents on different machines on different networks. This project was created using python 3.7, pygame and the sockets module from python3. It runs on a basic client server system where a server script handles all incoming connections and game management. The clients simply handle the UI and game play.
 
# Motivation:
> Even though we are three driven individuals, we were faced with huge challenges. But the good thing is that we are committed and willingly to learn. 
  The first challenge we were faced with is finding a platform to design our game remotely, we spend huge time testing different platforms like collab, and others. But finally, we got one that was cool and easily to use.
  Another challenge was working with sockets. We did tons of research on how to design a server and how to easily connect clients/users to our server.
  Lastly, though we are at the stage where everything seem a bit in shape, we are still challenged with making payment for an online server, to handle 100 or more clients/users to play our game. We are proud of the sleepless night! It was worth it :) . 
  
# Correctness of Algorithm
> For the board.py,We have a class called Board...Which has two parameters passed in it,which is the row and column
  This is our first method of the class which is update_moves(self):
    
    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)
> Time complexity of the code is big o(n2)....This is because it has a nested for loop which makes it iterate in two processes.(Quadratic runtime complexity)
  Space complexity  of the code is big O(n)......This is because the rows aand columns are iterable which means if the row or column increases then the space that     would be used would increase.
> OUR SECOND METHOD
      
      def draw(self, win, color):
        if self.last and color == self.turn:
            y, x = self.last[0]
            y1, x1 = self.last[1]

            xx = (4 - x) + round(self.startX + (x * self.rect[2] / 8))
            yy = 3 + round(self.startY + (y * self.rect[3] / 8))
            pygame.draw.circle(win, (0, 0, 255), (xx + 32, yy + 30), 34, 4)
            xx1 = (4 - x) + round(self.startX + (x1 * self.rect[2] / 8))
            yy1 = 3 + round(self.startY + (y1 * self.rect[3] / 8))
            pygame.draw.circle(win, (0, 0, 255), (xx1 + 32, yy1 + 30), 34, 4)

        s = None
        for i in range(self.rows):
            """We decided to use arrays instead of LinkedList because 
            getting one specific element in the middle is a lot faster in an array. So in our board, 
            we wanted to access any element in the board"""
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win, color)
                    if self.board[i][j].isSelected:
                        s = (i, j)
> Time complexity of our second method  is O(n2)
  The Algoorithm Varies with the square of the problem size ,n.
  Space complexity O(n).....The parameter in the function can be iterated through which increases the space based on the number of elements in the array
  It is also called Constant space compexity

> OUR THIRD METHOD
    
    def get_danger_moves(self, color):
        danger_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        for move in self.board[i][j].move_list:
                            danger_moves.append(move)
                            
> Time complexity of our  third method is O(n2)
 The Algorithm Varies with the square of the problem size ,n.
 Space complexity O(1)...color takes a constant space which is not iterable
 It is also called Linear space comlexity
  
> OUR FOURTH METHOD

    def is_checked(self, color):
        self.update_moves( )
        danger_moves = self.get_danger_moves(color)
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_pos = (j, i)
                        
> Time complexity of this METHOD is O(n2).....Quadratic runtime complexity
  The Algoorithm Varies with the square of the problem size ,n.
  Space complexity O(1)...color takes a constant space which is not iterable
  It is also called Linear space comlexity

> OUR FiFTH METHOD

     def select(self, col, row, color):
        changed = False
        prev = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        prev = (i, j)
> Time complexity is 0(n2) due to its quadratic runtime Complexity
  The Algorithm Varies with the square of the problem size,n.

>  OUR SIXTH METHOD

       def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False
                    #Time Complexity is O(n2)....
                    #The algorithm varies with the square of the problem size, n.
                    # Space complexity O(n)... The parameter in the function can be iterated through which increases the space based on the rows or columns
                    #  It is also called constant space complexity
                    
 > OUR SEVENTH METHOD
      
      def move(self, start, end, color):
        checked_Before = self.is_checked(color)
        changed = True
        nBoard = self.board[:]
        if nBoard[start[0]][start[1]].pawn:
            nBoard[start[0]][start[1]].first = False
> Time complexity is O(1)
  This means that the algorithm does a fixed number of operations no matter the number of inputs.                           # # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
> Space complexity O(1)...color takes a constant space which is not iterable
        
        if block piece takes Auxiliary space
        nBoard[start[0]][start[1]].change_pos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard
        if self.is_checked(color) or (checked_Before and self.is_checked(color)):
            changed = False
            nBoard = self.board[:]
> Time complexity is O(1)
  This means that the algorithm does a fixed number of operations no matter the number of inputs.
  Space complexity O(1)...color takes a constant space which is not iterable
  if block piece takes Auxiliary space
           
           if nBoard[end[0]][end[1]].pawn:
                nBoard[end[0]][end[1]].first = True
 > Time complexity is O(1)
   This means that the algorithm does a fixed number of operations no matter the number of inputs.
   Space complexity O(1)...color takes a constant space which is not iterable
      
            if block piece takes Auxiliary space
            nBoard[end[0]][end[1]].change_pos((start[0], start[1]))
            nBoard[start[0]][start[1]] = nBoard[end[0]][end[1]]
            nBoard[end[0]][end[1]] = 0
            self.board = nBoard
        else:
            self.reset_selected( )
        self.update_moves( )
        if changed:
            self.last = [start, end]
 > Time Complexity is O(1)
   This means that the algorithm does a fixed number of operations no matter the number of inputs.
   Space complexity O(1)...color takes a constant space which is not iterable
          
          (if block piece takes Auxiliary space)
            if self.turn == "w":
                self.storedTime1 += (time.time( ) - self.startTime)
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space
            else:
                self.storedTime2 += (time.time( ) - self.startTime)
            self.startTime = time.time( )
            # Space complexity O(1)...color takes a constant space which is not iterable
            # if block piece takes Auxiliary space

        return changed
   ---------------This is the analysis for the board.py of our codes_______________________
   
   ---------------Client.py_________
> In our client.py,We have a class called network and we have different methods too
> OUR FIRST METHOD

       def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096*8)
      # Time Complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # Space complexity O(1)...There is no iteration taking place
    # if block piece takes Auxiliary space
    OUR SECOND METHOD
        def disconnect(self):
        self.client.close()
> Time Complexity is O(1)
  This means that the algorithm does a fixed number of operations no matter the number of inputs.
  Space complexity O(1)...There is  no iteration taking place
  
    (if block piece takes Auxiliary space)
    def send(self, data, pick=False):
        """
        :param data: str
        :return: str
        """
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                if pick:
                    self.client.send(pickle.dumps(data))
                else:
                    self.client.send(str.encode(data))
                reply = self.client.recv(4096*8)
                try:
                    reply = pickle.loads(reply)
                    break
                except Exception as e:
                    print(e)
              except socket.error as e:
                print(e)
  > Time Complexity is O(1)
    This means that the algorithm does a fixed number of operations no matter the number of inputs.
    Space complexity O(1)...color takes a constant space which is not iterable
    if block piece takes Auxiliary space
         ---------------This is the analysis for the client.py of our codes_______________________
           
           ---------------game.py_________ 
  + OUR FIRST METHOD for game.py
          
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
> Time complexity(Olog2n)Logarithmic runtime complexity
  This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to   compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
  We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed     to get from n elements to 1 element.
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        #Time complexity is O(n).....A for  Loop
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(1)...name takes a constant space which is not iterable
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
                    
   > Time complexity is O(1).........
   This means that the algorithm does a fixed number of operations no matter the number of inputs.
   This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
    Space complexity O(1)...color takes a constant space which is not iterable
     if block piece takes Auxiliary space
     
 > OUR SECOND METHOD
 
    def redraw_gameWindow(win, bo, p1, p2, color, ready):
      win.blit(board, (0, 0))
      bo.draw(win, color)
  + This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
  + Space complexity O(1)...color takes a constant space which is not iterable
    if block piece takes Auxiliary space

        formatTime1 = str(int(p1//60)) + ":" + str(int(p1%60))
        formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))
        if int(p1%60) < 10:
            formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
     > Time complexity is O(1)
       This means that the algorithm does a fixed number of operations no matter the number of inputs.
        Space complexity O(1)...color takes a constant space which is not iterable
        if block piece takes Auxiliary space
        
        if int(p2%60) < 10:
            formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]
      > Time complexity is O(1)
        This means that the algorithm does a fixed number of operations no matter the number of inputs.
        Space complexity O(1)...color takes a constant space which is not iterable
        if block piece takes Auxiliary space

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
    + Time complexity is O(1)
      This means that the algorithm does a fixed number of operations no matter the number of inputs.

          if not ready:
              show = "Waiting for Player"
              if color == "s":
                  show = "Waiting for Players"
              font = pygame.font.SysFont("comicsans", 80)
              txt = font.render(show, 1, (255, 0, 0))
              win.blit(txt, (width/2 - txt.get_width()/2, 300))
    + Time complexity is O(1)
      This means that the algorithm does a fixed number of operations no matter the number of inputs.
      Space complexity O(1)...color takes a constant space which is not iterable
      if block piece takes Auxiliary space

          if not color == "s":
              font = pygame.font.SysFont("comicsans", 30)
        + Time complexity is O(1)
        + This means that the algorithm does a fixed number of operations no matter the number of inputs.

        > Space complexity O(1)...color takes a constant space which is not iterable
          if block piece takes Auxiliary space
                      
                      if color == "w":
                          txt3 = font.render("YOU ARE WHITE", 1, (255, 0, 0))
                          win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))
                          
         > This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
              Space complexity O(1)...color takes a constant space which is not iterable
              if block piece takes Auxiliary space
              
          else:
              txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
              win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))
        > Time complexity is O(1)
          This means that the algorithm does a fixed number of operations no matter the number of inputs.
          Space complexity O(1)...color takes a constant space which is not iterable
          if block piece takes Auxiliary space

          if bo.turn == color:
              txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
              win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
          else:
              txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
              win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
    > Time complexity is O(1)
     This means that the algorithm does a fixed number of operations no matter the number of inputs.
    Space complexity O(1)...color takes a constant space which is not iterable
    if block piece takes Auxiliary space

        pygame.display.update()

      > OUR THIRD METHOD

         def quite_screen(win, text):
          pygame.font.init()
          font = pygame.font.SysFont("comicsans", 80)
          txt = font.render(text,1, (255,0,0))
          win.blit(txt, (width / 2 - txt.get_width() / 2, 300))
          pygame.display.update()


         pygame.time.set_timer(pygame.USEREVENT+1, 3000)
    > Time complexity is O(1)
      This means that the algorithm does a fixed number of operations no matter the number of inputs.
      Space complexity O(1)...color takes a constant space which is not iterable
      if block piece takes Auxiliary space

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
> Time complexity of this O(log2n)-Logarithmic runtime complexity
 This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
 We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps

> OUR FOURTH METHOD
      
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

> Time complexity is O(1)
  This means that the algorithm does a fixed number of operations no matter the number of inputs.
  Space complexity O(1)...color takes a constant space which is not iterable
  if block piece takes Auxiliary space

> OUR FIFTH METHOD

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
> Time complexity of this O(log2n)-Logarithmic runtime complexity
  This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed to get from n elements to 1 element.
 
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
            
            ______________This is the Analysis of the game.py of our codes___________
            
            
            ___________________________piece.py_______________________________
            
            We have  classes which are Knight,Bishop,King,pawn,queen,Rook
            
    class Bishop(Piece):
    img = 0

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break

            djL += 1
            # Time Complexity is O(1)
            # The Algoorithm Varies with the square of the problem size ,n.
            # Space complexity O(n)...the parameter in this function can be iterated through


        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1
            # Time Complexity is O(n)
            # The Algoorithm Varies with the square of the problem size ,n.
            # Space complexity O(n)...the parameter in this function can be iterated through

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break
            djL += 1
            # Time Complexity is O(n)
            #This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1
            # Time Complexity is O(n)
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through


        return moves


    class King(Piece):
        img = 1

        def __init__(self, row, col, color):
            super().__init__(row, col, color)
            self.king = True

        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []

            if i > 0:
                # TOP LEFT
                if j > 0:
                    p = board[i - 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i - 1,))
                        # Time Complexity is O(1)
                        # This means that the algorithm does a fixed number of operations no matter the number of inputs.

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

            # TOP RIGHT
            if j < 7:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

        if i < 7:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

            # BOTTOM RIGHT
            if j < 7:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))
                    # Time Complexity is O(1)
                    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        # MIDDLE RIGHT
        if j < 7:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        return moves
    # Time Complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.


    class Knight(Piece):
        img = 2

        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []

            # DOWN LEFT
            if i < 6 and j > 0:
                p = board[i + 2][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 2))
                elif p.color != self.color:
                    moves.append((j - 1, i + 2))
                    # Time Complexity is O(1)
                    #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                    # Space complexity O(1)...color takes a constant space which is not iterable
                    # if block piece takes Auxiliary space

        # UP LEFT
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0:
                moves.append((j - 1, i - 2))
            elif p.color != self.color:
                moves.append((j - 1, i - 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.

        # DOWN RIGHT
        if i < 6 and j < 7:
            p = board[i + 2][j + 1]
            if p == 0:
                moves.append((j + 1, i + 2))
            elif p.color != self.color:
                moves.append((j + 1, i + 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        # UP RIGHT
        if i > 1 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))
            elif p.color != self.color:
                moves.append((j + 1, i - 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i > 0 and j > 1:
            p = board[i - 1][j - 2]
            if p == 0:
                moves.append((j - 2, i - 1))
            elif p.color != self.color:
                moves.append((j - 2, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i > 0 and j < 6:
            p = board[i - 1][j + 2]
            if p == 0:
                moves.append((j + 2, i - 1))
            elif p.color != self.color:
                moves.append((j + 2, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i < 7 and j > 1:
            p = board[i + 1][j - 2]
            if p == 0:
                moves.append((j - 2, i + 1))
            elif p.color != self.color:
                moves.append((j - 2, i + 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...color takes a constant space which is not iterable
                # if block piece takes Auxiliary space

        if i < 7 and j < 6:
            p = board[i + 1][j + 2]
            if p == 0:
                moves.append((j + 2, i + 1))
            elif p.color != self.color:
                moves.append((j + 2, i + 1))

        return moves
    # Time Complexity is O(1)
    # This means that the algorithm does a fixed number of operations no matter the number of inputs.
    # Space complexity O(1)...color takes a constant space which is not iterable
    # if block piece takes Auxiliary space


    class Pawn(Piece):
        img = 3

        def __init__(self, row, col, color):
            super().__init__(row, col, color)
            self.first = True
            self.queen = False
            self.pawn = True

        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []
            try:
                if self.color == "b":
                    if i < 7:
                        p = board[i + 1][j]
                        if p == 0:
                            moves.append((j, i + 1))
                            # Time Complexity is O(1)
                            # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space


                    # DIAGONAL
                    if j < 7:
                        p = board[i + 1][j + 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j + 1, i + 1))
                                # Time Complexity is O(1)
                                # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                                # Space complexity O(1)...color takes a constant space which is not iterable
                                # if block piece takes Auxiliary space

                    if j > 0:
                        p = board[i + 1][j - 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j - 1, i + 1))
                                # Time Complexity is O(1)
                                # This means that the algorithm does a fixed number of operations no matter the number of inputs.

                if self.first:
                    if i < 6:
                        p = board[i + 2][j]
                        if p == 0:
                            if board[i + 1][j] == 0:
                                moves.append((j, i + 2))
                        elif p.color != self.color:
                            moves.append((j, i + 2))
                            # Time Complexity is O(1)
                            # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space
            # WHITE
            else:

                if i > 0:
                    p = board[i - 1][j]
                    if p == 0:
                        moves.append((j, i - 1))
                        # Time Complexity is O(1)
                        # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                        # Space complexity O(1)...color takes a constant space which is not iterable
                        # if block piece takes Auxiliary space

                if j < 7:
                    p = board[i - 1][j + 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j + 1, i - 1))
                            # Time Complexity is O(1)
                            # This means that the algorithm does a fixed number of operations no matter the number of inputs.
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space

                if j > 0:
                    p = board[i - 1][j - 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j - 1, i - 1))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.

                if self.first:
                    if i > 1:
                        p = board[i - 2][j]
                        if p == 0:
                            if board[i - 1][j] == 0:
                                moves.append((j, i - 2))
                        elif p.color != self.color:
                            moves.append((j, i - 2))
                # Time Complexity is O(1)
                #This means that the algorithm does a fixed number of operations no matter the number of inputs.
                # Space complexity O(1)...the parameter in this function can be iterated through
        except:
            pass

        return moves


class Queen(Piece):
    img = 4

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9

            djL += 1
            # Time Complexity is O(n)
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9
            djL += 1
            # Time Complexity is O(n)
            # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
            # Space complexity O(n)...the parameter in this function can be iterated through
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through




        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves
    # Time Complexity is O(n)
    # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
    # Space complexity O(n)...the parameter in this function can be iterated through


    class Rook(Piece):
        img = 5

        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []

            # UP
            for x in range(i - 1, -1, -1):
                p = board[x][j]
                if p == 0:
                    moves.append((j, x))
                elif p.color != self.color:
                    moves.append((j, x))
                    break
                else:
                    break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        # Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        #Time Complexity is O(n)
        # This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # Space complexity O(n)...the parameter in this function can be iterated through
        return moves
        ______________This is the Analysis of the games.py of our code______
        
        
        
        ____________________________server.py_________________-
        
        
        These are our methods
        server = "192.168.1.65"
    port = 5555

    server_ip = socket.gethostbyname(server)

    try:
        s.bind((server, port))

    except socket.error as e:
        print(str(e))
    # # Time Complexity is O(1)
    s.listen()
    print("[START] Waiting for a connection")

    connections = 0

    games = {0:Board(8, 8)}

    spectartor_ids = [] 
    specs = 0

    def read_specs():
        global spectartor_ids

    spectartor_ids = []
    try:
        with open("specs.txt", "r") as f:
            for line in f:
                spectartor_ids.append(line.strip())
    except:
        print("[ERROR] No specs.txt file found, creating one...")
        open("specs.txt", "w")


    def threaded_client(conn, game, spec=False):
        global pos, games, currentId, connections, specs

    if not spec:
        name = None
        bo = games[game]

        if connections % 2 == 0:
            currentId = "w"
        else:
            currentId = "b"

        bo.start_user = currentId
        # Time Complexity is O(1)
        #This means that the algorithm does a fixed number of operations no matter the number of inputs.



        # Pickle the object and send it to the server
        data_string = pickle.dumps(bo)

        if currentId == "b":
            bo.ready = True
            bo.startTime = time.time()

        conn.send(data_string)
        connections += 1
        # Time Complexity is O(1)
        #This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space

        while True:
            if game not in games:
                break

            try:
                d = conn.recv(8192 * 3)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    if data.count("select") > 0:
                        all = data.split(" ")
                        col = int(all[1])
                        row = int(all[2])
                        color = all[3]
                        bo.select(col, row, color)
                        # Time Complexity is O(log2n)
                        # This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
                        # We then decide which half of the array to look at next, which is repeated until X is found. The expected number

                    if data == "winner b":
                        bo.winner = "b"
                        print("[GAME] Player b won in game", game)
                        # Space complexity O(1)...color takes a constant space which is not iterable
                        # if block piece takes Auxiliary space

                    if data == "winner w":
                        bo.winner = "w"
                        print("[GAME] Player w won in game", game)
                        # Space complexity O(1)...color takes a constant space which is not iterable
                        # if block piece takes Auxiliary space

                    if data == "update moves":
                        bo.update_moves()
                        # Space complexity O(1)...color takes a constant space which is not iterable
                        # if block piece takes Auxiliary space

                    if data.count("name") == 1:
                        name = data.split(" ")[1]
                        if currentId == "b":
                            bo.p2Name = name
                        elif currentId == "w":
                            bo.p1Name = name
                            # Time Complexity is O(log2n)
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space


                    #print("Recieved board from", currentId, "in game", game)

                    if bo.ready:
                        if bo.turn == "w":
                            bo.time1 = 900 - (time.time() - bo.startTime) - bo.storedTime1
                        else:
                            bo.time2 = 900 - (time.time() - bo.startTime) - bo.storedTime2
                            # Time Complexity is O(1)
                            # Space complexity O(1)...color takes a constant space which is not iterable
                            # if block piece takes Auxiliary space

                    sendData = pickle.dumps(bo)
                    #print("Sending board to player", currentId, "in game", game)

                conn.sendall(sendData)

            except Exception as e:
                print(e)
        
        connections -= 1
        try:
            del games[game]
            print("[GAME] Game", game, "ended")
        except:
            pass
        print("[DISCONNECT] Player", name, "left game", game)
        conn.close()

    else:
        available_games = list(games.keys())
        game_ind = 0
        bo = games[available_games[game_ind]]
        bo.start_user = "s"
        data_string = pickle.dumps(bo)
        conn.send(data_string)

        while True:
            available_games = list(games.keys())
            bo = games[available_games[game_ind]]
            try:
                d = conn.recv(128)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    try:
                        if data == "forward":
                            print("[SPECTATOR] Moved Games forward")
                            game_ind += 1
                            if game_ind >= len(available_games):
                                game_ind = 0
                        elif data == "back":
                            print("[SPECTATOR] Moved Games back")
                            game_ind -= 1
                            if game_ind < 0:
                                game_ind = len(available_games) -1

                        bo = games[available_games[game_ind]]
                    except:
                        print("[ERROR] Invalid Game Recieved from Spectator")

                    sendData = pickle.dumps(bo)
                    conn.sendall(sendData)

            except Exception as e:
                print(e)
        # Time Complexity is O(log2n)
        # This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
        # We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed to get from n elements to 1 element.

        print("[DISCONNECT] Spectator left game", game)
        specs -= 1
        conn.close()


      while True:
          read_specs()
          if connections < 6:
              conn, addr = s.accept()
              spec = False
              g = -1
        print("[CONNECT] New connection")
   > Time Complexity is O(log2n)
     This is associated with the binary search algorithm that searches by doing necessary halvings to get the item being searched for. The essence of this method is to compare the value being searched for, let’s name it X, with the middle element of the array and if X is not found there.
     #We then decide which half of the array to look at next, which is repeated until X is found. The expected number of steps depends on the number of halvings needed to get from n elements to 1 element.




        for game in games.keys():
            if games[game].ready == False:
                g=game
        # Time Complexity is O(n)
        #This means that the runtime complexity of your algorithm increases linearly with the size of the input data.
        # Space complexity O(n)...the parameter in this function can be iterated through
        # Space complexity O(n)...the parameter in this function can be iterated through



        if g == -1:
            try:
                g = list(games.keys())[-1]+1
                games[g] = Board(8,8)
            except:
                g = 0
                games[g] = Board(8,8)
        # Time Complexity is O(1)
        #This means that the algorithm does a fixed number of operations no matter the number of inputs.
        # Space complexity O(1)...color takes a constant space which is not iterable
        # if block piece takes Auxiliary space

        '''if addr[0] in spectartor_ids and specs == 0:
            spec = True
            print("[SPECTATOR DATA] Games to view: ")
            print("[SPECTATOR DATA]", games.keys())
            g = 0
            specs += 1'''

        print("[DATA] Number of Connections:", connections+1)
        print("[DATA] Number of Games:", len(games))

        start_new_thread(threaded_client, (conn,g,spec))
        
        
        ______________That is the Analysis of our server.py_____________________-

           

# Analysis of Algorithm
> Algorithm Used in Our Chess Game
  Tree: We use heuristic methods to build, search and evaluate trees representing sequences of moves from the current 
  position and attempt to execute the best such sequence during play.
  
> Implementation of the tree algorithm in our Chess Game
   In our chess game, we consider chess moves as a game tree. In theory, it works by examining all moves, 
   then all counter-moves to those moves, then all moves countering them, and so on, where each individual 
   move by one player is called a "ply". This evaluation continues until a certain maximum search depth or the 
   program determines that a final "leaf" position has been reached (e.g. checkmate). At each ply the "best" move by the player 
   is selected; one player is trying to maximize the score, the other to minimize it. By this alternating process, one particular 
   terminal node whose evaluation represents the searched value of the position will be arrived at. Its value is backed up to the root, 
   and that evaluation becomes the valuation of the position on the board. This search process is called 'minimax'.
   
> Our Naive Implementation 
  Our implementation of the tree algorithm can only search to a small depth in a practical amount of time, but we tried various methods 
  to greatly speed the search for good moves.
 
> Test Cases
import unittest
from board import *

      #Test for border class
       class TestBorder(unittest.TestCase):
    def test_rightcolumn(self):
        Board1 = Board(10, 12)
        Board2 = Board(10, 13 )
        self.assertEqual(Board1.cols, 10)
        self.assertEqual( Board2.cols, 10)

    def test_rightrow(self):
       Board3=Board(10,12)
       Board4=Board(10,13)
       self.assertEqual(Board3.rows,12)
       self.assertEqual(Board4.rows,13)

    def test_wrongrow(self):
        Board3 = Board(10, 12)
        Board4 = Board(10, 13)
        self.assertNotEqual(Board3.rows, 9)
        self.assertNotEqual(Board4.rows, 4)

    def test_wrongcols(self):
        Board3 = Board(10, 12)
        Board4 = Board(10, 13)
        self.assertNotEqual(Board3.cols, 15)
        self.assertNotEqual(Board4.cols, 16)

     #All these Tests should be passed
      #Test for Bishop class
     class TestNewBishop(unittest.TestCase):
    def test_Bishopcolor(self):
        Bishop1=Bishop(3,4,"WHITE")
        Bishop2=Bishop(6,7,"Black")
        self.assertEqual(Bishop1.color,"WHITE")
        self.assertEqual(Bishop2.color,"Black")
         def test_Bishoprow(self):
          Bishop1=Bishop(3,4,"WHITE")
        Bishop2=Bishop(6,7,"Black")
        self.assertEqual(Bishop1.row,4)
        self.assertEqual(Bishop2.col,6)
      #Test for Knight class
          class TestNewKnight(unittest.TestCase):
            def test_Knight(self):
        Knight1=Knight(3,4,"White")
        self.assertEqual(Knight1.col,3)
        
      #Test for king class       
               class TestNewKing(unittest.TestCase):
               def test_King(self):
               King1=King(10,11,"black")
               self.assertEqual(King1.col,10)




if __name__ == '__main__':
    unittest.main()
 
  
# Solution
> Essay (150 words)

Probably, it was a great opportunity, an experience for me and my Team to work on this Idea which to Build Chess Game . The Reason Behind this app is that We wanna help ALU students to relax and Chill with this game during the Holidays. The Problem which gave us the motivation to build this game is that we realize that a lot of people at ALU they really like playing Chess Game to relax and Also as the school will end very soon, as Computer science We wanna create this App so that we can help them to relax and Chill with our new App without pay fees for it.

Here I and my Team mates, we  have come a long way up with this solution  to build this app and we believe that with this new App, they Can enjoy and Chill during this Holidays. We wanna ensure that everyone will Enjoy this amazing Holidays.
# Addition


> Video : https://drive.google.com/file/d/1id3uQo1ia3fFFYhf4clRYIsfcfUXsXKn/view?usp=sharing

# Reference:
- https://chesstempo.com/play-chess-online/?gclid=Cj0KCQjwsLWDBhCmARIsAPSL3_2CU1oaX6ijNamBYGn7IwKlqfM7CvlAYiUp1qnDRWmdpwZQVe0jeQQaAuoGEALw_wcB
- https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
- https://en.wikipedia.org/wiki/Computer_chess
- https://medium.com/analytics-vidhya/how-chess-algorithm-works-69e8ae165323
- https://www.geeksforgeeks.org/design-a-chess-game/
