import aiohttp
import asyncio
import langcodes
import json
import re
import os
import sys
import pytz
from bs4 import BeautifulSoup
from googletrans import Translator
from lxml import etree
from datetime import datetime


class Main:
    async def twice():
        async with aiohttp.ClientSession() as session:
            async with session.get("https://twice.fandom.com/wiki/TWICE") as response:
                slogan = []
                labels = {}
                labelsURL = []
                officialColor = {}
                website = {}
                sns = {}
                xpath = etree.HTML(await response.text())
                soup = BeautifulSoup(await response.text(), "html.parser")

                name = (
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
                    else "TWICE"
                )

                origin = (
                    soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "origin"},
                    )
                    .find("div", class_="pi-data-value pi-font")
                    .get_text()
                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "origin"},
                    )
                    else None
                )

                genres = (
                    soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "genres"},
                    )
                    .find("div", class_="pi-data-value pi-font")
                    .get_text()
                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "genres"},
                    )
                    else None
                )

                activeYears = (
                    soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "active"},
                    )
                    .find("div", class_="pi-data-value pi-font")
                    .get_text()
                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "active"},
                    )
                    else None
                )

                for a in (
                    soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "labels"},
                    )
                    .find("div", class_="pi-data-value pi-font")
                    .find_all("a")
                ):
                    labelText = a.get_text()
                    labelsURL.append(a.get("href"))
                    for x in labelsURL:
                        async with session.get(f"https://twice.fandom.com{x}") as res:
                            beautysoup = BeautifulSoup(await res.text(), "html.parser")
                            resu = {}
                            otherNames = (
                                beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "other"},
                                )
                                .find("div", class_="pi-data-value pi-font")
                                .get_text()
                                .split(", ")
                                if beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "other"},
                                )
                                else None
                            )
                            founded = (
                                beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "founded"},
                                )
                                .find("div", class_="pi-data-value pi-font")
                                .get_text()
                                if beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "founded"},
                                )
                                else None
                            )
                            if beautysoup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "founder"},
                            ):
                                founder = [
                                    text
                                    for text in (
                                        beautysoup.find(
                                            "div",
                                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                                            attrs={"data-source": "founder"},
                                        )
                                        .find("div", class_="pi-data-value pi-font")
                                        .stripped_strings
                                    )
                                ]
                            else:
                                founder = None
                            location = (
                                beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "location"},
                                )
                                .find("div", class_="pi-data-value pi-font")
                                .get_text()
                                if beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "location"},
                                )
                                else None
                            )
                            if beautysoup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "distributors"},
                            ):
                                distributor = [
                                    y
                                    for y in (
                                        beautysoup.find(
                                            "div",
                                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                                            attrs={"data-source": "distributors"},
                                        )
                                        .find("div", class_="pi-data-value pi-font")
                                        .stripped_strings
                                    )
                                ]
                            else:
                                distributor = None

                            url = (
                                beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "website"},
                                )
                                .find(
                                    "a",
                                    class_="external text",
                                    attrs={
                                        "target": "_blank",
                                        "rel": "nofollow noreferrer noopener",
                                    },
                                    href=True,
                                ).text
                                if beautysoup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "website"},
                                )
                                else None
                            )

                            resu = {
                                "otherNames": otherNames,
                                "founded": founded,
                                "founder": founder,
                                "location": location,
                                "distributors": distributor,
                                "website": url,
                            }
                    labels[labelText] = resu

                associatedActs = (
                    list(
                        (
                            soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "acts"},
                            ).find("div", class_="pi-data-value pi-font")
                        ).stripped_strings
                    )
                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "acts"},
                    )
                    else None
                )

                fandomName = (
                    soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "fandom"},
                    )
                    .find("div", class_="pi-data-value pi-font")
                    .get_text()
                    if soup.find(
                        "div",
                        class_="pi-item pi-data pi-item-spacing pi-border-color",
                        attrs={"data-source": "fandom"},
                    )
                    else None
                )

                if soup.find(
                    "div",
                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                    attrs={"data-source": "official_color"},
                ):
                    for x in (
                        soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "official_color"},
                        )
                        .find("div", class_="pi-data-value pi-font")
                        .find_all("table")
                    ):
                        for y in x.find("tbody").find("tr").find_all("td"):
                            if y.find("span"):
                                officialColorName = y.find("span").get_text()
                                officialColorCode = (
                                    y.find("span")["style"].split("; ")[1].strip()
                                )
                                officialColor[officialColorName] = officialColorCode
                else:
                    officialColor = None

                    if (
                        soup.find("section", class_="pi-item pi-group pi-border-color")
                        .find(
                            "table",
                            class_="pi-horizontal-group pi-horizontal-group-no-labels",
                        )
                        .find("tbody")
                        .find("tr")
                        .find(
                            "td",
                            class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing",
                            attrs={"data-source": "website"},
                        )
                    ):
                        tdElement = (
                            soup.find("section", class_="pi-item pi-group pi-border-color")
                            .find(
                                "table",
                                class_="pi-horizontal-group pi-horizontal-group-no-labels",
                            )
                            .find("tbody")
                            .find("tr")
                            .find(
                                "td",
                                class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing",
                                attrs={"data-source": "website"},
                            )
                        )

                        for b, a in zip(tdElement.find_all("b"), tdElement.find_all("a")):
                            key = b.get_text()
                            website[key] = a["href"]

                        popCafe = tdElement.find_all("a", class_="external text", attrs={"rel": "nofollow noreferrer noopener"}, href=True)
                        for z in popCafe:
                            if z.find_previous_sibling("small") and z.find_previous_sibling("small").get_text() == "Closed":
                                key = z.get_text() + f" ({z.find_previous_sibling('small').get_text()})"
                                website[key] = z["href"]
                    else:
                        website = None

                if (
                    soup.find_all("section", class_="pi-item pi-group pi-border-color")[1]
                    .find(
                        "table",
                        class_="pi-horizontal-group pi-horizontal-group-no-labels",
                    )
                    .find("tbody")
                    .find("tr")
                    .find(
                        "td",
                        class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing",
                        attrs={"data-source": "sns"},
                    )
                ):
                    tdElement = (
                        soup.find_all("section", class_="pi-item pi-group pi-border-color")[1]
                        .find(
                            "table",
                            class_="pi-horizontal-group pi-horizontal-group-no-labels",
                        )
                        .find("tbody")
                        .find("tr")
                        .find(
                            "td",
                            class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing",
                            attrs={"data-source": "sns"},
                        )
                    )

                    for a in tdElement.find_all("a"):
                        if "instagram.com" in a["href"]:
                            key = "Instagram"
                        elif "twitter.com" in a["href"] or "x.com" in a["href"]:
                            key = "Twitter"
                        elif "facebook.com" in a["href"]:
                            key = "Facebook"
                        elif "tiktok.com" in a["href"]:
                            key = "TikTok"
                        elif "youtube.com" in a["href"]:
                            key = "YouTube"
                        elif "zepeto.me" in a["href"]:
                            key = "Zepeto"
                        elif "line.me" in a["href"]:
                            key = "Line"
                        elif "dailymotion.com" in a["href"]:
                            key = "Dailymotion"
                        elif "snapchat.com" in a["href"]:
                            key = "Snapchat"
                        elif "channels.vlive.tv" in a["href"]:
                            key = "VLive"
                        else:
                            key = "Other"

                        if a.parent.parent.name == "p":
                            key += " (Inactive)"
                        elif "jp" in a["href"] or "japan" in a["href"]:
                            key += " (Japan)"

                        sns[key] = a["href"]
                else:
                    sns = None

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

                if (
                    soup.find("div", class_="mw-content-ltr mw-parser-output")
                    .find_all("table", class_="cquote", attrs={"style": "margin:auto;"})
                ):
                    for x in (
                        soup.find("div", class_="mw-content-ltr mw-parser-output")
                        .find_all(
                            "table", class_="cquote", attrs={"style": "margin:auto;"}
                        )
                    ):
                        sloganText = (
                            x.find("tbody")
                            .find("tr")
                            .find(
                                "td", attrs={"valign": "top", "style": "padding:3px;"}
                            )
                        )
                        sloganText = sloganText.get_text()
                        slogan.append(sloganText.replace("\n", ""))
                else:
                    slogan = None

                if xpath.xpath(
                    '//*[@id="mw-content-text"]/div/table[3]/tbody/tr[1]/td[2]'
                ):
                    groupNameMeaning = (
                        BeautifulSoup(
                            etree.tostring(
                                xpath.xpath(
                                    '//*[@id="mw-content-text"]/div/table[3]/tbody/tr[1]/td[2]'
                                )[0],
                                pretty_print=True,
                            ).decode(),
                            "html.parser",
                        )
                        .get_text()
                        .replace("\n", "")
                    )
                else:
                    groupNameMeaning = None

                otherNames = ["NaJeongMoSaJiMiDaChaeTzu", "Teudoongie"]

                sns = {k: sns[k] for k in sorted(sns)}

                fandom = "https://twice.fandom.com/wiki/TWICE"

                data = {
                    "name": name,
                    "otherNames": otherNames,
                    "origin": origin,
                    "genres": genres,
                    "activeYears": activeYears,
                    "labels": labels,
                    "associatedActs": associatedActs,
                    "fandomName": fandomName,
                    "officialColor": officialColor,
                    "slogan": slogan,
                    "groupNameMeaning": groupNameMeaning,
                    "website": website,
                    "sns": sns,
                    "images": images,
                    "fandom": fandom,
                }

                for key, value in data.items():
                    if isinstance(value, str):
                        data[key] = value.replace("\u2013", "-")

        return data

    async def member():
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
        async with Translator() as translator:
            async with aiohttp.ClientSession() as session:
                for x in memberName:
                    async with session.get(
                        f"https://twice.fandom.com/wiki/{x}"
                    ) as response:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        family = []
                        relatives = []
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

                        if "Mina" in name:
                            native = "묘이 미나"
                        else:
                            name, native = name.split(" (")
                            native = native.replace(")", "")
                        detectedLang = await translator.detect(native)
                        nativeLang = detectedLang.lang.split("-", 1)[0]

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

                            otherNames[nativeLang] = native

                        if otherNames[nativeLang] == "湊﨑 紗夏":
                            otherNames.pop(nativeLang)

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

                        birthDate = int(
                            datetime.strptime(birthDate, "%B %d, %Y").replace(tzinfo=pytz.UTC).timestamp()
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

                        if name == "Son Chae-young":
                            soloDebut = "Second half 2025"
                        else:
                            soloDebut = (
                                datetime.strptime(soup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "solo debut"},
                                )
                                    .find("div", class_="pi-data-value pi-font")
                                    .text.split(" (")[0], "%B %d, %Y").replace(tzinfo=pytz.UTC).timestamp()
                                if soup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "solo debut"},
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
                            .contents[0].strip()
                            if soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "mbti"},
                            )
                            else None
                        )

                        occupation = (
                            soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "occupation"},
                            )
                            .find("div", class_="pi-data-value pi-font")
                            .text.title()
                            .split(", ")
                            if soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "occupation"},
                            )
                            else None
                        )

                        if soup.find(
                            "td",
                            class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing",
                            attrs={"data-source": "sns"},
                        ):
                            instagram = []
                            twitter = []
                            zepeto = []
                            youtube = []
                            for y in (
                                soup.find(
                                    "td",
                                    class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing",
                                    attrs={"data-source": "sns"},
                                )
                                .find_all(
                                    "a",
                                    class_="external text",
                                    attrs={
                                        "target": "_blank",
                                        "rel": "nofollow noreferrer noopener",
                                    },
                                    href=True,
                                )
                            ):
                                if "instagram.com" in y["href"]:
                                    instagram.append(y["href"])
                                elif "twitter.com" in y["href"] or "x.com" in y["href"]:
                                    twitter.append(y["href"])
                                elif "zepeto.me" in y["href"]:
                                    zepeto.append(y["href"])
                                elif "youtube.com" in y["href"]:
                                    youtube.append(y["href"])
                        else:
                            instagram = None
                            twitter = None
                            zepeto = None
                            youtube = None

                        position = re.findall(r'[A-Z][a-z]*(?:-[A-Z][a-z]*)*(?:\s[a-z]+)*(?:\s[A-Z][a-z]*)*', soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "position"},
                        ).find("div", class_="pi-data-value pi-font").text)

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
                            [
                                item.strip()
                                for item in soup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "emoji"},
                                )
                                .find("div", class_="pi-data-value pi-font")
                                .decode_contents()
                                .replace("<br/>", "\n")
                                .split("\n")
                            ]
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
                            .text.split(", ")
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

                        associatedActs = list(
                            (
                                soup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "associated"},
                                ).find("div", class_="pi-data-value pi-font")
                            ).stripped_strings
                            if soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "associated"},
                            ).find("div", class_="pi-data-value pi-font")
                            else None
                        )

                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "partner"},
                        ):
                            partnerInfo = (
                                soup.find(
                                    "div",
                                    class_="pi-item pi-data pi-item-spacing pi-border-color",
                                    attrs={"data-source": "partner"},
                                )
                                .find("div", class_="pi-data-value pi-font")
                                .stripped_strings
                            )
                            partnerInfo = list(partnerInfo)
                            partner = {
                                "name": partnerInfo[0],
                                "years": partnerInfo[1].strip("()"),
                            }
                        else:
                            partner = None

                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "family"},
                        ):
                            family = []
                            for y in soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "family"},
                            ).find_all("div", class_="pi-data-value pi-font"):
                                familyList = y.get_text().split(")")
                                familyList = [i for i in familyList if i]
                                for i in range(len(familyList)):
                                    familyName, relationship = familyList[i].split(" (")
                                    family.append(
                                        {
                                            "name": familyName.strip(),
                                            "relationship": relationship.strip().capitalize(),
                                        }
                                    )

                        if soup.find(
                            "div",
                            class_="pi-item pi-data pi-item-spacing pi-border-color",
                            attrs={"data-source": "relatives"},
                        ):
                            relatives = []
                            for y in soup.find(
                                "div",
                                class_="pi-item pi-data pi-item-spacing pi-border-color",
                                attrs={"data-source": "relatives"},
                            ).find_all("div", class_="pi-data-value pi-font"):
                                relativesList = y.get_text().split(")")
                                relativesList = [i for i in relativesList if i]
                                for i in range(len(relativesList)):
                                    relativesName, relationship = relativesList[i].split(
                                        " ("
                                    )
                                    relatives.append(
                                        {
                                            "name": relativesName.strip(),
                                            "relationship": relationship.strip().capitalize(),
                                        }
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
                            soup.find("div", class_="mw-content-ltr mw-parser-output")
                            .find("figure", class_="mw-halign-center")
                            .find("a", class_="image")["href"]
                            + "&format=original"
                        )

                    async with session.get(
                        f"https://twice.fandom.com/wiki/{x}/Facts"
                    ) as response:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        facts = []
                        for y in (
                            soup.find("div", class_="mw-content-ltr mw-parser-output")
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
                        "soloDebut": soloDebut,
                        "yearsActive": yearsActive,
                        "bloodType": bloodType,
                        "MBTI": MBTI,
                        "occupation": occupation,
                        "position": position,
                        "color": color,
                        "instagram": instagram,
                        "twitter": twitter,
                        "zepeto": zepeto,
                        "youtube": youtube,
                        "emoji": emoji,
                        "instrument": instrument,
                        "agency": agency,
                        "associatedActs": associatedActs,
                        "images": images,
                        "signature": signature,
                        "facts": facts,
                        "partner": partner,
                        "family": family,
                        "relatives": relatives,
                        "lovely": {
                            "name": lovelyName,
                            "height": lovelyHeight,
                            "weight": lovelyWeight,
                            "personality": lovelyPersonality,
                            "description": lovelyDescription,
                            "picture": lovelyPicture,
                            "banner": lovelyBanner,
                        },
                        "fandom": fandom,
                    }

                    for key, value in data.items():
                        if isinstance(value, str):
                            data[key] = value.replace("\u2013", "-")

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

                    try:
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
                    except AttributeError:
                        images = None

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

                for key, value in data.items():
                    if isinstance(value, str):
                        data[key] = value.replace("\u2013", "-")

                shipsData[name] = data

        return shipsData


if __name__ == "__main__":
    try:
        twiceData = asyncio.run(Main.twice())
        memberData = asyncio.run(Main.member())
        shipsData = asyncio.run(Main.ships())
        combinedData = {"twice": twiceData, "member": memberData, "ships": shipsData}
        with open("twice.json", "w", encoding="utf-8") as f:
            json.dump(combinedData, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
