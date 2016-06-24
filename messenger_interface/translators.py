# NOTE: The responses given ensure that only text messages and postbacks will be processed by quiz_bot.

from exceptions import Exception


class MessageTypeDoesNotExist(Exception):

    def __init__(self, error_message):
        super(MessageTypeDoesNotExist, self).__init__(self, error_message)


def quiz_bot_message(sender_id, message_type, text):
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
            return quiz_bot_message(sender_id=message['sender']['id'], message_type='raw', text=message['message']['text'])
        else:
            return None

    elif 'postback' in message:
        if 'payload' in message['postback']:
            return quiz_bot_message(sender_id=message['sender']['id'], message_type='postback', text=message['postback']['payload'])
        else:
            return None

    else:
        return None


translate = {
    'messenger': {'quiz_bot': translate_for_quiz_bot},
}