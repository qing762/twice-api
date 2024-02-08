import sys
import aiohttp
import subprocess
import json
import asyncio
import re
import os
from googletrans import Translator

if len(sys.argv) < 2:
    print("Please provide a file name as a command-line argument.")
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
        print(f"Linting failed with {str(e)}")
        sys.exit(1)
    try:
        subprocess.run(
            [
                "flake8",
                ".",
                "--count",
                "--exit-zero",
                "--max-complexity=15",
                "--max-line-length=300",
                "--statistics",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Linting failed with {str(e)}")
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

    all_links_valid = True
    invalidURL = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                if response.status == 200:
                    print("0")
                else:
                    print(f"Link is invalid: {url}")
                    all_links_valid = False
                    invalidURL.append(url)

    if all_links_valid:
        print("All links are valid!\n\n")
    else:
        print(f"Invalid links found:\n{invalidURL}\n\n")
        sys.exit(1)


async def validateLang():
    print("Validating language of output json")
    file = sys.argv[1]
    translator = Translator()
    all_lang_valid = True
    invalidLang = {}

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)

    for x in data:
        if x == "member":
            for member in data:
                for key, value in data[member]["otherNames"].items():
                    detected = translator.detect(value)
                    detected_lang = detected.lang
                    if isinstance(detected_lang, list):
                        detected_lang = detected_lang[0]
                    if detected_lang == "zh-CN":
                        detected_lang = "zh"
                    if isinstance(detected_lang, str) and detected_lang != key:
                        if value == "名井南" and detected_lang == "ja":
                            continue
                        elif value == "Dubu (Tofu)" and detected_lang == "zh":
                            continue
                        elif value == "平井桃" and detected_lang == "ja":
                            continue
                        elif value == "凑崎纱夏" and detected_lang == "ja":
                            continue
                        else:
                            all_lang_valid = False
                            json.dump(
                                {
                                    "value": value,
                                    "key": key,
                                    "detected_lang": detected_lang,
                                },
                                invalidLang,
                            )
                            sys.exit(1)
                    print("0")

        if all_lang_valid:
            print("All languages are correct!\n")
        else:
            print(
                f"Incorrect languages found:\n{[x['value'] for x in invalidLang]}\n\n"
            )
            sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(lintCheck())
        asyncio.run(validateLinks())
        asyncio.run(validateLang())
        print("All check passed!")
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
