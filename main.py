from PIL import Image

path = "TEST_B.png"
image = Image.open(path)


class ImageModifications:
    def __init__(self, img_before):
        self.img_before = img_before

    def blur(self, save_as):
        # A basic blue can be achieved by averaging the rgb values in a square around the image

        img = self.img_before

        for x in range(img.size[0]):
            for y in range(img.size[1]):
                surroundingVals = [0, 0, 0, 0]
                bigRGB = [0, 0, 0]

                surroundingVals[0] = img.getpixel((x, y))
                surroundingVals[1] = img.getpixel((x - 1, y))
                surroundingVals[2] = img.getpixel((x - 1, y - 1))
                surroundingVals[3] = img.getpixel((x, y - 1))
                for i in surroundingVals:
                    bigRGB[0] += i[0]
                    bigRGB[1] += i[1]
                    bigRGB[2] += i[2]
                finalRGB = (int(bigRGB[0] / 4), int(bigRGB[1] / 4), int(bigRGB[2] / 4))

                img.putpixel((x, y), finalRGB)
        img.save(save_as)


IM = ImageModifications(image)
IM.blur("TEST_A.png")
