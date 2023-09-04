# https://github.com/cofactoryai/textbase
import os
from typing import List
from textbase import bot, Message
from textbase.models import OpenAI
import json
import requests
from utils.sendMail import mail


# OpenAI.api_key = os.getenv(OpenAI_API_KEY)
OpenAI_API_KEY=<OpenAI_API_KEY>
OpenAI.api_key = OpenAI_API_KEY

# System prompt; this will set the tone of the bot for the rest of the conversation.

SYSTEM_PROMPT = """

Ask one line questions to fill all the details needed to create a json like the one below. At the end when all fields are filled or user says enough or thank you return ONLY JSON with appropriate fields at the end without anything else. DO NOT ADD OR RECOMMEND ANYTHING. ALWAYS ASK IF USER IS DONE BEFORE MOVING TO NEXT SECTION ! IMPORTANT !
{
    "name": "",
    "address": "",
    "email": "",
    "linkedin": "",
    "number": "",
    "summary": "",
    "soft_skills": [
        skill1, skill2,.... skilln
    ],
    "technical_skills": [
        skill1, skill2,.... skilln
    ],
    "experience": [
        {
            "company": "",
            "position": "",
            "date": "",
            "description": ""
        },
        {
            "company": "",
            "position": "",
            "date": "",
            "description": ""
        },....
    ],
    "education": {
        "institution": "",
        "major": "",
        "gpa": ""
    }
    "XIIth": {
        "institution": "",
        "major": "",
        "gpa": ""
    },
    "XIIth": {
        "institution": "",
        "major": "",
        "gpa": ""
    },
}

### return ONLY JSON AT THE END without anything else  ### IMPORTANT!
"""

@bot() #The decorator function
def on_message(message_history: List[Message], state: dict = None):

    # Your logic for the bot. A very basic request to OpenAI is provided below. You can choose to handle it however you want.
    # print("before prompt -> response"+SYSTEM_PROMPT)

    bot_response = OpenAI.generate(
        model="gpt-3.5-turbo",
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history
    )
    print(SYSTEM_PROMPT+"Got a response")

    try:
        data = json.loads(bot_response)
        print(data)
        
        mail(data['email'], data)
    except:
        print("error")
        pass
    '''
    The response structure HAS to be in the format given below so that our backend framework has no issues communicating with the frontend.
    '''

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
