import json

from tests import BaseCase
from tests.fixtures.black_list_fixture import BlackEmailFixture


class TestBlackList(BaseCase):

    def test_register_black_email_then_success(self):
        # Arrange
        app_id = "4dd6939a-b54b-11ec-b04e-308d9912cae6"
        payload = json.dumps({
            "app_id": app_id,
            "email": "heraldmatias.oz+4@gmail.com",
            "blocked_reason": "test"
        })

        # Act
        response = self.run_authenticated(
            app_id, 'post', '/api/blacklists', data=payload)

        # Assert
        json_response = response.json
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(json_response['id'])

    def test_register_black_email_then_fail(self):
        # Arrange
        app_id = "4dd6939a-b54b-11ec-b04e-308d9912cae6"
        payload = json.dumps({
            "app_id": app_id,
            "email": None,
            "blocked_reason": "test"
        })

        # Act
        response = self.run_authenticated(
            app_id, 'post', '/api/blacklists', data=payload)

        # Assert
        json_response = response.json
        self.assertEqual(400, response.status_code)
        self.assertIsNotNone({'body_params': [{'loc': [
                             'email'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]}, json_response['validation_error'])

    def test_searching_existing_black_email_by_email_then_success(self):
        # Arrange
        black_email = BlackEmailFixture().create()

        # Act
        response = self.run_authenticated(
            black_email.app_id, 'get', f'/api/blacklists/{black_email.email}')

        # Assert
        json_response = response.json
        self.assertEqual(200, response.status_code)
        self.assertEqual(black_email.email, json_response['email'])
        self.assertEqual(black_email.id, json_response['id'])

    def test_searching_non_existing_black_email_by_email_then_fail(self):
        # Arrange
        black_email = BlackEmailFixture().create()

        # Act
        response = self.run_authenticated(
            black_email.app_id, 'get', f'/api/blacklists/nonexisting@example.com')

        # Assert
        json_response = response.json
        self.assertEqual(404, response.status_code)
        self.assertIsNone(json_response)
