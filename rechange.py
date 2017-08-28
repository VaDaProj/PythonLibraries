#WARNING: Make backup copy before you work with this module
#For change data in files with regular expressions

import re #Regular expressions


class ReChange:  #Main class for change data
    def __init__(self, file):
        global filename  #Name of change file
        filename = file

    def change(self,object ,change):
        """Change 'object' on 'change' in the file"""
        pattern = re.compile(object)  #Template of object for change
        with open(filename) as f_in:
            result = """"""  #In this variable will be write result
            for line in f_in:
                result += pattern.sub(change, line)  #Add line
            print(result)
        with open(filename, 'w') as f_out:
            f_out.write(result)  #Write the result in file

    def remove(self, object):
        """Remove 'object' from the file"""
        pattern = re.compile(object)  #Template of object for remove
        with open(filename) as f_in:
            result = """"""  #In this variable will be write result
            for line in f_in:
                result += pattern.sub('', line)  #Add line
            print(result)
        with open(filename, 'w') as f_out:
            f_out.write(result)  #Write the result in file

    def add(self, object, place):
        """Add 'object' in 'place' in the file"""
        pattern = re.compile(place)  #Template of place in wich will be add object
        with open(filename) as f_in:
            result = """"""  #In this variable will be write result
            for line in f_in:
                result += pattern.sub(place + object, line)  #Add line
            print(result)
        with open(filename, 'w') as f_out:
            f_out.write(result)  #Write result in the file


def main():  #Main function
    change = ReChange('changes.txt')



if __name__ == "__main__":
    main()
