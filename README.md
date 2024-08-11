# Magical Guesser

## Overview

Magical Guesser is an interactive text-to-speech and speech recognition application that allows users to play guessing games. The application can guess a number, a letter, or a symbol that the user is thinking of. It uses Python libraries for speech recognition and text-to-speech functionalities.

## Features

- **Number Guesser**: Guess a number between 1 and 100.
- **Alphabet Guesser**: Guess a letter between A and Z.
- **Symbol Guesser**: Guess a symbol from a predefined set.
- **Speech Interaction**: The application speaks to the user and listens for their responses, handling interruptions and adjusting speech dynamically.

## Installation

1. **Clone the Repository**

   
   git clone <repository_url>
   cd <repository_directory>

2. **Create a Virtual Environment (optional but recommended)**


    python -m venv venv
    `venv\Scripts\activate`
3. **Install the Required Libraries**

Install the dependencies listed in requirements.txt:
pip install -r requirements.txt
## Usage
Run the script to start the game:

python NUMBER_GUESSER.py
## Playing the Game
1. **Number Guesser**: Think of a number between 1 and 100. The application will attempt to guess it based on your responses.

2. **Alphabet Guesser**: Think of a letter between A and Z. The application will guess the letter you are thinking of.

3. **Symbol Guesser**: Think of a symbol from the following list: !@#$%^&*()_+-=[]{}|;:'",.<>?/~`. The application will try to guess it.

## Speech Interaction
The application uses text-to-speech to communicate with you and listens for your spoken responses. If the speech output is interrupted by your response, the application will handle it gracefully and adjust the output accordingly.

## Troubleshooting
Ensure you have a working microphone and speakers.
If you encounter issues with speech recognition, verify your internet connection and microphone settings.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to fork the repository and submit pull requests with improvements or bug fixes.

For any issues or questions, please open an issue in the repository or contact the author.

## Author
[Suraj Verma]
[sv9052788@gmail.com]