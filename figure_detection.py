import cv2


class FigureMath:
    def __init__(self, image):
        self.image = image

    # Вращение картинки
    def rotate(self):
        ima = self.image
        ls = []
        for i in range(6):
            ls.append(ima)
            (h, w) = ima.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((int(w / 2), int(h / 2)), -30, 0.6)
            rotated = cv2.warpAffine(ima, rotation_matrix, (w, h))
            ima = rotated
        return ls

        # Функция вычисления хэша
    def CalcImageHash(self):
        resized = cv2.resize(self.image, (16, 16), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
        ret, threshold_image = cv2.threshold(gray_image, gray_image.mean(), 255, 0)  # Бинаризация по порогу
        # Рассчитаем хэш
        _hash = ""
        for x in range(16):
            for y in range(16):
                if threshold_image[x, y] == 255:
                    _hash += "1"
                else:
                    _hash += "0"
        return _hash

    @staticmethod
    def CompareHash(hash1, hash2):
        count = 0
        for i in range(len(hash1)):
            if hash1[i] != hash2[i]:
                count += 1
        return count
