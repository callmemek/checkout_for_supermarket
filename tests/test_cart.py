import unittest
from supermarket import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # Arrange (for all tests)
        self.cart = ShoppingCart()
        self.cart.add_item("candy", 2, 1.0)
        self.cart.add_item("gum", 3, 0.5)

    # Unit tests for add_item
    def test_add_item_new(self):
        # Arrange
        initial_total = self.cart.total
        
        # Act
        self.cart.add_item("Orange", 4, 50.0)
        
        # Assert
        self.assertEqual(self.cart.items["Orange"]["quantity"], 4)
        self.assertEqual(self.cart.total, initial_total + (4*50.0))

    def test_add_item_existing(self):
        # Arrange
        initial_quantity = self.cart.items["candy"]["quantity"]
        initial_total = self.cart.total
        
        # Act
        self.cart.add_item("candy", 3, 1.0)
        
        # Assert
        self.assertEqual(self.cart.items["candy"]["quantity"], initial_quantity + 3)
        self.assertEqual(self.cart.total, initial_total + (3*1.0))

    # Edge tests for add_item
    def test_add_item_zero_quantity(self):
        # Arrange/Act/Assert
        with self.assertRaises(ValueError):
            self.cart.add_item("Orange", 0, 50.0)

    def test_add_item_negative_price(self):
        # Arrange/Act/Assert
        with self.assertRaises(ValueError):
            self.cart.add_item("Orange", 4, -50.0)

    