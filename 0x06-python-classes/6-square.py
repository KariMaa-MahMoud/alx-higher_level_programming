#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (
            isinstance(position, tuple)
            and len(position) == 2
            and isinstance(position[0], int)
            and isinstance(position[1], int)
            and position[0] >= 0
            and position[1] >= 0
        ):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        print("{}".format("\n" * self.__position[1]), end="")
        print(
            "{}".format(
                "\n".join([" " * self.__position[0] + "#" * self.__size] * self.__size)
            )
        )

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], int)
            and isinstance(value[1], int)
            and value[0] >= 0
            and value[1] >= 0
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

