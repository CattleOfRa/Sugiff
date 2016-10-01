import facebook


class user(object):


    def __init__(self, access_token, version='2.7'):
        """Access facebook user information through access token"""

        self.access_token = access_token
        self.access_token = 'EAAQRjZAUNIncBALbpmCThVZBO7ZB0ZCQP0No3HDr1goXYa1vxZCAurLZBt2W7ei53eEaIT8aAgenE6XGayhSI2ZAOlrxwKWHc4BKp5Xkgmru3Rs3ExN4ObLgs8m0gi4TSlVosn3nKiJAqA82TXC6hFvkfobVqbllicw78H83ltyaqamGKNRIDxH'
        self.version = version
        self.graph = facebook.GraphAPI(access_token=self.access_token, version=self.version)

    def get_birthdays(self):
        """Get user's list of upcoming birthdays"""

        args = {'fields' : 'birthday,name' }
        events = self.graph.get_object("me/friends", **args)
        return events

