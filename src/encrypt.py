"Install pyAesCrypt module using pip-command"
import pyAesCrypt
import os

class Encrypt():
    """
        Contains encryptdata() & decryptdata() functions that uses AES256-CBC encryption
        algorithm to encrypt and decrypt Files/Databases where the buffer size if 64Kb.
    """
    def __init__(self):
        """
            This class constructor initialises the buffersize instances of the parent class.
        """
        self.bufferSize = 64 * 1024

    def encryptdata(self,fileName,userName,userPassword):
        """
            This function takes the userName and userPassword to encrypt the database/file
            and creates another new file having same name with ".crypt" extension.
            REMEMBER - This function dosen't affect the original file. It just creates an 
                        encrypted file using the original. You Manually need to delete the
                        original file after successfull encryption.
        """
        pyAesCrypt.encryptFile(fileName ,fileName + "_" +userName+".crypt",userPassword,self.bufferSize)
    
    def decryptdata(self,fileName,userName,userPassword):
        """
            This function takes the userName and userPassword to decrypt the database/file
            and creates another new file having same name without ".crypt" extension.
            REMEMBER - This function dosen't affect the original(.crypt) file. It just creates an 
                        encrypted file using the original. You Manually need to delete the
                        original file after successfull encryption.
        """
        name = fileName[:len(fileName)-(7+len(userName))]
        pyAesCrypt.decryptFile(fileName ,name,userPassword,self.bufferSize)


