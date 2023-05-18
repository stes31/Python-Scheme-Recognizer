import cv2
import easyocr
import matplotlib.pyplot as plt


class Image:
    def __init__(self, *, path):
        self.image = cv2.imread(path)

    def show_text(self, *, text):
        for t in text:
            bbox, txt, score = t
            cv2.rectangle(self.image, [int(bbox[0][0]), int(bbox[0][1])], [int(bbox[2][0]), int(bbox[2][1])],
                          (0, 255, 0), 5)
            cv2.putText(self.image, txt, [int(bbox[0][0]), int(bbox[0][1])], cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0),
                        2)
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.show()

    def get_text(self, *, language='ru'):
        reader = easyocr.Reader([language], gpu=True)
        return reader.readtext(self.image)


if __name__ == '__main__':
    path = 'pictures/doc.jpg'
    image = Image(path=path)
    text = image.get_text(language='ru')
    image.show_text(text=text)
