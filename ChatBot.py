import random

# Instructions on how to use the chatbot
print("""
Welcome to the Friendly Chatbot!
This chatbot is here to talk about your day and respond in a way that matches your mood.
Simply type something about your day, like how you're feeling or what you've been up to.
The chatbot will try to understand your emotions based on keywords you use.
If it doesn't understand, it will ask you to teach it new words and responses.
Type 'bye' anytime to end the conversation. Have fun chatting!
""")

# Greeting options
greetings = ["Hi there!", "Hey, how was your day?", "Hello, tell me about your day!", "Hi, what's new?", "Hey, how are you feeling today?"]
goodbyes = ["Take care!", "Catch you later!", "Goodbye!", "See you soon!", "Have a great day!"]

# Expanded keyword categories
positive_keywords = [
    "happy", "awesome", "productive", "good", "great", "excited", "joyful", "fantastic", 
    "amazing", "wonderful", "cheerful", "thrilled", "positive", "delighted", "smiling", 
    "blessed", "lucky", "proud", "energetic", "enthusiastic", "content", "uplifted"
]
negative_keywords = [
    "sad", "frustrated", "tired", "bad", "angry", "upset", "depressed", "lonely", 
    "anxious", "stressed", "worried", "heartbroken", "miserable", "down", "hopeless", 
    "hurt", "exhausted", "drained", "overwhelmed", "defeated", "discouraged", "lost"
]
neutral_keywords = [
    "meh", "okay", "fine", "average", "alright", "nothing", "so-so", "normal", 
    "usual", "neutral", "plain", "ordinary", "indifferent", "same", "moderate", "stable"
]

# Responses
positive_responses = [
    "Sounds like your day was full of good vibes!", "That's awesome to hear!", "You're spreading positivity!", 
    "Your energy is contagious!", "Keep up the great mood!", "You deserve all the joy!", "Love hearing that!"
]
negative_responses = [
    "Sorry to hear that, hope you're okay.", "That sounds rough, hang in there.", "I'm here if you want to talk more.", 
    "Take it one step at a time.", "Bad days happen, but tomorrow's a fresh start.", "Sending you a virtual hug!", 
    "You’re stronger than you think!"
]
neutral_responses = [
    "Seems like your day was pretty average.", "Alright, nothing extraordinary but that's okay!", "Thanks for sharing your day.", 
    "Not every day has to be special, and that's alright.", "Sounds like a balanced day.", "Sometimes neutral is good, too!"
]

# Keywords for chatbot's feelings
bot_keywords = positive_keywords + negative_keywords + neutral_keywords

# Learning dictionary
learning = {}

def chatbot():
    print(random.choice(greetings))
    
    while True:
        user_input = input("You: ").lower()
        
        # End conversation if user types "bye"
        if user_input == "bye":
            print(random.choice(goodbyes))
            break

        # Immediately end conversation if "you" is mentioned
        if "you" in user_input:
            bot_feeling = random.choice(bot_keywords)
            print(f"I am feeling {bot_feeling}. I'm tired, I enjoyed talking with you. " + random.choice(goodbyes))
            break

        # Check keywords and calculate scores
        positive_score = sum(word in user_input for word in positive_keywords)
        negative_score = sum(word in user_input for word in negative_keywords)
        neutral_score = sum(word in user_input for word in neutral_keywords)
        
        # Determine response based on scores
        if positive_score > 1:
            print(random.choice(positive_responses))
        elif negative_score > 1:
            print(random.choice(negative_responses))
        elif positive_score > 0 and negative_score > 0:
            print(random.choice(neutral_responses))
        elif positive_score > 0 or negative_score > 0 or neutral_score > 0:
            print(random.choice(neutral_responses))
        elif user_input in learning:
            print(learning[user_input])
        else:
            print("I didn't understand that. Can you teach me?")
            new_response = input("Your response: ")
            emotion = input("Is this positive, negative, or neutral? ").lower()
            learning[user_input] = new_response
            if emotion == "positive":
                positive_keywords.append(user_input)
            elif emotion == "negative":
                negative_keywords.append(user_input)
            elif emotion == "neutral":
                neutral_keywords.append(user_input)

# Run the chatbot
chatbot()
