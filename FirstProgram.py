#FirstProgram.py
#Name: Hilary Lawson
#Date: 8/28/24
#Assignment: Lab 1

def main():
  #print("First Program")
  #Say hello
  print("hello!")
  #Ask for the user's name
  name = input("What is your name?")
  #Use the user's name in the program.
  print("Nice to meet you", name)
  #Ask the user for their age.
  age = input("How old are you?")
  #Tell the user what year they were born in.
  age = int(age)
  #Assume that they have not had their birthday yet this year.
  birthYear = 2024 - age
  print("You were born in", birthYear)

  
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
