from future.utils import isint
from linebot.models import TextSendMessage


class Response():

    def __init__(self, key, text):
        
        if isinstance(key, str):
            self._key = [key]
        elif isinstance(key, list):
            self._key = key
        else:
            raise TypeError("`key` should be either str() or list()")

        self._text = text
        
        
    @property
    def text(self):
        return self._text
    
    
    @property
    def key(self):
        return self._key


    @property
    def message(self):
        return TextSendMessage(self._text)


    def should_reply_to(self, message):
        return any(key in message or message in key for key in self._key)


class MultipleResponses(Response):

    def __init__(self, key, texts):
        super().__init__(key, texts)

    
    @property
    def message(self):
        return [TextSendMessage(res['text']) 
                    for res in self._text]