from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float, quantity: int, active: bool):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def is_active(self) -> bool:
        if self.quantity == 0:
            self.active = False
        return self.active

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity: int):
        try:
            self.quantity += quantity
            if self.quantity <= 0:
                self.deactivate()
            else:
                self.activate()
            return f"Added {quantity} units to total amount {self.quantity}"
        except TypeError:
            return f"Wrong input, Please enter Integer"

    def show(self) -> str:
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()
        return f"{self.name}, " \
               f"Price: {self.price}, " \
               f"Quantity: {self.quantity}, " \
               f"Active: {self.active}, " \
               # f"Promotion: {Promotions.get_promotion(self)}"

    def buy(self, quantity):
        if quantity > self.quantity:
            return f"insufficient item quantity, Only {self.quantity} units available."
        else:
            purchase_price = quantity * self.price
            self.quantity = self.quantity - quantity
            return f"Total item price: ${purchase_price}"


class NonStockedProducts(Product):
    def __init__(self, name: str, price: float, quantity: str, active: bool):
        super().__init__(name, price, quantity, active)
        self.name = name
        self.price = price
        self.quantity = "Unlimited"
        self.active = active

    def is_active(self):
        return self.active

    def get_quantity(self) -> str:
        return self.quantity

    def show(self) -> str:
        return f"{self.name}, " \
               f"Price: {self.price}, " \
               f"Quantity: {self.quantity}, " \
               f"Active: {self.active}, " \
               # f"Promotion: {Promotions.get_promotion()}"

    def buy(self, quantity):
        purchase_price = quantity * self.price
        return f"Total item price: ${purchase_price}"


class LimitedProducts(Product):
    def __init__(self, name: str, price: float, quantity: int, active: bool, order_limit: int):
        super().__init__(name, price, quantity, active)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        self.order_limit = order_limit

    def show(self) -> str:
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()
        return f"{self.name}, " \
               f"Price: {self.price}, " \
               f"Limited to {self.order_limit} per order, " \
               f"Active: {self.active}, " \
               # f"Promotion: {Promotions.get_promotion()}"

    def buy(self, quantity) -> str:
        if quantity > self.order_limit:
            return f"Only {self.order_limit} units per order."
        else:
            purchase_price = quantity * self.price
            self.quantity = self.quantity - quantity
            return f"Total item price: ${purchase_price}"


class Promotions(ABC):
    def __init__(self, promo):
        self._promo = promo

    def get_promotion(self):
        return self._promo

    def set_promotion(self, promo):
        self._promo = promo


class SecondHalfPrice(Promotions):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        if quantity < 2:
            return product * quantity  # No discount if only buying one item
        else:
            discount = product / 2  # Half price discount for second item onwards
            total_price = product + discount * (quantity - 1)  # Apply discount to all but the first item
            return total_price


class ThirdOneFree(Promotions):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        if quantity < 3:
            return product * quantity  # no discount applied
        else:
            free_items = quantity // 3  # calculate number of free items
            total_items = quantity - free_items  # calculate total number of items after discount
            total_cost = product * total_items  # calculate total cost after discount
            return total_cost


class PercentDiscount(Promotions):
    @abstractmethod
    def apply_promotion(self, product, quantity, discount_percent) -> float:
        price = product
        total = price * quantity
        discount = total * (discount_percent / 100)
        return total - discount






