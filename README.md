# Restaurant Chatbot

Welcome to the Restaurant Chatbot project! This chatbot is designed to assist customers in placing orders, understanding their meal preferences, providing information about the menu, and catering to their needs.

## Features

- **Order Placement:** Customers can place orders for their desired meals.
- **Meal Preferences:** The chatbot understands and caters to customers' meal preferences and cuisines.
- **Menu Information:** Customers can inquire about the menu and available dishes.
- **Customer Needs:** The chatbot addresses various customer needs related to restaurant services.

## Project Structure

- **Data:**
  - `data/nlu.yml`: Contains examples for training the Natural Language Understanding (NLU) model.
  - `data/stories.yml`: Defines sample conversations for training the dialogue model.
  - `domain.yml`: Specifies the domain, including intents, entities, and actions.
  
- **Model Configuration:**
  - `config.yml`: Configures the Rasa NLU and Core pipeline.

## Dataset

The dataset for this chatbot includes examples of different intents, entities, and scenarios related to restaurant services.

## Getting Started

1. Install Rasa: `pip install rasa-x --extra-index-url https://pypi.rasa.com/simple`
2. Install Spacy modalities for Rasa: `pip install rasa[spacy]`
3. Download Spacy: `python -m spacy download en_core_web_md `
4. Train the Model: `rasa train`
5. Run the Chatbot: `rasa shell`

### rasa_chatbot.py can be run to note down the various outputs that are given by the trained model along with their confidence scores.
### The test folder has the confusion matrix images which were obtained by running the model in the test mode.

Happy chatting and dining! 🍽️🤖
