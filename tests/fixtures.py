from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class SubFactorySimpleModel:
    first_name: str = ""
    last_name: str = ""
    birthday: Optional[date] = None


@dataclass
class SimpleModel:
    first_name: str = ""
    last_name: str = ""
    birthday: Optional[date] = None
