from abc import ABC, abstractmethod

class Remote(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
class TV(Remote):

    def turn_on(self):
        print("TV is ON 📺")

    def turn_off(self):
        print("TV is OFF 📺")
tv = TV()
tv.turn_on()
tv.turn_off()