#MadLib.py
#Name: Hilary Lawson
#Date: 9/1/24
#Assignment:Lab 1

def main():
  #print("Madlib")
  #Ask user for words
  place1 = input("Enter a place: ")
  noun1 = input("Enter a noun: ")
  adj1 = input("Enter an adjective: ")
  noun2 = input("Enter another noun: ")
  adj2 = input("Enter another adjective: ")
  adj3 = input("Enter another adjective: ")
  noun3 = input("Enter another noun: ")
  verb1 = input("Enter a verb: ")


  
  #Print the story with the user supplied words.
  print("Here is your MadLib: Today I went to the" , place1 , "with my" , noun1 , "and saw a" , adj1 , noun2 , "with a" , adj2 , noun3 + ". Then the" , noun2 , "went to" , verb1 , "with my" , noun1 + ". That made me very" , adj3 + ".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
  main()