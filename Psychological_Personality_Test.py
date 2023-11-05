score=0
print("DISCLAIMER.....")
print("\nThis test is not the complete personality examination. \nThere are no right or wrong answers.\n")
print("There might be ambiguity in the questions too. \nALSO, the answers might be based on the subject's current mind set and mood.\n")
dict1={"1":"Are you usually carefree?","2":"Do you stop and think things over before doing anything?","3":"Do you find it very hard to say no as an answer?", "4":"When people shout at you, do you shout back at them?", "5":"Do you often worry about things you should not have done or said?", "6":"Do you often do things at the spur of the moment?","7":"Would you do almost anything for a dare?", "8":"Do you suddenly feel shy when you want to talk to an attractive stranger?", "9":"Do other people think of you as being very lively?", "10":"After you have done something important, do you often come away feeling you could have done better?", "11":"Are you mostly quiet when you are with other people?", "12":"Generally, do you prefer reading over meeting people?", "13":"If there is something you want to know about, would you rather look up in a book than talk to someone about it?", "14":"Do you like doing things in which you have to act quickly?", "15":"Do you like playing pranks on others?"}
tuple_dict1= tuple(dict1.items())
for i in tuple_dict1:
    qnum,question=i
    print("{0}.{1}\n\n Yes (or) No:".format(qnum,question))
    say_no=[2,7,10,11,13]
    response=input()
    if int(qnum) not in say_no:
        if (response.lower()=="yes"):
            score+=1
        elif(response.lower()=="no"):
            score+=0
        else:
            print("Invalid response")
    else:
        if(response.lower()=="no"):
            score+=1
        elif(response.lower()=="yes"):
            score+=0
        else:
            print("Invalid response")
if (score<=6):
    print("Your personality type: Introvert")
    str1="Introvert"
elif(7<=score<=9):
    print("Your personality type: Ambivert")
    str1="Ambivert"
elif(10<=score<=15):
    print("Your personality type: Extrovert")
    str1="Extrovert"
else:
    print("Your score is zero, try giving honest answers")
