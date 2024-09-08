"""
This is a demonstration of how the syncronize_folders function and logging work.

For the demonstration we will replicate the folder "demo_src_dir" and all its contents to "demo_repl_dir" every 20 seconds
for 10 cycles.
"""
import os.path
import time
import logging
import shutil
from app.synchronizer.synchronizer import synchronize_folders

if __name__ == '__main__':

    if os.path.isdir("demo_repl_dir"):
        shutil.rmtree("demo_repl_dir")

    if os.path.isfile("sync_log.txt"):
        os.remove("sync_log.txt")

    count = 0
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler("sync_log.txt"),
            logging.StreamHandler()
        ]
    )

    while count < 10:
        logging.info("Starting synchronization...")
        synchronize_folders("demo_src_dir", "demo_repl_dir")
        logging.info("Synchronization completed.")
        time.sleep(20)
        count += 1



