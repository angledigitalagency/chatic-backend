import os
import json
import unittest
from unittest.mock import patch, MagicMock
from webhook_server import app

class TestStripeWebhook(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('webhook_server.stripe.Webhook.construct_event')
    def test_webhook_routing(self, mock_construct_event):
        headers = {'Stripe-Signature': 't=123,v1=signature'}

        # Case 1: Fluency Radio Purchase
        print("\n--- Testing Fluency Radio Webhook ---")
        mock_payload_fluency = {
            'id': 'evt_test_fluency',
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'id': 'cs_test_fluency',
                    'customer': 'cus_fluency_123',
                    'metadata': {'source': 'fluency'},
                    'customer_details': {'email': 'test_fluency@example.com', 'name': 'Fluency Student'},
                }
            }
        }
        mock_construct_event.return_value = mock_payload_fluency
        resp_fluency = self.app.post('/webhook', data=json.dumps(mock_payload_fluency), headers=headers, content_type='application/json')
        print(f"Fluency Response: {resp_fluency.status_code}")
        self.assertEqual(resp_fluency.status_code, 200)

        # Case 2: Chatic Purchase
        print("\n--- Testing Chatic Webhook ---")
        mock_payload_chatic = {
            'id': 'evt_test_chatic',
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'id': 'cs_test_chatic',
                    'customer': 'cus_chatic_456',
                    'metadata': {'source': 'chatic'},
                    'customer_details': {'email': 'test_chatic@example.com', 'name': 'Chatic Student'},
                }
            }
        }
        mock_construct_event.return_value = mock_payload_chatic
        resp_chatic = self.app.post('/webhook', data=json.dumps(mock_payload_chatic), headers=headers, content_type='application/json')
        print(f"Chatic Response: {resp_chatic.status_code}")
        self.assertEqual(resp_chatic.status_code, 200)

if __name__ == '__main__':
    unittest.main()
