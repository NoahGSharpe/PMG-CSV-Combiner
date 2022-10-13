import unittest
import os


class TestCSVCombiner(unittest.TestCase):

    def test_Barn_Birds_Pets(self):
        os.system(
            "py Combine_CSVs.py ./Testing/Barnyard.csv ./Testing/Birds.csv ./Testing/Pets.csv > ./Testing/testCombined.csv")
        with open("./Testing/Barn_Birds_Pets.csv") as BBP, open("./Testing/testCombined.csv") as test:
            self.assertListEqual(list(BBP), list(test))

    def test_Barn_Birds(self):
        os.system(
            "py Combine_CSVs.py ./Testing/Barnyard.csv ./Testing/Birds.csv > ./Testing/testCombined.csv")
        with open("./Testing/Barn_Birds.csv") as BBP, open("./Testing/testCombined.csv") as test:
            self.assertListEqual(list(BBP), list(test))

    def test_Birds_Pets(self):
        os.system(
            "py Combine_CSVs.py ./Testing/Birds.csv ./Testing/Pets.csv > ./Testing/testCombined.csv")
        with open("./Testing/Birds_Pets.csv") as BBP, open("./Testing/testCombined.csv") as test:
            self.assertListEqual(list(BBP), list(test))


if __name__ == "__main__":
    unittest.main()
