# Third step
import cv2
import glob

fps = 30
image_folder = '/home/duy/Documents/mmdetection/result_images/result_4'
video_name = './' + str(fps) + '_fps_video.avi'
img_array = []
frameSize = ()
for filename in sorted(glob.glob(image_folder + '/*.png')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    image_size = (width, height)
    frameSize = image_size
    img_array.append(img)

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), fps, frameSize)
for i in range(len(img_array)):
    video.write(img_array[i])
video.release()
