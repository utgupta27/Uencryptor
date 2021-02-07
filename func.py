import os
from tkinter import filedialog
from encrypt import Encrypt


class Functions():

    def getFilesAddress(self):
        filesAddress = filedialog.askopenfilenames(title='Choose a file')
        return filesAddress

    def analyseEncryption(self,filesAddress):
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
        for eachFile in filesAddress:
            Encrypt().encryptdata(eachFile,userName,userPassword)
            os.remove(eachFile)

    def decryptFile(self,filesAddress,userName,userPassword):
        for eachFile in filesAddress:
            Encrypt().decryptdata(eachFile,userName,userPassword)
            os.remove(eachFile)

    def verify(self,fileAddress,userName,userPassword):
        eachFile = fileAddress[0]
        try:
            Encrypt().decryptdata(eachFile,userName,userPassword)
        except:
            return False
        else:
            path = eachFile[:len(eachFile)-(7+len(userName))]
            os.remove(path)
            return True


if __name__ == "__main__":
    pass