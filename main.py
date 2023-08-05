#CyHelp Starter Code
cybersecurityBirthYear = 1970


#Greets user
print("Hello! I'm CyHelp.\n")
userName = input("What's your name?\n")
print("\nNice to meet you " + userName + "!")


#Recounts start of Cybersecurity
todaysYear = input("\nWhat year is it?\n") # assumes user types in a String
timePassed = int(todaysYear) - cybersecurityBirthYear
print("\nWow! That means it has been " + str(timePassed) + " years since Cybersecurity began!") # cannot concatenate String + Integer, must typecast
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("Press enter to continue.\n")
# input() waits for user input, which is "enter" in this case


#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")
print("These people can be governments/nations, individuals, companies, community organizations, and hackers.")
input("Press enter to continue.\n")


#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability.")
print("\nWould you like to learn about the CIA Triad?")
giveInfo = input("Type 'yes' or 'no.'\n")


#Explains pillars of CIA Triad
while (giveInfo.lower() == "yes"):
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) confidentiality, (b) integrity, (c) availability, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("\nConfidentiality makes sure data is private.")
  elif topic.lower() == "b":
    print("\nIntegrity makes sure data has not been tampered with and can be trusted.")
  elif topic.lower() == "c":
    print("\nAvailability makes sure authorized people can access the data.")
  elif topic.lower() == "d":
    break
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
    
  input("Press enter to continue.")

    
#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")