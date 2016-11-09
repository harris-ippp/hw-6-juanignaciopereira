import requests
from bs4 import BeautifulSoup

url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General" #
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')

with open("ELECTION_ID", "w") as out:
    for result in soup.find_all("tr", "election_item"):
        year = result.find("td", "year first").contents[0]
        id_number = result["id"].split("-")[2]
        out.write("{} {}\n".format(year, id_number))
