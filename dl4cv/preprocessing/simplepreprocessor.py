# import the necessary packages
import cv2

class SimplePreProcessor(object):
    """
    Store the width, height and interpolation method that will be used
    when resizing the image.
    """
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        """
        Preprocess the image given the chosen width, height and interpolation
        method.

        :param image:
        :return:
        """
        preprocessed_image = cv2.resize(image, )
        return
