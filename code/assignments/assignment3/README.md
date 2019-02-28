# ASSIGNMENT 3

## Directions

Create a database, clear the screen and write temperatures to database using SQLite3, by modifying the blinkTemp.py script.

### Creating a database

1. Create a New Directory called log under the assignment folder.

```bash
mkdir log
```
The reason for creating a subdirectory is simple. It enables the end user to keep their data organized.

2. Switch to log directory and create a new .db file using "touch".

```bash
cd log
touch tempLog.db
```
If you create the database ahead of time, when you are adjusting it in the SQLite console session (next step) you can just tab it in, avoiding any mistakes and also making the experience slightly less frustrating. I am real lazy so this helps.

3. Start a SQLite3 console session.
```bash
sqlite3
```
This is the part where we set up the database.

4. Create table.

**NOTE**: Due to formatting related nonsense, text is ideal for both the date and temp fields.

```bash
sqlite3> CREATE TABLE tempRecord(Date TEXT, Temp TEXT);
```
Now that the tables are created, you can import previous tables as well as add new records.

5. (OPTIONAL) Import previous data from a .CSV file.

If you have data that you have previously saved inside a CSV (Comma Separated Values) files, you can import it using the following method.

```bash
sqlite> .mode csv
sqlite> .header on
sqlite> .import tempRecord.csv tempRecord.
```
In the case of this assignment I had some data stored in a CSV file prior to creating the sqlite3 database, so I figured it would be a good idea to import it into the database for simplicity's sake.
I also decided to select everything inside to verify that the data had been successfully imported.

```bash
sqlite> SELECT * FROM tempRecord;
```

6. Save the table into the .db file

```bash
sqlite> .save tempLog.db
```
This will enable us to use the database inside of the python script.

