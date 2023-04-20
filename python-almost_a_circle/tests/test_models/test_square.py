"""
    unit test for square.py
"""

import unittest
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        Tests square
    """
    def setUp(self):
        """
            Initialize square instance
            With size only
        """
        self.sq = Square(20)

    def tearDown(self):
        """
            Deletes new instance
        """
        del self.sq

    def test_size(self):
        """
            Tests square size getter
        """
        self.assertEqual(20, self.sq.width)

    def test_x(self):
        """
            Tests the x getter
        """
        self.sq.x = 2
        self.assertEqual(2, self.sq.x)
        self.assertEqual(0, self.sq.y)

    def test_y(self):
        """
            Tests the y getter
        """
        self.sq.y = 2
        self.assertEqual(2, self.sq.y)
        self.assertEqual(0, self.sq.x)

    def test_square_id(self):
        """
            Tests the id of the square
        """
        sq1 = Square(1, 0, 0, 12)
        self.assertEqual(12, sq1.id)

    def test_size_str(self):
        """
            Tests wrong type for size: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square("s")

    def test_size_list(self):
        """
            Tests wrong type for size: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square([12, 43])

    def test_size_bool(self):
        """
            Tests wrong type for size: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(True)

    def test_x_str(self):
        """
            Tests wrong type for x: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square(72, "x", 0)

    def test_x_list(self):
        """
            Tests wrong type for x: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square(26, [13, 22], 83)

    def test_x_bool(self):
        """
            Tests wrong type for x: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(24, True, 97)

    def test_y_str(self):
        """
            Tests wrong type for y: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square(26, 30, "y")

    def test_y_list(self):
        """
            Tests wrong type for y: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square(21, 26, [41, 92])

    def test_y_bool(self):
        """
            Tests wrong type for y: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 9, True)

    def test_size_negative(self):
        """
            Tests negative value for size
        """
        with self.assertRaises(ValueError):
            sq1 = Square(-2)

    def test_size_zero(self):
        """
            Tests zero value for size
        """
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_x_negative(self):
        """
            Tests negative value for x
        """
        with self.assertRaises(ValueError):
            sq1 = Square(2, -1, 0)

    def test_y_negative(self):
        """
            Tests negative value for y
        """
        with self.assertRaises(ValueError):
            sq1 = Square(34, 42, -4)

    def test_area(self):
        """
            Tests for area()
        """
        sq1 = Square(20)
        self.assertEqual(sq1.area(), 20 * 20)

    def test_str_overload(self):
        """
            Tests the str overload
        """
        sq = Square(10, 2, 3, 9)
        self.assertEqual(sq.__str__(), "[Square] (9) 2/3 - 10")

    def test_update(self):
        """
            Test update function with *args
        """
        sq1 = Square(1)
        sq1.update(2, 4)
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_update_kwargs(self):
        """
            Test update() function with **kwargs
        """
        sq1 = Square(1)
        sq1.update(size=7, y=1, id=12)
        self.assertEqual(sq1.__str__(), "[Square] (12) 0/1 - 7")

    def test_update_both(self):
        """
            Test update() with both args and kwargs
        """
        sq1 = Square(1)
        sq1.update(2, 4, **{'x': 3, 'y': 4})
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_create_dict_equal(self):
        """
            Tests creating square is not equal
        """
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)

    def test_create_dict_is(self):
        """
            Tests create squaree is (sq1 is sq2)
        """
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_save_to_file_none(self):
        """
            Tests save to file none
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_empty(self):
        """
            Tests save to file empty list
        """
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_rect(self):
        """
            Tests save to file with proper input
        """
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(json.loads(content), [{"id": 5,
                                                    "size": 1,
                                                    "x": 3, "y": 4}])

    def test_save_to_file_noargs(self):
        """
            Tests save to file with no arguments
        """
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_type(self):
        """
            Tests save to file , format saved in
        """
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(str, type(content))

    def test_load_from_file_noexist(self):
        """
            Tests load from file that doesnt exist
        """
        sq1 = Square(1)
        Square.save_to_file([sq1])
        list_output = Square.load_from_file()
        self.assertEqual(sq1.width, list_output[0].size)

    def test_stf_None(self):
        """
            Test save_to_file with None
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

