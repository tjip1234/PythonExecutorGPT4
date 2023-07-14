# Overview

The "Execute Code" plugin allows you to execute Python code directly within the ChatGPT environment by running a local Python instance. This plugin enables you to run Python code and interact with the output seamlessly during your conversations with the ChatGPT model.

## Setup

To set up and use the "Execute Code" plugin, follow the steps below:

1. Install the required packages by running the following command in your terminal or command prompt:

pip install -r requirements.txt

2. Start the local server by running the following command:

python main.py

This will start the server on `localhost:5003`.

3. Open the ChatGPT web interface by navigating to [https://chat.openai.com](https://chat.openai.com).

4. In the model selection drop-down, choose "Plugins".

5. Select "Plugin store".

6. Click on "Develop your own plugin".

7. Enter `localhost:5003` as the URL since the server is running locally, and click "Find manifest file".

8. The "Execute Code" plugin will be added to your list of available plugins.

## Usage

To use the "Execute Code" plugin in your conversation with ChatGPT, follow these steps:

1. Begin a conversation with ChatGPT using the "Execute Code" plugin selected as the active plugin.

2. When you want to execute Python code, just ask it to generate code and execute it.

## Development

A lot of things are not working, for example matplotlib output or installing libraries automatically.
Superceded by openAI's own implementation

