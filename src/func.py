"Importing the OS module for accessing system functionality"
"'remove' to delete the junk files from the system to free up space"
from os import remove
"FileDialogue Module for asking system, where to save the files or which folder to be selected"
from tkinter import filedialog
"Importing the Encrypt Module for encrypting and Decrypting te files"
from encrypt import Encrypt


class Functions():
    """
        This class contains all the External that are required for the proper functioning 
        of this program.
    """
    def getFilesAddress(self):
        """
            "getFileAddress" uses the python3-tkinter module's filedialog module to ask the
            opresting system to show a browse file window through which the user selects the
            various files that are used for encryption and decryption functions.
            This function returns the list of files addresses that are selcted by the user
        """
        filesAddress = filedialog.askopenfilenames(title='Choose a file')
        return filesAddress

    def analyseEncryption(self,filesAddress):
        """
            "analyseEncryption" function is used to ensure wheather the files that are going
            to be ecrypted by the user (i.e, selected by the user) for ecryption purposes,
            thus ensuring that all the files are not ecrypted already.
            NOTE: This function returns true if all the selected files don't have any ".crypt"
            extension else returns false.
        """
        for i in filesAddress:
            result=[]
            if i[len(i)-5:] != "crypt":
                result.append(0)
            else:
                result.append(1)
        if sum(result)== 0:
            return True
        else:
            return False

    def analyseDecryption(self,filesAddress):
        """
            "analyseDecryption" funtion is used to ensure wheather the files that are going
            to be decrypted by the user (i.e, selected by the user) for decryption purpose
            have same extension format i.e, ".crypt" in every file. This ensures the robustness
            of the program
            NOTE: This function returns true if all the files have the same extension format
            else return false.
        """
        for i in filesAddress:
            result=[]
            if i[len(i)-5:] == "crypt":
                result.append(0)
            else:
                result.append(1)
        if sum(result)==0:
            return True
        else :
            return False

    def analyseUser(self,filesAddress,userName):
        """
            "analyseUser" function is used to ensure wheather the files that are going
            to be decrypted by the user (i.e, selected by the user) for decryption purposes 
            are created by the same user. it check for "_userName" in every file.
            NOTE: This function returns true if all the selected files are created by the same user 
            else returns false.
        """
        for i in filesAddress:
            result = []
            if userName in i:
                result.append(0)
            else :
                result.append(1)
        if sum(result) == 0:
            return True
        else:
            return False

    def encryptFile(self,filesAddress,userName,userPassword):
        """
            "encryptFile" function encrypts all the files  one by one in a sequence and after 
            successfull encrypton it deletes all the temporary data from the hard-drive.
        """
        for eachFile in filesAddress:
            Encrypt().encryptdata(eachFile,userName,userPassword)
            remove(eachFile)

    def decryptFile(self,filesAddress,userName,userPassword):
        """
            "decryptFile" function decrypts all the files one by one in a sequence and after
            successfull decryption it deletes all the temporary data form the hard-drive.
        """
        for eachFile in filesAddress:
            Encrypt().decryptdata(eachFile,userName,userPassword)
            remove(eachFile)

    def verify(self,fileAddress,userName,userPassword):
        """
            "verify" function verifies that the password is correct or not for the user
            if the password matches with the previous password it returns "True" else the function
            returns "False" created by the same user 
        """
        eachFile = fileAddress[0]
        try:
            Encrypt().decryptdata(eachFile,userName,userPassword)
        except:
            return False
        else:
            path = eachFile[:len(eachFile)-(7+len(userName))]
            remove(path)
            return True
