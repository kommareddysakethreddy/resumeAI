# 🤖 resumeAI 🧠📝
Welcome to the world of resumeAI! 🚀 Where engaging, knowledgeable, and empathetic conversations converge seamlessly! This project aims to interact with the user to collect their information to create a resume using the open-AI's chatGPT API, and customize using various templates as required. ✨

💻[Demo Video](https://drive.google.com/drive/folders/17mjzoJ-T3DF-aFqvTF6QNSwNMeV2p0Up?usp=sharing)

### Abstract 📜
Welcome to the future of resume creation with ResumeAI, an innovative project that leverages the power of OpenAI's ChatGPT API to provide users with an engaging, knowledgeable, and empathetic experience. In today's competitive job market, a well-crafted resume is the key to unlocking professional opportunities, and ResumeAI aims to streamline this process.

ResumeAI seamlessly blends the art of conversation with intelligent data collection to help users create personalized and effective resumes. Through natural and interactive dialogue, users can input their professional information, career aspirations, and achievements. The ChatGPT API, powered by OpenAI's advanced language model, ensures that the interaction is not only informative but also engaging and empathetic, making the resume creation process an enjoyable experience.


## Framework: Textbase
✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py`, and Textbase will take care of the rest! 😊

Since it is just Python, you can use whatever models, libraries, vector databases, and APIs you want.

## Project Features 🚀

- Integration of OpenAI's GPT-3.5 Turbo 🚄
- Integration of pdfcrowd to convert HTML files to PDF
- Using SMTP to send the final resume (pdf) directly to end user
- Using SMTP to send final resume (word) to allow more customization by user (work in progress)
- Twilio integration (work in progress) 📱

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
- [ ] Implementing Features to enhance ATS scores for user.
- [ ] Integration of HuggingFace's for user friendly interactions 📱
- [ ] Web deployment via `textbase deploy` 🌐
- [ ] Native integration of additional models (Claude, Llama, etc.) 🤩

## Contributions 🤝

Contributions are welcome! If you have any suggestions, feedback, or code improvements, feel free to open an issue or submit a pull request.

Happy chatting with resumeAI bot! 🌐🤖

