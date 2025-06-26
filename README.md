# codex2

This repository contains a simple Python script that demonstrates how to store
information both in a text file and in a MySQL database.

## Requirements

- Python 3
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- A running MySQL server

Install the Python dependency with:

```bash
pip install mysql-connector-python
```

Make sure your MySQL server is running and adjust the connection settings in
`info_storage.py` if necessary.

## Usage

Run the script and follow the prompts to enter information. Each entry is
appended to `info.txt` and inserted into the `info_db.entries` table.

```bash
python info_storage.py
```

After each entry, the script prints the current contents stored in MySQL.
