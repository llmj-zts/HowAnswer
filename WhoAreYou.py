import random
import json
import os
os.system("chcp 65001")
def rand(quest):
    return random.sample(quest, len(quest))

def judge(problem):
    answer = input("Q: "+problem["question"]+"\n")
    if answer in problem["answer"]:
        print("\033[32mCorrect!!!\033[0m")
        return True
    print("\033[31mMistake!!!\033[0m")
    print("\033[33mcorrect answer:\033[32m%s\033[0m" %"or".join(problem["answer"]))
    return False

def result(correct, all):
    print("Congrats!You complete all question")
    print("\033[32mCorrect:\033[0m %d" % correct)
    print("\033[31mMistake:\033[0m %d" % (all-correct))
    input("Enter......")
    
def main(correct=0):
    file = open("question.json", 'rb')
    quest = json.load(file)
    file.close()
    problem = rand(quest)
    for i in problem:
        if judge(i):
            correct += 1
        input("Enter to continue...")
    result(correct, len(quest))
            
if __name__ == "__main__":
    main()