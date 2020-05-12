#import modules
import random,sys,csv

#class
class magic8ball:
    def __init__(self ,name):
        self.__name= name
        self.__mquestions = []
        self.__start_game()
        
    def __start_game(self):
        mresponse =["It is certain","You may rely on it","As I see it ,yes","It is decidedly so","Without a doubt","Yes deifintely","Yup","Of course"]
        lQuestions= True

        print("Welcome " +  self.__name)

        while lQuestions :
            mQues = input("Please enter a question: ")

            mRespond = mresponse[random.randint(0,7)]
            
            if mQues =="":
                print("Thank you for playing")
                self.__write_questions()

                sys.exit()

            else :
                print(mRespond)

                self.__mquestions.append(mQues)

    def  __write_questions(self):
            f = open("magic_questions.csv" ,"a", newline="")
            wrt = csv.writer(f)

            for q in self. __mquestions:
                wrt.writerow([q])

            f.close()
