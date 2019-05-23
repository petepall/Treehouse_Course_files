class Protected:
    __name = "Security"

    def __method(self):
        return self.__name


prot = Protected()
prot.__name
prot.__method()
