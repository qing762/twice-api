> [!NOTE]  
> Join the [Discord server](https://qing762.is-a.dev/discord) for issues. Thanks a lot!

# TWICE API

An API that scrapes data from [Twice Wiki](https://twice.fandom.com) and convert into JSON format.

## How it works

It scrapes data from [Twice Wiki](https://twice.fandom.com) and format/beautify it into a JSON format.

## API Reference

### Get TWICE Data

```http
GET /api/twice
```

Returns the entire TWICE data.

#### Response

```json
{
    "twice": {
        "name": "TWICE",
        "otherNames": ["트와이스"],
        "origin": "South Korea",
        "genres": ["K-pop", "J-pop"],
        "activeYears": "2015–present",
        "labels": ["JYP Entertainment"],
        "associatedActs": ["JYP Nation"],
        "fandomName": "ONCE",
        "officialColor": "Apricot & Neon Magenta",
        "slogan": "One in a Million",
        "groupNameMeaning": "The act of touching people's hearts twice: once through the ears, and once again through the eyes.",
        "website": "http://twice.jype.com",
        "fandom": "http://once.jype.com"
    },
    "member": {
        "Nayeon": { ... },
        "Jeongyeon": { ... },
        ...
    },
    "ships": {
        "2Yeon": { ... },
        "SaTzu": { ... },
        ...
    }
}
```

### Get TWICE Group Data

```http
GET /api/twice/group
```

Returns the TWICE group data.

#### Response

```json
{
    "name": "TWICE",
    "otherNames": ["트와이스"],
    "origin": "South Korea",
    "genres": ["K-pop", "J-pop"],
    "activeYears": "2015–present",
    "labels": ["JYP Entertainment"],
    "associatedActs": ["JYP Nation"],
    "fandomName": "ONCE",
    "officialColor": "Apricot & Neon Magenta",
    "slogan": "One in a Million",
    "groupNameMeaning": "The act of touching people's hearts twice: once through the ears, and once again through the eyes.",
    "website": "http://twice.jype.com",
    "fandom": "http://once.jype.com"
}
```

### Get TWICE Members

```http
GET /api/twice/members
```

Returns the list of TWICE members.

#### Response

```json
{
    "Nayeon": { ... },
    "Jeongyeon": { ... },
    ...
}
```

### Get Specific TWICE Member Data

```http
GET /api/twice/members/{member}
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
GET /api/twice/ships
```

Returns the list of TWICE ships.

#### Response

```json
{
    "2Yeon": { ... },
    "SaTzu": { ... },
    ...
}
```

### Get Specific TWICE Ship Data

```http
GET /api/twice/ships/{ship}
```

Returns data for a specific TWICE ship.

#### Response

```json
{
    "name": "MiChaeng",
    "shipped": [
        "Mina",
        "Chaeyoung"
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