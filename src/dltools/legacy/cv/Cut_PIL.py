from PIL import Image
import os 
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
 
src_folder = "D:/Data_saver/shanyin_original/0/"
tar_folder = "D:/Data_saver/shanyin_crop_third/"
backup_folder = "D:/Data_saver/backup/"
 
def isCrust(pix):
    return sum(pix) < 25
 
def hCheck(img, y, step = 50):
    count = 0
    width = img.size[0]
    for x in xrange(0, width, step):
        if isCrust(img.getpixel((x, y))):
            count += 1
        if count > width / step / 2:
            return True
    return False
 
def vCheck(img, x, step = 50):
    count = 0
    height = img.size[1]
    for y in xrange(0, height, step):
        if isCrust(img.getpixel((x, y))):
            count += 1
        if count > height / step / 2:
            return True
    return False
 
def boundaryFinder(img,crust_side,core_side,checker):
    if not checker(img,crust_side):
        return crust_side
    if checker(img,core_side):
        return core_side
 
    mid = (crust_side + core_side) / 2
    while  mid != core_side and mid != crust_side:
        if checker(img,mid):
            crust_side = mid
        else:
            core_side = mid
        mid = (crust_side + core_side) / 2
    return core_side
    pass
 
def handleImage(filename,tar):
    img = Image.open(os.path.join(src_folder,filename))
    if img.mode != "RGB":
        img = img.convert("RGB")
    width, height = img.size
 
    left = boundaryFinder(img, 0, width/2, vCheck)
    right = boundaryFinder(img, width-1, width/2, vCheck)
    top = boundaryFinder(img, 0, height/2, hCheck)
    bottom = boundaryFinder(img, height-1, width/2, hCheck)
    if left == right:
        left = left - 2
        right = right + 1
    if top == bottom:
        top = top - 4
        right = right + 1
    
    
    rect = (left+1, top+1, right-1, bottom-1)
    print rect
    region = img.crop(rect)
    region.save(os.path.join(tar,filename),'PNG')
    pass
 
def folderCheck(foldername):
    if foldername:
        if not os.path.exists(foldername):
            os.mkdir(foldername) 
            print "Info: Folder \"%s\" created" % foldername
        elif not os.path.isdir(foldername):
            print "Error: Folder \"%s\" conflict" % foldername
            return False
    return True
    pass
 
def main():
    if folderCheck(tar_folder) and folderCheck(src_folder) and folderCheck(backup_folder):
        for filename in os.listdir(src_folder):
            if filename.split('.')[-1].upper() in ("JPG","JPEG","PNG","BMP","GIF"):
                handleImage(filename,tar_folder)
                os.rename(os.path.join(src_folder,filename),os.path.join(backup_folder,filename))
        pass
 
 
if __name__ == '__main__':
    main()
    #handleImage('Screenshot_2013-10-13-21-55-14.png','')
