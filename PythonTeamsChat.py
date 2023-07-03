# Python script to message Teams via a python script

# Create new team or Channel where you/group would like to have a message recieved

# Create a webhook in MS Teams

# Add an incoming webhook to a Teams channel:

# Navigate to the channel where you want to add the webhook and select (•••) Connectors from the top navigation bar.
# Search for Incoming Webhook, and add it.
# Click Configure and provide a name for your webhook.
# Copy the URL which appears and click "OK".

# 2. Install pymsteams in python terminal 
# pip install pymsteams


# 3. Create your python script

#Example:
import pymsteams
myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>")
myTeamsMessage.text("Hello World!!!")
myTeamsMessage.send()
