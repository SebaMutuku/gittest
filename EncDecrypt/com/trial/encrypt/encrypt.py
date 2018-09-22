from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os,random,sys,pkg_resources

class encrypt():
    def encrpyt(key,file):
        size=64*1024
        outstream=os.path.join(os.path.dirname(file)),"encrpted: "+os.path.basename(file)
        fileSize=str(os.path.getsize(file))

        IV=''
        for i in range(16):
            IV+=chr(random.randint(0,0xFF))

            encrypting=AES.new(key,AES.MODE_CBC,IV)
            with open(file,"rb") as infile:
                with open(outstream,"wb") as outfile:
                    outfile.write(fileSize)
                    outfile.write(IV)
                    while True:
                        size=infile.read(size)

                        if len(size)==0:
                            break
                        elif len(size)%16!=0:
                            size+=''*(16-(len(size)%16))
                            outfile.write(encrypting.encrypt(size))
    def decrypt(key,filename):
        outFile=os.path.join(os.path.dirname(filename),os.path.basename(filename[11:]))
        sized=64*1024
        with open(filename,"rb") as inFile:
            filesize=inFile.read(16)
            IV=inFile.read(16)
            #IV=filesize

            decrypting=AES.new(key,AES.MODE_CBC,IV)
            with open(outFile,"wb") as outFile:
                while True:
                    fileTobeRead=inFile.read(sized)
                    if len(fileTobeRead)==0:
                        break

                    outFile.write(decrypting.decrypt(fileTobeRead))
                outFile.truncate(int(filesize))


    def AllFiles(self):
        allFiles=[]

        for root,subfiles,files in os.walk(os.getcwd()):
            for names in files:
                allFiles.append(os.path.join(root,names))

        return  allFiles
        choice=raw_input("Do you want to (E)ncrypt or (D)ecrypt ?")
        password=raw_input("Enter password to encrypt")
        encFile = allFiles()

        if choice=='E':
            for TFile in encFile:
                if os.path.basename(TFile).startswith("encrypted"):
                    print"%s is already encypted" %str(TFile)
                    pass
                elif TFile==os.path.join(os.getcwd(),sys.argv[0]):
                    pass
                else:
                    encrypt(SHA256.new(password).digest(),str(TFile))
                    print"Done encrypting %s" %str(TFile)


        elif choice=="D":
            filename=raw_input("Enter the filename to decrypt: ")
            if not os.path.exists(filename):
                print ("File does not exist in the specified directory")
                sys.exit()
            elif not filename.startswith("(encrypted)"):
                print ("%s is already encrypted")%filename
                sys.exit()
            else:
                decrypt(SHA256.new(password).digest(),filename)
                print("Done decrytping file %s")%filename
                os.remove(filename)


        else:
            print("Invalid choice!\nPlease choice a valid choice")

enc=encrypt()
print(enc.AllFiles())
enc.encrpyt(file="")




        


