import os, time
from slackclient import SlackClient
from eight_percent import *


token = os.environ.get('SLACK_TOKEN')
client = SlackClient(token)

if client.rtm_connect():
    while True:
        last_read = client.rtm_read()
        if last_read:
            try:
                parsed = last_read[0]['text']
                message_channel = last_read[0]['channel']
                if parsed and 'list' in parsed:
                    deals = investments()
                    investment_list = ""
                    for d in deals:
                        d = "{title:>10} {grade:<4} {interest:>8} {duration:>8} {amount:>10} {progress:>5} {status:>5} \n".format(**d)
                        investment_list += d
                    client.rtm_send_message(message_channel, investment_list)

            except:
                pass
        time.sleep(1)
