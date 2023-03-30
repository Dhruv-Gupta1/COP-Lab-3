import connexion
import six

from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util


def create_tag(body):  # noqa: E501
    """Create tag

    Create tag # noqa: E501

    :param body: Tag to be added to the database
    :type body: dict | bytes

    :rtype: Tag
    """
    if connexion.request.is_json:
        body = Tag.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_tag(tag_id=None):  # noqa: E501
    """Delete an tag

    Delete an tag # noqa: E501

    :param tag_id: Tag id
    :type tag_id: str

    :rtype: Tag
    """
    return 'do some magic!'


def get_tag_data(tag_id=None):  # noqa: E501
    """Get tag data

    Get tag data # noqa: E501

    :param tag_id: Tag id
    :type tag_id: str

    :rtype: Tag
    """
    return 'do some magic!'
