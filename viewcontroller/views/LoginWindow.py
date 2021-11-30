import hashlib
import os
import uuid
from PyQt4 import uic

path = os.path.dirname(os.path.abspath(__file__))
LoginWindowUI, LoginWindowBase = uic.loadUiType(os.path.join(path, 'UI/login.ui'))


class LoginWindow(LoginWindowBase, LoginWindowUI):
    def __init__(self, stack):
        super(LoginWindow, self).__init__()

        self.stack = stack
        # Makes Canvas full screen
        self.showMaximized()
        # Launches Canvas from login.ui
        self.setupUi(self)
        # Moves focus to Password when Return Key Triggered
        self.username_text.returnPressed.connect(self.set_pass_focus)
        # Verify Password When Return Key is Triggered
        self.password_text.returnPressed.connect(self.password_verify)

    def set_pass_focus(self):
        # Moves Focus to Password TextField
        self.password_text.setFocus()

    def password_verify(self):

        # Retrieves curently typed username and password in textfields
        user_in = self.username_text.text()
        password_in = self.password_text.text()
        self.check_password(password_in, user_in)

    def set_password(self, raw_password):
        alg = 'sha512'
        salt = uuid.uuid4().hex
        hsh = hashlib.sha512(alg + salt + raw_password).hexdigest()

    def check_password(self, password_in, user):

        user = user.replace(" ", "$")
        user_path = "/home/audatica/PycharmProjects/audatica1-ui/users/"
        hash_file_path = user_path + user + '.user'
        open_hash = open(hash_file_path, 'rw')
        enc_password = str(open_hash.read())
        # Splitting hash into designated variables
        alg, salt, hsh = enc_password.split("$")
        # Creating comparison hash
        hsh_comp = hashlib.sha512(alg + salt + password_in).hexdigest()
        # Comparing hash
        if hsh_comp == hsh:
            self.stack.go_home()
        else:
            print "Incorrect"



