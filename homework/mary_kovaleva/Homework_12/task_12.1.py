class Flower:

    def __init__(self, name, colour, freshness, stem_length, price):
        self.__name = name
        self.__colour = colour
        self.__freshness = freshness
        self.__stem_length = stem_length
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def colour(self):
        return self.__colour

    @property
    def freshness(self):
        return self.__freshness

    @freshness.setter
    def freshness(self, value):
        self.__freshness = value

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class Tulip(Flower):

    def __init__(self, name, colour, freshness, stem_length, price):
        super().__init__(name, colour, freshness, stem_length, price)

    def __str__(self):
        return (f"{self.name}, Colour: {self.colour}, Freshness: {self.freshness}/10, "
                f"Stem length: {self.stem_length} cm, Price: {self.price} RUB")


class Daffodil(Flower):

    def __init__(self, name, colour, freshness, stem_length, price):
        super().__init__(name, colour, freshness, stem_length, price)

    def __str__(self):
        return (f"{self.name}, Colour: {self.colour}, Freshness: {self.freshness}/10, "
                f"Stem length: {self.stem_length} cm, Price: {self.price} RUB")


class Rose(Flower):

    def __init__(self, name, colour, freshness, stem_length, price):
        super().__init__(name, colour, freshness, stem_length, price)

    def __str__(self):
        return (f"{self.name}, Colour: {self.colour}, Freshness: {self.freshness}/10, "
                f"Stem length: {self.stem_length} cm, Price: {self.price} RUB")


class Snowdrop(Flower):

    def __init__(self, name, colour, freshness, stem_length, price):
        super().__init__(name, colour, freshness, stem_length, price)

    def __str__(self):
        return (f"{self.name}, Colour: {self.colour}, Freshness: {self.freshness}/10, "
                f"Stem length: {self.stem_length} cm, Price: {self.price} RUB")


class Bouquet:

    def __init__(self):
        self.flower_list = []
        self.__price = 0
        self.__freshness = 1

    @property
    def price(self):
        return self.__price

    @property
    def freshness(self):
        return self.__freshness

    def add_flower(self, flower):
        self.flower_list.append(flower)
        self.__count_price()
        self.__calc_freshness()

    def remove_flower(self, name):
        flower_to_remove = [flower for flower in self.flower_list if flower.name == name]
        for flower in flower_to_remove:
            self.flower_list.remove(flower)
        self.__count_price()
        self.__calc_freshness()

    def __count_price(self):
        self.__price = sum([flower.price for flower in self.flower_list])

    def __calc_freshness(self):
        overall_freshness = sum([flower.freshness for flower in self.flower_list])
        number_of_flowers = len(self.flower_list)
        self.__freshness = round(overall_freshness / number_of_flowers, 1)

    def sort_flowers(self, param):
        self.flower_list.sort(key=lambda x: getattr(x, param, 'Error'))
        return [str(flower) for flower in self.flower_list]

    def search_flower(self, param, value):
        return [str(flower) for flower in self.flower_list if getattr(flower, param) == value]

    def __str__(self):
        return f"This is a bouquet with flowers: {', '.join([flower.name for flower in self.flower_list])}"

    def __repr__(self):
        return f"This is a bouquet with flowers: {', '.join([flower.name for flower in self.flower_list])}"


tulip = Tulip('Rembrandt', 'red', 10, 40, 400)
daffodil = Daffodil('Triandus Thalia', 'white', 8, 38, 250)
rose = Rose('Engagement', 'pink', 7, 70, 600)
snowdrop = Snowdrop('Alpine', 'white', 9, 25, 200)
bouquet = Bouquet()
bouquet.add_flower(tulip)
bouquet.add_flower(rose)
bouquet.add_flower(daffodil)
bouquet.add_flower(rose)
bouquet.add_flower(snowdrop)
print(bouquet)
print(bouquet.price)
print(bouquet.freshness)
print(bouquet.search_flower('colour', 'white'))
print(bouquet.sort_flowers('freshness'))
bouquet.remove_flower('Engagement')
print(bouquet)
print(bouquet.price)
print(bouquet.freshness)
