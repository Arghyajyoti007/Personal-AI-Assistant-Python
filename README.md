# Personal-AI-Assistant-Python

# Project Description:
Personal AI is a Python-based voice assistant designed to simplify your daily tasks through intuitive voice commands and natural language understanding. Leveraging Google's Gemini AI and robust speech recognition, Personal AI empowers you to perform a variety of functions, including:
•	Seamless Web Browsing: Effortlessly open websites by voice command (e.g., "Open YouTube," "Open Amazon"). Personal AI intelligently handles both predefined websites and general web searches.
•	Engaging Conversational AI: Participate in natural and context-aware conversations powered by Google's Gemini AI. Personal AI retains conversation history within a session for more relevant interactions.
•	Instant Time Information: Retrieve the current time with a simple voice prompt.
•	Local Music Playback: Enjoy your local music files with voice commands.
•	AI-Driven Information Retrieval: Utilize AI to answer questions and gather information from the web.
•	Flexible Chat History Management: Easily reset or clear the chat history as needed.
•	News Updates: Get the latest news updates through voice commands. Users can request news from a specific date or get yesterday's news based on topic.


# Key Features:
•	Accurate Voice Recognition: Employs the speech recognition library for precise voice command interpretation. 
•	Advanced Natural Language Processing (NLP): Integrates Generative AI (LLM) for natural conversations and intelligent information retrieval. 
•	Automated Web Interaction: Utilizes the specific module to streamline website access and web searches. 
•	Clear Text-to-Speech Output: Uses particular module, for natural and understandable voice feedback. 
•	Dynamic Website Integration: Adapts to user behaviour by adding newly opened websites to its internal list. 
•	Robust Error Handling: Implements comprehensive error handling to manage unexpected inputs and network disruptions gracefully. 
•	News Retrieval: Integrates the News API to retrieve and deliver current news information. Users can request news by topic and specify a date.


# Technologies Used:
•	Python: The core programming language, providing the foundation for the application's logic and functionality.
•	speech_recognition Library: Enables accurate conversion of spoken language into text, facilitating voice command interpretation. Specifically, the Houndify API within this library is used for speech recognition.
•	win32com.client Module: Facilitates Text-to-Speech (TTS) functionality on Windows systems, providing clear and audible voice output.
•	webbrowser Module: Enables automated interaction with web browsers, allowing the application to open websites and perform web searches programmatically.
•	google-generativeai Library: Integrates Google's Gemini AI model, providing advanced natural language processing capabilities for conversational interactions and information retrieval.
•	requests Library: Handles HTTP requests, allowing the application to check website availability, retrieve web-based data, and interact with the News API.
•	re (Regular Expressions) Module: Enables pattern matching and text manipulation for precise command parsing and website extraction.
•	urllib.parse Module: Facilitates URL encoding and parsing, ensuring proper handling of web addresses and search queries.
•	NewsAPI.org: Used to fetch news articles based on user-specified topics and dates. The requests library is used to make API calls, and the json library is used to parse the API responses.
•	datetime module: Used to handle date and time related operations, mainly for the News API functionality.

# Target Audience:
This project is ideal for individuals seeking to:
•	Enhance their productivity through voice-controlled automation.
•	Experience the convenience of an intelligent voice assistant.
•	Explore the capabilities of natural language processing and voice recognition.
•	Stay up to date with the latest news.

# Future Enhancements:
•	Integration with real-time weather APIs. 
•	Expanded music playback features, including specific song selection. 
•	Improved error handling and enhanced user feedback mechanisms. 
•	Refined website handling for greater accuracy. 
•	More refined news retrieval and customization.
•	Weather API Integration.

# Conclusion
This project showcases the potential of combining voice recognition and AI to create a practical and user-friendly personal assistant.

