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
from slack_sdk import WebClient

CHART_URL = 'https://www.nhc.noaa.gov/storm_graphics/AT10/AL102023_5day_cone_no_line_and_wind.png' # replace with your storm path image url
DB_PATH = '/tmp/etag.db'
SLACK_TOKEN = 'your slack token here'
SLACK_CHANNEL = 'your channel here'

monitor = EtagMonitor(dbpath=DB_PATH, url=CHART_URL)
slack = WebClient(SLACK_TOKEN)

if monitor.has_updated() is True:
    curtime = time.strftime('%b %d, %Y at %H:%M')
    nocache = "?nocache=" + time.strftime('%d%H%M')
    msg_text = 'Updated GEFS Chart: ' + curtime + '\n(NOAA)'
    msg_attachments = [{"title": "Storm Track - Updated " + curtime, "image_url": CHART_URL + nocache}]

    slack.chat_postMessage(channel=SLACK_CHANNEL,
                   text=msg_text, attachments=msg_attachments)
