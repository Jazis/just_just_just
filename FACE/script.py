from PIL import Image

center = []


def first():
    image = Image.open('unnamed.jpg').convert("L") 
    print image.size
    wid = image.size[0]
    hig = image.size[1]
    pix = image.load()
    image.save("out.jpg")

def second():
    greens = []
    face_left = []
    image = Image.open('russian.jpg')
    print image.size
    wid = image.size[0] + 100
    hig = image.size[1] + 100
    print hig
    pix = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # print pix[i,j]
            try:
                if pix[i, j] <= (200, 200, 200):
                    if i > image.size[0]/2:
                        greens.append([pix[i, j], i, j])
                    pix[i, j] = 0, 255, 0
                    if pix[i-1, j-1] == (0, 255, 0) and i > image.size[0]/2:
                        face_left.append([pix[i, j], i, j])
                    # print "pixed"
                if pix[i, j] >= (200, 200, 200):
                    pix[i, j] = 0, 0, 255 
            except IndexError:
                pass
    # image.show()
    pix[0, 0] = 255, 255, 255
    print "Start hairs - " +  str(greens[0])
    print "Start face  - " + str(face_left[0])
    pix[greens[0][1], greens[0][1]] = 255, 255, 255 
    pix[face_left[0][1], face_left[0][1]] = 255, 255, 255 
    image.save("out13.jpg")

def pixels_sorting(face_pixels):
    good = []
    uchastok = []
    maybees = []
    for i in range(len(face_pixels)):
        good.append(face_pixels[i][1])
    good.sort()
    # print good
    try:
        for i in range(len(good)):
            if (good[i+1] - good[i]) < 6:
                uchastok.append(good[i])
    except IndexError:
        pass
    for j in range(len(uchastok)):
        for k in range(len(face_pixels)):
            if uchastok[j] == face_pixels[k][1]:
                maybees.append(face_pixels[k])
            else:
                pass
    print maybees

        
        

def third():
    face_pixels = []
    pixels_green = []
    image = Image.open('out13.jpg')
    print image.size
    wid = image.size[0]
    hig = image.size[1]
    img = Image.new("RGB", (image.size[0], image.size[1]), (255, 255, 255))
    imgo = img.load()
    pix = image.load()
    center = [wid/2, hig/2]
    one_four = [wid/4, hig/4]
    for i in range(one_four[0],image.size[0]-one_four[0]):
        for j in range(one_four[1], image.size[1]-one_four[1]):
            face = pix[i, j]
            if pix[i, j] == (0, 255, 0):
                pixels_green.append([i, j])
                # print "work"
                if len(pixels_green) == 5:
                    face_pixels.append([i-5, j-5])
                    pix[i, j] = 255, 0, 0
                    imgo[i, j] = 0, 0, 0
                    # print i, j
                    # print "White pixed. eeee"
                else:
                    pass
            if pix[i, j] != (0, 255, 0):
                pixels_green = []
    img.save('img1.jpg')
    image.save("out22.jpg")
    # print face_pixels
    pixels_sorting(face_pixels)


            

if __name__ == "__main__":
    third()