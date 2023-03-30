# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.question import Question  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQuestionController(BaseTestCase):
    """QuestionController integration test stubs"""

    def test_ask_query(self):
        """Test case for ask_query

        Ask your query
        """
        body = Question()
        response = self.client.open(
            '/question',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_question(self):
        """Test case for change_question

        Change question data
        """
        body = Question()
        query_string = [('question_id', 'question_id_example')]
        response = self.client.open(
            '/question/{questionId}',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_query(self):
        """Test case for delete_query

        Delete a query
        """
        query_string = [('question_id', 'question_id_example')]
        response = self.client.open(
            '/question/{questionId}',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data(self):
        """Test case for get_data

        Get all query data
        """
        query_string = [('question_id', 'question_id_example')]
        response = self.client.open(
            '/question/{questionId}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upvote_question(self):
        """Test case for upvote_question

        Upvote/Downvote a question
        """
        body = Question()
        query_string = [('question_id', 'question_id_example')]
        response = self.client.open(
            '/question/votes/{questionId}',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
