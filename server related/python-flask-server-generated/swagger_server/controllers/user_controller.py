import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def change_user(user_id=None):  # noqa: E501
    """Change data of user

    Change data of user # noqa: E501

    :param user_id: User id
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def create_user(body):  # noqa: E501
    """Create user

    Create user # noqa: E501

    :param body: User to be added to the database
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user_id=None):  # noqa: E501
    """Delete an user

    Delete an user # noqa: E501

    :param user_id: User id
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def get_user_data(user_id=None):  # noqa: E501
    """Get user data

    Get user data # noqa: E501

    :param user_id: User id
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def login_user(username=None, password=None):  # noqa: E501
    """Login user

    Login user # noqa: E501

    :param username: Username
    :type username: str
    :param password: Password
    :type password: str

    :rtype: User
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logout user

    Logout user # noqa: E501


    :rtype: User
    """
    return 'do some magic!'


def sign_up_user(body, username=None, email=None, password=None):  # noqa: E501
    """Create user

    Create user # noqa: E501

    :param body: User to be added to the database
    :type body: dict | bytes
    :param username: 
    :type username: str
    :param email: 
    :type email: str
    :param password: 
    :type password: str

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
