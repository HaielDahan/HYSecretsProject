import unittest
from PIL import Image
from HYS_en import HYS_encoding
from HYS_dec import dec_HYS
import os
# from file_reader import get_image_metadata

image_path = "C:\\Users\\חיאל דהן\\Desktop\\FinalProject\\hd3.png"
message = "Hello, world!"
original_image = Image.open(image_path)

class HYSEncodingTestCase(unittest.TestCase):

    def setUp(self):
        # Set up any necessary fixtures or resources for your tests
        pass

    def tearDown(self):
        # Clean up any resources after your tests
        pass

    def test_HYS_encoding_result_type(self):
        # Call the function being tested
        result = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        self.assertIsInstance(result, Image.Image)

    def test_HYS_encoding_image_size(self):
        # Call the function being tested
        result = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        self.assertEqual(result.size, original_image.size)

    def test_HYS_encoding_image_mode(self):
        # Call the function being tested
        result = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        self.assertEqual(result.mode, original_image.mode)

    def test_HYS_encoding_pixel_data(self):
        # Call the function being tested
        result = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        self.assertNotEqual(list(result.getdata()), list(original_image.getdata()))


    def test_HYS_encoding_image_not_found(self):
        # Define the inputs for the test
        image_path = "nonexistent_image.png"
        # Call the function being tested and expect it to raise an exception
        with self.assertRaises(FileNotFoundError):
            HYS_encoding(image_path, message)

    def test_HYS_encoding_same_formats(self):
        # Call the function being tested to encode the image
        encoded_image = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        # Ensure that the encoded image format is PNG
        self.assertEqual(encoded_image.format, "PNG")

    def test_HYS_encoding_different_formats(self):
        # Call the function being tested to encode the image
        encoded_image = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        # Ensure that the encoded image format is PNG
        self.assertNotEqual(encoded_image.format, "JPG")

    # def test_HYS_encoding_metadata(self):
    #
    #     # Get the original metadata from the image
    #     original_metadata = self.get_image_metadata(image_path)
    #
    #     # Call the function being tested to encode the image
    #     encoded_image = HYS_encoding(image_path, message)
    #
    #     # Get the metadata from the encoded image
    #     encoded_metadata = self.get_image_metadata(encoded_image)
    #
    #     # Perform assertions to check the expected outcome
    #     self.assertEqual(encoded_metadata, original_metadata)
    #
    # def get_image_metadata(self, image_path):
    #     with Image.open(image_path) as image:
    #         return image.info

    def test_HYS_encoding_empty_message_result(self):
        # Define the inputs for the test
        message = ""
        # Call the function being tested
        result = HYS_encoding(image_path, message)
        # Perform assertions to check the expected outcome
        self.assertNotEqual(result, Image.open(image_path))

    def test_HYS_encoding_empty_message_image_size(self):
        # Define the inputs for the test
        message = ""
        # Call the function being tested
        result = HYS_encoding(image_path, message)
        # Perform assertions to check the expected outcome
        self.assertEqual(result.size, original_image.size)

    def test_HYS_encoding_empty_message_image_mode(self):
        # Define the inputs for the test
        message = ""
        # Call the function being tested
        result = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        self.assertEqual(result.mode, original_image.mode)

    def test_HYS_encoding_empty_message_pixel_data(self):
        # Define the inputs for the test
        message = ""
        # Call the function being tested
        result = HYS_encoding(image_path, message)

        # Perform assertions to check the expected outcome
        self.assertNotEqual(list(result.getdata()), list(original_image.getdata()))

    def test_HYS_encoding_message_too_large(self):
        # Define the inputs for the test
        message = "A" * 10000  # A very long message

        # Call the function being tested and expect it to truncate the message
        result = HYS_encoding(image_path, message)



dec_image_path = "C:\\Users\\חיאל דהן\\Desktop\\FinalProject\\hd3_HYS.png"
class HYSDecodingTestCase(unittest.TestCase):
    def test_HYS_decoding(self):
        # Call the function being tested to decode the image
        decoded_image = dec_HYS(dec_image_path)
        # Perform assertions to check the expected outcome
        self.assertIsInstance(decoded_image[0], Image.Image)

    def test_dec_HYS_decoded_message_type(self):
        # Call the function being tested
        decoded_image= dec_HYS(dec_image_path)
        # Perform assertions to check the expected outcome
        self.assertIsInstance(decoded_image[1], str)

    # def test_HYS_encoding_and_decoding(self):
    #
    #     message = "haiel and yakir"
    #     # Call the function being tested to encode the image
    #     encoded_image = HYS_encoding(image_path, message)
    #     # Call the decoding function on the encoded image
    #     decoded_message = dec_HYS(dec_image_path)
    #     # Perform assertions to check the expected outcome
    #     self.assertEqual(decoded_message[1], message)

    def test_dec_HYS_original_image_exists(self):
        # Perform assertions to check the expected outcome
        self.assertTrue(os.path.exists(dec_image_path))

    def test_dec_HYS_decoded_message_not_empty(self):
        # Call the function being tested
        decoded_message = dec_HYS(dec_image_path)

        # Perform assertions to check the expected outcome
        self.assertNotEqual(decoded_message[1], "")




if __name__ == "__main__":
    unittest.main()


    # def test_HYS_encoding(self):
    #     # Define the inputs for the test
    #
    #
    #     original_image = Image.open(image_path)
    #     # Call the function being tested
    #     result = HYS_encoding(image_path, message)
    #
    #     # Perform assertions to check the expected outcome
    #     self.assertIsInstance(result, Image.Image)
    #     # Verify image size equality
    #     self.assertEqual(result.size, original_image.size)
    #     # Verify image mode equality
    #     self.assertEqual(result.mode, original_image.mode)
    #     # Compares the pixel data of the encoded image
    #     self.assertNotEqual(list(result.getdata()), list(original_image.getdata()))

    # def test_HYS_encoding_empty_message(self):
    #     # Define the inputs for the test
    #     message = ""
    #
    #     original_image = Image.open(image_path)
    #     # Call the function being tested and expect it to return the original image
    #     result = HYS_encoding(image_path, message)
    #     self.assertNotEqual(result, Image.open(image_path))
    #     # Perform assertions to check the expected outcome
    #     # Verify image size equality
    #     self.assertEqual(result.size, original_image.size)
    #     # Verify image mode equality
    #     self.assertEqual(result.mode, original_image.mode)
    #     # Compares the pixel data of the encoded image
    #     self.assertNotEqual(list(result.getdata()), list(original_image.getdata()))