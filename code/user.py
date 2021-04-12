from datetime import datetime
import secrets

class User:
    def __init__(self, userid = '', password = '',loginStatus = False , registerDate = ''):
        self._userid = userid
        self._password = password
        self._loginStatus = loginStatus
        self._registerDate = registerDate

    def register(self, id, pswd):
            self._userid = id
            self._password = pswd
            self._registerDate = datetime.now()

    def disp(self):
        print(f"{self._userid} {self._password} {self._registerDate}")


class Consumer(User):
    def __init__(self, consumer = None):
        if(consumer):
            self._consumerName = consumer._consumerName
            self._email = consumer._email
            User.__init__(self, consumer._userid, consumer._password, consumer._loginStatus, consumer._registerDate)
        else:
            self._consumerName = ''
            self._email = ''
            User.__init__(self)

    def register(self, name, email, password):
        self._consumerName = name
        self._email = email

        User.register(self, secrets.token_hex(nbytes=16), password)

    def disp(self):
        print(f"{self._consumerName} {self._email}", end = ' ')
        User.disp(self)


class Creator(Consumer):
    def __init__(self, cardno, consumer):
        self.__creditcardInfo = cardno
        Consumer.__init__(self, consumer)
    def disp(self):
        print(f"{self.__creditcardInfo}", end = ' ')
        Consumer.disp(self)



consumer1 = Consumer()
consumer1.register('sriram', 'sriram@gmail.com', 'allahwhoakbar')
consumer1.disp()


creator1 = Creator('123', consumer1)
creator1.disp()
