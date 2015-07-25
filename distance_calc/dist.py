from xml.etree.ElementTree import parse
import time
import webbrowser

# Reference latitude
office_lat = 41.980262

# Set of bus ids that you want to monitor.
busids = { '1909' }

def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
    busid = bus.findtext('id')
    if busid in busids:
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        dist = distance(lat, office_lat)
        print dist
        direction = bus.findtext('d')
        print('%s %s %0.2f miles' % (busid, direction, dist))
        
        webbrowser.open('http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (lat, lon))

