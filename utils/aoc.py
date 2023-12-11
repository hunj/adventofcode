from dotenv import load_dotenv
from pathlib import Path
from os import environ
from typing import List
import requests

load_dotenv(dotenv_path=Path('.env'))
AOC_SESSION = environ['AOC_SESSION']


def get_data_for(day: int = 0) -> List[str]:
    if not day:
        raise Exception()

    url = f"https://adventofcode.com/2023/day/{day}/input"

    res = requests.get(url, cookies={'session': AOC_SESSION})
    return res.content.decode().split('\n')
