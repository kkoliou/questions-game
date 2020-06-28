#Class 'Player' has been created for the distiction of scores, names, helps etc of each player. 
class Player:

    def __init__(self,name,score):      #The constructor initializes each players name, score at 0 and helps
        self.name = name
        self.score = score
        self.Helps = ['50-50','Skip this Question']

    def IncreaseScore (self):           #This method increases each players score by 10 points every time they answer correctly to a question
        self.score += 10

    def RemoveHelp (self,X):            #This method removes the used help of each player when used
        self.Helps.remove(X)
        
    def DisplayHelps (self):            #This method displays each players avilable helps
        print(self.Helps)

    def Bonus (self):                   #This method calculates, prints and add on the total score each player's bonus points
        bonus = len(self.Helps) * 5
        print(self.name + ",you got a bonus of " + str(bonus) + " points!")
        self.score += bonus




#List of questions and their answers
Q1=["Hitler party which came into power in 1933 is known as", "A. Labour Party", "B. Nazi Party", "C. Ku-Klux-Klan", "D. Democratic Party"]
Q2=["Galileo was an Italian astronomer who", "A. developed the telescope", "B. discovered four satellites of Jupiter", "C. discovered that the movement of pendulum produces a regular time measurement", "D. All of the above"]
Q3=["During World War II, when did Germany attack France?", "A. 1940", "B. 1941", "C. 1942", "D. 1943", "A"]
Q4=["Economic goods are", "A. all commodities that are limited in quantity as compared to their demand", "B. Commodities that is available according to their demand", "C. Commodities that is available more as compared to demand", "D. None of the above"]
Q5=["In a normal human body, the total number of red blood cells is", "A. 15 trillion", "B. 20 trillion", "C. 25 trillion", "D. 30 trillion"]
Q6=["In which season do we need more fat?", "A. Rainy season", "B. Spring", "C. Winter", "D. Summer"]
Q7=["'OS' computer abbreviation usually means?", "A. Order of Significance", "B. Open Software", "C. Operating System", "D. Optical Sensor"]
Q8=["The sampling rate, (how many samples per second are stored) for a CD is...?", "A. 48.4 kHz", "B. 22,050 Hz", "C. 44.1 kHz", "D. 48 kHz"]
Q9=["The World Environment Day is celebrated on", "A. April 7", "B. June 5", "C. August 6", "D. June 16"]
Q10=["In international volleyball competitions, how many members are allowed per team, not including substitutes?", "A. 6", "B. 7", "C. 5", "D. 8"]
Q11=["The value of x + x(x^x) when x = 2 is:", "A. 10", "B. 16", "C. 18", "D. 36"]
Answers=["B", "D", "A", "A", "D", "C", "C", "C", "B", "A", "A"]

Questions=[Q1[0],Q2[0],Q3[0],Q4[0],Q5[0],Q6[0],Q7[0],Q8[0],Q9[0],Q10[0],Q11[0]] 
Possible_Answers=[Q1[1:],Q2[1:],Q3[1:],Q4[1:],Q5[1:],Q6[1:],Q7[1:],Q8[1:],Q9[1:],Q10[1:],Q11[1:]]
Answers_50_50=[Q1[2:4],Q2[3:5],Q3[1:3],Q4[1:3],Q5[3:5],Q6[2:4],Q7[2:4],Q8[2:4],Q9[2:4],Q10[1:3]] #The choice of 50-50 questions is restricted by Python's usage of lists


print("******************************INSTRUCTIONS******************************")
print(" ")
print("Welcome to our game, where three players battle each other over questions regarding various topics. There is a total of 10 Questions each player has to answer." 
      +"One by one, your answer the exact same question. There will be 4 possible answers for each question, marked with letters A,B,C and D. Each player is given" 
      +"2 helps, one called '50-50', by which you get the same question with 2 possible answers and the other one called 'Skip this Question', which allows you to" 
      +"skip the given question and take an alternative one instead. Each correct answer is rewarded with 10 points. Use your helps wisely, as you'll be given a bonus"
      +"of 5 points for each help you don't use till the end of the game. Good luck to everyone! May the wisest WIN! ")
print("Accepted answers: A, B, C, D, H1(Help 1), H2(Help 2)")
print(" ")
print("************************************************************************")
print(" ")

#Creation of three Player objects 
name1 = input("Enter 1st player's name: ")
player1 = Player(name1, 0)
name2 = input("Enter 2nd player's name: ")
player2 = Player(name2, 0)
name3 = input("Enter 3rd player's name: ")
player3 = Player(name3, 0)
Players = [player1, player2, player3] #Creation of a list with these objects, so they can be used easier further in the program 

#This method checks the validity of each answer
def CheckAnswer ():
    A = input("Type your answer: ")
    while (A!="A" and A!="B" and A!="C" and A!="D" and A!="H1" and A!="H2"):
        A = input("Entry not correct! Please type your answer again: ")

    return A



#MAIN BODY: This is the implementation of the game 
i=0
while(i<=9):   #This loop runs 10 times, as of the number of questions
    print(" ")
    print("*************** QUESTION " + str(i+1) + " ***************")
    j=0
    while(j<=2):  #This loop runs 3 times, as of the number of players
        print(" ")
        print("********* " + Players[j].name + " Playing **********")
        print(Questions[i])
        print(Possible_Answers[i])
        Players[j].DisplayHelps()
        Ans = CheckAnswer()
        if (Ans == Answers[i]):
            Players[j].IncreaseScore()
        elif (Ans == "H1"):     #Case of using '50-50' help
            Players[j].RemoveHelp('50-50')
            print(Questions[i])
            print(Answers_50_50[i])
            Ans = CheckAnswer()
            if (Ans == Answers[i]):
                Players[j].IncreaseScore()
        elif (Ans == "H2"):     #Case of using 'Skip this Question' help
            print(" ")
            print("*************** ALTERNATIVE QUESTION ***************")
            Players[j].RemoveHelp('Skip this Question')
            print(Questions[10])
            print(Possible_Answers[10])
            Ans = CheckAnswer()
            if (Ans == Answers[10]):
                Players[j].IncreaseScore()
            
        j = j + 1
    i = i + 1 

#Calculation of each player's bonus points, based on the number of remaining helps 
print(" ")
print("***************BONUS POINTS***************")
for i in range(3):
    Players[i].Bonus()




#Finding the winner and posisitions
P1 = 0
P2 = 1
P2 = 2
if (Players[0].score > Players[1].score):
               First = Players[0].score
               P1 = 0
               Second = Players[1].score
               P2 = 1
else:
               First = Players[1].score
               P1 = 1
               Second = Players[0].score
               P2 = 0

if (Players[2].score > First): 
               Third = Second
               P3 = 1
               Second = First
               P2= 0
               First = Players[2].score
               P1= 2
elif(Players[2].score > Second):
               Third = Second
               P3 = 1
               Second = Players[2].score
               P2 = 2
else:
               Third = Players[2].score
               P3 = 2
      
     
     
#Printing the results      
print(" ")     
print("THE WINNER IS: " + Players[P1].name + "!!")
print(" ")
print("***************POSITIONS***************")
print(" ")
print("1ST: " + Players[P1].name + " POINTS: " + str(First))
print("2ND: " + Players[P2].name + " POINTS: " + str(Second))
print("3RD: " + Players[P3].name + " POINTS: " + str(Third))



        
                
            



