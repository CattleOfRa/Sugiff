import facebook


class user(object):


    def __init__(self, access_token, version='2.7'):
        """Access facebook user information through access token"""

        self.access_token = access_token
        self.access_token = 'EAAQRjZAUNIncBAAAQ123btvEBBAUoZAYKnwXZBwVR3VI1gzSqZALjcLGCOi3xi1ZBUoNuIVPBFngzrHA6gjcTtyTxTzLtkYqLbCKAiRZBpW1WKGY6tzULtk5uZAI8y6tMG8NxuuCfJLmYDDZBbWv1dpZBJ0VqorPzZAPWh7Mc1jXBZCZAf1EEg6d8ZBvv'
        self.version = version
        self.graph = facebook.GraphAPI(access_token=self.access_token, version=self.version)

    def get_birthdays(self):
        """Get user's list of upcoming birthdays"""

        args = {'fields' : 'birthday,name' }
        events = self.graph.get_object("me/friends", **args)
        return events

