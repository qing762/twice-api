import sys
import aiohttp
import subprocess
import json
import asyncio
import re


async def lintCheck():
    subprocess.run(
        [
            "flake8",
            ".",
            "--count",
            "--select=E9,F63,F7,F82",
            "--show-source",
            "--statistics",
        ]
    )
    subprocess.run(
        [
            "flake8",
            ".",
            "--count",
            "--exit-zero",
            "--max-complexity=15",
            "--max-line-length=300",
            "--statistics",
        ]
    )


async def validateLinks():
    if len(sys.argv) < 2:
        print("Please provide a file name as a command-line argument.")
        return

    file = sys.argv[1]

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Convert the dictionary back into a string
    data_str = json.dumps(data)

    url_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    urls = re.findall(url_pattern, data_str)
    print(urls)

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
        print("All links are valid!")
    else:
        print("Invalid links found:")
        print(invalidURL)


if __name__ == "__main__":
    asyncio.run(lintCheck())
    asyncio.run(validateLinks())
