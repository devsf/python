# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.apiregistration_v1_api import ApiregistrationV1Api


class TestApiregistrationV1Api(unittest.TestCase):
    """ ApiregistrationV1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.apiregistration_v1_api.ApiregistrationV1Api()

    def tearDown(self):
        pass

    def test_create_api_service(self):
        """
        Test case for create_api_service

        
        """
        pass

    def test_delete_api_service(self):
        """
        Test case for delete_api_service

        
        """
        pass

    def test_delete_collection_api_service(self):
        """
        Test case for delete_collection_api_service

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_api_service(self):
        """
        Test case for list_api_service

        
        """
        pass

    def test_patch_api_service(self):
        """
        Test case for patch_api_service

        
        """
        pass

    def test_read_api_service(self):
        """
        Test case for read_api_service

        
        """
        pass

    def test_replace_api_service(self):
        """
        Test case for replace_api_service

        
        """
        pass

    def test_replace_api_service_status(self):
        """
        Test case for replace_api_service_status

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
