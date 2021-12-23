*AirBnB clone*
MySQL
=========

Tasks|Done|Pending|Desc.
-----| [] | [] |--------
 [x]0| [x] | [] | fork
 []1 | [] | [x] | UnitTesting idx #1
 [x]2 | [x] | [] |...
 [x]3 | [x] | [] |...
 [x]4 | [x] | [] |...
 []5 | [] | [x] |...
 []6 | [] | [x] |...
 []7 | [] | [x] |...
 []8 | [] | [x] |...
 []9 | [] | [x] |...
 []10| [] | x[] | DBStorage - Amenity... and BOOM!

***Background Context***
> Environment variables will be your best friend for this project!

* `HBNB_ENV`: running environment. It can be *“dev”* or *“test”* for the moment (“production” soon!)
* `HBNB_MYSQL_USER`: the **username** of your MySQL
* `HBNB_MYSQL_PWD`: the **password** of your MySQL
* `HBNB_MYSQL_HOST`: the **hostname** of your MySQL
* `HBNB_MYSQL_DB`: the **database name** of your MySQL
* `HBNB_TYPE_STORAGE`: the **type of storage** used. It can be ***“file”*** (using `FileStorage`) or `db` (using `DBStorage`)

Learning Objectives
--------------------
***General***
1. What is Unit testing and how to implement it in a large project
2. What is \*args and how to use it
3. What is \*\*kwargs and how to use it
4. How to handle named arguments in a function
5. How to create a MySQL database
6. How to create a MySQL user and grant it privileges
7. What ORM means
8. How to map a Python Class to a MySQL table
9. How to handle 2 different storage engines with the same codebase
10. How to use environment variables
11. File Imports

## Requirements

***Python Scripts***
```
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
```

***Python Unit Tests***
```
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge cases
```

***SQL Scripts***
```
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
Your files will be executed with SQLAlchemy version 1.4.x
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
```

1. What is Unit testing and how to implement it in a large project
------------------------------------------------------------------

Version Check|[]
Connecting|[]
Declare Mapping|[]
Create Schema|[]
Create an Instance of Mapped Class|[]
Create Session|[]
Add/Update Objects|[]
Textual SQL|[]



2. What is \*args and how to use it
----------------------------------------

3. What is \*\*kwargs and how to use it
----------------------------------------

4. How to handle named arguments in a function
-----------------------------------------------

5. How to create a MySQL database
---------------------------------

6. How to create a MySQL user and grant it privileges
------------------------------------------------------

## 7. What ORM means
------------------
<p>
The SQLAlchemy *"**O**bject **R**elational **M**apper"*:

```
presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. It includes a system that transparently synchronizes all changes in state between objects and their related rows, called a unit of work, as well as a system for expressing database queries in terms of the user defined classes and their defined relationships between each other.
```

add attributes for SQLAlchemy:
they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)
</p>

ref:

* [Mapper Config](Mapper Configuration)
* [Relationship Configuration](https://docs.sqlalchemy.org/en/13/orm/relationships.html)
* [ORM Configuration](https://docs.sqlalchemy.org/en/13/index.html#sqlalchemy-orm)
* [SQLAlchemy ORM: Decalrative Table](https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#declarative-table)

## 8. How to map a Python Class to a MySQL table
----------------------------------------------

The DBStorage- States & Cities:
<p>
All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.

</p>

* Separate mapping and class design
  ```
  The ORM standardizes on a "Declarative" configurational system that allows construction of user-defined classes inline with the table metadata they map to, in the same way most other object-relational tools provide. However this system is totally optional - at its core, the ORM considers the user-defined class, the associated table metadata, and the mapping of the two to be entirely separate. Through the use of the mapper() function, any arbitrary Python class can be mapped to a database table or view. Mapped classes also retain serializability (pickling) for usage in various caching systems.
  ```
* Self-referential Object Mappings
```
Self-referential mappings are supported by the ORM. Adjacency list structures can be created, saved, and deleted with proper cascading, with no code overhead beyond that of non-self-referential structures. Loading of self-referential structures of any depth can be tuned to load collections recursively via a single statement with a series of joins (i.e. a joinedload), or via multiple statements where each loads the full set of records at a distinct level of depth (i.e. subqueryload). Persistence with tables that have mutually-dependent foreign key pairs (i.e. "many x"/"one particular x") are also supported natively using the "post update" feature.
```
* Inheritance Mapping
```
Explicit support is available for single-table, concrete-table, and joined table inheritance. Polymorphic loading (that is, a query that returns objects of multiple descendant types) is supported for all three styles. The loading of each may be optimized such that only one round trip is used to fully load a polymorphic result set.
```

###### Some other key features of SQLAlchemy at a glance: [here](https://www.sqlalchemy.org/features.html)



9. How to handle 2 different storage engines with the same codebase
--------------------------------------------------------------------

10. How to use environment variables
--------------------------------------

`os.getenvb(key, default=None)`
Return the value of the environment variable key if it exists, or default if it doesn’t. key, default and the result are bytes.

getenvb() is only available if supports_bytes_environ is True.

## 11. details from modules & Tasks
---------------------------

|**Modules**|**File sys Imports**|**Ref.**|
|:----------|:------------------:|-------:|
|||[File and Directory Access](https://docs.python.org/3/library/filesys.html#file-and-directory-access)|
|db_storage.py| os.getenvb(key, default=None)|#10|


Resources
=============
***Read or watch:***

* [cmd module](https://docs.python.org/3/library/cmd.html)
packages concept page
* [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
  * [python UnitTesting Doc](https://docs.python.org/3/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
  * [Add attributes for SQLAlchemy](https://docs.sqlalchemy.org/en/14/core/type_basics.html)
  * [Declarative Table](https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#declarative-table)
  * [SQLAlchemy Philosophy](SQLALCHEMY'S PHILOSOPHY)
  * [Unit of Work](https://martinfowler.com/eaaCatalog/unitOfWork.html)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [AirBnB clone - ORM](https://www.youtube.com/watch?v=jeJwRB33YNg) *( Youtube Video)*


Commenting SQL files:
```
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
