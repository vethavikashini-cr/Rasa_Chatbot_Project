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
  - `data/domain.yml`: Specifies the domain, including intents, entities, and actions.
  
- **Model Configuration:**
  - `config.yml`: Configures the Rasa NLU and Core pipeline, including the SentimentAnalyzer.

## Dataset

The dataset for this chatbot includes examples for different intents, entities, and scenarios related to restaurant services.

## Getting Started

1. Install Rasa: `pip install rasa`
2. Train the Model: `rasa train`
3. Run the Chatbot: `rasa shell`


Happy chatting and dining! 🍽️🤖
