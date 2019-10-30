from abc import ABC, abstractmethod, abstractproperty
from typing import Iterable


class Plugin(ABC):
    def __init__(self, module_path: str, module_name: str, exclude_paths: Iterable[str]):
        self.module_path = module_path
        self.module_name = module_name
        self.exclude_paths = exclude_paths

    @abstractproperty
    def plugin_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def run(self) -> int:
        raise NotImplementedError

    def set_up(self) -> None:
        pass

    def tear_down(self) -> None:
        pass
