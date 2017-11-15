# =============================================================================
# ENSE 799 - Master's thesis - 	Amar Vamsi Krishna - UID : 114921871
# University of Maryland, College Park
# Start Date    :   25th October, 2017
# Current Date  :   15th November, 2017
# Advisor       :   Dr. Anindo Roy
# Team          :   Amar Vamsi Krishna, Suchitra Chandar, Rahul Subramonian
# Topic         :   Development of a novel interactive visual task for robot assisted gait training in stroke
# Task 2.1      :   Programming - Create a Video game - create a screen cursor and visual environment
# Version-1.1   :   Creating a window using pygame and displaying the events (Keyboard presses and mouse movements) on the terminal window using object oriented approach
# Configuration and Dependancies - Uses python version2.7.12 and pygame version 1.9.3. Currently using Spyder IDE and Sublime Text editor for development
# Source for the tutorial : https://pythonprogramming.net/pygame-python-3-part-1-intro/
# =============================================================================

# =============================================================================
# Importing the libraries
# =============================================================================
import pygame                    #  Pygame Library for the primary gaming platform
from pygame.locals import *      #  Imports all the constants used in Pygame under the pygame modeule namespace
import sys                       #  The sys module provides information about constants, functions and methods of the Python interpreter
import random                    #  Random module is used to generate pseudo-random numbers
import numpy as np               #  Numpy is the standard package for scientific computing in Python

# =============================================================================
# Creating a class that runs the game
# =============================================================================
class Game:
    def on_execute(self):       #   Create a placeholder method
        pass                    #   Do nothing
# =============================================================================
#  Main function
# =============================================================================
if __name__ == "__main__" :
    theGame = Game()              #   Create an object of the class App
    theGame.on_execute()         #   Just calling the placeholder method