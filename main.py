from tkinter import *
from tkinter import ttk
from func import Functions


class Driver():

    # def updateProgressBar(self,value):
    #     self.progressBar['value'] = value

    def getAddress(self):
        self.filesAddress = Functions().getFilesAddress()
        self.displaySelectedFiles.config(text = "")
        self.root.update()
  
        displayFrame1 =Frame(self.root)
        for i in range(len(self.filesAddress)):
            Label(displayFrame1,text=self.filesAddress[i]).grid(column = 0, row = i+1)
            self.root.update()
        displayFrame1.grid(column = 0 , row = 3)


    def doEnc(self):
        if self.userPwd.get() == self.confirmUserPwd.get():
            pwdMatched = Label(self.confirmFrame,text="Password Matched",font=('calibri',8),bg='green')
            pwdMatched.grid(column = 0, row=0 )
            self.root.update()

            # Encrypt Files here and Delete the old file
            Functions().encryptFile(self.filesAddress,self.userName.get(),self.userPwd.get())
            print("Files Encrypted Syccessfully")
            displaySuccess= Label(self.confirmFrame,text='Encryption Successfull',font=('calibri',20,'bold'),bg='green',foreground='white')
            displaySuccess.grid(column = 0, row= 2)
            self.root.update()
    
        else:
            pwdMatched = Label(self.confirmFrame,text="Password Not Matched",font=('calibri',8),bg='red')
            pwdMatched.grid(column = 0, row=0 )
            self.root.update()

    def doDec(self):
        if Functions().verify(self.filesAddress,self.userName.get(),self.userPwd.get()) == True:
            pwdMatched = Label(self.confirmFrame,text="Password Matched",font=('calibri',8),bg='green')
            pwdMatched.grid(column = 0, row=0 )
            self.root.update()

            # Decrypt Files here and delete the old ones
            Functions().decryptFile(self.filesAddress,self.userName.get(),self.userPwd.get())
            # progressDisplay.config(text= str(percent) + "%",font= ("calibri",12,"bold"),bg='yellow')
            displaySuccess= Label(self.confirmFrame,text='Decryption Successfull',font=('calibri',20,'bold'),bg='green',foreground='white')
            displaySuccess.grid(column = 0, row= 2)
            
            print("Files Decrypted Successfully")
            self.root.update()

        else:
            pwdMatched = Label(self.confirmFrame,text="Incorrect Password",font=('calibri',8),bg='red')
            pwdMatched.grid(column = 0, row=0 )
            self.root.update()

        

    def checkEnc(self):
        if Functions().analyseEncryption(self.filesAddress) == True:
            self.displaySelectedFiles.config(text = "Files Can be Encrypted",bg = "light green" ,font=('calibri',12,'bold'))
            userIDFrame = Frame(self.root)
            self.root.update()
        
            askIDLable = Label(userIDFrame,text = " Enter Your Username:",pady=10,font=('calibri',12,'bold'))
            askIDLable.grid(column =0 , row = 0)
            self.root.update()
            self.userName = StringVar()
            userNameEntry = Entry(userIDFrame,textvariable = self.userName,width = 23)
            userNameEntry.grid(column =1 , row = 0)
            self.root.update()

            userIDFrame.grid(column=0, row=6)


            self.root.update()

            askPwdFrame =  Frame(self.root)

            askPwdLable = Label(askPwdFrame,text = " Enter Your Password:",pady=10,font=('calibri',12,'bold'))
            askPwdLable.grid(column =0 , row = 1)
            self.root.update()
            self.userPwd=StringVar()
            userPwdEntry = Entry(askPwdFrame,textvariable = self.userPwd,width = 23)
            userPwdEntry.grid(column =1 , row = 1)
            askPwdLable = Label(askPwdFrame,text = " Confirm Password:    ",pady=10,font=('calibri',12,'bold'))
            askPwdLable.grid(column =0 , row = 2)
            self.root.update()
            self.confirmUserPwd=StringVar()
            comfirmPwdEntry = Entry(askPwdFrame,textvariable = self.confirmUserPwd,width = 23)
            comfirmPwdEntry.grid(column =1 , row = 2)
            self.root.update()

            askPwdFrame.grid(column= 0, row =7)




            self.confirmFrame = Frame(self.root)
            self.root.update()
            
            confirmButton= Button(self.confirmFrame,text='Encrypt',command = self.doEnc)
            confirmButton.grid(column = 0, row =1)
            self.root.update()

            self.confirmFrame.grid(column= 0, row = 8)

            # progress Bar Display starts here
            # progressFrame = Frame(self.root)

            # self.progressBar = ttk.Progressbar(progressFrame,orient=HORIZONTAL,length =390,mode ='determinate')
            # self.progressBar.grid()

            # progressFrame.grid(column = 0, row = 8)


        elif Functions().analyseEncryption(self.filesAddress) == False:
            self.displaySelectedFiles.config(text = "Select only Unencrypted files ... !", bg = "red",font=('calibri',12,'bold'))
            self.root.update()


    def checkDec(self):
        if Functions().analyseDecryption(self.filesAddress) == True:
            self.displaySelectedFiles.config(text = "Files Can be Decrypted", bg = "light green",font=('calibri',12,'bold'))
            userIDFrame = Frame(self.root)
        
            askIDLable = Label(userIDFrame,text = " Enter Your Username:",pady=10,font=('calibri',12,'bold'))
            askIDLable.grid(column =0 , row = 0)
            self.root.update()
            self.userName = StringVar()
            userNameEntry = Entry(userIDFrame,textvariable = self.userName,width = 23)
            userNameEntry.grid(column =1 , row = 0)
            self.root.update()

            userIDFrame.grid(column=0, row=6)

            askPwdFrame =  Frame(self.root)

            askPwdLable = Label(askPwdFrame,text = " Enter Your Password:",pady=10,font=('calibri',12,'bold'))
            askPwdLable.grid(column =0 , row = 1)
            self.root.update()
            self.userPwd=StringVar()
            userPwdEntry = Entry(askPwdFrame,textvariable = self.userPwd,width = 23)
            userPwdEntry.grid(column =1 , row = 1)
            askPwdFrame.grid(column= 0, row =7)
            self.root.update()

            self.confirmFrame = Frame(self.root)
            
            confirmButton= Button(self.confirmFrame,text='Decrypt',command = self.doDec)
            confirmButton.grid(column = 0, row =1)
            self.root.update()


            self.confirmFrame.grid(column= 0, row = 8)

            # progress Bar Display starts here
            # progressFrame = Frame(self.root)

            # self.progressBar = ttk.Progressbar(progressFrame,orient=HORIZONTAL,length =390,mode ='determinate')
            # self.progressBar.grid()

            # progressFrame.grid(column = 0, row = 9)

            

        elif Functions().analyseDecryption(self.filesAddress)  == False:
            self.displaySelectedFiles.config(text = "Select only Encrypted files ... !", bg = "red",font=('calibri',12,'bold'))
            self.root.update()

    def userInterface(self):
        self.root  = Tk()
        self.root.title('Uencryptor - File Encryptor')
        self.root.resizable(0,0)

        titleFrame = Frame(self.root)
        # contents in titleFrame 
        title = Label(titleFrame,text="Uencryptor",font = ('calibri',40,'bold'),padx=40,pady=5,bg='green',foreground='white')
        title.grid(column=0)
        subTitle = Label(titleFrame,text="Encrypt your personal files.",font=('calibir',10,'bold'),bg='light green',padx=103)
        subTitle.grid(column = 0, row = 1)
        titleFrame.grid(column =0,row =0)

        

        inputFrame = Frame(self.root)
        # contents to interact with user are here 
        selectFile = Label(inputFrame,text = "Select Files to Encrypt/Decrypt : ",pady=10,font=('calibri',12,'bold'))
        selectFile.grid(column =0 , row = 0)

        selectFileButton =  Button(inputFrame,text='Choose Files',command = self.getAddress)
        selectFileButton.grid(column =1 , row = 0)

        inputFrame.grid(column=0, row =1)




        displayFrame = Frame(self.root)
        # contents of display frame
        selectedFiles = Label(displayFrame,text = "Selected Files Are : ",font=('calibri',12,'bold'))
        selectedFiles.grid(column =0 , row = 0)
        blankLable = Label(displayFrame,pady = 5,text='                                                        ')
        blankLable.grid(column = 1 , row = 0)

        displayFrame.grid(column =0, row =2)

        # displayframe2 for message
        displayFrame2 = Frame(self.root)
        self.displaySelectedFiles = Label(displayFrame2,text='Selected files will be displayed here.')
        self.displaySelectedFiles.grid(column = 0, row =0 )
        displayFrame2.grid(column = 0, row = 4)

        buttonFrame = Frame(self.root)

        encryptButton = Button(buttonFrame,text='Verify Encryption',command= self.checkEnc)
        encryptButton.grid(column=0, row = 0)
        blankLable2 = Label(buttonFrame,pady = 5,text='                ')
        blankLable2.grid(column = 1 , row = 0)

        decryptButton = Button(buttonFrame,text='Verify Decryption',command= self.checkDec)
        decryptButton.grid(column=2,row=0)
        buttonFrame.grid(column = 0,row = 5)


        self.root.mainloop()


if __name__ ==  "__main__":
    obj= Driver()
    obj.userInterface()