import unittest
import os
import shutil
from unittest.mock import patch, MagicMock
from app.synchronizer.synchronizer import create_directories, copy_or_update_files, \
    remove_extra_files_and_directories, synchronize_folders, DirectoryNotFoundError


class TestSynchronizeFolders(unittest.TestCase):

    def setUp(self):
        """Set up temporary directories for testing."""
        self.source_dir = 'test_source'
        self.replica_dir = 'test_replica'
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.replica_dir, exist_ok=True)

        # Create a test file in source directory
        with open(os.path.join(self.source_dir, 'test_file.txt'), 'w') as f:
            f.write('Hello, world!')

    def tearDown(self):
        """Clean up temporary directories and files."""
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.replica_dir)

    def test_create_directories(self):
        """Test that directories are created correctly."""
        os.makedirs(os.path.join(self.source_dir, 'subdir'), exist_ok=True)
        create_directories(self.source_dir, self.replica_dir)
        self.assertTrue(os.path.exists(os.path.join(self.replica_dir, 'subdir')))

    @patch('app.synchronizer.synchronizer.calculate_md5')
    def test_copy_or_update_files(self, mock_calculate_md5):
        """Test that files are copied or updated correctly."""
        mock_calculate_md5.return_value = 'dummy_md5'
        copy_or_update_files(self.source_dir, self.replica_dir)
        self.assertTrue(os.path.exists(os.path.join(self.replica_dir, 'test_file.txt')))

    @patch('app.synchronizer.synchronizer.calculate_md5')
    @patch('app.synchronizer.synchronizer.shutil.copy2')
    def test_copy_or_update_files_fail(self, mock_copy2, mock_calculate_md5):
        """Test that copying files fails properly."""
        mock_calculate_md5.return_value = 'dummy_md5'
        mock_copy2.side_effect = IOError("Failed to copy")
        with self.assertRaises(IOError):
            copy_or_update_files(self.source_dir, self.replica_dir)

    def test_remove_extra_files_and_directories(self):
        """Test that extra files and directories are removed correctly."""
        os.makedirs(os.path.join(self.replica_dir, 'extra_dir'), exist_ok=True)
        with open(os.path.join(self.replica_dir, 'extra_file.txt'), 'w') as f:
            f.write('Extra file')
        remove_extra_files_and_directories(self.source_dir, self.replica_dir)
        self.assertFalse(os.path.exists(os.path.join(self.replica_dir, 'extra_dir')))
        self.assertFalse(os.path.exists(os.path.join(self.replica_dir, 'extra_file.txt')))

    def test_synchronize_folders(self):
        """Test the overall synchronization process."""
        synchronize_folders(self.source_dir, self.replica_dir)
        # Since the functions are mocked, checking the mocks is enough
        with patch('app.synchronizer.synchronizer.create_directories') as mock_create, \
                patch('app.synchronizer.synchronizer.copy_or_update_files') as mock_copy, \
                patch('app.synchronizer.synchronizer.remove_extra_files_and_directories') as mock_remove:
            synchronize_folders(self.source_dir, self.replica_dir)
            mock_create.assert_called_once_with(self.source_dir, self.replica_dir)
            mock_copy.assert_called_once_with(self.source_dir, self.replica_dir)
            mock_remove.assert_called_once_with(self.source_dir, self.replica_dir)

    def test_synchronize_folders_fail(self):
        """Test that the overall synchronization process handles failures."""
        with patch('app.synchronizer.synchronizer.create_directories') as mock_create, \
                patch('app.synchronizer.synchronizer.copy_or_update_files') as mock_copy, \
                patch('app.synchronizer.synchronizer.remove_extra_files_and_directories') as mock_remove:
            mock_create.side_effect = RuntimeError("Create directories failed")
            mock_copy.side_effect = RuntimeError("Copy files failed")
            mock_remove.side_effect = RuntimeError("Remove files/directories failed")

            with self.assertRaises(RuntimeError):
                synchronize_folders(self.source_dir, self.replica_dir)

    def test_synchronize_folders_source_not_found(self):
        """Test that the synchronization process raises an error if the source directory does not exist."""
        non_existent_dir = 'non_existent_source'
        with self.assertRaises(DirectoryNotFoundError):
            synchronize_folders(non_existent_dir, self.replica_dir)


if __name__ == '__main__':
    unittest.main(verbosity=2)
