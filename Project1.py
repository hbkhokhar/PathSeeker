# Hassan Khokhar 33778724 and Lucas Argueza 95528693. Lab 10. Project 1.

from pathlib import Path
import os
import shutil
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.0225)

def WelcomeBanner() -> str:
    delay_print('\n**********************************************\n')
    delay_print('******  WELCOME TO FILEPATH PROGRAM!!!  ******\n')
    delay_print('**********************************************\n')
    time.sleep(1.5)
    print()
    print('Enter the file path')
    print('-------------------')
    
######################################
##    FIRST LINE OF INPUT (PATH)    ##
######################################

def RecursiveSearch(path: str) -> list:
    ''' Takes a string representing a path and recursively searches through the
    directories returning a list of all files/subdirectories under it '''

    ListofPaths = []                                                               # empty list where paths are appended to
    try:
        d = Path(path)                                                             # string is converted into a path
        if d.is_dir() and d.exists():                                              # Checks if path is directory and it exists
            List1 = list(d.iterdir())
            if len(List1) == 0:
                raise exception
            else:
                for x in d.iterdir():                                                  # Iterates through paths in directory
                    if x.is_dir():                               
                        ListofPaths.extend(RecursiveSearch(x))                         # Repeats process if path is sub-directory, hence, recursively going deeper.              
                    elif x.is_file():                                                  # Files are appended to the final list
                        ListofPaths.append(x)

                return ListofPaths                                                     # returns the list of paths
    except:
        print('ERROR')                                                             # Raises an 'ERROR' if the input given is not a valid path



######################################
## SECOND LINE OF INPUT ( N, E, S ) ##
######################################

def MatchingName(s: str, L: list) -> list:
    ''' Takes a string representing a filename and a given list of
    path objects returning a new refined list of matches in filename '''

    Matches = []                                                                   # empty list where paths with matching name are appended to
    for path in L:                                                                 # iterates through the input (i.e. given list of paths)
        StringPath = str(path)                                                     # Converts each path in the list to a string
        PC = "\\"
        Mac = "/"
        if PC in StringPath:                                                       # If the path is from Windows or Mac it performs the appropriate action
            DividedPaths = StringPath.split('\\')                                  # Next lines split the string so that only the filename is left
            FileName = DividedPaths[-1]                           
            if s == FileName:
                Matches.append(path)                                               # if the string matches the filename it is appended to the list
        elif Mac in StringPath:
            DividedPaths = StringPath.split('/')                                
            FileName = DividedPaths[-1]
            if s == FileName:
                Matches.append(path)        
    return Matches                                                                 # returns the list


        
def MatchingExtension(s: str, L: list) -> list:
    ''' Takes a string representing a file extension and a given list of
    path objects returning a new refined list of matches in file extension '''

    Matches = []                                                                   # empty list where paths with matching extension are appended to                                       
    for path in L:                                                                 # iterates through the input (i.e. given list of paths)
        StringPath = str(path)                                                     # Converts each path in the list to a string
        DividedPaths = StringPath.split('/')                                       # Next two lines split the string so that the ending piece of the path is left     
        FileExt = DividedPaths[-1]                       
        if s == FileExt[-(len(s)):]:                        
            Matches.append(path)                                                   # if the string matches the file extension it is appended to the list
    return Matches                                                                 # returns the list



def FileSize(s: str, L: list) -> list:
    ''' Takes a string respresenting a size of a file in terms of bytes and a given list of path objects and
    return a list of matches whose size is greater than or equal to the given string amount '''

    Matches = []                                                                    # empty list where paths with matching or greater size are appended to
    try:
        StringToInt = int(s)                                                        # Converts the given string into an integer
        for path in L:                                                              # iterates through the input (i.e. given list of paths)
            StringPath = str(path)                                                  # Converts each path to a string
            Size = os.path.getsize(StringPath)                                      # Function gets the size of the file in terms of bytes
            if Size >= StringToInt:                               
                Matches.append(path)                                                # if the file size is greater than or equal to given int it is appended to the list
        return Matches                                                              # returns the list
    except ValueError:
        return Matches                                                              # ValueError placed so if s is not inherently an int it can catch exception
                                                                                    # below in user_interface2() [i.e. it stays an empty list]


