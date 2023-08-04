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

        self.cmds1 = ["f", "r", "u", "b", "l"]
        self.cmds2 = ["d", "f", "l", "b", "u", "d", "r", "b", "f", "l"]
        self.cmds3 = ["u", "f", "l", "f", "r", "f"]

    def test_print_position_direction(self):
        self.assertEqual(self.craft1.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        self.assertEqual(self.craft2.__str__(), "Final Position: (9, 4, -3)\nFinal Direction: S")

    def test_run_spacecraft(self):
        craft8 = SpaceCraft(0, 0, 0, "N")
        craft8.run_spacecraft(self.cmds1)
        self.assertEqual(craft8.__str__(), "Final Position: (0, 1, -1)\nFinal Direction: W")

        craft8 = SpaceCraft(0, 0, 0, "N")
        craft8.run_spacecraft(self.cmds2)
        self.assertEqual(craft8.__str__(), "Final Position: (-1, 0, -1)\nFinal Direction: N")

        craft8 = SpaceCraft(0, 0, 0, "N")
        craft8.run_spacecraft(self.cmds3)
        self.assertEqual(craft8.__str__(), "Final Position: (-1, 1, 1)\nFinal Direction: N")

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

    def test_turn(self):
        craft7 = SpaceCraft(0, 0, 0, "N")
        craft7.turn("l")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: W")

        craft7 = SpaceCraft(0, 0, 0, "N")
        craft7.turn("r")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: E")

        craft7 = SpaceCraft(0, 0, 0, "N")
        craft7.turn("u")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: U")

        craft7 = SpaceCraft(0, 0, 0, "N")
        craft7.turn("d")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: D")

        craft7 = SpaceCraft(0, 0, 0, "S")
        craft7.turn("l")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: E")

        craft7 = SpaceCraft(0, 0, 0, "S")
        craft7.turn("r")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: W")

        craft7 = SpaceCraft(0, 0, 0, "S")
        craft7.turn("u")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: U")

        craft7 = SpaceCraft(0, 0, 0, "S")
        craft7.turn("d")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: D")

        craft7 = SpaceCraft(0, 0, 0, "E")
        craft7.turn("l")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        craft7 = SpaceCraft(0, 0, 0, "E")
        craft7.turn("r")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: S")

        craft7 = SpaceCraft(0, 0, 0, "E")
        craft7.turn("u")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: U")

        craft7 = SpaceCraft(0, 0, 0, "E")
        craft7.turn("d")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: D")

        craft7 = SpaceCraft(0, 0, 0, "W")
        craft7.turn("l")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: S")

        craft7 = SpaceCraft(0, 0, 0, "W")
        craft7.turn("r")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        craft7 = SpaceCraft(0, 0, 0, "W")
        craft7.turn("u")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: U")

        craft7 = SpaceCraft(0, 0, 0, "W")
        craft7.turn("d")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: D")

        craft7 = SpaceCraft(0, 0, 0, "U")
        craft7.turn("l")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: W")

        craft7 = SpaceCraft(0, 0, 0, "U")
        craft7.turn("r")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: E")

        craft7 = SpaceCraft(0, 0, 0, "U")
        craft7.turn("u")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: S")

        craft7 = SpaceCraft(0, 0, 0, "U")
        craft7.turn("d")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        craft7 = SpaceCraft(0, 0, 0, "D")
        craft7.turn("l")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: E")

        craft7 = SpaceCraft(0, 0, 0, "D")
        craft7.turn("r")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: W")

        craft7 = SpaceCraft(0, 0, 0, "D")
        craft7.turn("u")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")

        craft7 = SpaceCraft(0, 0, 0, "D")
        craft7.turn("d")
        self.assertEqual(craft7.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: S")


if __name__ == "__main__":
    unittest.main()
