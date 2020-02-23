# W Package

This is a simple example package. You can install this package to get weekday name by passing date(i.e. YY-MM-DDDD). 

## Instruction:

1. To download the repo project in the command line type "git clone https://github.com/cdchinmoy/pythonpackage.git" and enter.

2. Go to dist directory and type "pip install cmdpackage-0.0.7-py3-none-any.whl" to install the package

3. To display the result follow the below instruction:
    1. import example_pkg
    2. obj = example_pkg.Date_convert()
    3. day = obj.findDay('27-02-2020');
    4. print(day)

4. After passing date throuth the "findDay" function as a paramiter, you will get the weekday frequentry.  