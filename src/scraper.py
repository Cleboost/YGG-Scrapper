from botasaurus.browser import Driver
from .static import CATEGORIES


def extract_torrents_data(driver: Driver):
    driver.wait_for_element("table.table")

    torrents = []

    tbody = driver.select("table.table tbody")
    all_row = tbody.select_all("tr")

    for row in all_row:
        all_td = row.select_all("td")
        type_id = all_td[0].text.strip()
        type_name = CATEGORIES.get(type_id, type_id)
        name = all_td[1].text.strip()
        comments = all_td[3].text.strip()
        age = all_td[4].text.strip()
        size = all_td[5].text.strip()
        completed = all_td[6].text.strip()
        seed = all_td[7].text.strip()
        leech = all_td[8].text.strip()
        torrents.append({
            "type": type_name,
            "type_id": type_id,
            "name": name,
            "comments": comments,
            "age": age,
            "size": size,
            "completed": completed,
            "seed": seed,
            "leech": leech
        })

    return torrents
