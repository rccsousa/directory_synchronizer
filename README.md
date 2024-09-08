# Directory Synchronizer

A Python application for synchronizing the contents of two directories. This tool ensures that files and directories in the source folder are mirrored to the replica folder, including handling updates and removals.

## Features

- **Synchronize Directories:** Keeps the replica folder synchronized with the source folder.
- **Copy or Update Files:** Updates files in the replica folder if they are missing or different from the source.
- **Remove Extra Files:** Deletes files and directories from the replica that do not exist in the source.
- **Configurable Sync Interval:** Periodically synchronizes folders based on a user-defined interval.

## Installation

### Option 1 - Clone repository
1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/directory_synchronizer.git
    cd directory_synchronizer
    ```

2. **Install the package:**

    ```bash
    pip install .
    ```

### Option 2 - Pull repository using python pip

```bash
pip install git+https://github.com/rccsousa/directory_synchronizer
```

## Usage

You can run the synchronizer script directly or use the installed command-line tool.

### Running the Script

To start the synchronization, use the following command:

```bash
python app/main.py <source_folder> <replica_folder> [sync_interval] [log_file]
```
* `source_folder`: Path to the source directory.
* `replica_folder`: Path to the replica directory.
* `sync_interval` (optional): Synchronization interval in seconds (default is 60).
* `log_file` (optional): Path to the log file (default is log.txt).

### Using the Command-Line tool

After installation, you can use the sync-folders command:

```bash
sync-folders <source_folder> <replica_folder> [sync_interval] [log_file]
```

### Example
Synchronize the `/path/to/source` directory with `/path/to/replica` every 120 seconds and log to `sync.log`:

```bash
sync-folders /path/to/source /path/to/replica 120 sync.log
```

License
This project is licensed under the MIT License - see the LICENSE file for details.

### Author
Rui Sousa - [contact@ruisousa.me](mailto:contact@ruisousa.me) 
