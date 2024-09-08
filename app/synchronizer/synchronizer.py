import os
import shutil
import logging
from app.utils.calculate_md5 import calculate_md5

class DirectoryNotFoundError(Exception):
    """Exception raised when the source directory is not found."""
    pass

def create_directories(source: str, replica: str) -> None:
    """Create directories in replica that exist in source."""
    for dirpath, dirnames, _ in os.walk(source):
        replica_dirpath = dirpath.replace(source, replica, 1)
        for dirname in dirnames:
            replica_dirname = os.path.join(replica_dirpath, dirname)
            if not os.path.exists(replica_dirname):
                os.makedirs(replica_dirname)
                logging.info(f"Directory created: {replica_dirname}")

def copy_or_update_files(source: str, replica: str) -> None:
    """Copy or update files from source to replica."""
    for dirpath, _, filenames in os.walk(source):
        replica_dirpath = dirpath.replace(source, replica, 1)
        for filename in filenames:
            source_file = os.path.join(dirpath, filename)
            replica_file = os.path.join(replica_dirpath, filename)
            if not os.path.exists(replica_file) or calculate_md5(source_file) != calculate_md5(replica_file):
                shutil.copy2(source_file, replica_file)
                logging.info(f"File copied/updated: {replica_file}")

def remove_extra_files_and_directories(source: str, replica: str) -> None:
    """Remove files and directories from replica that don't exist in source."""
    for dirpath, _, filenames in os.walk(replica):
        source_dirpath = dirpath.replace(replica, source, 1)
        for filename in filenames:
            replica_file = os.path.join(dirpath, filename)
            source_file = os.path.join(source_dirpath, filename)
            if not os.path.exists(source_file):
                os.remove(replica_file)
                logging.info(f"File removed: {replica_file}")
        for dirname in os.listdir(dirpath):
            replica_dirname = os.path.join(dirpath, dirname)
            source_dirname = os.path.join(source_dirpath, dirname)
            if not os.path.exists(source_dirname):
                shutil.rmtree(replica_dirname)
                logging.info(f"Directory removed: {replica_dirname}")

def synchronize_folders(source: str, replica: str) -> None:
    """Synchronize contents of source folder to replica folder."""
    # Ensure source directory exists
    if not os.path.isdir(source):
        logging.info(f"Source folder does not exist '{source}'.")
        raise DirectoryNotFoundError(f"The source directory '{source}' does not exist.")

    # Create replica directory if it doesn't exist
    os.makedirs(replica, exist_ok=True)

    # Perform synchronization
    create_directories(source, replica)
    copy_or_update_files(source, replica)
    remove_extra_files_and_directories(source, replica)