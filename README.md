# py-etype-tts-sample-code

This is a Python Sample code showing how to send a voice message in Hebrew to a user's phone using the Nexmo Voice API

Requirements
- Create a Nexmo account (free)
- Create an application and save the private key
- Rent a Nexmo number (make sure you have enough credits)
- Link your Nexmo number to your voice application

Code configuration
- add your application_id (line 3)
- make sure you pointthe private_key (line 4) to your application private key file
- set the phone number (international format) of the recipient (line 9)
- set the phone number (international format) of the caller (line 10). This is the number you've rented and linked to the Nexmo application
- set the answer_url to your json file

NCCO (Nexmo Call Control Object)
- the file needs to be of a mime type application/json
- it contains one action: talk
- the voiceName determine the language. Here Carmit is Hebrew
- text is the text that will be said to the end user
