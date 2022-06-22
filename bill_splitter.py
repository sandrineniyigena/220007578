stage_one
number_of_people= int(input("Enter the number of every friend (including you):\n"))
if number_of_people<=0:
   print ("No one is joining for the party")
else: 
    participant ={}
    print("enter their names:")
    for x in range(1,number_of_people+1):
        names= input()
        participant.update({names:0})
    print(participant)
    
   stage_two
   
    import random
print("Enter the number of friends joining (including you):")
number_of_people = input()
if int(number_of_people) == 0 or int(number_of_people) < 0:
    print("No one is joining for the party")
else:
    participants = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for u in range(int(number_of_people)):
        names = input()
        participants.update({ names: 0})
    print("Enter the total bill value:")
    total_bill = input()
    names = list(participants.keys())
    single_bill = float(float(total_bill) / int(number_of_people))
    for n in names:
        participants.update({n: round(single_bill, 2)})
    print(participants)
    
    stage_three
    import random
print("Enter the number of friends joining (including you):")
number_of_people = input()
if int(number_of_people) == 0 or int(number_of_people) < 0:
    print("No one is joining for the party")
else:
    people_joining_party = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(int(number_of_people)):
        names_of_people = input()
        people_joining_party.update({ names_of_people: 0})
    print("Enter the total bill value:")
    bill_amount = input()
    names_of_friends = list(people_joining_party.keys())
    single_bill = float(float(bill_amount) / int(number_of_people))
    for b in names_of_friends:
        people_joining_party.update({b: round(single_bill, 2)})
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input()
    if(response.upper() == "YES"):
        random_lucky = random.choice(names_of_friends)
        print("{} is the lucky one!".format(random_lucky))
    else:
        print("No one is going to be lucky")
        
        stage_four
        import random
print("Enter the number of friends joining (including you):")
number_of_friends = input()
if int(number_of_friends) == 0 or int(number_of_friends) < 0:
    print()
    print("No one is joining for the party")
else:
    friends_joining_the_party = {}
    print()
    print("Enter the name of every friend (including you), each on a new line:")
	
    for a in range(int(number_of_friends)):
        names_of_friends = input()
        friends_joining_the_party.update({ names_of_friends: 0})  
    print("Enter the total bill value:")
    total_bill = input()
    friends_names = list(friends_joining_the_party.keys())
    single_bill = int(total_bill) / int(number_of_friends)
    for b in friends_names:
        friends_joining_the_party.update({b: round(float(single_bill), 2)})
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
	
    choice_answer = input()
    if choice_answer.upper() == "YES":
        lucky_friend = random.choice(friends_names)
        print("{} is lucky one!".format(lucky_friend))
        for c in friends_names:
            if c == lucky_friend:
                friends_joining_the_party.update({c: 0})
            else:
                single_bill = float(total_bill) / float((int(number_of_friends) - 1))
                friends_joining_the_party.update({c: round(float(single_bill), 2)})
        print(friends_joining_the_party)
    else:
        print("No one is going to be lucky")
        print()
        print(friends_joining_the_party)
    
