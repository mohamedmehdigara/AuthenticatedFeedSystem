from uuid import uuid4
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4, UUID
from pydantic.types import UUID1
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(Enum, str):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    firstname: str
    lastname: str
    middlename: Optional[str]
    gender: Gender
    roles: List[Role]
