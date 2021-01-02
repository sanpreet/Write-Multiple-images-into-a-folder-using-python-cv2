# import the library opencv
import cv2
# globbing utility.
import glob
# select the path
path = "A:\images\input_images\*.*"
for bb,file in enumerate (glob.glob(path)):
    image_read = cv2.imread(file)
    # conversion numpy array into rgb image to show
    c = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', c)
    # writing the images in a folder output_images
    cv2.imwrite('A:\images\output_images\messigray{}.png'.format(bb), c)
    #wait for 1 second
    k = cv2.waitKey(1000)
    #destroy the window
    cv2.destroyAllWindows()
