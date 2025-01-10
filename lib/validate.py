import sys
import aiohttp
import subprocess
import json
import asyncio
import re
import os
from googletrans import Translator
from datetime import datetime


if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print("No file provided as command-line argument.")
    sys.exit(1)


async def lintCheck():
    print("Checking format and style...")
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--select=E9,F63,F7,F82",
                "--show-source",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed! {str(e)}")
        sys.exit(1)
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--max-complexity=30",
                "--max-line-length=300",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed! {str(e)}")
        sys.exit(1)
    print("Linting passed!\n\n")


async def validateLinks():
    print("Validating links...")
    file = sys.argv[1]

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)

    data_str = json.dumps(data)

    url_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    urls = re.findall(url_pattern, data_str)

    allLinksValid = True
    invalidURL = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                response = await session.get(
                    url,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
                    },
                    timeout=aiohttp.ClientTimeout(total=5),
                )
                if response.status == 200:
                    print("0")
                elif response.status != 200 and url.startswith("https://www.instagram.com"):
                    print(f"Detected Instagram link and it returns with code {response.status}, skipping validation since it could be Github Actions IP blocked.")
                elif response.status != 200 and url.startswith("https://www.dailymotion.com"):
                    print(f"Detected Dailymotion link and it returns with code {response.status}, skipping validation since it could be Github Actions IP blocked.")
                else:
                    print(f"Link is invalid: {url}")
                    allLinksValid = False
                    invalidURL.append(url)
            except (aiohttp.ClientError, asyncio.TimeoutError):
                continue

    if allLinksValid:
        print("All links are valid!\n\n")
    else:
        print(f"Invalid links found:\n{invalidURL}\n\n")
        sys.exit(1)


async def validateLang():
    print("Validating language of output json")
    file = sys.argv[1]
    translator = Translator()
    allLangValid = True
    invalidLang = {}

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)

    for x in data["member"]:
        for key, value in data["member"][x]["otherNames"].items():
            detected = translator.detect(value)
            detected_lang = detected.lang
            if isinstance(detected_lang, list):
                detected_lang = detected_lang[0]
            if detected_lang == "zh-CN" or detected_lang == "zh-TW":
                detected_lang = "zh"
            if isinstance(detected_lang, str) and detected_lang != key:
                if value == "名井南" and detected_lang == "ja" and key == "zh":
                    continue
                elif (
                    value == "Dubu (Tofu)"
                    and detected_lang in ["zh", "ja", "ha"]
                    and key == "informal"
                ):
                    continue
                elif value == "平井桃" and detected_lang == "ja" and key == "zh":
                    continue
                elif value == "凑崎纱夏" and detected_lang == "ja" and key == "zh":
                    continue
                elif value == "Katarina Son" and detected_lang == "ja" and key == "en":
                    continue
                elif value == "Sharon Myoui" and detected_lang == "ja" and key == "en":
                    continue
                else:
                    allLangValid = False
                    print(
                        json.dumps(
                            {
                                "value": value,
                                "key": key,
                                "detected_lang": detected_lang,
                            }
                        ),
                    )
                    sys.exit(1)
            print("0")

    if allLangValid:
        print("All languages are correct!\n")
    else:
        print(f"Incorrect languages found:\n{[x['value'] for x in invalidLang]}\n\n")
        sys.exit(1)


async def validateTimestamp():
    file = sys.argv[1]
    with open(file, "r") as file:
        data = json.load(file)
    format_string = "%B %d, %Y"
    for x in data["member"]:
        date_string_from_timestamp = datetime.fromtimestamp(
            datetime.strptime(
                datetime.fromtimestamp(data["member"][x]["birthDate"]).strftime(
                    "%B %d, %Y"
                ),
                format_string,
            ).timestamp()
        ).strftime(format_string)
        if (
            datetime.fromtimestamp(data["member"][x]["birthDate"]).strftime("%B %d, %Y")
            != date_string_from_timestamp
        ):
            print(f'Invalid timestamp: {data["member"][x]["birthDate"]}')
            sys.exit(1)
        else:
            print("0")
    print("All timestamps are valid.")


if __name__ == "__main__":
    try:
        asyncio.run(lintCheck())
        asyncio.run(validateLinks())
        asyncio.run(validateLang())
        asyncio.run(validateTimestamp())
        print("All check passed!")
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
