# **Python Media Scraper**

## Features
A deprecated, (mainly) unfinished, and nonfunctioning project developed in the Winter of 2021 to pull information from a database of social media links on social media sites, starting with functionality of [Instagram] and [TikTok].

## Dependencies
- [Python] with PyCharm coding environment. Chosen for easy implementation, simplicity, and readability.
- [Requests] inbuilt Python HTTP library for interacting with JSON data on web connections.
- [BeautifulSoup4] as main device for inputting data from extracted data taken from [Requests].
- [PyAutoGui] allows for certain user inputs to be made easily - imported as necessary.
- [OpenPYXL] to read and write from spreadsheets to put extracted data taken from [BeautifulSoup4].

## Installation
Installation is relatively simple; a ```batch``` script was utilized to install all necessary modules (includes all dependencies in [dependencies](#dependencies). A link is provided to that [here][GHub_install].

Unfortunately, the main script for this code is currently unavailable for download.

## Current Files
| File | HYPERLINK |
| ---- | --------- |
| readme | [github][GHub_readme] | 
| install | [github][GHub_install] |
| main script | [github][GHub_scraperpy] |
| example csv | [github][GHub_linkcsv] |

[//]: # (reference links)

[TikTok]: <https://tiktok.com>
[Instagram]: <https://instagram.com>
[Python]: <https://www.python.org/>
[BeautifulSoup4]: <https://beautiful-soup-4.readthedocs.io/en/latest/>
[PyAutoGui]: <https://pyautogui.readthedocs.io/en/latest/>
[OpenPYXL]: <https://openpyxl.readthedocs.io/en/stable/>
[Requests]: <https://pypi.org/project/requests/>
[GHub_readme]: <https://github.com/andrewleachtx/pymediascraper/blob/main/README.md>
[GHub_install]: <https://github.com/andrewleachtx/pymediascraper/blob/main/install.bat>
[GHub_scraperpy]: <https://github.com/andrewleachtx/pymediascraper/blob/main/pymediascraper.py>
[GHub_linkcsv]: <https://github.com/andrewleachtx/pymediascraper/blob/main/examplesheet.csv>
