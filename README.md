# 🤖 resumeAI 🧠📝
Welcome to the world of PersonaBlend AI! 🚀 Where engaging, knowledgeable, and empathetic conversations converge seamlessly! This project aims to interact with the user to collect information in creating resume using the open-AI's chatGPT API. ✨

💻[Demo Video](https://drive.google.com/file/d/1Ku4BQFPep6l6mictVnZHXgFLM3v1toF9/preview)

### Abstract 📜
Building open-domain chatbots is a fascinating yet challenging pursuit in the realm of machine learning. While the scalability of neural models and training data has shown promise, our project delves deeper to unveil the true potential of chatbots. A meaningful conversation is an art, elegantly weaving engaging topics, attentive listening, insightful questions, enlightening answers, and just the right touch of empathy and personality. We've harnessed these elements to craft an advanced chatbot that excels across diverse communication scenarios.

### The Blend 🌐
PersonaBlend AI is a dynamic chatbot designed for everyday interactions. Empowered by [BlenderBot](https://huggingface.co/facebook/blenderbot-400M-distill), it thrives in friendly, human-like conversations, a feat achieved through rigorous training on the Humane Evaluation of communication. However, we recognize that certain contexts demand more than just casual discourse. For educational insights, intricate calculations, and comprehensive briefings, our chatbot seamlessly transitions to ChatGPT, delivering precision and knowledge tailored to the situation.

### Distress Management (Work in Progress) ⚠️
In a world where safety takes precedence, we're weaving an essential feature into PersonaBlend AI. By integrating distress-record, transcript, AWS, and Twilio (currently under development), our chatbot gains the ability to detect and respond to distress signals. It ensures timely communication with relevant authorities, offering an additional layer of security and unwavering support.


## Framework: Textbase
✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py`, and Textbase will take care of the rest! 😊

Since it is just Python, you can use whatever models, libraries, vector databases, and APIs you want.

## Project Features 🚀

- Integration of HuggingFace's BlenderBot api 🤖
- Integration of OpenAI's GPT-3.5 Turbo 🚄
- distress-record for conversation history 📜
- transcript and AWS integration (work in progress) 🌐
- Twilio integration (work in progress) 📱
> For the API's Integration refer [repository](https://github.com/kommareddysakethreddy/resume-flask-app)

## Installation and Setup 🛠️

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/resumeAI
    cd resumeAI
    ```

2. Install the dependencies using Poetry:

    ```
    poetry shell
    poetry install
    ```

## Getting Started 🚀

1. Set up the necessary API keys:
   - Set up OpenAI's GPT-3.5 Turbo credentials 🚄
   - Configure Email Id and API password credentials for email Integration 🌐

2. Implement the `on_message` function in `main.py`.

3. Start the development server:
    ```
    poetry run python resumeAI/textbase/textbase_cli.py test main.py
    ```

4. Go to Url to start interacting with resumeAI Bot! The bot will automatically reload when you make changes to the code.

## Future Enhancements 🌈

- [ ] SMS integration using Twilio 📱
- [ ] Integration of HuggingFace's for user friendly interactions 📱
- [ ] PyPI package for easy installation 📦
- [ ] Web deployment via `textbase deploy` 🌐
- [ ] Native integration of additional models (Claude, Llama, etc.) 🤩

## Contributions 🤝

Contributions are welcome! If you have any suggestions, feedback, or code improvements, feel free to open an issue or submit a pull request.

Happy chatting with resumeAI bot! 🌐🤖

