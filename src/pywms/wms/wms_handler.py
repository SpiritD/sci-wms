'''
Created on Oct 17, 2011

@author: ACrosby
'''
from datetime import date

class wms_handler(object):
    '''
    classdocs
    '''

    def make_action_request(self, requestobj):
        layers = requestobj.GET["LAYERS"]
        try:
            levels = requestobj.GET["ELEVATION"]
            if levels == "":
                levels = "0"
        except:
            levels = "0"
        '''
        Implement more styles and things here
        '''
        try:
            time = requestobj.GET["TIME"]
            if time == "":
                now = date.today().isoformat()
                time = now + "T00:00:00"#
        except:
            now = date.today().isoformat()
            time = now + "T00:00:00"#
        time = time.split("/")
        #print time
        for i in range(len(time)):
            #print time[i]
            if len(time[i]) == 16:
                time[i] = time[i] + ":00"
            elif len(time[i]) == 13:
                time[i] = time[i] + ":00:00"
            elif len(time[i]) == 10:
                time[i] = time[i] + "T00:00:00"
        if len(time) > 1:
            timestart = time[0]
            timeend = time[1]
        else:
            timestart = time[0]
            timeend = time[0]
        box = requestobj.GET["BBOX"]
        box = box.split(",")
        latmin = box[1]
        latmax = box[3]
        lonmin = box[0]
        lonmax = box[2]

        height = requestobj.GET["HEIGHT"]
        width = requestobj.GET["WIDTH"]
        styles = requestobj.GET["STYLES"].split(",")[0].split("_")
        colormap = styles[2].replace("-", "_")
        climits = styles[3:5]
        topology_type = styles[5]
        magnitude_bool = styles[6]
        #reqtype = requestobj.GET["REQUEST"]

        class action_request:
            pass

        action_request.GET = {u'latmax':latmax, u'lonmax':lonmax,
                          u'projection':u'merc', u'layer':levels,
                          u'datestart':timestart, u'dateend':timeend,
                          u'lonmin':lonmin, u'latmin':latmin,
                          u'height':height, u'width':width,
                          u'actions':("image," + \
                          "," + styles[0] + "," + styles[1]),
                          u'colormap': colormap,
                          u'climits': climits,
                          u'variables': layers,
                          u'topologytype': topology_type,
                          u'magnitude': magnitude_bool,
                          }
        if float(lonmax)-float(lonmin) < .0001:
            action_request == None

        return action_request



    def __init__(self, requestobj):
        '''
        Constructor
        '''
        self.request = requestobj