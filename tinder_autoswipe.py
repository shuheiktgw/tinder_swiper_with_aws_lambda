import pynder


def lambda_handler(event, context):
    FBID = event['fbid'].encode('utf-8')
    FBTOKEN = event['fbtoken'].encode('utf-8')

    session = pynder.Session(FBID, FBTOKEN)
    users = session.nearby_users()

    counter = 0
    for user in users[:5]:
        user.like()
        counter += 1

    result = {'result': counter}
    return result