import json
import os

import requests

requestURL = "https://translations.roblox.com/v1/translations/en_us?consumerType="
translationStringFolderLocation = ""

consumerTypes = [
"AndroidApp",
"IOSApp",
# "Web",
"LuaApp",
"Studio",
"RobloxInGameContent",
]

if not os.path.exists(translationStringFolderLocation):
    os.mkdir(translationStringFolderLocation)

for consumerType in consumerTypes:
    translationStringURLRequest = requests.get(requestURL + consumerType)
    if translationStringURLRequest.status_code != 200:
        raise Exception("Error " + str(translationStringURLRequest.status_code) + " when retrieving consumerType URL for consumerType " + str(consumerType) + ": " + translationStringURLRequest.text)
    translationStringURLResponse = translationStringURLRequest.json()
    translationStringConsumerTypeRequest = requests.get(translationStringURLResponse["url"])
    if translationStringConsumerTypeRequest.status_code != 200:
        raise Exception("Error " + str(translationStringConsumerTypeRequest.status_code) + " when retrieving translation strings for consumerType " + str(consumerType) + ": " + translationStringConsumerTypeRequest.text)
    translationStringConsumerTypeResponse = translationStringConsumerTypeRequest.json()
    translationStringConsumerTypeText = json.dumps(translationStringConsumerTypeResponse, ensure_ascii=False, sort_keys=False, indent=4)
    translationStringConsumerTypeFile = open(os.path.join(translationStringFolderLocation, consumerType) + ".json", "w", encoding="utf-8-sig")
    translationStringConsumerTypeFile.write(translationStringConsumerTypeText)
    translationStringConsumerTypeFile.close()
    