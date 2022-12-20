import os
import datetime
import requests
import pandas as pd
from requests_html import HTML


now = datetime.datetime.now()
year = now.year

BASE_DIR = os.path.dirname(__file__)


def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", "w") as f:
                f.write(html_text)
        return html_text
    return ''



def parse_and_extract(url,name="2022"):
    html_text = url_to_txt(url)
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"


    r_table = r_html.find(table_class)

    table_data = []
    header_names = []

    if len(r_table):
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")
        header_row = rows[0]
        header_cols = header_row.find("th")
        header_names = [x.text for x in header_cols]
        for row in rows[1:]:
            # print(row.text)
            cols = row.find("td")
            row_data = []
            for i, col in enumerate(cols):
                # print(i, col.text, '\n\n')
                row_data.append(col.text)
            table_data.append(row_data)
        df = pd.DataFrame(table_data, columns=header_names)
        path = os.path.join(BASE_DIR,'data')
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join('data',f'{name}.csv')
        df.to_csv(filepath, index=False) 

url = "https://www.boxofficemojo.com/year/world/2019"       
parse_and_extract(url, name = "2019")
