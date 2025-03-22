import os
import win32com.client
import speech_recognition as sr
import webbrowser
import datetime
from google import genai
from google.genai import types
import requests
import re
import urllib.parse
import json
import datetime


# History of the local chat
chat_history = ""

# List of general sites
sites = [
    ['youtube', 'https://www.youtube.com/'],
    ['wikipedia', 'https://www.wikipedia.org/'],
    ['flipkart', 'https://www.flipkart.com/'],
    ['amazon', 'https://www.amazon.in/ref=nav_logo'],
    ['google', 'https://www.google.com/'],
    ['myntra', 'https://www.myntra.com/'],
    ['facebook', 'https://www.facebook.com/'],
    ['instagram', 'https://www.instagram.com/']
]


# General conversation
def chat(query, chatStr):
    global chat_history

    chatStr += f"User: {query}\nAI Assistant: "
    client = genai.Client(api_key="AIzaSyB56L9q1GA4EO5GoKDbt573tj9KjizZwzw")  # Replace with your API key

    model = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=chatStr,
        config=genai.types.GenerateContentConfig(
            candidate_count=1,
            max_output_tokens=50,  # Limit output tokens for single-line responses
            temperature=0.2,  # Lower temperature for more precise responses
            top_p=0.8,
            top_k=1
        )
    )

    try:
        response_text = model.text.strip().replace('\n', ' ')
    except AttributeError:
        response_text = "Sorry, I couldn't generate a response."

    chatStr += f'{response_text}\n'
    say(response_text)

    return response_text, chatStr  # return the updated chat history


# Computer try to Say
def say(text):
    # Help to Speak according to given input text
    # while 1:
    #     print("Enter word")
    #     s=input()
    #     speaker.Speak(s)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


# Computer try to listen
def takeCommand():
    # Computer will be listens through this and will take the command we provide
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_houndify(audio, "WXdnwfO7BOWEWtwFB72Lpg==",
                                         '3qp9aiYSjUyTmE3TkcNi-pfUCwD6JvVEHIU2IVvm4Rp5smhC5us44SaVwbJpQyTlKskgZT1PQoVTZgZKuayGuA==')
            print(f"User Said: {query[0]}")  # query[0] as returns a tuple and query consist of the (Speech,Score)
            return query[0]
        except Exception as e:
            return "Sorry Error Occurred. I can't understand you!"


# response from OpenAI
def ai(prompt):
    # openai.api_key = OPENAI_API_KEY
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    client = genai.Client(api_key="AIzaSyB56L9q1GA4EO5GoKDbt573tj9KjizZwzw")
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    print("The response is: ", response.text)
    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
    except Exception as e:
        # print("Sorry no choices")
        pass
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


# checks if a website is valid or not
def website_exists(url):
    """Checks if a website exists."""
    try:
        response = requests.head(url, timeout=5)  # Added timeout.
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False


# helps to open a website
def open_website(query):
    if not query:  # Check if query is empty
        return  # Do nothing if no query

    query_lower = query.lower()
    for site_name, site_url in sites:
        if re.search(rf"\bopen\s+{site_name}\b", query_lower):  # use regex for better matching.
            say(f"Opening {site_name} Sir")
            print(f"Opening {site_name}")
            webbrowser.open(site_url)
            return

        # If not a known site, try to open it as a search query or URL
    try:
        # Attempt to extract a website name or search terms.
        extracted_query = re.search(r"open\s+(.+)", query_lower).group(1)  # extract the site name or query
        if extracted_query.startswith("www.") or extracted_query.startswith("http"):
            webbrowser.open(extracted_query)
            sites.append([extracted_query, extracted_query])  # add it to sites list
            print(f"Opening and adding {extracted_query} Sir")  # Replace with your say function
        else:
            # Assume it's a search query
            search_query = urllib.parse.quote_plus(extracted_query)
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            print(f"Searching for {extracted_query} Sir")  # Replace with your say function

    except AttributeError:
        print("Could not understand the website request.")  # Replace with your say function


def daily_news(news_of_perticular_date):
    say("What is the type of news you want to see")
    print("listning...")
    topic_news = takeCommand()
    if not topic_news:
        return
    url = f"https://newsapi.org/v2/everything?q={topic_news}&from={news_of_perticular_date}&sortBy=popularity&apiKey=8f18f7ceec6d4b329dece285bdda8625"
    # print(url)
    r = requests.get(url)
    news = json.loads(r.text)

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("______________________________")


def wether_report(query):
    pass
def main():
    if __name__ == '__main__':
        say("I'm Your Personal AI")
        chat_history = ""
        while True:
            print("Listening")
            query = takeCommand()
            if not query:  # Check if query is empty
                say("Please provide input")
                continue
            elif "exit".lower() in query.lower():  # checked
                say("Exiting")
                break

            elif "quit".lower() in query.lower():
                say("Quiting")
                break

            # to open sites
            # todo : Add more Sites
            # for site in sites:
            #     if f"Open {site[0]}".lower() in query.lower():
            #         say(f"Opening {site[0]} Sir")
            #         webbrowser.open(site[1])
            elif "open".lower() in query.lower():
                open_website(query)

            # to play music
            # todo : Add a feature to play specific song
            elif "play music".lower() in query.lower():  # checked
                musicPath = "D:\Python\sampleMusic.mp3"
                os.startfile(musicPath)

            # to know the time
            elif "the time" in query:  # checked
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")

            # Get AI Response
            elif 'using artificial intelligence'.lower() in query.lower():
                if query:
                    ai(prompt=query)
                else:
                    say("Give some query")

            elif "reset chat".lower() in query.lower():
                chat_history = ""

            elif "clear".lower() is query.lower():
                chat_history=""

            # todo : News API
            elif "news".lower() in query.lower():
                say("Do you want to see news from any particular date")
                print("listning...")
                user_input = takeCommand()

                if "yes".lower() in user_input.lower():
                    year = int(input("Enter the Year: "))
                    month = int(input("Enter the month: "))
                    day = int(input("Enter the day: "))
                    news_of_perticular_date = datetime.datetime(year, month, day)
                    daily_news(news_of_perticular_date)
                else:
                    today = datetime.date.today()
                    yesterday_date = today - datetime.timedelta(days = 1)
                    daily_news(yesterday_date)
            else:
                response, chat_history = chat(query, chat_history)
                print("AI Assistant:", response)

    # todo : Weather API



main()