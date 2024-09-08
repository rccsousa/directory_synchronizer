"""
Simple script to copy all files from one directory to another and maintain them syncronized.

#TODO - Add use-cases and exceptions for when there are no permissions to edit/copy files
#TODO - Add GUI?

"""

import time
import argparse
import logging

from app.synchronizer.synchronizer import synchronize_folders
from app.utils.get_unique_filename import get_unique_filename

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Synchronize two folders.")

    parser.add_argument("source_folder",
                        help="Path to the source folder")

    parser.add_argument("replica_folder",
                        help="Path to the replica folder")

    parser.add_argument("sync_interval",
                        type=int,
                        help="Synchronization interval in seconds. Default 60.",
                        default=60,
                        nargs="?")

    parser.add_argument("log_file",
                        help="Path to the log file",
                        default="log.txt",
                        nargs="?")

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler(get_unique_filename(args.log_file)),
            logging.StreamHandler()
        ]
    )

    # Main loop to synchronize folders periodically
    while True:
        logging.info("Starting synchronization...")
        synchronize_folders(args.source_folder, args.replica_folder)
        logging.info("Synchronization completed.")
        time.sleep(args.sync_interval)

if __name__ == "__main__":
    main()
