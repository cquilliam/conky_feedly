## Conky Feedly script

**Description**

This conky script allows you to display the unread articles of a given Feedly category on your desktop.  This is for display purposes only, and the articles are not clickable.  Once you view the article in Feedly, it will be removed from the list in the next refresh (every 5 minutes).

**Requirements**

- Python3
- Various python modules like json and requests
- Conky
- A Feedly account with Categories set up (http://www.feedly.com)

**Installation**

- Move/Copy conky_feedly directory and rename it to something like ~/.conky/Feedly to make it easier to find in Conky Manager
- Go to https://feedly.com/v3/auth/dev and request your access token via email
- Edit settings.json file and paste your access token between the quotes where indicated
- Run 'python get_streamid.py' to get a list of your user categories from Feedly, and paste the one you want to follow in the appropriate place in settings.json
- Run Conky Manager, select the script in the list, and all should be well.


**Troubleshooting**

Nothing displayed?  

Try running from the console "conky -c ~/.conky/Feedly/conkyrc" and see what the message is.  Probably a missing python module or something.

Credits

This is solely based on the work of the following projects.  I basically took their work and modified it for my needs of only showing Feedly:

FeedlyClient by zgw21cn https://github.com/zgw21cn/FeedlyClient

Awesome Conky by madhur https://github.com/madhur/awesome-conky
