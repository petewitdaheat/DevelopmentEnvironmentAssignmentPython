class tv:
    def __init__(self, channel, volume, on):
        try:
            if(channel < 1 or channel > 120):
                raise ValueError("Channel must be between 1 and 120.")
        except ValueError as e:
            exit(e)
        else:
            self.__channel = channel
        
        try:
            if(volume < 1 or volume > 7):
                raise ValueError("Volume must be between 1 and 7.")
        except ValueError as e:
            exit(e)
        else:
            self.__volume = volume

        try:
            if(on != True and on != False):
                raise ValueError("On must be True or False.")
        except ValueError as e:
            exit(e)
        else:
            self.__on = on
        
    def setChannel(self, channel):
        if (self.__on and channel >= 1 and channel <= 120):
            self.__channel = channel

    def setVolume(self, volume):
        if (self.__on and volume >= 1 and volume <= 7):
            self.__volume = volume

    def turnOn(self):
        self.__on = True

    def turnOff(self):
        self.__on = False

    def channelUp(self):
        if (self.__on and self.__channel < 120):
            self.__channel += 1

    def volumeUp(self):
        if (self.__on and self.__volume < 7):
            self.__volume += 1

    def channelDown(self):
        if (self.__on and self.__channel > 1):
            self.__channel -= 1

    def volumeDown(self):
        if (self.__on and self.__volume > 1):
            self.__volume -= 1

    def __str__(self):
        return f"TV channel={self.__channel} volume={self.__volume} on{self.__on}"

    