import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server import util


def change_answer(answer_id=None):  # noqa: E501
    """Change data of answer

    Change data of answer # noqa: E501

    :param answer_id: Answer data
    :type answer_id: str

    :rtype: Answer
    """
    return 'do some magic!'


def delete_answer(answer_id=None):  # noqa: E501
    """Delete an answer

    Delete an answer # noqa: E501

    :param answer_id: Answer data
    :type answer_id: str

    :rtype: Answer
    """
    return 'do some magic!'


def get_datafrom_answer(answer_id=None):  # noqa: E501
    """Get all answer data

    Get all answer data # noqa: E501

    :param answer_id: Answer data
    :type answer_id: str

    :rtype: Answer
    """
    return 'do some magic!'


def post_answer(body, question_id=None):  # noqa: E501
    """Post your answer

    Post your answer # noqa: E501

    :param body: Answer to be added to the database
    :type body: dict | bytes
    :param question_id: Query data
    :type question_id: str

    :rtype: Answer
    """
    if connexion.request.is_json:
        body = Answer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upvote_answer(answer_id=None):  # noqa: E501
    """Upvote/Downvote an answer

    Upvote/Downvote an answer # noqa: E501

    :param answer_id: Answer id
    :type answer_id: str

    :rtype: Answer
    """
    return 'do some magic!'
