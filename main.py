from PIL import Image

path = "TEST_B.png"
# Image.open(path).save("TEST_B.png")
image = Image.open(path)


class ImageModifications:
    def __init__(self, img_before):
        self.img_before = img_before

    def blur(self, save_as):
        # A basic blue can be achieved by averaging the rgb values in a square around the image
        img = self.img_before

        for x in range(img.size[0]):
            for y in range(img.size[1]):

                bigRGB = [0, 0, 0]  # RBG before averaging
                finalRGB = [0, 0, 0]
                blur_mode = self.blur_mode(x, y, "square")

                for i in blur_mode:  # adds up all od the red, green, and blue values of the surrounding pixels
                    bigRGB[0] += i[0]
                    bigRGB[1] += i[1]
                    bigRGB[2] += i[2]

                for j in range(3):
                    finalRGB[j] = int(bigRGB[j] / len(blur_mode))

                img.putpixel((x, y), tuple(finalRGB))
        img.save(save_as)

    def blur_mode(self, x, y, string):
        img = self.img_before
        symbols = []
        surroundingVals = []

        if string == "old":
            # X O/X
            # X X
            surroundingVals = [0, 0, 0, 0]
            symbols = [(0, 0), (-1, 0), (-1, -1), (0, -1)]

        elif string == "square":
            # places a square around each pixel to determine average (O is desired pixel, and X is surrounding box)
            # X X X
            # X O X
            # X X X
            surroundingVals = [0, 0, 0, 0, 0, 0, 0, 0]
            symbols = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        for num, pos in enumerate(symbols):
            try:
                surroundingVals[num] = img.getpixel((x + pos[0], y + pos[1]))
            except IndexError:
                surroundingVals[num] = (0, 0, 0)
                pass
        return surroundingVals


IM = ImageModifications(image)
IM.blur("TEST_A_1.png")