########################################
## THIRD LINE OF INPUT ( P, F, D, T ) ##
########################################

def PrintPath(L: list) -> list:
    ''' Takes a refined list of paths matched by name, extension, or size and returns each
    path printed out top-down on the console '''
    
    for path in L:                                                                  # iterates through the input (i.e. given list of paths)                 
        print(path)                                                                 # Prints each path in the list

        

def ReadFirstLine(L: list) -> list:
    ''' Takes a refined list of paths matched by name, extension, or size and returns each
    path printed out top-down along with the first line of the file assuming it's text '''

    for path in L:                                                                  # iterates through the input (i.e. given list of paths)
        print(path)                                                                 # Prints each path in the list
        f = open(str(path), 'r')                                                    # These lines open the file and read the first line
        x = f.readlines()
        for i in x:
            print(i)                                                                  # These lines print the first line and close the file
        f.close()



def DuplicateFile(L: list) -> list:
    ''' Takes a refined lists of paths matched by name, extension, or size and returns each
    path printed out top-down along with the path of duplicated file in the same directory '''
    
    for path in L:                                                                  # iterates through the input (i.e. given list of paths)
        print(path)                                                                 # Prints each path in the list
        StringPath = str(path)                                                      # Converts each path in the list to a string                  
        StringPath2 = StringPath + '.dup'                                           # Appends .dup to the filename to signify that the path is a duplicate
        CopiedPath = shutil.copy2(StringPath, StringPath2)                          # Function copies the file given to the same directory returning a new path
        print(CopiedPath)                                                           # Prints each duplicate path in the list



def TouchFile(L: list) -> list:
    ''' Takes a refined lists of paths matched by name, extension, or size and returns each
    path printed out top-down along with the modified timestamp of the file to be the current date/time '''

    for path in L:                                                                  # iterates through the input (i.e. given list of paths)
        print(path)                                                                 # Prints each path in the list
        StringPath = str(path)                                                      # Converts each path in the list to a string
        path.touch(StringPath)                                                      # 'Touches' each file and modifies its timestamp
        print("Modified Timestamp : ", time.ctime(os.path.getmtime(StringPath)))    # Prints out the modified timestamp of the file to the console


def RunFile(L: list):
    ''' Takes a refined lists of paths matched by name, extension, or size and executes the given file '''
    for path in L:
        StringPath = str(path)
        os.system(StringPath)

###########################################
## User Interfaces for Program Execution ##
###########################################

def user_interface() -> list:
    ''' Repeatedly asks the user to specify a path until the proper paramter is given.
    When it is, it returns a refined list with all the paths under it unless the path could not be
    read, in which case a brief error message is displayed instead. '''
    
    RefinedList = []
    WelcomeBanner()
    while True:
        file_path = input('').strip()                                               # Input is stripped and read in the following lines

        if file_path == '':                                                         # If the input is an empty string then the program breaks
            break

        try:
            RefinedList.extend(RecursiveSearch(file_path))                          # Calls to the function RecursiveSearch() which gives list of paths
            return RefinedList                                                      # list of paths are appended to the refined list and returned
        except:
            print('ERROR')                                                          # Exception is raised when function does not work properly and starts over



