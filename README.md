# Coffee shopts checker

Coffee shopts checker is a Python script thats find close coffee shops based on your location. 

## Installation

First of all you need to download all the files in this repo to your computer. Then you need to create and run a virtual environment with these commands:

On Mac OS and Linux:
```bash
# create environment with name venv
virtualenv venv -p python3
# runing venv enviroment
source venv/bin/activate
```

On Windows:
```bash
# create environment with name env
python -m venv env
# runing env enviroment
env\Scripts\activate
```

The next step is to install the necessary modules. This command will help:
```bash
pip install -r requirements.txt
```

## Description of the Data Structure

The program works with a JSON file whose structure looks like a list of dictionaries:
```bash
  [
    {
      "global_id": 1061827454,
      "Latitude_WGS84": "55.7849277658219190",
      "ID": "00280872",
      "Name": "ÏÐÀÂDÀ Êîôå",
      "IsNetObject": "äà",
      "OperatingCompany": "ÏÐÀÂDÀ Êîôå",
      "TypeObject": "êàôåòåðèé",
      "AdmArea": "Ñåâåðíûé àäìèíèñòðàòèâíûé îêðóã",
      "District": "ðàéîí Áåãîâîé",
      "Address": "ãîðîä Ìîñêâà, óëèöà Ïðàâäû, äîì 8, êîðïóñ 49",
      "PublicPhone": [
        {
          "PublicPhone": "(800) 555-19-66"
        }
      ],
      "SeatsCount": 0,
      "SocialPrivileges": "íåò",
      "Longitude_WGS84": "37.5789000000000040",
      "geoData": {
        "type": "Point",
        "coordinates": [
          37.578900000000004,
          55.78492776582192
        ]
      }
    },
    {
      "global_id": 1061827455,
      "Latitude_WGS84": "55.6394907237606730",
      "ID": "00278418",
      "Name": "ÏÐÀÂDÀ Êîôå",
      "IsNetObject": "äà",
      "OperatingCompany": "ÏÐÀÂDÀ Êîôå",
      "TypeObject": "êàôåòåðèé",
      "AdmArea": "Þæíûé àäìèíèñòðàòèâíûé îêðóã",
      "District": "ðàéîí Ìîñêâîðå÷üå-Ñàáóðîâî",
      "Address": "ãîðîä Ìîñêâà, Êàíòåìèðîâñêàÿ óëèöà, äîì 58",
      "PublicPhone": [
        {
          "PublicPhone": "íåò òåëåôîíà"
        }
      ],
      "SeatsCount": 4,
      "SocialPrivileges": "íåò",
      "Longitude_WGS84": "37.6445210000000050",
      "geoData": {
        "type": "Point",
        "coordinates": [
          37.644521000000005,
          55.63949072376067
        ]
      }
    },
    ...
    ...
  ]
```

You can make the same json data structure by yourself or download this data structure from this website https://data.mos.ru/opendata

## Usage

In order to start script, you need to run `main.py` file with this command:

```bash
python main.py
```

After pressing Enter button, you will see this question:

```bash
Где вы находитесь?
```

You need to wrote some place in Moscow. For example:
```bash
Где вы находитесь? Красная площадь
```

After pressing Enter button, you will see this output:

```bash
Ваши координаты:  ('37.621202', '55.753544')
[{'distance': 0.07830555782131858,
  'latitude': 37.621529,
  'longitude': 55.754660757023636,
  'title': 'Bosco Cafe'},
 {'distance': 0.07830555782131858,
  'latitude': 37.621529,
  'longitude': 55.754660757023636,
  'title': 'КОФЕМАНИЯ'},
 {'distance': 0.1972945556737127,
  'latitude': 37.626224999999984,
  'longitude': 55.75321475660388,
  'title': 'Кофейня Просвет'},
 {'distance': 0.24545510779907528,
  'latitude': 37.621987746,
  'longitude': 55.75706419199997,
  'title': 'Кофе Хауз'},
 {'distance': 0.2999999367411837,
  'latitude': 37.614625717781195,
  'longitude': 55.75579132932476,
  'title': 'Кофе Хауз'}]
```

this script show you top 5 coffee shops that being near to your location. 

Then you can run `site.py` file that showed you the exact location of this shops on the map.
You need to run `site.py` file with this command:

```bash
python site.py
```

and then you'll see this output on the console:
```bash
     * Serving Flask app 'site'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:5000
     * Running on http://192.168.0.101:5000
    Press CTRL+C to quit
```

All you need to do is open a browser and check this url http://127.0.0.1:5000 or this http://192.168.0.101:5000

And you will see map with 5 coffee shops

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Project Goals
This code was written for educational purposes as part of an online course for web developers at dvmn.org.

## Contacts

You can find my on telegram: https://t.me/bashir_77