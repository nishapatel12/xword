# May 22, 2020: Jeremiah & Nisha

# NOTE: The first version will just work on filling in the words as best it can based on the placement order. The second
# version should look to optimize the placement of words so that other wrods can be made. Maybe by filling in the larger
# words first and then filling in smaller ones. Would also be good to allow user to block off certain squares.

# 5/19 -- Need to figure out a way of locating where a words starts, and its direction. Ideally some kind of vector
# (currently called 'master_slots' that [3 0 5 1] = 4th row, first column, 5 characters, vertical. Then there needs to
# be a score of how long the word is and if its already been filled in already. Much to do, but getting closer!!

# 5/22 -- Still need to figure out how to store/determine slots space is the longest, as it should be filled first.
# From there we will need to create the function that places the word in the grid (dependent on orientation). After that
# there shouldn't be too much more on the backend side for now.

import random

# INPUTS:
# 1. Players answers and clues
# 2. Current Game Board State

# OUTPUTS:
# 1. Current Game Board State
# 2. Answers and clues
# 3. Answer positions

# Create a grid filled with "?"
#FIX:Can honestly probably remove this function as the puzzle file will be coming in from somewhere else.
def createGrid(grid_size):
  grid = []
  for row in range(grid_size):
    grid.append([])
    for column in range(grid_size):
      grid[row].append("?") # Adds blank space
  return grid


# Print the grid to the screen
def showGrid(grid):
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      print(grid[row][column]),
      #print(grid[row][column], end="")
    print()


def wordFinder(slots):
  slot_num = -1
  answers = [idx for idx in master_dict.keys() if len(idx) == len(slots)] # Selects words that are the right length
  for space in slots:
    slot_num += 1
    if space != "?":
        answers = [word2 for word2 in answers if word2[slot_num].lower() == space.lower()] # Creates list of all answers starting with 'letter

  if not answers:
    answers = "No Words Found" #FIX: Probably changes this to throw an error or put a blank space?

  print(answers)
  return answers


def fillGrid(grid, grid_size):
  lengths = []

  for row in range(grid_size):
    roi = grid[row][:]  # Row of Interest
    roi = ''.join(roi)  # Turns the list into a string so it can be split
    if roi.isalpha():  # Check if the row is all filled; if so, pass
      continue
    else:
      slots = roi.split("!")  # Finds any black slots
      # print(slots)
      max_len = 0
      if len(max(slots, key=len)) > max_len:
        max_len = len(max(slots, key=len))

  for column in range(grid_size):
    colm = findColumn(grid,grid_size,column)
    coi = ''.join(colm)
    if coi.isalpha(): # Check if the row is all filled; if so, pass
      continue
    else:
      slots = coi.split("!")
      #print(slots)
      res = max(slots, key=len)
      max_len = 0
      if len(res) > max_len:
        max_len = len(res)

  print(max_len)

  final_answers = [] # Will contain answers so clues can be found later
  # Create for loop to go through all slots. Need some kind of data structure to hold values
  for slot in master_slots: #FIX: Need to create a file that has all the slots
    slots = "?w???"  #FIX: This is just to test. Make sure to remove
    words = wordFinder(slots)
    word = random.choice(words)  # Randomly chooses one of the words. Maybe could be optimized to choose the one with most vowels?
    final_answers.append(word)
        #if row
        # if column
    # update grid
    placeGrid(grid, word, pos)
    #iterate until full

  print("Grid is filled")
  return grid, final_answers


def placeGrid(grid,word,pos):
  # Takes a word and places it in the given position in the grid
  print('Grid Placed')


def findColumn(grid,grid_size,column):
  col = []
  for row in range(grid_size):
    col.append(grid[row][column])
  return col


#############

# Import the chosen dictionary of words to fill in
dict_file = 'eng_words.txt'
master_dict = {} # Dictionary to contain answers and their clues !!Could there be multiple clues

# Imports the puzzle text file
#puzzle_file = 'large_test_puzzle.txt'
puzzle_file = 'test_puzzle.txt'
puzzle = open(puzzle_file, "r")
with open(puzzle_file, 'r') as p_file:
  puzzle_grid = [line.strip() for line in p_file]  # Takes each line from text file


showGrid(puzzle_grid)

grid_size = len(puzzle_grid[0])  # Finds the length of the grid
with open(dict_file, "r") as a_file: # Opens file with answers/clues
  for line in a_file:
    stripped_line = line.strip()
    #(answer, clue) = stripped_line.split(maxsplit=1)
    (answer, clue) = stripped_line.split(' ',1)
    #FIX: Something needs to be changed so that there can be 2+ clues for the same answer
    master_dict[answer] = clue[4:]  # Files the string into the master dictionary

## Fill in the rest of the missing spaces
# fillGrid(puzzle_grid, grid_size)

# showGrid(puzzle_grid)

# ## Find the clues for the corresponding answers

# ## Clear unused clues

# # Save/Export puzzle
# with open(puzzle_file, 'w') as puzzle_final:
#   for row in puzzle_grid:
#     puzzle_final.write("%s\n" % row)

# wordFinder("a???t")





