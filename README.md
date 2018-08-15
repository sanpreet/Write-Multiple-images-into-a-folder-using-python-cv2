# Write-Multiple-images-into-a-folder-using-python-cv2
## Vision of this code
This code is used Write Multiple images into a folder using python cv2. For fetching the images we have folder **images** and for writing  we have folder **output_images**. I will show how the images look when they are written in the folder *output_images*
![new_improved](https://user-images.githubusercontent.com/3431730/44174584-2e61ca00-a101-11e8-85d3-12ca4307fffe.jpg)

## Approach::sweat_smile:
I have used python programming to implement such piece of work. I have used enumerate function to get the index of each image and write the image with index and format function. For more details please refer to the below code.


---

```
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
```
    
---

## How to run the code:
Please downloaded the file and folders and run the below command. Note, please change address by yourself
```
python reading_writing_multiple_images_opencv2.py
```

