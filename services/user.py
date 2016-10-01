import facebook


class user(object):

    def __init__(self, access_token):
        """Access facebook user information through access token"""

        self.access_token = access_token
        self.access_token = 'EAAQRjZAUNIncBAGeBy3mZBMn3BkEHXu0KgoVvKFcQe3cDrlfyJD6uop5UwTZBnrn3r55Y219HZAvpqCaqkYdSoqPsZBhLtTBT6sXWjkaW0hj1GntCZB3yEu968jH1LwCYZCajij8cefTW7NDPVIf7oIvKGBZCOSj7N5PYpbPdaJLH5oTo2Hg6fco'
        graph = facebook.GraphAPI(access_token=at, version='2.7')

    def get_birthdays(self):
        """Get user's list of upcoming birthdays"""

        args = {'fields' : 'birthday,name' }
        events = graph.get_object("me/friends", **args)
        return events

