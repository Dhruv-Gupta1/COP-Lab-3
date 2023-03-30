# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.search import Search  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_search_tags(self):
        """Test case for search_tags

        Search tags
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open(
            '/search/tags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sort_questions(self):
        """Test case for sort_questions

        Sort questions
        """
        query_string = [('sort_id', 'sort_id_example')]
        response = self.client.open(
            '/search/{sortId}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
