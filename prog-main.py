import os
import sys
import pandas as pd

# for GUI Version 
from appJar import gui

appg=None
csv_path=None
df=None
df_select=None

def intro():
  '''
  Shows description of this program.
  '''  

  # os.get_terminal_size is some os class type. See it's attributes
  # using dir(size). The one we needed here was columns.
  size=os.get_terminal_size().columns

  print("\n")

  # if size is used instead of 20, the * prints exceeds the terminal screen width, 
  # apparently, there is a difference between column width and the no. of printed chars
  # check that out later.
  for i in range(0,20):
    print("*",end = " ")
    if i == 19:
      print("*")
  print("CSVPlay:\nGenerate various views from data in CSV.")
  for i in range(0,20):
    print("*",end = " ")
    if i == 19:
      print("*")
  print("\n")

def generate_data_frame():
  global df
  df = pd.read_csv(csv_path)
  print("Generated dataframe.")

# get the requested fields to analyze in a data frame
def get_requested_fields(fields):
  global df_select
  fields_list = fields.strip().replace(" ","").split(",")
  print("Requested fields:")
  print(fields_list)
  df_select = df[fields_list] 
  print("Generated dataframe for requested fields.")

def set_csv_path(path):
  global csv_path
  csv_path = path
  print(".csv filepath give as : "+csv_path + "...")

# handle button events
def press(button):
    global df, df_select
    if button == "Process":
      try:
        set_csv_path(appg.getEntry(".csv Path: "))
        generate_data_frame()
      except OSError:
        print("Please enter a valid path.")
    elif button == "Top 5":
      try:
        print(df.head())
      except AttributeError:
        print("Please process csv first.")
    elif button == "Process Selection":
      get_requested_fields(appg.getEntry("Select Fields: ")) 
    elif button == "Selection Top 5":
      print(df_select.head())
def gui_version():
  '''
  Opens GUI Version of CSVPlay
  '''

  # create a GUI variable called app
  global appg 
  appg = gui("CSVPlay", "500x350")
  appg.setBg("white")
  appg.setFont(18)

  # add & configure widgets - widgets get a name, to help referencing them later
  appg.addLabel("title", "Generate views of data in CSV")
  appg.setLabelBg("title", "gray")
  appg.setLabelFg("title", "white")

  appg.addLabelEntry(".csv Path: ")

  # link the buttons to the function called press
  appg.addButtons(["Process", "Top 5"], press)

  appg.addLabelEntry("Select Fields: ")
  appg.addButtons(["Process Selection"], press)
  appg.addButtons(["Selection Top 5"], press)
  appg.setFocus(".csv Path: ")

  # start the GUI
  appg.go()

def userselect_main():
  val = input("Select Task: \n [0] Exit \n [1] Test \n [2] Open GUI version.\n> ")
  if val == "2":
    gui_version()
    userselect_main()
  if val == "1":
    print("I am running!")
    userselect_main()
  elif val == "0":
    print("Exiting.")
    sys.exit()
  else:
    print("Please select a valid entry.")
    userselect_main()

intro()
userselect_main()

"""
References:
- http://appjar.info/#appjar
"""

