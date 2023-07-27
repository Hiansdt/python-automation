import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

responses = {
    "bye": "Goodbye! Have a great day!",
    "How are you?": "I'm doing well, thank you!",
    "default": "I'm not sure how to respond to that.",
    "hello": "Hello! How can I assist you?",
}


def preprocess_input(user_input):
    stop_words = set(stopwords.words("english")) - {"how", "are", "you"}
    words = word_tokenize(user_input)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

    return filtered_words


def generate_response(user_input):
    filtered_input = preprocess_input(user_input)

    for pattern in responses:
        if all(word in filtered_input for word in preprocess_input(pattern)):
            print(preprocess_input(user_input))
            print(pattern)
            return responses[pattern]
        else:
            return responses["default"]


def main():
    print("Welcome to the chatbot! Please enter your message below.")
    while True:
        user_input = input("You: ")
        response = generate_response(user_input)
        print("Bot: " + response)


if __name__ == "__main__":
    main()
