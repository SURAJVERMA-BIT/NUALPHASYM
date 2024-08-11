import speech_recognition as sr
import pyttsx3
import threading

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# To handle the text-to-speech interruptions
def speak(text):
    global tts_thread
    if tts_thread and tts_thread.is_alive():
        tts_engine.stop()  # Stop current speech if it's still running
    tts_thread = threading.Thread(target=lambda: tts_engine.say(text))
    tts_thread.start()
    tts_engine.runAndWait()

def listen(max_attempts=2):
    for _ in range(max_attempts):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)
                response = recognizer.recognize_google(audio)
                print(f"You said: {response}")
                return response.lower()
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Could you please repeat?")
            except sr.RequestError:
                speak("Sorry, my speech recognition service is down.")
                return None
            except sr.WaitTimeoutError:
                speak("Listening timed out. Please try again.")
    
    # After exceeding max_attempts, ask user to type their response
    speak("I couldn't understand you. Please type your response.")
    return input("Type your response: ").strip().lower()

def get_valid_response(options):
    speak(f"Please respond with one of the following: {', '.join(options)}")
    while True:
        response = listen()
        if response in options:
            return response
        speak(f"I didn't understand. Please say one of the following: {', '.join(options)}")

def magical_number_guesser():
    speak("Think of a number between 1 and 100.")
    
    low, high = 1, 100
    
    while low <= high:
        guess = (low + high) // 2
        speak(f"My guess is {guess}. Was it correct?")
        correct = get_valid_response(['yes', 'no'])
        
        if correct == 'yes':
            speak("I guessed your number!")
            return
        
        speak("Is your number higher or lower?")
        higher_lower = get_valid_response(['higher', 'lower'])
        
        if higher_lower == 'higher':
            low = guess + 1
        elif higher_lower == 'lower':
            high = guess - 1

def magical_alphabet_guesser():
    speak("Think of a letter between A and Z.")
    
    low, high = ord('A'), ord('Z')
    
    while low <= high:
        guess = chr((low + high) // 2)
        speak(f"My guess is {guess}. Was it correct?")
        correct = get_valid_response(['yes', 'no'])
        
        if correct == 'yes':
            speak("I guessed your letter!")
            return
        
        speak("Is your letter higher or lower in the alphabet?")
        higher_lower = get_valid_response(['higher', 'lower'])
        
        if higher_lower == 'higher':
            low = ord(guess) + 1
        elif higher_lower == 'lower':
            high = ord(guess) - 1

def magical_symbol_guesser():
    symbols = list("!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~")
    speak("Think of a symbol.")
    
    low, high = 0, len(symbols) - 1
    
    while low <= high:
        guess_index = (low + high) // 2
        guess = symbols[guess_index]
        speak(f"My guess is '{guess}'. Was it correct?")
        correct = get_valid_response(['yes', 'no'])
        
        if correct == 'yes':
            speak("I guessed your symbol!")
            return
        
        speak("Is your symbol higher or lower in the list?")
        higher_lower = get_valid_response(['higher', 'lower'])
        
        if higher_lower == 'higher':
            low = guess_index + 1
        elif higher_lower == 'lower':
            high = guess_index - 1

def advanced_magical_guesser():
    speak("Would you like to play the number guesser, alphabet guesser, or symbol guesser?")
    choice = get_valid_response(['number', 'alphabet', 'symbol'])

    if choice == 'number':
        magical_number_guesser()
    elif choice == 'alphabet':
        magical_alphabet_guesser()
    elif choice == 'symbol':
        magical_symbol_guesser()

tts_thread = None  # Initialize the thread variable
advanced_magical_guesser()
