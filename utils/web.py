import requests
from bs4 import BeautifulSoup


def get_properties():
    # 指定されたURLからコンテンツを取得
    url = "https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=020&ta=13&jspIdFlg=patternShikugun&sc=13104&kb=1&kt=9999999&km=1&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&kw=1&srch_navi=1"
    response = requests.get(url)
    response.encoding = response.apparent_encoding  # 文字化け防止

    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.text, "html.parser")
    # 物件情報を格納するリスト
    properties = []

    # 物件のコンテナを見つける
    property_units = soup.find_all("div", class_="property_unit-content")

    for unit in property_units:
        # 物件名を取得
        title_element = unit.find("h2", class_="property_unit-title")
        name = title_element.text.strip() if title_element else ""
        link = title_element.find("a")["href"] if title_element else ""
        url = "https://suumo.jp" + link if link else ""

        # 販売価格を取得
        price_element = unit.find("dt", text="販売価格").find_next_sibling("dd")
        price = price_element.get_text(strip=True) if price_element else ""

        # 所在地を取得
        location_element = unit.find("dt", text="所在地").find_next_sibling("dd")
        location = location_element.get_text(strip=True) if location_element else ""

        # 沿線・駅を取得
        station_element = unit.find("dt", text="沿線・駅").find_next_sibling("dd")
        station = station_element.get_text(strip=True) if station_element else ""

        # 間取りを取得
        layout_element = unit.find("dt", text="間取り").find_next_sibling("dd")
        layout = layout_element.get_text(strip=True) if layout_element else ""

        # 建物面積を取得
        area_element = unit.find("dt", text="建物面積").find_next_sibling("dd")
        area = area_element.get_text(strip=True) if area_element else ""

        properties.append(
            {
                "name": name,
                "link": url,
                "price": price,
                "location": location,
                "station": station,
                "layout": layout,
                "area": area,
            }
        )

    print(properties)

    return properties
