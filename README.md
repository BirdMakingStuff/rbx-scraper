## rbxpyscraper

rbxpyscraper is a scraper built with Python running on GitHub Actions scraping fast flags (FFlags) and translations.

### FFlags
Translations are scraped from clientsettingscdn.roblox.com/v2/ (in FFlags.py).

If there any FFlag channels which are not currently present, please file an issue.

### Translations
Translations are scraped from:
- create.roblox.com for Creator Dashboard (in Translations-CreatorDashboard.py)
- translations.roblox.com for all other endpoints (in Translations.py)

Web translations used to be scraped by an older version of rbxpyscraper using the translations.roblox.com endpoint but stopped working as of late 2023. A new scraper for Web translations may be implemented in the future.

## Requirements
- Python 3.12
    - requests 2.31.0
    - BeautifulSoup 4.12.3