import requests

from bs4 import BeautifulSoup
from typing import List

global toVisit
global visited
global files

def isDirectory(name: str) -> bool:
    if isinstance(name, str) and len(name) > 0:
        return name[-1] == "/"
    
    return False

def getFiles(url: str,
             ignore: List[str] = ["/", "/distfiles/", "http://www.tds.net", "https://osuosl.org/", "https://osuosl.org/contribute"]
            ) -> None:
    if not isinstance(url, str) or len(url) == 0 or url in visited:
        return
    
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    
    for cell in soup.find_all('td', ):
        for link in cell.find_all('a'):
            target = link.get("href")

            if target not in ignore:
                if isDirectory(target) == True:
                    toVisit.add(f"{url}/{target}")
                else:
                    files.append(f"{url}/{target}")

def getAllFiles(url: str):
    global toVisit
    global visited
    global files

    toVisit = set()
    visited = set()
    files = []

    toVisit.add(url)

    print("=== Run starting ===")

    while(len(toVisit) > 0):
        url = toVisit.pop()

        print(f"=== Retrieving from: {url}")

        getFiles(url=url)

    print("=== Run complete ===")

if __name__ == "__main__":
    url = "https://gentoo.osuosl.org/distfiles"
    output = "files.txt"
    
    getAllFiles(url)

    writer = open(output, "w")

    for file in files:
        writer.write(f"- {file}\n")

    print(f"Files written to {output}.")