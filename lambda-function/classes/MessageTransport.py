class MessageTransport:

    # constructor
    def __init__(self, message):
        self.__set_message(message)

    # set message//private
    def __set_message(self, message):
        self.__message = message

    # get message
    def get_message(self):
        return self.__message