import os, time
import re
from slackclient import SlackClient
from eight_percent import *


token = os.environ.get('SLACK_TOKEN')
client = SlackClient(token)
NO_DEAL = "Have not deal!"

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
                elif parsed and 'deal' in parsed:
                    deal_number = int(re.findall(r'\d+', parsed)[0])
                    detail = deal_detail(deal_number)
                    if not detail:
                        client.rtm_send_message(message_channel, NO_DEAL)
                    else:
                        message = str(deal_number) + "호 {title} : {detail} \n 모집현황: {progress}% 기간: {duration} 수익률: {interest} 금액: {amount} 상환방식: {refund_method} \n".format(**detail)
                        client.rtm_send_message(message_channel, message)

            except:
                pass
        time.sleep(1)
