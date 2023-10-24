import unittest
import requests
import xmlrunner
import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('test.log', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root_logger.addHandler(handler)


class TestRandomImageAPI(unittest.TestCase):
    api_url = "https://dog.ceo/api/breeds/image/random"

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.debug("Executed once before running all tests")
        cls.logger.info(f'Running {cls.__name__}')

    def setUp(self) -> None:
        self.logger.info(f'Setting up for: {self._testMethodName}')

    def tearDown(self) -> None:
        self.logger.info(f'Tearing down for: {self._testMethodName}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.debug(f'Finished running all tests in {cls.__name__}')

    def test_status_code(self):
        response = requests.get(self.api_url)
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        response = requests.get(self.api_url)
        print(response)
        print(response.headers)
        print(response.json())
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_image_url_validation(self):
        response = requests.get(self.api_url)
        data = response.json()
        self.assertIn("message", data)
        image_url = data["message"]
        self.assertTrue(image_url.startswith("https://"))

    def test_randomness(self):
        image_urls = set()
        for _ in range(5):  # Making 5 requests to test randomness
            response = requests.get(self.api_url)
            data = response.json()
            self.assertIn("message", data)
            image_url = data["message"]
            image_urls.add(image_url)
        # Could be image_urls == 5
        self.assertGreater(len(image_urls), 1)


if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports')
    )
