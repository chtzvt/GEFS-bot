"""
    GEFS Chart Bot
    Polls NOAA's GEFS storm graphics, but it can
    really be used to monitor/notify about changes to any file on the web.

    (c) Charlton Trezevant 2017
    MIT License

    Enjoy!
"""

import time, sys
import requests, tempfile, os
sys.dont_write_bytecode = True
sys.path.insert(0, 'lib')

from EtagMonitor import EtagMonitor
from slack_sdk import WebClient

CHART_URL = 'https://www.nhc.noaa.gov/storm_graphics/AT10/AL102023_5day_cone_no_line_and_wind.png'
DB_PATH = 'etag.db'
SLACK_TOKEN = ''
SLACK_CHANNEL = ''

monitor = EtagMonitor(dbpath=DB_PATH, url=CHART_URL)
slack = WebClient(SLACK_TOKEN)

if monitor.has_updated() is True:
    curtime = time.strftime('%b %d, %Y at %H:%M')
    nocache = "?nocache=" + time.strftime('%d%H%M')
    msg_text = 'Updated GEFS Chart: ' + curtime + ' (via NOAA)'

    temp = tempfile.NamedTemporaryFile(delete=False)

    response = requests.get(CHART_URL)
    response.raise_for_status()

    open(temp.name, 'wb').write(response.content)

    slack.files_upload_v2(
        channel=SLACK_CHANNEL,
        title=msg_text,
        file=temp.name,
        initial_comment=msg_text,
    )

    temp.close()
    os.unlink(temp.name)
