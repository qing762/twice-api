import aiohttp
import asyncio
import json
import re
from bs4 import BeautifulSoup


class Main:
    async def Main():
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

                    div = soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "other_name"},
                    )

                    if div:
                        text = div.find("div", class_="pi-data-value pi-font").text
                        otherName = {}
                        for line in text.split("\n"):
                            if ":" in line:
                                matches = re.findall(
                                    r"([A-Za-z]+): ([\u4e00-\u9fff|\u3040-\u30ff]+)",
                                    line,
                                )
                                for match in matches:
                                    lang, name = match
                                    otherName[lang] = name
                            else:
                                if "Dubu (Tofu)" in line:
                                    otherName["Informal"] = "Dubu (Tofu)"
                                elif "(" in line and ")" in line:
                                    name, lang = line.split(" (")
                                    lang = lang.replace(")", "")
                                    otherName[lang] = name
                    else:
                        otherName = None

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
                            .replace("\u00A0", " ")
                            .strip()
                        )

                fandom = f"https://twice.fandom.com/wiki/{x}"

                data = {
                    "name": name,
                    "otherName": otherName,
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


if __name__ == "__main__":
    memberData = asyncio.run(Main.Main())
    with open("twice.json", "w", encoding="utf-8") as f:
        json.dump(memberData, f, indent=2)
