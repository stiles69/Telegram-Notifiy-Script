#!/usr/bin/python
import sys
import apprise

try:
    (scriptname, notification_type, notification_title, notification_text, parameters) = sys.argv
except:
    print("No commandline parameters found!")
    sys.exit(1)

# create an Apprise instance
apobj = apprise.Apprise()

# Add all of the notification services by their server url.
# A sample telegram notification
apobj.add('tgram://API TOKEN:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/chatid')

SABNZBD_NOTIFICATION_MAP = {
    # Startup/Shutdown
    'startup': (
        'Startup/Shutdown',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Added NZB
    'download': (
        'Added NZB',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Post-processing started
    'pp': (
        'Post-Processing Started',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Job finished
    'complete': (
        'Job Finished',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Job failed
    'failed': (
        'Job Failed',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Warning
    'warning': (
        'Warning',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Error
    'error': (
        'Error',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Disk full
    'disk_full': (
        'Disk Full',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # Queue finished
    'queue_done': (
        'Queue Finished',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
    # User logged in
    'new_login': (
        'User Logged In',
        'https://sabnzbd.org/images/icons/apple-touch-icon-76x76-precomposed.png',
    ),
}

#apobj.add(str(url))

# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
            title=str(notification_title),
            body=SABNZBD_NOTIFICATION_MAP[notification_type][0]
)

# Success code
sys.exit(0)
