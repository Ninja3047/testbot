#!/bin/env python

import json
from configparser import ConfigParser
from watson_developer_cloud import ConversationV1

config = ConfigParser()
config.read("secrets.ini")

conversation = ConversationV1(
        username=config['watson']['username'],
        password=config['watson']['password'],
        version='2016-10-01')

workspace_id = config['watson']['workspace_id']

while True:
    text = input()
    if text == "exit":
        break
    response = conversation.message(workspace_id=workspace_id, message_input={'text': text})
    # print(json.dumps(response, indent=2))
    print(response['output']['text'][0])
