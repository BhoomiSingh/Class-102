import cv2
import dropbox
import time
import random
start_time= time.time()
def take_snapshot():
    number= random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name= 'img'+ str(number)+'.png'
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print('takensnapshot')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token='sl.A85l_KpA4jf9IxhEuffifz7dSY86G1Ho_u_zwf10MvH3QkrrUQ6i2-2TVQUCEqiwDhyzvGur1eJI5QhybmYfhY3zQOD0GsLFRbBQDkSxfHDGwc5YO1bqCsQ0bQXl3B3BUo26m0_IA4M'
    file= img_name
    file_from=file
    file_2='/testfolder/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_2,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()
