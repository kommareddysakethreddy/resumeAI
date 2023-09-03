# https://github.com/cofactoryai/textbase
import os
from typing import List
from textbase import bot, Message
from textbase.models import OpenAI
import json
import requests
from utils.sendMail import mail


OpenAI.api_key = os.getenv(OpenAI_API_KEY)

# System prompt; this will set the tone of the bot for the rest of the conversation.

SYSTEM_PROMPT = """
###Personal Information###
Name:
Address:
Email:
LinkedIn:
Phone Number:
Summary:

###Soft Skills### 
###Technical Skills### 
Includes front end and back end technologies
Other Skills

###Current Education:###
-->College name
year of completion 
CGPA or percentage of marks
-->12th Education 
-->10th Education 

###Work Experience###
format : Company name,worked from a to b 
Information user wants to provide related to projects worked in company 

###Projects###
Projects worked on 
Format: project names, project details, Tech Stack Used


Ask one line question or reply to answer in one statement and get all the above details one by one and convert it to a appropriate json format with fiels and nested fields. return only json with appropriate fields.  

"""
m=[]
@bot() #The decorator function
def on_message(message_history: List[Message], state: dict = None):

    # Your logic for the bot. A very basic request to OpenAI is provided below. You can choose to handle it however you want.
    # print("before prompt -> response"+SYSTEM_PROMPT)

    bot_response = OpenAI.generate(
        model="gpt-3.5-turbo",
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history
    )
    print(SYSTEM_PROMPT+"after prompt -> response")

    m.append(bot_response)
    print(bot_response)

    try:
        da = json.loads(bot_response)
        print(type(bot_response), type(da))
        api = "https://saketh63.pythonanywhere.com/generate-resume-api"
        res = requests.post(api, json=da)
        print(res.text)
        mailing(da['email'], res.text)
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
