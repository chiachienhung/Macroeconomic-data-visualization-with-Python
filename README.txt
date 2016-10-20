%% Readme.txt
%% for Python (v2.7.11 on win32)

Name:-         Macroeconomic data visualization with Python
Authors:-      C.C, Hung (lisa5432126@gmail.com) 
               X.Y, Lai  (laixiaoya96@163.com)
Date:-         September 24, 2016



(1) INTRODUCTION
----------------
This is the project which mainly based on the data visualization by using Python. 
The dataset we used are the macroeconomic data from IMF(International Monetary Fund) and Wikipedia.
The purpose we want to build this project is to let the people who have less knowledge on economics perspectives can easily understand the relationship among countries and have an access to get to know more on the country status by using different methods in our project.
¡iMacroeconomic data visualization with Python¡j is our project folder.
There are four python files in this folder: Country Profile and the Ranking.py, GeoMap.py, country trends and comparison.py, convert image to gif.py.
There are two folders in this folder: font (this includes 9 font styles), world_gdppercapita 2006-2015 (containing ten figures showing the GDP of the world), and result.
There is seven csv files in this folder: worlddata.csv, GDP.csv, CPI.csv, population.csv, employment.csv, Net_debt.csv, unemployment_rate.csv
There is one svg file in this folder: worldmap.svg
¡iFinal Paper¡j is the folder where we save our essay: Data visualization by using Python.pdf and the Manual.pdf

(2) REQUIRED SYSTEMS
--------------------
The programming language we use is Python. 
Download at least version 2.7.11 (See more on: https://www.python.org/downloads/).
You need to make sure the version you download is compatible with your environment (Windows, Linux, Mac IOS).
And also for text editor, you can download Pycharm (See more on: https://www.jetbrains.com/pycharm/download/).

(3) PACKAGE FILES
-----------------
Python have many useful packages and you can download the packages on PyPI website: https://pypi.python.org/pypi
The packages we use in this project are as following: 
-csv             %import and export format for spreadsheets and databases
-scipy           %scientific computing with a collection of packages
-pandas          %provide rich data structures for the efficiency of data working environment
-BeautifulSoup   %pull data out of HTML and XML files and do navigating, searching, and modifying on
-PIL             %provide powerful image processing and graphics capabilities
-svgwrite        %create SVG drawings
-svgutils        %an utility package that helps to edit and concatenate SVG files
-string          %contain a number of useful constants and classes on string
-matplotlib      %produce plots and other 2D data visualizations
-numpy           %scientific computing with a collection of packages
-PySide          %Python bindings for the Qt cross-platform application and UI framework
-os              %provide a portable way of using operating system dependent functionality
-shutil          %offer a number of high-level operations on files and collections of files
-Images2gif      %read and write animated gifs

There might be many versions of a single package. You need to make sure that the latest version really fit the computer environment(Windows, Linux, Mac IOS) and could be compatible with the version of the python you installed. Otherwise, you should choose the former version of the package instead of the latest version.
¡iCase1¡jIf you download the package in .whl file, you need to first open a console and cd to the folder where you save.
>>cd C:\some-packagepath
And use
>>pip install some-package.whl
If pip is not found in path, use
>>python -m pip install some-package.whl

¡iCase2¡jIf you download the package in .tar.gz or .zip file, you need to unpack the tar.gz file into a folder.
And then open a console and cd to the folder.
>>cd C:\some-packagepath
And use the following code to successfully install
>>python setup.py install

¡iCase3¡jIf you download the package in .exe file, you just need to run the .exe file and choose the compatible environment.


(4) USAGE  
----------------------------------------
See Manual.pdf in ¡iMacroeconomic data visualization with Python¡jfolder for full details.


(5) BUG REPORTING
-----------------
There might exist bug as soon as you start to compile.
If there are some problems running the .py file or you have any suggestion for improvement, 
please don't hesitate to contact us:
C.C, Hung (lisa5432126@gmail.com) 
X.Y, Lai  (laixiaoya96@163.com)
We will try our best to work on the better coding structure and features to improve our original version. 

(6) LICENSE
-----------
This project is an open source for free.
You can redistribute it and/or modify it under the terms of the Python License (See more on: https://www.python.org/download/releases/2.7/license/)

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

-----------------
END OF Readme.txt
-----------------


