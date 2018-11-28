from GPSPhoto import gpsphoto

def getTag(path):
    metaData = gpsphoto.getGPSData(path)
    geoLocalization = [0,0]

    for tag in metaData.keys():
        #print ("%s: %s" % (tag, metaData[tag]))
        if tag == "Latitude":
            geoLocalization[0] = metaData[tag]
        if tag == "Longitude":
            geoLocalization[1] = metaData[tag]

    return geoLocalization