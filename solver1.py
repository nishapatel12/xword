# May 22, 2020: Jeremiah & Nisha

# NOTE: The first version will just work on filling in the words as best it can based on the placement order. The second
# version should look to optimize the placement of words so that other wrods can be made. Maybe by filling in the larger
# words first and then filling in smaller ones. Would also be good to allow user to block off certain squares.

# 5/19 -- Need to figure out a way of locating where a words starts, and its direction. Ideally some kind of vector so
# that [3 0 5 1] = 4th row, first column, 5 characters, vertical. Then there needs to be a score of how long the word is
# and if its already been filled in already. Much to do, but getting closer!!

import random

## Import the chosen dictionary of words to fill in
dict_file = 'eng_words.txt'

## Import the filled in squares
  # Also needs to import the clues
puzzle = open("test_puzzle.txt", "r")

answers = [] # Words that can be added to fill in the puzzle
master_dict = {} # Dictionary to contain answers and their clues !!Could there be multiple clues

with open(dict_file, "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    (answer, clue) = stripped_line.split(maxsplit=1)
    #FIX: I think the dict needs to be switched so that the clue is the 'key', therefore ans can have 2+ clues
    master_dict[answer] = clue # Files the string into the master dictionary

answers = master_dict.keys() # Takes the answers from the dictionary

## Get the user-fill in Board

## Fill in the rest of the missing spaces
  # Choose the first word
  # Find a word that fits (right letter, right length)
  # Place word

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
    print("Slots in column:", colm)
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

  # select the longest row/column
  # get the current slots
  # find words that fit
  slots = "?w???"
  words = wordFinder(slots)
  word = words[0] #FIX: make this so it randomly chooses one of the possible words
    # choose and place a word
      #if row
      # if column
  # update grid
  #iterate until full
  print("Grid is filled")
  print(grid)
  return grid


# Create a grid filled with "?" representing a blank
def createGrid(grid_size):
  grid = []
  for row in range(grid_size):
    grid.append([])
    for column in range(grid_size):
      grid[row].append("?")
  return grid


# Print the grid to the screen
def showGrid(grid):
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      print(grid[row][column], end = "")
    print()


def findColumn(grid,grid_size,column):
  col = []
  for row in range(grid_size):
    col.append(grid[row][column])
  return col



# The control starts here

grid_size = 5
grid = createGrid(grid_size)
#showGrid(grid)
grid[0][:] = "ALAMO"
grid[1][3] = "!"
grid[2][2] = "!"
grid[3][3] = "!"
grid[4][1] = "!"
showGrid(grid)
print("#######")

wordFinder("a???t")
#fillGrid(grid, grid_size)

## Find the clues for the corresponding answers

## Clear unused clues

## Save file