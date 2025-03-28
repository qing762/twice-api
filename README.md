> [!NOTE]  
> Join the [Discord server](https://qing762.is-a.dev/discord) for issues. Thanks a lot!

# TWICE API

An API that scrapes data from [Twice Wiki](https://twice.fandom.com) and convert into JSON format.

## How it works

It scrapes data from [Twice Wiki](https://twice.fandom.com) and format/beautify it into a JSON format.

## API Reference

### Get TWICE Data

```http
GET https://qing762.is-a.dev/api/twice
```

Returns the entire TWICE data.

#### Response

```json
{
    "twice": {
        "name": "TWICE",
        "otherNames": [ ...],
        "origin": "Seoul, South Korea",
        "genres": "K-pop, J-pop",
        "activeYears": "2015-present",
        "labels": {
            "JYP Entertainment": {
                "otherNames": null,
                "founded": "April 25, 1997",
                "founder": ["J.Y. Park (Park Jin Young)"],
                "location": "Seoul, South Korea",
                "distributors": ["KT Music"],
                "website": "https://www.jype.com/"
            },
            ...
        },
        "associatedActs": ["SIXTEEN", "JYP Nation", ...],
        "fandomName": "ONCE",
        "officialColor": {
            "Neon Magenta": "#FF5FA2",
            "Apricot": "#FCC89B"
        },
        "slogan": [
            "One in a Million! 안녕하세요, 트와이스 임니다!",
            ...
        ],
        "groupNameMeaning": "One in a Million! Hi, we are TWICE!",
        "website": {},
        "sns": {
            "Dailymotion (Inactive)": "https://www.dailymotion.com/TWICEonAir",
            "Facebook": "https://www.facebook.com/JYPETWICE",
            "Instagram": "https://www.instagram.com/twicetagram",
            "Instagram (Japan)": "https://www.instagram.com/jypetwice_japan",
            "Line (Japan)": "https://line.me/R/ti/p/@twice_japan",
            "Snapchat (Inactive)": "https://snapchat.com/add/twiceofficial",
            "TikTok": "https://www.tiktok.com/@twice_tiktok_official",
            "TikTok (Japan)": "https://www.tiktok.com/@twice_tiktok_officialjp",
            "Twitter": "https://www.twitter.com/JYPETWICE_JAPAN",
            "VLive (Inactive)": "https://www.channels.vlive.tv/EDBF",
            "YouTube": "https://www.youtube.com/@TWICE",
            "YouTube (Japan)": "https://www.youtube.com/@twicejapan_official",
            "Zepeto": "https://web.zepeto.me/share/user/profile/jypetwice"
        },
        "images": [
            "https://static.wikia.nocookie.net/twicenation/images/5/58/Strategy_Step_1_1.jpg/revision/latest?cb=20241116002141&format=original",
            ...
        ],
        "fandom": "https://twice.fandom.com/wiki/TWICE"
    },
    "member": {
        "Nayeon": {
            "name": "Im Na-yeon",
            "otherNames": {
                "zh": "林娜璉",
                "ja": "ナヨン",
                "ko": "임나연"
            },
            "birthDate": 811728000,
            "age": "29",
            "birthPlace": "Seoul, South Korea",
            "height": "163cm (5'4\")",
            "weight": "48kg (106lbs)",
            "yearsActive": "2015-present",
            "bloodType": "A",
            "MBTI": "ISTP",
            "occupation": [
                "Singer",
                ...
            ],
            "position": [
                "Lead Dancer",
                "Lead Vocalist",
                ...
            ],
            "color": "Sky Blue",
            "instagram": [
                "https://www.instagram.com/nayeonyny/"
            ],
            "twitter": null,
            "zepeto": [
                "https://user.zepeto.me/nayeon"
            ],
            "emoji": [
                "🐰"
            ],
            "instrument": null,
            "agency": "JYP Entertainment",
            "associatedActs": [
                "TWICE",
                "JYP Nation",
                "SIXTEEN"
            ],
            "images": [
                "https://static.wikia.nocookie.net/twicenation/images/a/a7/Nayeon_Strategy_Step_1_1.jpg/revision/latest?cb=20241116002546&format=original",
                ...
            ],
            "signature": "https://static.wikia.nocookie.net/twicenation/images/4/4b/Nayeon_Signature.png/revision/latest?cb=20200717041312&format=original",
            "facts": [
                "Nayeon was originally set to debut in the girl group 6mix with Jeongyeon, Jihyo and Sana.",
                ...
            ],
            "partner": null,
            "family": [
                {
                    "name": "Cheon Se-ah",
                    "relationship": "Mother"
                },
                ...
            ],
            "relatives": [
                {
                    "name": "Ji Yun Seo",
                    "relationship": "Maternal cousin"
                }
            ],
            "lovely": {
                "name": "Navely",
                "height": "23cm",
                "weight": "1.3kg",
                "personality": "Positive",
                "description": "'Loves kids!'",
                "picture": "https://static.wikia.nocookie.net/twicenation/images/5/5e/Navely.jpg/revision/latest?cb=20200514115137&format=original",
                "banner": "https://static.wikia.nocookie.net/twicenation/images/f/f2/Navely.gif/revision/latest?cb=20190221012000&format=original"
            },
            "fandom": "https://twice.fandom.com/wiki/Nayeon"
        },
        "Jeongyeon": { ... },
        ...
    },
    "ships": {
        "230s": {
            "name": "230s",
            "shipped": [
                "Jeongyeon",
                ...
            ],
            "otherNames": [
                "No TG"
                ...
            ],
            "rivals": [
                "2na",
                ...
            ],
            "similarities": [
                "Both are vocalists",
                ...
            ],
            "differences": [
                "Jeongyeon was born in South Korea while Sana was born in Japan",
                ...
            ],
            "facts": [
                "They didn't wear microphones in \"TWICE TV5 -TWICE in SWITZERLAND EP. 07\" because of their loud voices",
                ...
            ],
            "images": "https://static.wikia.nocookie.net/twicenation/images/5/52/230s_Profile-.jpeg/revision/latest?cb=20240224195502&format=original",
            "fandom": "https://twice.fandom.com/wiki/230s"
        },
        "2yeon": { ... },
        ...
    }
}
```

### Get TWICE Group Data

```http
GET https://qing762.is-a.dev/api/twice/group
```

Returns the TWICE group data.

#### Response

```json
{
    "name": "TWICE",
    "otherNames": [ ...],
    "origin": "Seoul, South Korea",
    "genres": "K-pop, J-pop",
    "activeYears": "2015-present",
    "labels": {
        "JYP Entertainment": {
            "otherNames": null,
            "founded": "April 25, 1997",
            "founder": ["J.Y. Park (Park Jin Young)"],
            "location": "Seoul, South Korea",
            "distributors": ["KT Music"],
            "website": "https://www.jype.com/"
        },
        ...
    },
    "associatedActs": ["SIXTEEN", "JYP Nation", ...],
    "fandomName": "ONCE",
    "officialColor": {
        "Neon Magenta": "#FF5FA2",
        "Apricot": "#FCC89B"
    },
    "slogan": [
        "One in a Million! 안녕하세요, 트와이스 임니다!",
        ...
    ],
    "groupNameMeaning": "One in a Million! Hi, we are TWICE!",
    "website": {},
    "sns": {
        "Dailymotion (Inactive)": "https://www.dailymotion.com/TWICEonAir",
        "Facebook": "https://www.facebook.com/JYPETWICE",
        "Instagram": "https://www.instagram.com/twicetagram",
        "Instagram (Japan)": "https://www.instagram.com/jypetwice_japan",
        "Line (Japan)": "https://line.me/R/ti/p/@twice_japan",
        "Snapchat (Inactive)": "https://snapchat.com/add/twiceofficial",
        "TikTok": "https://www.tiktok.com/@twice_tiktok_official",
        "TikTok (Japan)": "https://www.tiktok.com/@twice_tiktok_officialjp",
        "Twitter": "https://www.twitter.com/JYPETWICE_JAPAN",
        "VLive (Inactive)": "https://www.channels.vlive.tv/EDBF",
        "YouTube": "https://www.youtube.com/@TWICE",
        "YouTube (Japan)": "https://www.youtube.com/@twicejapan_official",
        "Zepeto": "https://web.zepeto.me/share/user/profile/jypetwice"
    },
    "images": [
        "https://static.wikia.nocookie.net/twicenation/images/5/58/Strategy_Step_1_1.jpg/revision/latest?cb=20241116002141&format=original",
        ...
    ],
    "fandom": "https://twice.fandom.com/wiki/TWICE"
}
```

### Get TWICE Members

```http
GET https://qing762.is-a.dev/api/twice/members
```

Returns the list of TWICE members.

#### Response

```json
{
    "Nayeon": {
            "name": "Im Na-yeon",
            "otherNames": {
                "zh": "林娜璉",
                "ja": "ナヨン",
                "ko": "임나연"
            },
            "birthDate": 811728000,
            "age": "29",
            "birthPlace": "Seoul, South Korea",
            "height": "163cm (5'4\")",
            "weight": "48kg (106lbs)",
            "yearsActive": "2015-present",
            "bloodType": "A",
            "MBTI": "ISTP",
            "occupation": [
                "Singer",
                ...
            ],
            "position": [
                "Lead Dancer",
                "Lead Vocalist",
                ...
            ],
            "color": "Sky Blue",
            "instagram": [
                "https://www.instagram.com/nayeonyny/"
            ],
            "twitter": null,
            "zepeto": [
                "https://user.zepeto.me/nayeon"
            ],
            "emoji": [
                "🐰"
            ],
            "instrument": null,
            "agency": "JYP Entertainment",
            "associatedActs": [
                "TWICE",
                "JYP Nation",
                "SIXTEEN"
            ],
            "images": [
                "https://static.wikia.nocookie.net/twicenation/images/a/a7/Nayeon_Strategy_Step_1_1.jpg/revision/latest?cb=20241116002546&format=original",
                ...
            ],
            "signature": "https://static.wikia.nocookie.net/twicenation/images/4/4b/Nayeon_Signature.png/revision/latest?cb=20200717041312&format=original",
            "facts": [
                "Nayeon was originally set to debut in the girl group 6mix with Jeongyeon, Jihyo and Sana.",
                ...
            ],
            "partner": null,
            "family": [
                {
                    "name": "Cheon Se-ah",
                    "relationship": "Mother"
                },
                ...
            ],
            "relatives": [
                {
                    "name": "Ji Yun Seo",
                    "relationship": "Maternal cousin"
                }
            ],
            "lovely": {
                "name": "Navely",
                "height": "23cm",
                "weight": "1.3kg",
                "personality": "Positive",
                "description": "'Loves kids!'",
                "picture": "https://static.wikia.nocookie.net/twicenation/images/5/5e/Navely.jpg/revision/latest?cb=20200514115137&format=original",
                "banner": "https://static.wikia.nocookie.net/twicenation/images/f/f2/Navely.gif/revision/latest?cb=20190221012000&format=original"
            },
            "fandom": "https://twice.fandom.com/wiki/Nayeon"
        },
        "Jeongyeon": { ... },
        ...
}
```

### Get Specific TWICE Member Data

```http
GET https://qing762.is-a.dev/api/twice/members/{member}
```

Returns data for a specific TWICE member.

#### Response

```json
{
    "name": "Son Chae-young",
    "otherNames": {
        "zh": "孙彩瑛",
        "en": "Katrina Son",
        "ko": "손채영"
    },
    "birthDate": 924825600,
    "age": "25",
    "birthPlace": "Dunchon-dong, Gangdong-gu, Seoul, South Korea",
    "height": "159cm (5'3\")",
    "weight": "46.4kg (102lbs)",
    "yearsActive": "2015-present",
    "bloodType": "B-",
    "MBTI": "INFP",
    "occupation": [
        "Rapper",
        ...
    ],
    "position": [
        "Main Rapper",
        ...
    ],
    "color": "Red",
    "instagram": [
        "https://www.instagram.com/chaeyo.0/"
    ],
    "twitter": null,
    "zepeto": [
        "https://user.zepeto.me/chaeyoung"
    ],
    "emoji": [
        "🐯"
    ],
    "instrument": [
        "Guitar"
    ],
    "agency": "JYP Entertainment",
    "associatedActs": [
        "TWICE",
        ...
    ],
    "images": [
        "https://static.wikia.nocookie.net/twicenation/images/9/9a/Chaeyoung_Strategy_Step_1_1.jpg/revision/latest?cb=20241116002537&format=original",
        ...
    ],
    "signature": "https://static.wikia.nocookie.net/twicenation/images/d/d7/Chaeyoung_Signature.png/revision/latest?cb=20200717042748&format=original",
    "facts": [
        "She is the shortest member of Twice.",
        ...
    ],
    "partner": {
        "name": "Zion.T",
        "years": "2024-present"
    },
    "family": [
        {
            "name": "Son Jeong-hun",
            "relationship": "Brother"
        }
    ],
    "relatives": [],
    "lovely": {
        "name": "Chaengvely",
        "height": "19cm",
        "weight": "1.9kg",
        "personality": "Creative",
        "description": "'Loves strawberries!'",
        "picture": "https://static.wikia.nocookie.net/twicenation/images/1/15/Chaengvely.jpg/revision/latest?cb=20200513210649&format=original",
        "banner": "https://static.wikia.nocookie.net/twicenation/images/1/11/Chaengvely.gif/revision/latest?cb=20190221021452&format=original"
    },
    "fandom": "https://twice.fandom.com/wiki/Chaeyoung"
}
```

### Get TWICE Ships

```http
GET https://qing762.is-a.dev/api/twice/ships
```

Returns the list of TWICE ships.

#### Response

```json
{
    "230s": {
            "name": "230s",
            "shipped": [
                "Jeongyeon",
                ...
            ],
            "otherNames": [
                "No TG"
                ...
            ],
            "rivals": [
                "2na",
                ...
            ],
            "similarities": [
                "Both are vocalists",
                ...
            ],
            "differences": [
                "Jeongyeon was born in South Korea while Sana was born in Japan",
                ...
            ],
            "facts": [
                "They didn't wear microphones in \"TWICE TV5 -TWICE in SWITZERLAND EP. 07\" because of their loud voices",
                ...
            ],
            "images": "https://static.wikia.nocookie.net/twicenation/images/5/52/230s_Profile-.jpeg/revision/latest?cb=20240224195502&format=original",
            "fandom": "https://twice.fandom.com/wiki/230s"
        },
        "2yeon": { ... },
        ...
    }
}
```

### Get Specific TWICE Ship Data

```http
GET https://qing762.is-a.dev/api/twice/ships/{ship}
```

Returns data for a specific TWICE ship.

#### Response

```json
{
    "name": "MiChaeng",
    "shipped": [
        "Mina",
        ...
    ],
    "otherNames": [
        "ChaengMi"
    ],
    "rivals": [
        "2na",
        ...
    ],
    "similarities": [
        "Both can sing and dance.",
        ...
    ],
    "differences": [
        "Mina is a ballet dancer while Chaeyoung isn’t.",
        ...
    ],
    "facts": [
        "Chaeyoung once told that if she had a chance to date TWICE members, she’ll choose Mina because she looks so handsome."
    ],
    "images": "https://static.wikia.nocookie.net/twicenation/images/1/19/MinaChaeyoung_IG_Story_Update_230827_1.jpg/revision/latest?cb=20230827203316&format=original",
    "fandom": "https://twice.fandom.com/wiki/MiChaeng"
}
```

## Run Locally

To build the API yourself, follow the steps below:

Clone the project

```bash
git clone https://github.com/qing762/twice-api
```

Go to the project directory

```bash
cd twice-api
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the code 

```bash
python main.py
```

You should see a `twice.json` file after this, meaning that it is built successfully and you can use the json file as an API for your projects.

## Contributing

Contributions are always welcome!

To contribute, fork this repository and improve it. After that, press the contribute button.

## Feedback / Issues

If you have any feedback or issues using the API, please join the [Discord server](https://qing762.is-a.dev/discord)

## License

[MIT LICENSE](https://choosealicense.com/licenses/mit/)