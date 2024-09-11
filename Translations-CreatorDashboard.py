import json
import os
import warnings

import requests
from bs4 import BeautifulSoup

translations = {
    "CreatorDashboard": [
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
        "PlaceThumbnails",
        "DeveloperItem",
        "Places",
        "Landing",
        "RoadMap",
        "GenreType",
        "VersionHistory",
        "PlaceAccess",
        "AssetPermissions",
        "DeveloperProducts",
        "CloudServices",
        "RightsPortal",
        "Transactions",
        "PriceOptimization",
        "StoreAnalytics",
        "MarketplaceOnboarding",
        "DataCollection",
        "Settings",
        "DataSharingSettingsV2",
        "AssetUpload",
        "Payouts",
        "Badges",
        "DevStatsExport",
        "SafetyControls",
        "ShareLinksManagament",
        "ComputeTelemetry",
        "LogIn",
        "HomepageTour",
        "ShareLinkAnalytics",
        "ShareLinkPromo",
        "AssetAnalytics",
        "Preferences",
        "Metadata",
        "DevStatsGame",
        "SignUp",
        "DataCollectionTerms",
        "Secrets",
        "DeveloperLanding",
    ],
    "Notifications": ["Preferences"],
}

folderLocation = "/home/runner/work/rbx-scraper/rbx-scraper/translations"


if not os.path.exists(folderLocation):
    os.mkdir(folderLocation)

if not os.path.exists(folderLocation + "/CreatorDashboard"):
    os.mkdir(folderLocation + "/CreatorDashboard")

for scope, _ in translations.items():
    if not os.path.exists(folderLocation + "/CreatorDashboard/" + scope):
        os.mkdir(folderLocation + "/CreatorDashboard/" + scope)


pageRequest = requests.get("https://create.roblox.com")
if pageRequest.status_code >= 400:
    raise ("Error when retrieving initial Creator Dashboard page: " + pageRequest.text)

soup = BeautifulSoup(pageRequest.text, "html.parser")
linkList = soup.findAll("link")
iconLink = linkList[0].get("href")
splitLink = iconLink.split("/")
versionHash = splitLink[1]
print("Version hash: " + versionHash)


for scope, namespaces in translations.items():
    for namespace in namespaces:
        namespaceRequest = requests.get(
            "https://create.roblox.com/"
            + versionHash
            + "/locales/en-US/" + scope + "."
            + namespace
            + ".json"
        )
        if namespaceRequest.status_code != 200:
            warnings.warn(
                "Error "
                + str(namespaceRequest.status_code)
                + " when retrieving CreatorDashboard translations for namespace "
                + namespace
                + ": "
                + namespaceRequest.text
            )
            continue
        namespaceResponse = namespaceRequest.json()
        namespaceText = json.dumps(
            namespaceResponse, ensure_ascii=False, sort_keys=False, indent=4
        )
        print("successfully retrieved " + scope + "." + namespace)
        namespaceFile = open(
            os.path.join(folderLocation + "/CreatorDashboard/" + scope,  namespace) + ".json",
            "w",
            encoding="utf-8-sig",
        )
        namespaceFile.write(namespaceText)
        namespaceFile.close()