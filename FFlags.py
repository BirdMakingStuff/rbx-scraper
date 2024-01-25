import json
import os

import requests

requestURL = "https://clientsettingscdn.roblox.com/v2/settings/application/"
fflagFolderLocation = "/home/runner/work/rbx-scraper/rbx-scraper/fflags"

fflagChannels = [
"PCDesktopClient",
"MacDesktopClient",
"PCClientBootstrapper",
"MacClientBootstrapper",
"PCStudioApp",
"MacStudioApp",
"PCStudioBootstrapper",
"MacStudioBootstrapper",
"XboxClient",
"AndroidApp",
"iOSApp",
"UWPApp",
"CreatorDashboard",
"PCDesktopClientCJV",
"AndroidAppCJV",
"iOSAppCJV",
"PCStudioAppCJV",
"QuestVRApp",
"PlayStationClient"
]

if not os.path.exists(fflagFolderLocation):
    os.mkdir(fflagFolderLocation)

for channel in fflagChannels:
    fflagChannelRequest = requests.get(requestURL + channel)
    if fflagChannelRequest.status_code != 200:
        raise Exception("Error " + str(fflagChannelRequest.status_code) + " when retrieving channel " + channel + ":" + fflagChannelRequest.text)
    fflagChannelResponse = fflagChannelRequest.json()
    fflagChannelResponse = fflagChannelResponse["applicationSettings"]
    fflagChannelText = json.dumps(fflagChannelResponse, ensure_ascii=False, sort_keys=False, indent=4)
    fflagChannelFile = open(os.path.join(fflagFolderLocation, channel) + ".json", "w", encoding="utf-8-sig")
    fflagChannelFile.write(fflagChannelText)
    fflagChannelFile.close()
    