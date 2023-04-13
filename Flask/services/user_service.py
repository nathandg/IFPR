''' User Service '''

users = []

def user_already_exists(cpf):
    """ Check if user already exists """
    for user in users:
        if user['CPF'] == cpf:
            return True

    return False


def add_user(user):
    """ Add user to users list """
    if user_already_exists(user['CPF']):
        print('User already exists')
        return False

    users.append(user)
    return True


def get_users():
    """ Return users list """
    return users


def get_user(cpf):
    """ Return user by CPF """
    for user in users:
        if user['CPF'] == cpf:
            return user

    return False
