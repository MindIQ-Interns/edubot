# edubot
An interface for creating and delivering quizzes.

Contains 3 modular apps:

1. The Facebook Messenger interface, which 
  a) receives messages from facebook, translates it to a format readable by the second app, and passes it to the second app.
  b) receives data from the second app, translates it into a json message, and posts it to Messenger.
2. The Quiz Bot, which receives messages, processes them, and returns appropriate responses via queries to the database which stores the quizzes.
3. The web portal, which allows users to upload quizzes to the database.

NOTE: STILL IN DEVELOPMENT


Format of JSON to be received by the Quiz Bot:
 {
    'sender_id': <sender_id>,
    'type': <'raw'/'postback'/'data'>,
    'text': <text>,
    'variable_tag': <'None' if 'type' is not 'data', else variable name>
 }