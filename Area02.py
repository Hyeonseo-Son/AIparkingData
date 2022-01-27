import datetime
import cv2
import os
from PIL import Image
import threading

capture = cv2.VideoCapture("rtsp://admin:1234556@10.252.73.31/stream0")
# area2_spotNumber = {
#     "spot14": [1544, 118, 1658, 250],
#     "spot15": [1463, 119, 1575, 251],
#     "spot16": [1377, 120, 1486, 255],
#     "spot17": [1288, 123, 1396, 259],
#     "spot18": [1204, 126, 1302, 264],
#     "spot19": [1136, 132, 1209, 267],
#     "spot20": [878, 153, 965, 286],
#     "spot21": [799, 159, 903, 293],
#     "spot22": [719, 167, 825, 300],
#     "spot23": [644, 178, 751, 309],
#     "spot24": [573, 188, 679, 315],
#     "spot25": [508, 196, 611, 323],
#     "spot26": [448, 206, 548, 331],
#     "spot27": [391, 217, 489, 337],
#     "spot28": [348, 227, 426, 340],
#     "spot29": [387, 507, 501, 684],
#     "spot30": [451, 503, 572, 688],
#     "spot31": [530, 500, 647, 690],
#     "spot32": [607, 498, 730, 691],
#     "spot33": [689, 494, 813, 692],
#     "spot34": [779, 492, 907, 697],
#     "spot35": [878, 488, 1005, 700],
#     "spot36": [977, 486, 1105, 700],
#     "spot37": [1084, 484, 1206, 700],
#     "spot38": [1194, 481, 1311, 698],
#     "spot39": [1303, 476, 1420, 698],
#     "spot40": [1413, 473, 1525, 695],
#     "spot41": [1509, 472, 1632, 694],
#     "spot42": [1608, 467, 1722, 689],
#     "spot69": [1629, 680, 1731, 920],
#     "spot70": [1522, 683, 1634, 929],
#     "spot71": [1406, 688, 1527, 934],
#     "spot72": [1293, 693, 1417, 936],
#     "spot73": [1176, 695, 1309, 934],
#     "spot74": [1063, 694, 1200, 933],
#     "spot75": [951, 693, 1089, 930],
#     "spot76": [846, 692, 985, 924],
#     "spot77": [747, 689, 883, 918],
#     "spot78": [656, 687, 784, 909],
#     "spot79": [568, 686, 693, 901],
#     "spot80": [480, 682, 609, 890],
#     "spot81": [413, 679, 530, 880],
#     "spot82": [347, 675, 462, 870]
# }

path = ".\\image\\Area02"
if not os.path.isdir(path):
    os.mkdir(path)

while True:

    ret, image = capture.read()

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nowHour = datetime.datetime.now().strftime("%H")
    nowMinute = datetime.datetime.now().strftime("%M")
    nowSecond = datetime.datetime.now().strftime("%S")
    print(str(now))

    if nowMinute == "00" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area02\\Parking_Area02_" + str(now) + ".png", image)
        except:
            continue
    elif nowMinute == "15" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area02\\Parking_Area02_" + str(now) + ".png", image)
        except:
            continue
    elif nowMinute == "30" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area02\\Parking_Area02_" + str(now) + ".png", image)
        except:
            continue
    elif nowMinute == "45" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area02\\Parking_Area02_" + str(now) + ".png", image)
        except:
            continue

    # if nowMinute == "00" and nowSecond == "00":
    #     cv2.imwrite("image\\Parking_Area02_" + str(now) + ".png", image)
    #
    #     for key in area2_spotNumber.keys():
    #         tempimage = Image.open("image\\Parking_Area02_" + str(now) + ".png")
    #         croppedImage1 = tempimage.crop(area2_spotNumber[key])
    #         # croppedImage1.show()
    #         print("잘려진 사진 크기 :", croppedImage1.size)
    #         savepath = ".\\cropImage"
    #         try:
    #             if not os.path.exists("cropImage\\Parking_Area02_" + str(now)):
    #                 os.makedirs("cropImage\\Parking_Area02_" + str(now))
    #         except OSError:
    #             print('Error: Creating directory. ' + str(now))
    #
    #         croppedImage1.save(
    #             ("cropImage\\Parking_Area02_" + str(now) + "\\Parking_Area02_" + str(now) + "_" + str(key) + ".png"))
    #
    # elif nowMinute == "15" and nowSecond == "00":
    #     cv2.imwrite("image\\Parking_Area02_" + str(now) + ".png", image)
    #
    #     for key in area2_spotNumber.keys():
    #         tempimage = Image.open("image\\Parking_Area02_" + str(now) + ".png")
    #         croppedImage1 = tempimage.crop(area2_spotNumber[key])
    #         # croppedImage1.show()
    #         print("잘려진 사진 크기 :", croppedImage1.size)
    #         savepath = ".\\cropImage"
    #         try:
    #             if not os.path.exists("cropImage\\Parking_Area02_" + str(now)):
    #                 os.makedirs("cropImage\\Parking_Area02_" + str(now))
    #         except OSError:
    #             print('Error: Creating directory. ' + str(now))
    #
    #         croppedImage1.save(
    #             ("cropImage\\Parking_Area02_" + str(now) + "\\Parking_Area02_" + str(now) + "_" + str(key) + ".png"))
    #
    # elif nowMinute == "30" and nowSecond == "00":
    #     cv2.imwrite("image\\Parking_Area02_" + str(now) + ".png", image)
    #     for key in area2_spotNumber.keys():
    #         tempimage = Image.open("image\\Parking_Area02_" + str(now) + ".png")
    #         croppedImage1 = tempimage.crop(area2_spotNumber[key])
    #         # croppedImage1.show()
    #         print("잘려진 사진 크기 :", croppedImage1.size)
    #         savepath = ".\\cropImage"
    #         try:
    #             if not os.path.exists("cropImage\\Parking_Area02_" + str(now)):
    #                 os.makedirs("cropImage\\Parking_Area02_" + str(now))
    #         except OSError:
    #             print('Error: Creating directory. ' + str(now))
    #
    #         croppedImage1.save(
    #             ("cropImage\\Parking_Area02_" + str(now) + "\\Parking_Area02_" + str(now) + "_" + str(key) + ".png"))
    #
    # elif nowMinute == "45" and nowSecond == "00":
    #     cv2.imwrite("image\\Parking_Area02_" + str(now) + ".png", image)
    #
    #     for key in area2_spotNumber.keys():
    #         tempimage = Image.open("image\\Parking_Area02_" + str(now) + ".png")
    #         croppedImage1 = tempimage.crop(area2_spotNumber[key])
    #         # croppedImage1.show()
    #         print("잘려진 사진 크기 :", croppedImage1.size)
    #         savepath = ".\\cropImage"
    #         try:
    #             if not os.path.exists("cropImage\\Parking_Area02_" + str(now)):
    #                 os.makedirs("cropImage\\Parking_Area02_" + str(now))
    #         except OSError:
    #             print('Error: Creating directory. ' + str(now))
    #
    #         croppedImage1.save(
    #             ("cropImage\\Parking_Area02_" + str(now) + "\\Parking_Area02_" + str(now) + "_" + str(key) + ".png"))
