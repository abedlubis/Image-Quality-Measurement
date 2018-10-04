# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import imutils
import matplotlib.pyplot as plt
import cv2


## construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--images", required=True,
#	help="path to input directory of images")
#ap.add_argument("-t", "--threshold", type=float, default=100.0,
#	help="focus measures that fall below this value will be considered 'blurry'")
#args = vars(ap.parse_args())
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
   
# loop over the input images
data = list(paths.list_images("Data/ori/all/"))
result = ""
for imagePath in data:
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    
    fm = variance_of_laplacian(gray)        
#    filename = image.filename
    text = "Blurry"
    
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm > 400:
        text = "Improve"
    if fm > 1500:
        text = "Good"
    
    	# show the image
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
#    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
#    resized_image = cv2.resize(image, (450, 600))
#    plt.imshow(imutils.opencv2matplotlib(image))
#    plt.show()
    cv2.waitKey(0)
    print("{} {}  {:.2f}".format(imagePath, text, fm))
    
    result = result + "File:{} {} {:.2f}\n".format(imagePath, text, fm)
    fp = open("OutputBlurDetection/hasil_blur_iterasi2.txt", "w")
    fp.write(result)
    fp.close()
    


   