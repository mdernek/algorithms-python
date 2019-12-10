import arraysamples
from arraysamples import find_all_pairs_in_array
import unittest

class FindAllPairsInArray_Test(unittest.TestCase):

    def test_sum_using_set_with_nonemptyarray(self):
        arr = [0, 14, 0, 4, 7, 8, 3, 5, 7]
        expectedResultTupleArray = [(7,4), (3,8), (7,4)]
        resultTupleArray = find_all_pairs_in_array.FindAllPairsInArray().sum_using_set(arr, 11)

        self.assertEqual(len(expectedResultTupleArray), len(resultTupleArray))

        for i in range(len(resultTupleArray)):
            self.assertEqual(expectedResultTupleArray[i], resultTupleArray[i])

    def test_sum_using_set_with_emptyarray(self):
        arr = []
        expectedResultTupleArray = []
        resultTupleArray = find_all_pairs_in_array.FindAllPairsInArray().sum_using_set(arr, 11)

        self.assertEqual(len(expectedResultTupleArray), len(resultTupleArray))

    def test_find_pairs_using_tw_pointers_with_nonemptyarray(self):
        arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
        expectedResultTupleArray = [(3,4), (5,2), (9,-2)]
        resultTupleArray = find_all_pairs_in_array.FindAllPairsInArray().sum_using_set(arr, 7)

        self.assertEqual(len(expectedResultTupleArray), len(resultTupleArray))

        for i in range(len(resultTupleArray)):
            self.assertEqual(expectedResultTupleArray[i], resultTupleArray[i])

    def test_find_pairs_using_tw_pointers_with_mptyarray(self):
        arr = []
        expectedResultTupleArray = []
        resultTupleArray = find_all_pairs_in_array.FindAllPairsInArray().sum_using_set(arr, 7)

        self.assertEqual(len(expectedResultTupleArray), len(resultTupleArray))


if __name__ == '__main__':
    unittest.main()