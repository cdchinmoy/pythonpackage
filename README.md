# Example Package

This is a simple example package. You can use to get weekday by passing date. 

## Instruction:

1. To download the repo project in the command line type "git clone https://github.com/cdchinmoy/pythonpackage.git" and enter.

2. Go to dist directory and type "pip install cmdpackage-0.0.7-py3-none-any.whl" to install the package

3. To display the result follow the below instruction:
    import example_pkg
    obj = example_pkg.Date_convert()
    day = obj.findDay('27-02-2020');
    print(day)

4. Passing date throuth the "findDay" function you will get the weekday frequentry.  