import os
from PyQt4 import QtCore, QtGui, uic
import hashlib,uuid
import os



path=os.path.dirname(os.path.abspath(__file__))
LoginWindowUI,LoginWindowBase= uic.loadUiType(os.path.join(path,'UI/login.ui'))

class LoginWindow(LoginWindowBase,LoginWindowUI):
    def __init__(self,parent=None):
        LoginWindowBase.__init__(self,parent)

        #super(LoginWindow,self).__init__(parent)
        #Makes Canvas Fullscreen
        self.showMaximized()
        #Launches Canvas from login.ui
        self.setupUi(self)
        # Moves focus to Password when Return Key Triggered
        self.username_text.returnPressed.connect(self.setFocus_pass)
        # Verify Password When Return Key is Triggered
        self.password_text.returnPressed.connect(self.password_verify)
    def setFocus_pass(self):
        #Moves Focus to Password TextField
        self.password_text.setFocus()
    def password_verify(self):

        #Retrieves Curently Types Username and Password in TextFields
        userin=self.username_text.text()
        password_in=self.password_text.text()
        self.check_password(password_in,userin)

    def set_password(self,raw_password):
        alg='sha512'
        salt=uuid.uuid4().hex
        hsh=hashlib.sha512(alg + salt + raw_password ).hexdigest()
        password='%s$%s$%s'%(alg,salt,hsh)



    def check_password(self,password_in,user):

        user=user.replace(" ","$")
        path=os.path.dirname(os.path.abspath(__file__))
        hash_file_path=path + '/Users/'+ user + '.user'
        open_hash = open(hash_file_path, 'rw')
        enc_password = str(open_hash.read())
        #Splitting hash into designated variables
        alg,salt,hsh=enc_password.split("$")
        #Creating comparison hash
        hsh_comp=hashlib.sha512(alg + salt + password_in ).hexdigest()
        #Comparing hash
        if hsh_comp==hsh:

            self.launchHome()
            #return self.main
        else:
            print "Incorrect"

    def launchHome(self):

        from A1_Home import A1_Home
        #Launches Home Page
        self.MainWindow=A1_Home()
        self.MainWindow.show()
        self.close()





