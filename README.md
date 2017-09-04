# GEFS Chart Bot

Polls https://www.tropicaltidbits.com/storminfo/11L_gefs_latest.png, but it can really be used to monitor/notify about changes to any file on the web (including other weather charts).

Made to keep our hurricane Irma channel up-to-date about projected storm paths, and the only dependencies are on python-slackclient, python-requests, and [Etag-Monitor](https://github.com/ctrezevant/Etag-Monitor) (which is bundled in this repo as a submodule).

If you're planning to run your own instance, a crontab appropriately adjusted for EST may be found in crontab.txt.

(c) Charlton Trezevant 2017
MIT License

Enjoy!
