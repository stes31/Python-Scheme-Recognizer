import figure_detection as fd
import cv2


if __name__ == "__main__":
    flag = False
    image1 = cv2.imread(r"pictures/doc.jpg")
    image2 = cv2.imread(r"pictures/doc_copy.jpg")

    sn1 = fd.FigureMath(image1)
    sn2 = fd.FigureMath(image2)
    hash2 = sn1.CalcImageHash()
    ls = sn2.rotate()
    for i in ls:
        sn2 = fd.FigureMath(i)
        hash1 = sn2.CalcImageHash()
        if sn1.CompareHash(hash1, hash2) < 80:
            flag = True
    if not flag:
        print("Несовпадение")
    else:
        print("Совпадение")

