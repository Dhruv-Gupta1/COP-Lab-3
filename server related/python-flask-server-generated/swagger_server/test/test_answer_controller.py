# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnswerController(BaseTestCase):
    """AnswerController integration test stubs"""

    def test_change_answer(self):
        """Test case for change_answer

        Change data of answer
        """
        query_string = [('answer_id', 'answer_id_example')]
        response = self.client.open(
            '/answer/{answerId}',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_answer(self):
        """Test case for delete_answer

        Delete an answer
        """
        query_string = [('answer_id', 'answer_id_example')]
        response = self.client.open(
            '/answer/{answerId}',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_datafrom_answer(self):
        """Test case for get_datafrom_answer

        Get all answer data
        """
        query_string = [('answer_id', 'answer_id_example')]
        response = self.client.open(
            '/answer/{answerId}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_answer(self):
        """Test case for post_answer

        Post your answer
        """
        body = Answer()
        query_string = [('question_id', 'question_id_example')]
        response = self.client.open(
            '/answer/{questionId}',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upvote_answer(self):
        """Test case for upvote_answer

        Upvote/Downvote an answer
        """
        query_string = [('answer_id', 'answer_id_example')]
        response = self.client.open(
            '/answer/votes/{answerId}',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
