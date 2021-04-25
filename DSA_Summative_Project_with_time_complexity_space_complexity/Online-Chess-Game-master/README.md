# Online Multiplayer Chess
Description: An online multiplayer chess game. Supports infinite players playing against random opponents on different machines on different networks. This project was created using python 3.7, pygame and the sockets module from python3. It runs on a basic client server system where a server script handles all incoming connections and game management. The clients simply handle the UI and game play.

# Algorithm Used in Our Chess Game
- Tree: We use heuristic methods to build, search and evaluate trees representing sequences of moves from the current 
  position and attempt to execute the best such sequence during play.

# Implementation of the tree algorithm in our Chess Game
-  In our chess game, we consider chess moves as a game tree. In theory, it works by examining all moves, 
   then all counter-moves to those moves, then all moves countering them, and so on, where each individual 
   move by one player is called a "ply". This evaluation continues until a certain maximum search depth or the 
   program determines that a final "leaf" position has been reached (e.g. checkmate). At each ply the "best" move by the player 
   is selected; one player is trying to maximize the score, the other to minimize it. By this alternating process, one particular 
   terminal node whose evaluation represents the searched value of the position will be arrived at. Its value is backed up to the root, 
   and that evaluation becomes the valuation of the position on the board. This search process is called 'minimax'.
   
# Our Naive Implementation 
- Our implementation of the tree algorithm can only search to a small depth in a practical amount of time, but we tried various methods 
  to greatly speed the search for good moves.
  
# Required:
- Python 3.x
- pygame




You will also need to run server.py on some kind of server. After that you can launch two instances of game from anywhere to play online chess.


# Known Bugs:
- Checkmate does not work, if you loose or win you will need to end the game by hitting "q"
- Very rare bug where a certain move will crash the game


# Run in Gitpod

You can also run Online Chess Game in Gitpod, a free online dev environment for GitHub:
