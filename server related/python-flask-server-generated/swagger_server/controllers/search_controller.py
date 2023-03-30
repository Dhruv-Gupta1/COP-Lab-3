import connexion
import six

from swagger_server.models.search import Search  # noqa: E501
from swagger_server import util


def search_tags(tags=None):  # noqa: E501
    """Search tags

    Search tags # noqa: E501

    :param tags: Tags to search
    :type tags: List[str]

    :rtype: Search
    """
    return 'do some magic!'


def sort_questions(sort_id=None):  # noqa: E501
    """Sort questions

    Sort questions # noqa: E501

    :param sort_id: Sort id
    :type sort_id: str

    :rtype: Search
    """
    return 'do some magic!'
