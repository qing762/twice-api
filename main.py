import aiohttp
import asyncio
import langcodes
import json
import re
import os
import sys
from bs4 import BeautifulSoup
from googletrans import Translator
from lxml import etree


class Main:
    async def Member():
        memberName = [
            "Nayeon",
            "Jeongyeon",
            "Momo",
            "Sana",
            "Jihyo",
            "Mina",
            "Dahyun",
            "Chaeyoung",
            "Tzuyu",
        ]
        memberData = {}
        translator = Translator()
        async with aiohttp.ClientSession() as session:
            for x in memberName:
                async with session.get(
                    f"https://twice.fandom.com/wiki/{x}"
                ) as response:
                    soup = BeautifulSoup(await response.text(), "html.parser")

                    name = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "birth_name"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "birth_name"},
                        )
                        else None
                    )

                    name, native = name.split(" (")
                    native = native.replace(")", "")
                    native_lang = translator.detect(native).lang.split("-", 1)[0]

                    div = soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "other_name"},
                    )

                    text = div.find("div", class_="pi-data-value pi-font").text

                    otherNames = {}
                    languages = ["Chinese", "Japanese", "Korean", "English"]

                    for line in text.split("\n"):
                        if ":" in line:
                            for lang in languages:
                                line = line.replace(lang + ":", ", " + lang + ":")
                            line = line[2:] if line.startswith(", ") else line
                            entries = line.split(",")
                            entries = [
                                entry.strip() for entry in entries if entry.strip()
                            ]
                            for entry in entries:
                                lang, lang_name = entry.split(":")
                                if "Dubu (Tofu)" in lang_name:
                                    lang_name = lang_name.partition("Dubu (Tofu)")[0]
                                    otherNames["informal"] = "Dubu (Tofu)"
                                lang = str(langcodes.find(lang.strip()))
                                otherNames[lang] = lang_name.strip()

                        otherNames[native_lang] = native

                    birthDate, age = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "birth_date"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text.split(" (age ")
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "birth_date"},
                        )
                        else None
                    )

                    age = age[:-1] if age else None

                    birthPlace = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "birth_place"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text.replace("[1]", "")
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "birth_place"},
                        )
                        else None
                    )

                    height = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "height"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "height"},
                        )
                        else None
                    )

                    weight = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "weight"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "weight"},
                        )
                        else None
                    )

                    yearsActive = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "years"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "years"},
                        )
                        else None
                    )

                    bloodType = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "blood"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "blood"},
                        )
                        else None
                    )

                    MBTI = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "mbti"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "mbti"},
                        )
                        else None
                    )

                    instagram = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "instagram"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .find(
                            "a",
                            class_="external text",
                            attrs={
                                "target": "_blank",
                                "rel": "nofollow noreferrer noopener",
                            },
                            href=True,
                        )["href"]
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "instagram"},
                        )
                        else None
                    )

                    position = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "position"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text.replace("  ", ", ")
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "position"},
                        )
                        else None
                    )

                    color = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "individual color"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .find("table")
                        .find("tbody")
                        .find("tr")
                        .find_all("td")
                    )

                    for y in color:
                        if y.find("span"):
                            color = y.find("span").text
                            break

                    lovelyName = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "lovely"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "lovely"},
                        )
                        else None
                    )

                    emoji = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "emoji"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "emoji"},
                        )
                        else None
                    )

                    instrument = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "instruments"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "instruments"},
                        )
                        else None
                    )

                    agency = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "agency"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "agency"},
                        )
                        else None
                    )

                    associatedActs = ", ".join(
                        link.text
                        for link in soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "associated"},
                        ).find_all("a")
                    )

                    signature = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "signature"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .find("a", class_="image")["href"]
                        + "&format=original"
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "signature"},
                        )
                        else None
                    )

                    images = []

                    for y in soup.find_all("div", class_="wds-tab__content"):
                        figure = y.find("figure", class_="pi-item pi-image")
                        if figure is not None:
                            a = figure.find("a", class_="image image-thumbnail")
                            if a is not None and a["title"] != "Lovely":
                                images.append(
                                    y.find(
                                        "figure",
                                        class_="pi-item pi-image",
                                    ).find(
                                        "a", class_="image image-thumbnail"
                                    )["href"]
                                    + "&format=original"
                                )
                            else:
                                pass

                async with session.get(
                    f"https://twice.fandom.com/wiki/{x}/Lovely"
                ) as response:
                    soup = BeautifulSoup(await response.text(), "html.parser")
                    lovelyHeight = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "height"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                    )

                    lovelyWeight = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "weight"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                    )

                    lovelyPersonality = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "personality"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text
                    )

                    lovelyDescription = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "official_description"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .text.replace('"', "'")
                    )

                    lovelyPicture = (
                        soup.find(
                            "figure",
                            class_="pi-item pi-image",
                            attrs={"data-source": "image1"},
                        ).find("a", class_="image image-thumbnail")["href"]
                        + "&format=original"
                    )

                    lovelyBanner = (
                        soup.find("div", class_="mw-parser-output")
                        .find("center")
                        .find("a", class_="image")["href"]
                        + "&format=original"
                    )

                async with session.get(
                    f"https://twice.fandom.com/wiki/{x}/Facts"
                ) as response:
                    soup = BeautifulSoup(await response.text(), "html.parser")
                    facts = []
                    for y in (
                        soup.find("div", class_="mw-parser-output")
                        .find("ul")
                        .find_all("li")
                    ):
                        facts.append(
                            re.sub(
                                r"\[\d+\]",
                                "",
                                y.get_text(),
                            )
                            .replace("''", '"')
                            .replace(" ", " ")
                            .strip()
                        )

                fandom = f"https://twice.fandom.com/wiki/{x}"

                data = {
                    "name": name,
                    "otherNames": otherNames,
                    "birthDate": birthDate,
                    "age": age,
                    "birthPlace": birthPlace,
                    "height": height,
                    "weight": weight,
                    "yearsActive": yearsActive,
                    "bloodType": bloodType,
                    "MBTI": MBTI,
                    "instagram": instagram,
                    "position": position,
                    "color": color,
                    "lovely": {
                        "name": lovelyName,
                        "height": lovelyHeight,
                        "weight": lovelyWeight,
                        "personality": lovelyPersonality,
                        "description": lovelyDescription,
                        "picture": lovelyPicture,
                        "banner": lovelyBanner,
                    },
                    "emoji": emoji,
                    "instrument": instrument,
                    "agency": agency,
                    "associatedActs": associatedActs,
                    "signature": signature,
                    "images": images,
                    "facts": facts,
                    "fandom": fandom,
                }

                memberData[x] = data

        return memberData

    async def ships():
        shipsData = {}
        shipsURL = []

        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://twice.fandom.com/wiki/Category:Pairings"
            ) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")
                xpath = etree.HTML(await response.text())
                div = soup.find("div", class_="category-page__members")

                for y in div.find_all("div", class_="category-page__members-wrapper"):
                    ul = y.find("ul", class_="category-page__members-for-char")
                    for z in ul.find_all("li", class_="category-page__member"):
                        div = z.find("div", class_="category-page__member-left")
                        url = f"https://twice.fandom.com{z.find('a')['href']}"
                        shipsURL.append(url)
            for z in shipsURL:
                otherNames = []
                similarities = []
                differences = []
                facts = []
                rivals = []
                async with session.get(z) as response:
                    soup = BeautifulSoup(await response.text(), "html.parser")
                    xpath = etree.HTML(await response.text())
                    name = (
                        soup.find(
                            "h2",
                            class_="pi-item pi-item-spacing pi-title pi-secondary-background",
                            attrs={"data-source": "name"},
                        ).get_text()
                        if soup.find(
                            "h2",
                            class_="pi-item pi-item-spacing pi-title pi-secondary-background",
                            attrs={"data-source": "name"},
                        )
                        else (
                            soup.find(
                                "h2",
                                class_="pi-item pi-item-spacing pi-title pi-secondary-background",
                                attrs={"data-source": "title1"},
                            ).get_text()
                            if soup.find(
                                "h2",
                                class_="pi-item pi-item-spacing pi-title pi-secondary-background",
                                attrs={"data-source": "title1"},
                            )
                            else None
                        )
                    )

                    shipped = (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "shipped"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .get_text()
                        .split(" and ")
                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "shipped"},
                        )
                        else None
                    )

                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "other names"},
                    ):
                        for y in (
                            soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "other names"},
                            )
                            .find("div", class_="pi-data-value pi-font")
                            .find("ul")
                            .find_all("li")
                        ):
                            otherNames.append(y.get_text())

                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "rivals"},
                    ):
                        for y in (
                            soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "rivals"},
                            )
                            .find("div", class_="pi-data-value pi-font")
                            .find("ul")
                            .find_all("li")
                        ):
                            rivals.append(y.get_text())

                    similaritiesSearch = xpath.xpath(
                        '//*[@id="mw-content-text"]/div/ul[2]'
                    )
                    if similaritiesSearch:
                        similaritiesSearch = BeautifulSoup(
                            etree.tostring(
                                similaritiesSearch[0],
                                pretty_print=True,
                            ).decode(),
                            "html.parser",
                        ).get_text()
                        similarities = [s for s in similaritiesSearch.split("\n") if s]

                    differencesSearch = xpath.xpath(
                        '//*[@id="mw-content-text"]/div/ul[3]'
                    )
                    if differencesSearch:
                        differencesSearch = BeautifulSoup(
                            etree.tostring(
                                differencesSearch[0],
                                pretty_print=True,
                            ).decode(),
                            "html.parser",
                        ).get_text()
                        differences = [d for d in differencesSearch.split("\n") if d]

                    factsSearch = xpath.xpath('//*[@id="mw-content-text"]/div/ul[4]')
                    if factsSearch:
                        factsSearch = BeautifulSoup(
                            etree.tostring(
                                factsSearch[0],
                                pretty_print=True,
                            ).decode(),
                            "html.parser",
                        ).get_text()
                        facts = [f for f in factsSearch.split("\n") if f]

                    images = (
                        soup.find(
                            "figure",
                            class_="pi-item pi-image",
                            attrs={"data-source": "image"},
                        ).find("a", class_="image image-thumbnail")["href"]
                        + "&format=original"
                        if soup.find(
                            "figure",
                            class_="pi-item pi-image",
                            attrs={"data-source": "image"},
                        ).find("a", class_="image image-thumbnail")
                        else None
                    )

                data = {
                    "name": name,
                    "shipped": shipped,
                    "otherNames": otherNames,
                    "rivals": rivals,
                    "similarities": similarities,
                    "differences": differences,
                    "facts": facts,
                    "images": images,
                    "fandom": z,
                }

                shipsData[name] = data

        return shipsData


if __name__ == "__main__":
    try:
        memberData = asyncio.run(Main.Member())
        shipsData = asyncio.run(Main.ships())
        combinedData = {"member": memberData, "ships": shipsData}
        with open("twice.json", "w", encoding="utf-8") as f:
            json.dump(combinedData, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
