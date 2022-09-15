import os, logging
from PIL import Image
from traceback import format_exc

logger = logging.getLogger()
try:
    import cv2
    import numpy as np

    # Load a model stored in Caffe
    # opencv_dnn_model = cv2.dnn.readNetFromCaffe("./Lib/deploy.prototxt",
    #                                              "./Lib/res10_300x300_ssd_iter_140000_fp16.caffemodel")

    pb_path = "./Lib/opencv_face_detector_uint8.pb"
    pbtxt_path = "./Lib/opencv_face_detector.pbtxt"
    if os.path.exists(pb_path) and os.path.exists(pbtxt_path):
        # Load a model stored in TensorFlow
        opencv_dnn_model = cv2.dnn.readNetFromTensorflow(pb_path, pbtxt_path)
        logger.info('OpenCV 初始化成功')
    else:
        logger.warning('OpenCV 初始化失败：Lib库文件缺失。')
        print('OpenCV 初始化失败：Lib库文件缺失。')
        print('建议重新下载程序，强制运行可能引发异常。')
        input('Press Enter to continue...')
except cv2.error:
    logger.warning('OpenCV 初始化失败：' + format_exc().replace('\n', ''))
    print('OpenCV 初始化失败，有可能是CPU或系统不兼容。')
    print('建议重新下载程序或关闭本地AI功能，强制运行可能引发异常。')
    input('Press Enter to continue...')


def find_faces(img):
    # 传递路径：等效于 cv2.imread，但支持文件名中文，仅支持 RGB 图像；np.fromfile 读取为数组，cv2.imdecode 解码为图像
    # img = np.fromfile(path, dtype=np.uint8)
    # img = cv2.imdecode(img, -1)

    # 传递二进制 RGB 图像：np.array 进行图像序列化，数列翻转转换为 BGR 图像
    img = np.array(img)
    img = img[:, :, ::-1]  # RGB to BGR

    # Perform the required pre-processings on the image and create a 4D blob from image.
    # Resize the image and apply mean subtraction to its channels
    # Also convert from BGR to RGB format by swapping Blue and Red channels.
    preprocessed_image = cv2.dnn.blobFromImage(img, scalefactor=1.0, size=(300, 300),
                                               mean=(104.0, 117.0, 123.0), swapRB=False, crop=False)
    # Get the height and width of the input image.
    image_height, image_width, _ = img.shape
    # Set the input value for the model.
    opencv_dnn_model.setInput(preprocessed_image)
    # Perform the face detection on the image.
    results = opencv_dnn_model.forward()

    for face in results[0][0]:
        # Retrieve the face detection confidence score.
        face_confidence = face[2]

        # Check if the face detection confidence score is greater than the thresold.
        if face_confidence > 0.5:

            # Retrieve the bounding box of the face.
            bbox = face[3:]

            # Retrieve the bounding box coordinates of the face and scale them according to the original size of the image.
            x1 = int(bbox[0] * image_width)
            y1 = int(bbox[1] * image_height)
            x2 = int(bbox[2] * image_width)
            y2 = int(bbox[3] * image_height)

            # Draw a bounding box around a face on the copy of the image using the retrieved coordinates.
            # cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=image_width // 200)
            # cv2.circle(img, (int(0.5 * x1 + 0.5 * x2), int(0.5 * y1 + 0.5 * y2)), 10, (0, 255, 0), 2)

            # return nose position x,y
            return 0.5 * (x1 + x2), 0.5 * (y1 + y2)
        else:
            # return center position
            return 0.5 * image_width, 0.5 * image_height
    # cv2.imshow('Result', img)


# test code
'''
for filename in os.listdir("./Downloads"):
    if 'jpg' in filename:
        pic = Image.open("./Downloads/" + filename)
        if pic.mode != "RGB": pic = pic.convert('RGB')
        result = find_faces(pic)
        print(filename, result)
    # k = cv2.waitKey(1000)
    # if k == 27:    # press 'ESC' to quit
    # break
# cv2.destroyAllWindows()
'''
