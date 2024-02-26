from abc import ABC, abstractmethod
# interfaz heredado de abc.ABC
# forzar a las clases que implementen esta interfaz con @abstractmethod
class Game(ABC):
    @abstractmethod
    def game_init(self, config):
        pass

    @abstractmethod
    def game_input(self) -> str:
        pass

    @abstractmethod
    def game_turn(self, input_str):
        pass

    @abstractmethod
    def game_print(self):
        pass

    @abstractmethod
    def game_is_finish(self) -> bool:
        pass

    @abstractmethod
    def game_finish_msg(self) -> str:
        pass
