import unittest
import consecutive_cities_problem as cp


class MyTestCase(unittest.TestCase):
    test_input_1 = (1, 1, 1, 1)
    test_output_1 = [[0, 1, 2, 3, 4],
                     [1, 0, 1, 2, 3],
                     [2, 1, 0, 1, 2],
                     [3, 2, 1, 0, 1],
                     [4, 3, 2, 1, 0]]

    test_input_2 = (3, 10, 12, 5)
    test_output_2 = [[0, 3, 13, 25, 30],
                     [3, 0, 10, 22, 27],
                     [13, 10, 0, 12, 17],
                     [25, 22, 12, 0, 5],
                     [30, 27, 17, 5, 0]]
    test_input_3 = (1,)
    test_output_3 = [[0, 1], [1, 0]]

    def test_calculate_dist_table_1(self):
        self.assertEqual(self.test_output_1, cp.calculate_dist_table_1(*self.test_input_1))
        self.assertEqual(self.test_output_2, cp.calculate_dist_table_1(*self.test_input_2))

    def test_calculate_dist_table_2(self):
        self.assertEqual(self.test_output_1, cp.calculate_dist_table_2(*self.test_input_1))
        self.assertEqual(self.test_output_2, cp.calculate_dist_table_2(*self.test_input_2))
        self.assertEqual(self.test_output_3, cp.calculate_dist_table_2(*self.test_input_3))

    def test_calculate_dist_table_3(self):
        self.assertEqual(self.test_output_1, cp.calculate_dist_table_3(*self.test_input_1))
        self.assertEqual(self.test_output_2, cp.calculate_dist_table_3(*self.test_input_2))
        self.assertEqual(self.test_output_3, cp.calculate_dist_table_3(*self.test_input_3))

    def test_calculate_dist_table_4(self):
        self.assertEqual(self.test_output_1, cp.calculate_dist_table_4(*self.test_input_1))
        self.assertEqual(self.test_output_2, cp.calculate_dist_table_4(*self.test_input_2))
        self.assertEqual(self.test_output_3, cp.calculate_dist_table_4(*self.test_input_3))


if __name__ == '__main__':
    unittest.main()
