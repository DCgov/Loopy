# Loopy

Loopy is the PCS data processing system. It is capable of preprocessing the PCS source files, extracting data from excel sheets, inserting data into CapTop database, and sending report emails. The figure below abstracts the structures of the Loopy system. 
![Image](https://raw.githubusercontent.com/DCgov/Loopy/master/System.png?token=ACaY9tmK1WtRhlzV05FzKG4ogG5j9cwFks5WgslkwA%3D%3D)

### Dependencies 

  - [Python 2.7]
  - [HTML.py] - Formatting html tables for email reports
  - [xlrd] - Parsing excel sheets

### Configurations

* Before running the scripts, make changes to the database connection file in ./Credentials 
* Run Loopy.py directly 

[Python 2.7]: <https://www.python.org/download/releases/2.7/>
[HTML.py]: <http://www.decalage.info/python/html>
[xlrd]: <https://pypi.python.org/pypi/xlrd>