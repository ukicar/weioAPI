def onMessage(newMessage) :
    """If implemented, this function will deliver a newMessage object from WEIO messaging service. NewMessage object consists of name of the object (string), it's specific data and time tag (newMessage.name, newMessage.data, newMessage.date)"""
def sendMessage(newMessage, withoutWeb=False):
    """Send message function will send a new message object to WEIO messaging service. NewMessage object consists of name of the object (string), it's specific data and time tag (newMessage.name, newMessage.data, newMessage.date). 
    If True is set for withoutWeb parameter than messaging service will not share this message with the web interface""" 

class Message :
    """Message class of objects is able to deliver data thru WEIO dispatcher to connected devices or other objects without knowing details of protocol that they are using"""
    destination = ""
    name = ""
    data = 0
    #date = weio.date()