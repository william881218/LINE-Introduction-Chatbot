from collections import OrderedDict
import json

from .response import Response, MultipleResponses


class ResponseHandler(object):
    '''
    This class reads text from the json file and output Response object for Line API.
    '''

    def __init__(self, text_filepath):

        self.text_filepath = text_filepath
        self.responses_json = None
        self.responses = []

        with open(self.text_filepath, 'r') as f:
            self.responses_json = json.load(f)

        self._load_responses_from_json()

    
    def _load_responses_from_json(self):

        for response_json in self.responses_json:

            response_type = response_json.get('type', None)
            key = response_json.get('key', None)
            text = response_json.get('text', None)
            responses = response_json.get('responses', None)

            if response_type == "built_in":
                self.__setattr__(response_json['key'], response_json['text'])
            elif response_type == 'response':
                self.responses.append(Response(key, text))
            elif response_type == 'multiple_responses':
                self.responses.append(MultipleResponses(key, responses))
            else:
                raise ValueError(f"Unknown response type in {self.text_filepath}: {response_type}")


    def response_to_message(self, message):
        response_messages = []
        for response in self.responses:
            if response.should_reply_to(message):
                response_message = response.message
                if isinstance(response_message, list):
                    response_messages.extend(response_message)
                else:
                    response_messages.append(response_message)
        if len(response_messages) == 0:
            raise UnknownMessageError


    def unknown_message(self, message):
        return Response("unknown_message", self.unknown_message.format(message)).message()


# A self-defined exception for unrecognizable user message.
class UnknownMessageError(Exception):
    pass