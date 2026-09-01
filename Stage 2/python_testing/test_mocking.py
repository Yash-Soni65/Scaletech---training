import unittest
from unittest.mock import patch, Mock

from mocking import get_weather


class TestWeather(unittest.TestCase):

    @patch("mocking.requests.get")
    def test_get_weather(self, mock_get):

    
        mock_response = Mock()

        
        mock_response.json.return_value = {
            "temperature": 30
        }

       
        mock_get.return_value = mock_response

        
        result = get_weather()

       
        self.assertEqual(result, {
            "temperature": 30
        })


if __name__ == "__main__":
    unittest.main()