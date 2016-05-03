fileNMEA={}
fileNMEA['$MVUP']=['time','lat','lon','vel','course','roll','pitch','yaw']

def readDataFile(file,fileType):
    """
    read data from simil NMEA Metis Vela code
    file: path to file, including extension
    fileType: NMEA list 
    """
    in_file = open(file,"r")
    content = in_file.readlines()
    in_file.close()
    nome,data,ora = content[0].split(' - ')
    time=[int(ora[4:6]),int(ora[2:4]),int(ora[0:2])+2]
    tipo=content[1].split(',')[0]
    data={
    label:[] for label in fileNMEA[tipo]
    }
    for item in content[1:]:
        values=item.split(',')
        data['time'].append(values[1])#millis
        data['lat'].append(values[2])
        data['lon'].append(values[4])
        data['vel'].append(values[6])#knots
        data['course'].append(values[8])
        data['roll'].append(values[10])
        data['pitch'].append(values[11])
        data['yaw'].append(values[12])
        #al momento il resto non interessa
    return time,data
 
 
time,data=readDataFile('fileStorage/vela012.txt',fileNMEA)