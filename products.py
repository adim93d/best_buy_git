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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}"

    def buy(self, quantity) -> str:
        if quantity > self.quantity:
            return f"insufficient item quantity, Only {self.quantity} units available."
        else:
            purchase_price = quantity * self.price
            self.quantity = self.quantity - quantity
            return f"Total item price: ${purchase_price}"


class NonStockedProducts(Product):
    def __init__(self, name: str, price: float, quantity: int, active: bool):
        super().__init__(name, price, active, quantity)
        self.name = name
        self.price = price
        self.active = active

    def is_active(self):
        return self.active

    def get_quantity(self) -> int:
        return self.quantity

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}"

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
        return f"{self.name}, Price: {self.price}, Limited to {self.order_limit} per order, Active: {self.active}"

    def buy(self, quantity) -> str:
        if quantity > self.order_limit:
            return f"Only {self.order_limit} units per order."
        else:
            purchase_price = quantity * self.price
            self.quantity = self.quantity - quantity
            return f"Total item price: ${purchase_price}"

