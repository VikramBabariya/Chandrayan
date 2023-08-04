import unittest
from spacecraft import SpaceCraft


class TestSpaceCraft(unittest.TestCase):

    def setUp(self):
        self.craft1 = SpaceCraft(0, 0, 0, "N")
        self.craft2 = SpaceCraft(9, 4, -3, "S")
        self.craft3 = SpaceCraft(4, -6, -2, "E")
        self.craft4 = SpaceCraft(1, 2, 5, "W")
        self.craft5 = SpaceCraft(-5, 0, 5, "U")
        self.craft6 = SpaceCraft(-5, 7, -5, "D")

    def test_print_position_direction(self):
        self.assertEqual(self.craft1.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        self.assertEqual(self.craft2.__str__(), "Final Position: (9, 4, -3)\nFinal Direction: S")

    def test_move(self):
        self.craft1.move("f")
        self.assertEqual(self.craft1.__str__(), "Final Position: (0, 1, 0)\nFinal Direction: N")

        self.craft1.move("b")
        self.assertEqual(self.craft1.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        self.craft2.move("f")
        self.assertEqual(self.craft2.__str__(), "Final Position: (9, 3, -3)\nFinal Direction: S")

        self.craft2.move("b")
        self.assertEqual(self.craft2.__str__(), "Final Position: (9, 4, -3)\nFinal Direction: S")

        self.craft3.move("f")
        self.assertEqual(self.craft3.__str__(), "Final Position: (5, -6, -2)\nFinal Direction: E")

        self.craft3.move("b")
        self.assertEqual(self.craft3.__str__(), "Final Position: (4, -6, -2)\nFinal Direction: E")

        self.craft4.move("f")
        self.assertEqual(self.craft4.__str__(), "Final Position: (0, 2, 5)\nFinal Direction: W")

        self.craft4.move("b")
        self.assertEqual(self.craft4.__str__(), "Final Position: (1, 2, 5)\nFinal Direction: W")

        self.craft5.move("f")
        self.assertEqual(self.craft5.__str__(), "Final Position: (-5, 0, 6)\nFinal Direction: U")

        self.craft5.move("b")
        self.assertEqual(self.craft5.__str__(), "Final Position: (-5, 0, 5)\nFinal Direction: U")

        self.craft6.move("f")
        self.assertEqual(self.craft6.__str__(), "Final Position: (-5, 7, -6)\nFinal Direction: D")

        self.craft6.move("b")
        self.assertEqual(self.craft6.__str__(), "Final Position: (-5, 7, -5)\nFinal Direction: D")


if __name__ == "__main__":
    unittest.main()