def user_interface2(List1: list) -> list:
    ''' Takes the list of refined paths from user_interface() and executes the second line of input.
    Repeatedly asks the user to specify a special characteristic until the proper paramter is given.
    When it is, it returns a new matched list with all the paths unless the special character was wrong,
    in which case a brief error message is displayed instead. '''

    RefinedList2 = []
    while True:
        SecondInput = input('').strip()                                             # Input is stripped and read in the following lines

        if SecondInput == '':                                                       # If the input is an empty string then the program breaks
            break

        if SecondInput[0] == 'N':                                                   # If the first character of the string is 'N' then this block executes
            Result = MatchingName(SecondInput[2:], List1)                           # Calls to the function MatchingName() which gives list of paths with same name
            RefinedList2.extend(Result)
            if len(RefinedList2) != 0:
                return RefinedList2                                                 # This result is then extended into the refined list and returned if it not an empty list
            else:
                print('ERROR')

        elif SecondInput[0] == 'E':                                                 # If the first character of the string is 'E' then this block executes
            Result2 = MatchingExtension(SecondInput[2:], List1)                     # Calls to the funct. MatchingExtension() which gives list of paths with same ext.
            RefinedList2.extend(Result2)                                            # This result is then extended into the refined list
            if len(RefinedList2) != 0:                                              # If the refined list is not an empty list it is returned...
                return RefinedList2
            else:
                print('ERROR')                                                      # ...otherwise an 'ERROR' is printed
        
        elif SecondInput[0] == 'S':                                                 # If the first character of the string is 'S' then this block executes
            Result3 = FileSize(SecondInput[2:], List1)                              # Calls to the func. FileSize() which gives paths with same file size or greater
            RefinedList2.extend(Result3)                                            # This result is then extended into the refined list
            if len(RefinedList2) != 0:                                              # If the refined list is not an empty list it is returned...
                return RefinedList2
            else:
                print('ERROR')                                                      # ...otherwise an 'ERROR' is printed
        else:
            print('ERROR')                                                          # If an invalid special character is entered an 'ERROR' will be printed
                                                                                    # and start over.



def user_interface3(List2: list) -> None:
    ''' Takes the list of refined paths from user_interface2() and executes the third line of input.
    Repeatedly asks the user to specify a special characteristic until the proper paramter is given.
    When it is, it performs an action specified by the program unless the special character was wrong,
    in which case a brief error message is displayed instead. '''

    while True:
        ThirdInput = input('').strip()                                              # Input is stripped and read in the following lines.

        if ThirdInput == '':                                                        # If the input is an empty string then the program breaks.
            break


        if ThirdInput[0] == 'P':                                                    # If the first character of the string is 'P' then this block executes.
            Result = PrintPath(List2)                                               # Calls to the function PrintPath() which prints a list of paths from the given
                                                                                    # input. This result is then printed in this form.

        elif ThirdInput[0] == 'F':                                                  # If the first character of the string is 'F' then this block executes.
            Result = ReadFirstLine(List2)                                           # Calls to the function ReadFirstLine() which prints the paths from the
                                                                                    # input and its first line. This result is then printed in this form.

        elif ThirdInput[0] == 'D':                                                  # If the first character of the string is 'D' then this block executes.
            Result = DuplicateFile(List2)                                           # Calls to the function DuplicateFile() which prints the paths from the
                                                                                    # input and their duplicate paths. This result is then printed in this form.

        elif ThirdInput[0] == 'T':                                                  # If the first character of the string is 'T' then this block executes.
            Result = TouchFile(List2)                                               # Calls to the function TouchFile() which prints the paths from the

        elif ThirdInput[0] == 'R':
            Result = RunFile(List2)
                                                                                    # input and modifies timestamp to be the current time. 
        else:                                                                       # This result is then printed in this form.
            print('ERROR')                                                         
                                                                                    # If an invalid special character is entered an 'ERROR' will be printed
                                                                                    # and start over.


###########################################
##      Main Module for the Program      ##
###########################################

if __name__ == '__main__':
    list1 = user_interface()                                                        # Excecution of user_interface() is stored in list1 (output is list)
    list2 = user_interface2(list1)                                                  # Output from user_interface() is taken as input for user_interface2()
    user_interface3(list2)                                                          # Output from user_interface2() is taken as input for user_inferface3()

    
