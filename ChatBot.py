import random
greetings = ["Hello!", "Sup amigo?!", "Nice to meet you!"]
goodbyes = ["Bye!", "Later Gator", "God Speed!", "See you on the other side."]

keywords = [ "book", "game", "work", "party", "parties", "friend", ]
responses = ["Books are a fun way to let your mind be enveloped by knowlage.", 
             "Video games are so much fun to play but can get a little violent.", 
             "Work sucks but it is nice to get paid.", 
             "Parties are so much fun. I wish I could have been there.", 
             "Parties are so much fun. I wish I could have been there.", 
             "Friends are so much fun to be around and I hope we can be friends."
            ]

print(random.choice(greetings) + " What did you do today?")

user = input("Say something (or type bye to quit): ")
user = user.lower()

while (user != "bye"):
    keyword_found = False

    for index in range(len(keywords)):
        if (keywords[index] in user):
            print("Bot: " + responses[index])
            keyword_found = True

    if (keyword_found == False):
        new_keyword = input("I'm not sure I know how to respsond. What keyword should I respond to? ")
        keywords.append(new_keyword)
        new_response = input("How should I respond to " + new_keyword + "? ")
        responses.append(new_response)

    user = input("Say something (or type bye to quit): ")
    user = user.lower()

print(random.choice(goodbyes))
