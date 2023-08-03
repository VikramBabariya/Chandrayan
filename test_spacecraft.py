import unittest
from spacecraft import SpaceCraft


class TestSpaceCraft(unittest.TestCase):

    def setUp(self):
        self.craft1 = SpaceCraft(0, 0, 0, "N")

    def test_print_position_direction(self):
        self.assertEqual(self.craft1.__str__(), "Final Position: (0, 0, 0)\nFinal Direction: N")


if __name__ == "__main__":
    unittest.main()
