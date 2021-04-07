# Author: 
- Roheem Deji, Serge Tessiga, and Santigie Sankoh

# What?: 
- Online Multiplayer Chess

# Technology Used: 
- pygame, python 3.x

# Required:
- Python 3.x
- Pygame
  
# How to Setup: 
- Once you download our game if you wish to run it from your machine, you will see a gitpod.yml file, this code once run will automatically install all necessary files in your system. We do this, to safe you time. But if you wish to experiment it yourself, you should only install pygame.
  
# Description: 
- An online multiplayer chess game. Supports infinite players playing against random opponents on different machines on different networks. This project was created using python 3.7, pygame and the sockets module from python3. It runs on a basic client server system where a server script handles all incoming connections and game management. The clients simply handle the UI and game play.
 
# Motivation:
- Even though we are three driven individuals, we were faced with huge challenges. But the good thing is that we are committed and willingly to learn. 
  The first challenge we were faced with is finding a platform to design our game remotely, we spend huge time testing different platforms like collab, and others. But finally, we got one that was cool and easily to use.
  Another challenge was working with sockets. We did tons of research on how to design a server and how to easily connect clients/users to our server.
  Lastly, though we are at the stage where everything seem a bit in shape, we are still challenged with making payment for an online server, to handle 100 or more clients/users to play our game. We are proud of the sleepless night! It was worth it :) . 

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
  
# Reference:
- https://chesstempo.com/play-chess-online/?gclid=Cj0KCQjwsLWDBhCmARIsAPSL3_2CU1oaX6ijNamBYGn7IwKlqfM7CvlAYiUp1qnDRWmdpwZQVe0jeQQaAuoGEALw_wcB
- https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
- https://en.wikipedia.org/wiki/Computer_chess
- https://medium.com/analytics-vidhya/how-chess-algorithm-works-69e8ae165323
- https://www.geeksforgeeks.org/design-a-chess-game/
