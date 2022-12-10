import doctest
class Televisions:
    def __init__(self, screen_diagonal: int, update_frequency: int, screen_resolution:string):
        """
        Создание и подготовка к работе объекта "Телевизор"
        :param screen_diagonal: Диагональ экрана
        :param update_frequency: Частота обновления
        :param screen_resolution: Разрешение экрана
        Примеры:
        >>> televisions= Televisions(55, 60,"1200x1440")  # инициализация экземпляра класса
        """
        if not isinstance(screen_diagonal, int):
            raise TypeError("Диагональ экрана должен быть типа int")
        if screen_diagonal <= 0:
            raise ValueError("Диагональ экрана должна быть положительным числом")
        self.screen_diagonal = screen_diagonal

        if not isinstance(update_frequency, int):
            raise TypeError("Частота обновления должно быть int")
        if update_frequency < 0:
            raise ValueError("Частота обновления не может быть отрицательным числом")
        self.update_frequency = update_frequency
        self.screen_resolution=screen_resolution
    def inclusion_televisions(self) -> bool:
        """
        Функция которая проверяет включен ли телевизор
        :return: Включен ли телевизор
        """
    def screen_resolution_change(self, screen_resolution: string) -> None:
        """
        Изменение диагонали экрана телевизора.
        """
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации



    class Table:
        def __init__(self, length_table: float, width_table: float, color_table: string):
            """
            Создание и подготовка к работе объекта "Стол"
            :param length_table: Длина стола
            :param width_table: Ширина стола
            :param color_table: Цвет стола
            Примеры:
            >>> table= Table(110, 90,"Белый")  # инициализация экземпляра класса
            """
            if not isinstance(length_table, (int,float)):
                raise TypeError("Длина стола быть типа int")
            if length_tabl <= 0:
                raise ValueError("Длина стола должна быть положительным числом")
            self.length_table = length_table

            if not isinstance(width_table, (int,float)):
                raise TypeError("Частота обновления должно быть int")
            if width_table < 0:
                raise ValueError("Частота обновления не может быть отрицательным числом")
            self.width_table = width_table
            self.color_table=color_table

        def table_size_selection(self, length_table: float, width_table: float) -> None:
            """
            Функция которая изменяет длину и ширину столешницы по запросу покупателя
            """

        def changing_color_table(self, color_table: string) -> None:
            """
            Изменение цвета стола.
            """
    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации


        class Headphones:
            def __init__(self, sound_volume: int, type_headphones: string, color_headphones: string):
                """
                Создание и подготовка к работе объекта "Наушники"
                :param sound_volume: Громкость звука
                :param type_headphones: Тип наушников
                :param color_headphones: Цвет наушников
                Примеры:
                >>> table= Table(50, "Вкладыши","Черный")  # инициализация экземпляра класса
                """
                if not isinstance(sound_volume, int):
                    raise TypeError("Громкость звука должна быть типа int")
                if sound_volume <= 0:
                    raise ValueError("Громкость звука должна быть положительным числом")
                self.sound_volume = sound_volume
                self.type_headphones=type_headphones
                self.color_headphones=color_headphones

            def sound_volume_change(self, sound:int) -> None:
                """
                      Добавление звука в наушниках.
                      :param sound: Добавляемая громкости
                      """
                if not isinstance(sound, int):
                    raise TypeError("Добавляемая громкостиь должна быть типа int или float")
                if sound < 0:
                    raise ValueError("Добавляемая громкости должна положительным числом")
                ...

            def changing_color_headphones(self, color_headphones: string) -> None:
                """
                Изменение цвета наушников.
                """
        if __name__ == "__main__":
            doctest.testmod()  # тестирование примеров, которые находятся в документации