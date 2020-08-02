# Twiiter-Bot
This is a chat bot for twitter which will re-tweet your tweet if you tweet it with the message "hi" or "#hi". The re-tweet will be as follows, hi @username whats up!.

You can modify the code as per your needs.
These are steps Involved in making this twitter bot,
Step1 --> You have to install the module tweepy which can done using pip, "pip install tweepy". 
Step2 --> You have to apply for Twitter Developer Acess. Once all the standard proccedures are done, you will be sent a confirmation mail.
          You can apply for Developer Acess here, 'http://developer.twitter.com' You will then have access to the Access keys and tokens. 
Step3 --> You have to copy and paste in the code where I have mentioned Access Keys and tokens. Now, your twitter bot is ready to run. 
Step4 --> You can now add or make changes to the code, for what your twitter bot should reply. 
Step5 --> Run your code in the terminal or server to start your twitter bot. 
Step6 --> The twitter bot is now fully functional and ready to reply.

#Note: lastseen.txt
          There will be situations where there will be multiple tweets where the bot would have to reply to all the tweets.
Since, the bot works in the manner of stack, it will reply to the already replied messages once again.  In order to stop this issue
I have added a last seen text, whenever the bot completes replying to all the tweets, it will store the last tweet id.  So, the next time
when the program runs, it wont reply to tweet past this id.
