import connexion
import six

from swagger_server.models.question import Question  # noqa: E501
from swagger_server import util


def ask_query(body):  # noqa: E501
    """Ask your query

    Ask your query # noqa: E501

    :param body: Query to be added to the database
    :type body: dict | bytes

    :rtype: Question
    """
    if connexion.request.is_json:
        body = Question.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def change_question(body, question_id=None):  # noqa: E501
    """Change question data

    Change question data # noqa: E501

    :param body: Query to be added to the database
    :type body: dict | bytes
    :param question_id: Query data
    :type question_id: str

    :rtype: Question
    """
    if connexion.request.is_json:
        body = Question.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_query(question_id=None):  # noqa: E501
    """Delete a query

    Delete a query # noqa: E501

    :param question_id: Query data
    :type question_id: str

    :rtype: Question
    """
    return 'do some magic!'


def get_data(question_id=None):  # noqa: E501
    """Get all query data

    Get all query data # noqa: E501

    :param question_id: Query data
    :type question_id: str

    :rtype: Question
    """
    return 'do some magic!'


def upvote_question(body, question_id=None):  # noqa: E501
    """Upvote/Downvote a question

    Upvote/Downvote a question # noqa: E501

    :param body: Query to be added to the database
    :type body: dict | bytes
    :param question_id: Question id
    :type question_id: str

    :rtype: Question
    """
    if connexion.request.is_json:
        body = Question.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
