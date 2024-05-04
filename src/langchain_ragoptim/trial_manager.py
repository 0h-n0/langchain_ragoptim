from typing import Any

from pydantic import BaseModel

from .dataset.base_dataset import BaseDataset


class TrialManager(BaseModel):
    llm: Any = None
    dataset: Any = None

    def run(self):
        pass