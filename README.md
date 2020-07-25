# whatsapp_web_bot
A simple python code snippet that utilises selenium to send messages to friends using the WhatsApp Web client
## Whatsapp Bot

### How does it work?
Initally you will need to locate the folder in which your cookies are located:

**Windows** this would typically be in your *AppData\\Local\\Google\\Chrome\\User Data\\Default*

**Mac** this would be in the *Library/Application Support/Google/Chrome/Default*

Replace the folder location in the whatsapp_web_bot.py file on line 14

```chrome_options.add_argument("user-data-dir=YOUR_DIRECTORY_HERE")```

By doing this we can bypass the QR code on launch after the initial scan to prevent the need to scan everytime!

### What can I do?
So far there is only one function which is to send a message to a specific user, however there will be added functionality such as scanning for new messages, notification for an online user etc.
