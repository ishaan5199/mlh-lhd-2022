from PIL import Image
import matplotlib.pyplot as plt

count = 0
def pixelGenerator(image, inputSize, outputSize, save):
    global count
    
    img = Image.open(image)

    #resizing image via bilinear interpolation
    resImg = img.resize(inputSize, Image.BILINEAR)
    
    
    #enlargin the resized image to original size, via nearest neighbour method
    newImg = resImg.resize(outputSize, Image.NEAREST)
    
    #saving the image
    if save:
        newImg.save(f"pixel80s{count}.png")
        count += 1     

    #displaying original and pixelated image
    figure, axis = plt.subplots(1, 2)
    axis[0].imshow(img)
    axis[0].set_title("Original Image")
    
    axis[1].imshow(newImg)
    axis[1].set_title("Pixelated Image")
    
    plt.show()

pixelGenerator("80smusic.jpg", (50, 50), (500, 500), False)
pixelGenerator("miami.jpg", (100, 100), (2048, 1152), True)
pixelGenerator("delorean.png", (80, 80), (3840, 2160), True)