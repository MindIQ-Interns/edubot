# NOTE: The responses given ensure that only text messages and postbacks will be processed by quiz_bot.

import json, requests
from pprint import pprint
from exceptions import Exception

from .secrets import POST_MESSAGE_URL


class MessageTypeDoesNotExist(Exception):

    def __init__(self, error_message):
        super(MessageTypeDoesNotExist, self).__init__(self, error_message)


def message_for_bot(sender_id, message_type, text):
    if message_type not in ['raw', 'postback']:
        raise MessageTypeDoesNotExist(text + ' is not a valid message type for quiz_bot.')

    else:
        return {
            'sender_id': sender_id,
            'type': message_type,
            'text': text,
        }


def translate_for_quiz_bot(message):
    if 'message' in message:
        if 'text' in message['message']:
            return message_for_bot(sender_id=message['sender']['id'], message_type='raw', text=message['message']['text'])
        else:
            return None

    elif 'postback' in message:
        if 'payload' in message['postback']:
            return message_for_bot(sender_id=message['sender']['id'], message_type='postback', text=message['postback']['payload'])
        else:
            return None

    else:
        return None


def raw_message(recipient_id, text):
    return {
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'text': text
        }
    }


def send(message_from_bot):
    pprint(message_from_bot)
    #message = json.dumps(message_from_bot)
    #status = requests.post(POST_MESSAGE_URL, headers={'Content-Type': 'application/json'}, data=message)
    #pprint(status.json())


def translate_and_send(message_from_bot):
    for message in message_from_bot:
        send(raw_message(recipient_id=message['recipient_id'], text=message['text']))