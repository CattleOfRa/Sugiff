import facebook

at = 'EAAQRjZAUNIncBAGeBy3mZBMn3BkEHXu0KgoVvKFcQe3cDrlfyJD6uop5UwTZBnrn3r55Y219HZAvpqCaqkYdSoqPsZBhLtTBT6sXWjkaW0hj1GntCZB3yEu968jH1LwCYZCajij8cefTW7NDPVIf7oIvKGBZCOSj7N5PYpbPdaJLH5oTo2Hg6fco'

graph = facebook.GraphAPI(access_token=at, version='2.7')

args = {'fields' : 'birthday,name' }

events = graph.get_object("me/friends", **args)
print(events)
