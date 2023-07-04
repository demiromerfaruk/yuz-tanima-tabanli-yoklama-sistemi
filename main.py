############################################# İÇERİ AKTARILACAK PAKETLER ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

############################################# FONKSİYONLAR ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='Bize Ulaşın', message="Lütfen bize ulaşın : 'aycanomer12@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Bazı dosya eksik', message='Lütfen yardım için bizimle iletişime geçin')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Eski Şifre bulunamadı', 'Lütfen aşağıya yeni bir şifre girin', show='*')
        if new_pas == None:
            mess._show(title='Şifre Girilmedi', message='Şifre ayarlanmadı!! Lütfen tekrar deneyin')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Şifre Kayıtlı', message='Yeni şifre başarıyla kaydedildi!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Hata', message='Yeni şifreyi tekrar onaylayın!!!')
            return
    else:
        mess._show(title='Yanlış şifre', message='Lütfen doğru eski şifreyi girin.')
        return
    mess._show(title='Şifre değişti', message='Parola başarıyla değiştirildi!!')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Sifre Degistir")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Eski Şifreyi Girin',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Yeni Şifreyi Girin', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Yeni şifreyi onayla', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="İptal et", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Kaydet", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Eski Şifre bulunamadı', 'Lütfen aşağıya yeni bir şifre girin', show='*')
        if new_pas == None:
            mess._show(title='Şifre Girilmedi', message='Şifre ayarlanmadı!! Lütfen tekrar deneyin')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Şifre Kayıtlı', message='Yeni şifre başarıyla kaydedildi!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Yanlış Şifre', message='Yanlış şifre girdiniz')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Fotoğraf Çek  >>>  2)Profili Kaydet"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Fotoğraf Çek  >>>  2)Profili Kaydet"
    message1.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # artan örnek numarası
                sampleNum = sampleNum + 1
                # yakalanan yüzün veri kümesi klasörüne kaydedilmesi TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # çerçeveyi göster
                cv2.imshow('Fotograf Cek', img)
            # 100 milisaniye bekleyin
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # örnek sayısı 100'den fazlaysa kırın
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Cekilen Resimler : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Doğru ismi giriniz"
            message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='Kayıt Yok', message='Lütfen önce birini kaydedin!!!')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profil Başarıyla Kaydedildi"
    message1.configure(text=res)
    message.configure(text='Şu ana kadar toplam kayıt  : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    # klasördeki tüm dosyaların yolunu al
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # boş yüz listesi oluştur
    faces = []
    # boş kimlik listesi oluştur
    Ids = []
    # şimdi tüm görüntü yolları arasında dolaşıp kimlikleri ve görüntüleri yükleyerek
    for imagePath in imagePaths:
        # görüntüyü yükleme ve gri skalaya dönüştürme
        pilImage = Image.open(imagePath).convert('L')
        # Şimdi PIL görüntüsünü numpy dizisine dönüştürüyoruz
        imageNp = np.array(pilImage, 'uint8')
        # resimden kimliği alma
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # yüzü eğitim görüntüsü örneğinden çıkarın
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Veri Eksik', message='Verileri sıfırlamak için lütfen Profili Kaydete tıklayın!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Ayrintilar Eksik', message='Öğrenci bilgileri eksik, lütfen kontrol edin!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

            else:
                Id = 'Bilinmiyor'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Katilim Alma', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()

######################################## KULLANILAN MADDELER ############################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'Ocak',
      '02':'Şubat',
      '03':'Mart',
      '04':'Nisan',
      '05':'Mayıs',
      '06':'Haziran',
      '07':'Temmuz',
      '08':'Ağustos',
      '09':'Eylül',
      '10':'Ekim',
      '11':'Kasım',
      '12':'Aralık'
      }

######################################## GUI ÖN-YÜZ ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Katılım Sistemi")
window.configure(background='#000000')

frame1 = tk.Frame(window, bg="#111012")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#111012")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Yüz Tanıma Tabanlı Katılım Sistemi" ,fg="white",bg="#000000" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="white",bg="#000000" ,width=55 ,height=1,font=('times', 18, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="white",bg="#000000" ,width=55 ,height=1,font=('times', 18, ' bold '))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="                       Yeni Kayıtlar İçin                       ", fg="white",bg="#111012" ,font=('times', 19, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                       Kayıtlı Olanlar için                      ", fg="white",bg="#111012" ,font=('times', 19, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="ID giriniz",width=20  ,height=1  ,fg="white"  ,bg="#111012" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="İsim giriniz",width=20  ,fg="white"  ,bg="#111012" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Fotoğraf Çek  >>>  2)Profili kaydet" ,bg="#111012" ,fg="white"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="" ,bg="#111012" ,fg="white"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Katılım",width=20  ,fg="#46f53d"  ,bg="#111012"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Şu ana kadar toplam kayıt  : '+str(res))

##################### MENU ÇUBUĞU #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Sifre Degistir', command = change_pass)
filemenu.add_command(label='Bize Ulasin', command = contact)
filemenu.add_command(label='Cikis',command = window.destroy)
menubar.add_cascade(label='Yardim',font=('times', 29, ' bold '),menu=filemenu)

################## DEVAM TABLOSU ####################

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')

###################### KAYDIRMA ÇUBUĞU ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTONLAR ##################################

clearButton = tk.Button(frame2, text="Temizle", command=clear  ,fg="black"  ,bg="red"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Temizle", command=clear2  ,fg="black"  ,bg="red"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Fotoğraf Çek", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=16  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=145, y=300)
trainImg = tk.Button(frame2, text="Profili kaydet", command=psw ,fg="white"  ,bg="blue"  ,width=16  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=145, y=380)
trackImg = tk.Button(frame1, text="Yoklama al", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=15  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=145,y=50)
quitWindow = tk.Button(frame1, text="Çıkış", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### SON ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################
