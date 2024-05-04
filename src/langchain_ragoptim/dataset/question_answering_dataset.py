from pathlib import Path
from typing import Any, Dict

import polars
from pydantic import BaseModel, Field, computed_field, field_validator

from .base_dataset import BaseDataset


class QuestionAnasweringDataset(BaseModel, BaseDataset):
    inputfile: Path = Field(frozen=True)
    context: bool = Field(default=False)

    @field_validator("inputfile")
    @classmethod
    def validate(cls, v):
        if not Path(v).exists():
            raise FileNotFoundError(f"File {v} does not exist")
        return v

    @computed_field(return_type=Any)
    def dataframe(self):
        return polars.read_csv(self.inputfile)

    def __len__(self) -> int:
        return self.dataframe.shape[0]

    def __getitem__(self, i: int) -> Dict[str, str]:
        return self.dataframe.to_dicts()[i]
