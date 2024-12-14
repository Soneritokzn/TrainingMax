from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Data:
    id: int
    name: str
    year: int
    color: str
    pantone_value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _year = int(obj.get("year"))
        _color = str(obj.get("color"))
        _pantone_value = str(obj.get("pantone_value"))
        return Data(_id, _name, _year, _color, _pantone_value)

@dataclass
class Support:
    url: str
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Support':
        _url = str(obj.get("url"))
        _text = str(obj.get("text"))
        return Support(_url, _text)


@dataclass
class Root:
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Data]
    support: Support

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _page = int(obj.get("page"))
        _per_page = int(obj.get("per_page"))
        _total = int(obj.get("total"))
        _total_pages = int(obj.get("total_pages"))
        _data = [Data.from_dict(y) for y in obj.get("data")]
        _support = Support.from_dict(obj.get("support"))
        return Root(_page, _per_page, _total, _total_pages, _data, _support)

    @staticmethod
    def from_json(json_string: str) -> 'Root':
        data_dict = json.loads(json_string)
        return Root.from_dict(data_dict)

