import requests
from bs4 import BeautifulSoup

base_url = "https://www.montegrappa.org/_monte/images/grande_guerra/caduti_grappa/cadutiitaliani.php?pageNum_Recordset1={page}&totalRows_Recordset1=2284"

for page in range(23):
    data=[]
    url = base_url.format(page=page)
    request = requests.get(url.format(page=0))
    soup = BeautifulSoup(request.text, "html.parser")
    table = soup.find_all("table")[3]
    rows = table.find_all("tr")[1:]  #salta riga header
    for td in rows:
        tds = td.find_all("td")
        element = ""
        if len(tds) == 8:
            for index, cell in enumerate(tds):
                element = element + cell.get_text(strip=True)
                if index!=7:
                    element = element + ","

            if element.__len__() > 2:
                data.append(element)
                print(element)

    mode = "w" if page == 0 else "a"
    with open("caduti.csv", mode, encoding="utf-8") as f:
        if mode=="w":
            f.write("tomba,grado,cognome,nome,corpo,data,luogo,medaglia\n")
        for line in data:
            f.write(line + "\n")
    print("✅ Pagina "+str(page)+" registrata")