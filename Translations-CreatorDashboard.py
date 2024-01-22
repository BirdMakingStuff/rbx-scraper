import json
import os
import warnings

import requests
from bs4 import BeautifulSoup

namespaces = [
"Features",
"AgreementsUpdate",
"Navigation",
"Creations",
"AssetTypes",
"Advanced",
"OpenCloud",
"Error",
"DataCollectionSettings",
"Controls",
"Analytics",
"ImmersiveAdsAnalytics",
"DeveloperSubscriptions",
"Insights",
"AvatarAnalytics",
"ConfigureItem",
"Passes",
"Table",
"ActivityFeed",
"Access",
"CommunicationSettings",
"DeveloperQuestionnaire",
"GameLocalization",
"GameLocalizationReports",
"GameLocalizationLanguages",
"GameLocalizationSettings",
"GameLocalizationTranslators",
"GameLocalizationTableManagement",
"Community",
"SocialLinks",
"Updates",
"Notifications",
"Home",
"DevEx",
"TranslatorPortal",
"GameTranslation",
"GameInfoTranslation",
"GameStringTranslation",
"GameProductTranslation",
"EngagementPayout",
"OAuth",
"ScopeSystem",
"Organization",
"PlaceThumbnail",
"DeveloperItem",
"Places",
"Landing",
"RoadMap",
]

folderLocation = "/home/runner/work/rbx-scraper/rbx-scraper/translations"

if not os.path.exists(folderLocation):
    os.mkdir(folderLocation)

if not os.path.exists(folderLocation + "/CreatorDashboard"):
    os.mkdir(folderLocation + "/CreatorDashboard")

pageRequest = requests.get("https://create.roblox.com")
if pageRequest.status_code >= 400:
    raise("Error when retrieving initial Creator Dashboard page: " + pageRequest.text)
soup = BeautifulSoup(pageRequest.text, 'html.parser')
linkList = soup.findAll("link")
iconLink = linkList[0].get("href")
splitLink = iconLink.split("/")
versionHash = splitLink[1]

print("Version hash: " + versionHash)

for namespace in namespaces:
    namespaceRequest = requests.get("https://create.roblox.com/" + versionHash + "/locales/en-US/CreatorDashboard." + namespace + ".json")
    if namespaceRequest.status_code != 200:
        warnings.warn("Error " + str(namespaceRequest.status_code) + " when retrieving CreatorDashboard translations for namespace " + str(namespace) + ": " + namespaceRequest.text)
        continue
    namespaceResponse = namespaceRequest.json()
    namespaceText = json.dumps(namespaceResponse, ensure_ascii=False, sort_keys=False, indent=4)
    namespaceFile = open(os.path.join(folderLocation + "/CreatorDashboard", namespace) + ".json", "w", encoding="utf-8-sig")
    namespaceFile.write(namespaceText)
    namespaceFile.close()