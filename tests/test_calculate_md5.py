import unittest
import hashlib
import os

from app.utils.calculate_md5 import calculate_md5


class TestCalculateMD5(unittest.TestCase):

    def setUp(self):
        """Set up a temporary file for testing."""
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('Hello, world!')

    def tearDown(self):
        """Remove the temporary file after testing."""
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)

    def test_md5_calculation(self):
        """Test that the MD5 hash is calculated correctly."""
        expected_md5 = hashlib.md5(b'Hello, world!').hexdigest()
        result_md5 = calculate_md5(self.test_file)
        self.assertEqual(result_md5, expected_md5)


if __name__ == '__main__':
    unittest.main()
