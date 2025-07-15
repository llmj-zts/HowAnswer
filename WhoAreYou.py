import random
import json
import os
os.system("chcp 65001")
def rand(quest):
    id = random.randint(1, len(quest))
    return quest[repr(id)]

def judge(problem):
    answer = input("Q: "+problem["question"]+"\n")
    if answer in problem["answer"]:
        print("\033[32mCorrect!!!\033[0m")
        return True
    print("\033[31mMistake!!!\033[0m")
    return False

def result(correct, all):
    os.system("cls")
    print("Congrats!You complete all question")
    print("\033[32mCorrect:\033[0m %d" % correct)
    print("\033[31mMistake:\033[0m %d" % (all-correct))
    input("Enter......")
    
def main(correct=0):
    file = open("question.json", 'rb')
    quest = json.load(file)
    file.close()
    for i in quest:
        problem = rand(quest)
        if judge(problem):
            correct += 1
        input("Enter to continue...")
    result(correct, len(quest))
            
if __name__ == "__main__":
    main()