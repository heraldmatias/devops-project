import json

from tests import BaseCase


class TestUserLogin(BaseCase):

    def test_given_valid_application_code_when_login_then_success(self):
        # Arrange
        user_payload = json.dumps({
            "application": "app1"
        })

        # Act
        response = self.client.post(
            '/api/access-token', headers={"Content-Type": "application/json"}, data=user_payload)

        # Assert
        json_response = response.json
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(json_response['token'])

    def test_given_no_valid_application_code_when_login_then_fail(self):
        # Arrange
        user_payload = json.dumps({
            "application": None
        })

        # Act
        response = self.client.post(
            '/api/access-token', headers={"Content-Type": "application/json"}, data=user_payload)

        # Assert
        json_response = response.json
        self.assertEqual(400, response.status_code)
        self.assertEqual({'body_params': [{'loc': [
                         'application'], 'msg': 'none is not an allowed value', 'type': 'type_error.none.not_allowed'}]}, json_response['validation_error'])
