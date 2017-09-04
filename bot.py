"""
    GEFS Chart Bot
    Polls https://www.tropicaltidbits.com/storminfo/11L_gefs_latest.png, but it can
    really be used to monitor/notify about changes to any file on the web.

    (c) Charlton Trezevant 2017
    MIT License

    Enjoy!
"""

import time, sys
sys.dont_write_bytecode = True
sys.path.insert(0, 'lib')

from EtagMonitor import EtagMonitor
from slackclient import SlackClient

CHART_URL = 'https://www.tropicaltidbits.com/storminfo/11L_gefs_latest.png'
DB_PATH = 'etag.db'
SLACK_TOKEN = ' '
SLACK_CHANNEL = ' '

monitor = EtagMonitor(dbpath=DB_PATH, url=CHART_URL)
slack = SlackClient(SLACK_TOKEN)

if monitor.has_updated() is True:
    curtime = time.strftime('%b %d, %Y at %H:%M')
    nocache = "?nocache=" + time.strftime('%d%H%M')
    msg_text = 'Updated GEFS Chart: ' + curtime + '\n(NOAA, Irma-GEFS)'
    msg_attachments = [{"title": "GEFS Chart - Updated " + curtime, "image_url": CHART_URL + nocache}]

    slack.api_call("chat.postMessage", channel=SLACK_CHANNEL,
                   text=msg_text, attachments=msg_attachments)
