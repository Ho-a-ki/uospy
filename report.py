
def get_desc():
    """
    Return random weather, just like the pros
    """

    from random import choice
    possi = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows?']
    return choice(possi)

