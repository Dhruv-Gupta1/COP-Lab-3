# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTagsController(BaseTestCase):
    """TagsController integration test stubs"""

    def test_create_tag(self):
        """Test case for create_tag

        Create tag
        """
        body = Tag()
        response = self.client.open(
            '/tags',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_tag(self):
        """Test case for delete_tag

        Delete an tag
        """
        query_string = [('tag_id', 'tag_id_example')]
        response = self.client.open(
            '/tags/{tagId}',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tag_data(self):
        """Test case for get_tag_data

        Get tag data
        """
        query_string = [('tag_id', 'tag_id_example')]
        response = self.client.open(
            '/tags/{tagId}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
