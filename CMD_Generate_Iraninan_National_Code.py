"""Python CMD program for generating valid Iranian national codes and saving them in a .txt file
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

import random
from datetime import datetime

def main():
     """
     main function for interacting with the user
     """
     while(True):
     # while loop to keep the program running

        print("Please enter the number of Iranian national codes you want to be created :")
        input_Number = int(input())
        # reading the next integer number

        result = storage_In_Array(input_Number)
        # passing the input_Number to storage_In_Array function for generating the required number of Iranian national codes 
        # and storing the results in result variable

        non_Duplicated_Result = array_Duplicate_Remover(result)
        # passing the generated Iranian national codes to the array_Duplicate_Remover function for removing dublicated Iranian national codes
        # and storing the results in non_Duplicated_Result variable

        print("Your Iranian national codes :")
        array_Printer(non_Duplicated_Result)
        write_Array_To_TXT_File(non_Duplicated_Result)
        # passing the non_Duplicated_Result to write_Array_To_TXT_File for saving the generated non duplicated Iranian national codes in a .txt file

        print("**************************************************************************")


def integer_To_Digits_Splitter(number):
    """
    function for splitting the digits of integer numbers.
    @param number: a number
    @type number: integer
    @return: array_Of_Digits
    @rtype: array of integers
    @examples: 
     >>> integer_To_Digits_Splitter(0)
         [0]
     >>> integer_To_Digits_Splitter(123)
         [3, 2, 1]   
    """
    string_Number = (str(number))
    # converting number to string to be able to use len() function

    number_Of_Digits = len(string_Number)
    # usung len() function to calculate number of digits

    array_Of_Digits = []
    # initializing an empty array to store digits in

    for i in range(number_Of_Digits):
        a = number//10
        reminder = number - a*10
        number = a
        array_Of_Digits.append(reminder)
        # appending the last digit to array_Of_Digits

    return array_Of_Digits


def Iranian_National_Code_Generator():
    """
    function for generating Iranian national code.
    @return: Iranian_National_Code
    @rtype: String
    @examples: 
     >>> Iranian_National_Code_Generator()
         4191907921
     >>> Iranian_National_Code_Generator()
         8448518853
    """
    city_Code = random.randint(1, 999)
    if city_Code <= 9:
        city_Code = "00" + str(city_Code)

    elif city_Code <= 99:
        city_Code = "0" + str(city_Code)

    else:
        city_Code = str(city_Code)
    # checking whether the city_Code has 3 digits or not, if not adding enough zeros so that it will have 3 digits

    unique_Code = random.randint(0, 999999)
    
    if unique_Code <= 9:
        unique_Code = "00000" + str(unique_Code)

    elif unique_Code <= 99:
        unique_Code = "0000" + str(unique_Code)

    elif unique_Code <= 999:
        unique_Code = "000" + str(unique_Code)

    elif unique_Code <= 9999:
        unique_Code = "00" + str(unique_Code)

    elif unique_Code <= 99999:
        unique_Code = "0" + str(unique_Code)

    else:
        unique_Code = str(unique_Code)
    # checking whether the unique_Code has 6 digits or not, if not adding enough zeros so that it will have 6 digits
    
    first_Part = int(city_Code + unique_Code)

    code_Lenght = len(str(first_Part))
    first_Part_Integer = int(first_Part)
    first_Part_Digits = integer_To_Digits_Splitter(first_Part_Integer)
    # passing the first_Part_Integer to the integer_To_Digits_Splitter function for splitting it's digits 
    # and storing the result in the first_Part_Digits variable

    first_Part_Digits_Lenght = len(first_Part_Digits)
    sum = 0
    for i in range(2, first_Part_Digits_Lenght + 2):
        sum += i*first_Part_Digits[i - 2]

    remind = sum%11
    if remind >= 2:
        remind = 11 - remind
    # algorithm for setting the final(10th) digit of Iranian_National_Code

    Iranian_National_Code = str(first_Part) + str(remind)

    if len(Iranian_National_Code) == 8:
        Iranian_National_Code = "00" + Iranian_National_Code

    elif len(Iranian_National_Code) == 9:
        Iranian_National_Code = "0" + Iranian_National_Code
    # checking whether the Iranian_National_Code has 10 digits or not, if not adding enough zeros so that it will have 10 digits

    return Iranian_National_Code


def storage_In_Array(number):
    """
    function for calling Iranian_National_Code_Generator and storing the results into an array.
    @param number: number of calling the Iranian_National_Code_Generator.
    @type number: integer
    @return: array_Of_Digits
    @rtype: array of integers
    @examples: 
     >>> storage_In_Array(0)
         []
     >>> storage_In_Array(3)
         [1962866998, 7145759802, 5994791040]   
    """
    array_Of_Iranian_National_Codes = []
    # initializing an empty array

    for i in range(0, number):
        array_Of_Iranian_National_Codes.append(Iranian_National_Code_Generator())

    return array_Of_Iranian_National_Codes


def array_Duplicate_Remover(array):
    """
    function removing dublicate elemnts in array.
    @param array: an array of elements
    @type array: generic
    @return: uniqe_Array
    @rtype: array of elements
    @examples: 
         array_1 = []
         array_2 = [3, 5, 3, 6]
     >>> array_Duplicate_Remover(array_1)
         []
     >>> array_Duplicate_Remover(array_2)
         [3, 5, 6]   
    """
    unique_Array = []
    for item in array:
        if item not in unique_Array:
            unique_Array.append(item)

    return unique_Array


def array_Printer(array):
    """
    function for printing each array element in a line.
    @param array: an array of elements.
    @type array: anything like integer, double and string.
    @examples: 
         array_1 = []
         array_2 = [1, 2, 3]
     >>> array_Printer(array_1)
          
     >>> array_Printer(array_2)
         1
         2
         3
    """
    for element in array:
        print(element)


def write_Array_To_TXT_File(array):
    """
    function for saving each element of the passed array in a line into a .txt file. 
    @param array: an array of elements.
    @type array: anything like integer, double and string.
    """
    file_Name = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    # naming each file by current time, so that there will not be 2 files with the same name.

    file_Name_Format = str(file_Name) + ".txt"
    f = open(file_Name_Format, "a")
    f.write("Your Iranian national codes :")
    f.write('\n')

    for element in array:
        f.write(element)
        f.write('\n')
        
    f.close()


if __name__ == '__main__':
    main()
    # run the main function after executing this file