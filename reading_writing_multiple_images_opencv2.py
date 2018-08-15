#import the library opencv
import cv2
#globbing utility.
import glob
#select the path
path = "A:\MY_company\Sanpreet_Singh\Client Work\OpenCV-Sanjeev\images\*.*"
for bb,file in enumerate (glob.glob(path)):
    print(bb,file)
    a= cv2.imread(file)
    print(a)
    # %%%%%%%%%%%%%%%%%%%%%
    #conversion numpy array into rgb image to show
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', c)
    #writing the images in a folder output_images
    cv2.imwrite('A:\MY_company\Sanpreet_Singh\Client Work\OpenCV-Sanjeev\images\output_images\messigray{}.png'.format(bb), c)
    #wait for 1 second
    k = cv2.waitKey(1000)
    #destroy the window
    cv2.destroyAllWindows()
























