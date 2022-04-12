import struct
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import time

def from_bytes(b, format, offset):
    calcsize = struct.calcsize(format)
    return struct.unpack(format, b[offset:offset+calcsize])[0]

def openXMLline(filename):
    num_lines = sum(1 for line in open(filename, "rb"))
    f = open(filename, "rb")
    lines = f.readlines()
    XMLline = str(lines[num_lines-1])
    startXML = XMLline.find("<SpeFormat")
    XMLline = XMLline[startXML:]
    
    PosVersion = XMLline.find("version") + 9
    Version = XMLline[PosVersion:PosVersion+3]
   
    PosFrame = XMLline.find("Frame") + 14
    Frame = XMLline[PosFrame:]
    PosFrameEnd = Frame.find("\"")
    Frame = Frame[:PosFrameEnd]
    
    PosWidth = XMLline.find("width") + 7
    Width = XMLline[PosWidth:]
    PosWidthEnd = Width.find("\"")
    Width = Width[:PosWidthEnd]
    
    PosHeight = XMLline.find("height") + 8
    Height = XMLline[PosHeight:]
    PosHeightEnd = Height.find("\"")
    Height = Height[:PosHeightEnd]
    
    PosLaser = XMLline.find("WavelengthLaserLine")
    Laser = XMLline[PosLaser:]
    PosLaser = Laser.find("\">") + 2
    Laser = Laser[PosLaser:]
    PosLaserEnd = Laser.find("<")
    Laser = Laser[:PosLaserEnd]
    
    PosCreate = XMLline.find("created") + 9
    Created = XMLline[PosCreate:]
    PosTime = Created.find("T")
    Date = Created[:PosTime]
    PosTimeEnd = Created.find(".")
    Time = Created[PosTime+1:PosTimeEnd]
    
    PosWave = XMLline.find("<Wavelength ")
    PosWaveEnd = XMLline.find("</Wavelength>")
    WaveData = XMLline[PosWave:PosWaveEnd]
    WaveData = WaveData[(WaveData.find("\">")+2):]
    
    Wavedata = []
    WavedataRound = []
    i = 0
    while i < int(Width):
        PosNext = WaveData.find(",")
        Wavedata.append(WaveData[:PosNext])
        WavedataRound.append(round(float(WaveData[:PosNext]), 2))
        WaveData = WaveData[PosNext+1:]
        i += 1

    PosExpTime = XMLline.find("<ExposureTime")
    PosExpTimeEnd = XMLline.find("</ExposureTime>")
    ExpTimeData = XMLline[PosExpTime:PosExpTimeEnd]
    ExpTime = ExpTimeData[(ExpTimeData.find("\">")+2):]
    
    PosCWL = XMLline.find("<CenterWavelength")
    PosCWLEnd = XMLline.find("</CenterWavelength>")
    CWLData = XMLline[PosCWL:PosCWLEnd]
    CWL = CWLData[(CWLData.find("\">")+2):]

    return Version, Frame, Width, Height, Laser, Date, Time, ExpTime, CWL, Wavedata, WavedataRound

