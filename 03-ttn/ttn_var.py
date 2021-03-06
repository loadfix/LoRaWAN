#
# TTN Gateway
#

# e.g. x = bytearray([ 0x01, 0x67, 0xc6, 0x00, 0x11, 0x22, 0x33, 0xff, 0xff, 0x44, 0x55, 0x66 ])  
x = bytearray([ 0x01, 0x67, 0xc6, 0x00, 0x??, 0x??, 0x??, 0xff, 0xff, 0x??, 0x??, 0x?? ])  
UDP_IP   = "52.169.76.203"
UDP_PORT = 1700

LATI = 25.058
LONG = 121.532
ALTI = 0
RXNB = 0    
RXOK = 0    
RXFW = 0    
ACKR = 0.0  
DWNB = 0    
TXNB = 0    
PFRM = "Single Channel Gateway"
MAIL = "benhoope@amazon.com"
DESC = "Test"


#
# TTN Device
#
DEV_ADDR = [0x00, 0x18, 0x5F, 0x86, 0x9B, 0x48, 0xAD, 0x3F]    # e.g. [0x00, 0x00, 0x00, 0x00]
NWS_KEY  = 0x42, 0x4C, 0x47, 0x22, 0x3D, 0x9B, 0xA6, 0x9A, 0xB8, 0xB7, 0x70, 0xA0, 0x49, 0x1C, 0xCA, 0xC3[]    # e.g. [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
APPS_KEY = [0x14, 0x35, 0xCB, 0x74, 0x56, 0x41, 0xE8, 0x7F, 0x1E, 0x9E, 0xF3, 0x88, 0xA0, 0xB4, 0x51, 0x91]    # e.g. [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

CHAN = 0
RFCH = 0
FREQ = 915.0
STAT = 1
MODU = "LORA"
DATR = "SF7BW125"
CODR = "4/5"
LSNR = 9
RSSI = -32
SIZE = 19


#
# TTN Application
#
user, password = "<AppID>", "<AppKey>"
ttn_router = "eu.thethings.network"




