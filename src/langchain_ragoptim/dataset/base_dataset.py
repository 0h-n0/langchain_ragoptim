from abc import ABC, abstractmethod


class BaseDataset(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, i: int):
        pass