def convert_txt(filename, FolderName, space="tab", header=True, invert=False):
    File = FolderName + "/SpectraNew.txt"
    Txt_Point = open(File, "w")                                                                                              #Erstellt und öffnet eine neue Datei im Schreibmodus

    Version, Frame, Width, Height, Laser, Date, Time, ExpTime, CWL, Wavedata, WavedataRound = openXMLline(filename)

    print("SPE version: ", Version)
    print("Frame width: ", Width)
    print("Frame height: ", Height)
    print("Number of frames: ", Frame)
    print("Exposure (ms): ", ExpTime)
    print("Date collected: ", Date)
    print("Time collected (hhmmss): ", Time)
    print("Laser Wavelength (nm): ", Laser)
    print("Central Wavelength (nm): ", CWL)
    if header==True:
        Txt_Point.write("SPE version: " + str(Version) + "\n")
        Txt_Point.write("Frame width: " + str(Width) + "\n")
        Txt_Point.write("Frame height: " + str(Height) + "\n")
        Txt_Point.write("Number of frames: " + str(Frame) + "\n")
        Txt_Point.write("Exposure (ms): " + str(ExpTime) + "\n")
        Txt_Point.write("Laser Wavelength (nm): " + str(Laser) + "\n")
        Txt_Point.write("Central Wavelength (nm): " + str(CWL) + "\n")
        Txt_Point.write("Date collected: " + str(Date) + "\n")
        Txt_Point.write("Time collected (hhmmss): " + str(Time) + "\n")
        Txt_Point.write("\n\n\n")

    Width = int(Width)
    Height = int(Height)
    Frame = int(Frame)

    file = open(filename, "rb")
    bytes = file.read()

    datatype = from_bytes(bytes, "h", 108)
    to_np_type = [np.float32, np.int32, np.int16, np.uint16, None, np.float64, np.uint8, None, np.uint32]
    np_type = to_np_type[datatype]
    itemsize = np.dtype(np_type).itemsize

    Count = Width * Height
    
    Px = int(math.sqrt(Frame))
    data = []
    for i in range(0, Frame):
        data.append(np.frombuffer(bytes, dtype=np_type, count=Count, offset=4100 + i*Count*itemsize))
    
    if invert == False:
        Txt_Point.write("Wavelength\t")
        for j in range(0, Width):
            Txt_Point.write(Wavedata[j] + "\t")        
        Txt_Point.write("\n")

        if space=="tab":
            for i in range(0, Frame):
                Txt_Point.write("Frame " + str(i+1))
                for j in range(0, Width):
                    Txt_Point.write("\t" + str(data[i][j]))
                Txt_Point.write("\n")
        else:
            for i in range(0, Frame):
                Txt_Point.write("Frame " + str(i+1))
                for j in range(0, Width):
                    Txt_Point.write("; " + str(data[i][j]))
                Txt_Point.write("\n")
    else:
        Txt_Point.write("Wavelength\t")
        for j in range(0, Frame):
            Txt_Point.write("Frame " + str(j+1) + "\t")        
        Txt_Point.write("\n")

        if space=="tab":
            for i in range(0, Width):
                Txt_Point.write(Wavedata[i])
                for j in range(0, Frame):
                    Txt_Point.write("\t" + str(data[j][i]))
                Txt_Point.write("\n")
        else:
            for i in range(0, Width):
                Txt_Point.write(Wavedata[i])
                for j in range(0, Frame):
                    Txt_Point.write("; " + str(data[j][i]))
                Txt_Point.write("\n")

    Txt_Point.close()
    file.close()
    print("done")

def spectralMap_integral(filename, FolderName, spectralMap=True, singleSpectra=False):
    
    Version, Frame, Width, Height, Laser, Date, Time, ExpTime, CWL, Wavedata, WavedataRound = openXMLline(filename)

    file = open(filename, "rb")
    bytes = file.read()

    datatype = from_bytes(bytes, "h", 108)
    frame_width = from_bytes(bytes, "H", 42)
    frame_height = from_bytes(bytes, "H", 656)
    num_frames = from_bytes(bytes, "i", 1446)
    
    print("datatype:", datatype)
    to_np_type = [np.float32, np.int32, np.int16, np.uint16, None, np.float64, np.uint8, None, np.uint32]
    np_type = to_np_type[datatype]
    itemsize = np.dtype(np_type).itemsize
    print("itemsize: ", itemsize)
    print("numpy type:", np_type)
    
    count = frame_width * frame_height
    Px = int(math.sqrt(num_frames))
    Integral = []
    for i in range(0, num_frames):
        print("Showing frame number ", i+1)
        data = np.frombuffer(bytes, dtype=np_type, count=count, offset=4100 + i*count*itemsize)
        Summe = sum(data)
        Integral.append(Summe)
        if singleSpectra == True:
            File = FolderName + "/Frame_" + str((i+1)) + ".png"
            plt.figure()
            plt.plot(WavedataRound, data)
            plt.savefig(File, dpi=300)
            plt.close()
    if spectralMap == True:
        try:
            File = FolderName + "/SpectralMap.png"
            dataInt = np.reshape(Integral, (Px,Px))
            plt.figure()
            plt.imshow(dataInt)
            plt.show()
            plt.close()
        except Exception as e: print(e)
    file.close()

def spectra_from_spe(FileName, spectralMap=True, singleSpectra=True, convert=True, space="tab", header=True, invert=True):
    print("Filename:", FileName)
    FolderName = time.strftime("Spectra_%Y-%m-%d_%H-%M-%S")
    if singleSpectra == True or convert == True:
        try:
            os.makedirs(FolderName)
            print("Data folder created")
        except:
            print("Data-Folder already exist")
    
    spectralMap_integral(FileName, FolderName, spectralMap=spectralMap, singleSpectra=singleSpectra)
    
    if convert == True:
        convert_txt(FileName, FolderName, space=space, header=header, invert=invert)