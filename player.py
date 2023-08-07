
class Player:
    def __init__(self,username,email,password,maxscore):
        self.__username=username
        self.__email=email
        self.__password=password
        self.__maxscore=maxscore
    
    @property
    def username(self):
        return self.__username
    
        
    @username.setter
    def username(self,username):
        self.__username=username

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email=email

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password


    @property
    def maxscore(self):
        return self.__maxscore
    
    @maxscore.setter
    def maxscore(self,maxscore):
        self.__maxscore=maxscore