# Please do not replace the text anything but sc.
# Ini sc gratisan tolong hargain yg buat dict!
# Rework by Yepz
# Id : Myyepz
# Thanks to team hello world
# -*- coding: utf-8 -*-
'''
ฟรีเครดิตทั้งหมดเป็นของฉัน Zero Cool
อย่าขายหรือให้เช่า!
© 2018 Self Bot
'''
from important import *
import pytz, datetime, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia, html5lib
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
import requests

# ตั้งค่าอาร์กิวเมนต์
parser = argparse.ArgumentParser (description = 'Selfbot Self Bot')
parser.add_argument ('- t', '- token', พิมพ์ = str, metavar = '', จำเป็น = False, help = 'Token | ตัวอย่าง: Exxxx')
parser.add_argument ('- e', '--email', พิมพ์ = str, default = '', metavar = '', จำเป็น = False, help = 'ที่อยู่อีเมล | ตัวอย่าง: example@xxx.xx')
parser.add_argument ('- p', '--passwd', พิมพ์ = str, default = '', metavar = '', ต้องการ = False, help = 'รหัสผ่าน | ตัวอย่าง: xxxx')
parser.add_argument ('- a', '--apptype', พิมพ์ = str, default = '', metavar = '', ต้องการ = False, ตัวเลือก = รายการ (ApplicationType._NAMES_TO_VALUES), ช่วย = 'ประเภทแอปพลิเคชัน | ตัวอย่าง: ChromeOS ')
parser.add_argument ('- s', '--systemname', ประเภท = str, default = '', metavar = '', ต้องการ = False, help = 'ชื่อระบบ | ตัวอย่าง: Chrome_OS')
parser.add_argument ('- c', '--channelid', ประเภท = str, default = '', metavar = '', จำเป็น = False, help = 'ID ช่องทาง | ตัวอย่าง: 1341209950')
parser.add_argument ('- T', '--traceback', พิมพ์ = str2bool, nargs = '?', default = False, metavar = '', ต้องการ = False, const = True, ตัวเลือก = [True, False], help = 'ใช้ Traceback | การใช้: จริง / เท็จ')
parser.add_argument ('- S', '--showqr', ชนิด = str2bool, nargs = '?', ค่าเริ่มต้น = False, metavar = '', ต้องการ = False, const = True, ตัวเลือก = [True, False], help = 'แสดง QR | การใช้: จริง / เท็จ')
args = parser.parse_args ()


# ลูกค้าเข้าสู่ระบบ
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
ลอง:
    พิมพ์ ('## ----- ลูกค้าเข้าสู่ระบบ ----- ##')
    บรรทัด = ไม่มี
    ถ้า args.apptype:
        tokenPath = เส้นทาง ('authToken.txt')
        ถ้า tokenPath.exists ():
            tokenFile = tokenPath.open ('r')
        อื่น:
            tokenFile = tokenPath.open ('w +')
        saveAuthToken = tokenFile.read (). strip ()
        authToken = saveAuthToken ถ้า saveAuthToken ไม่ใช่ args.token args.token อื่น
        idOrToken = authToken ถ้า authToken เป็นอย่างอื่น args.email
        ลอง:
            บรรทัด = LINE (idOrToken, args.passwd, appType = args.apptype, systemName = args.systemname, channelId = args.channelid, showQr = args.showqr)
            tokenFile.close ()
            tokenFile = tokenPath.open ('w +')
            tokenFile.write (line.authToken)
            tokenFile.close ()
        ยกเว้น TalkException เป็น talk_error:
            ถ้า args.traceback: traceback.print_tb (talk_error .__ traceback__)
            sys.exit ('++ ข้อผิดพลาด:% s'% talk_error.reason.replace ('_', ''))
        ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
            ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
            sys.exit ('++ ข้อผิดพลาด:% s'% str (ข้อผิดพลาด))
    อื่น:
        สำหรับ appType ใน listAppType:
            tokenPath = เส้นทาง ('authToken.txt')
            ถ้า tokenPath.exists ():
                tokenFile = tokenPath.open ('r')
            อื่น:
                tokenFile = tokenPath.open ('w +')
            saveAuthToken = tokenFile.read (). strip ()
            authToken = saveAuthToken ถ้า saveAuthToken ไม่ใช่ args.token args.token อื่น
            idOrToken = authToken ถ้า authToken เป็นอย่างอื่น args.email
            ลอง:
                บรรทัด = LINE (idOrToken, args.passwd, appType = appType, systemName = args.systemname, channelId = args.channelid, showQr = args.showqr)
                tokenFile.close ()
                tokenFile = tokenPath.open ('w +')
                tokenFile.write (line.authToken)
                tokenFile.close ()
                หยุด
            ยกเว้น TalkException เป็น talk_error:
                พิมพ์ ('++ ข้อผิดพลาด:% s'% talk_error.reason.replace ('_', ''))
                ถ้า args.traceback: traceback.print_tb (talk_error .__ traceback__)
                ถ้า talk_error.code == 1:
                    ต่อ
                sys.exit (1)
            ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
                พิมพ์ ('++ ข้อผิดพลาด:% s'% str (ข้อผิดพลาด))
                ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
                sys.exit (1)
ยกเว้นข้อยกเว้นเป็นข้อผิดพลาด:
    พิมพ์ ('++ ข้อผิดพลาด:% s'% str (ข้อผิดพลาด))
    ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
    sys.exit (1)
ถ้าบรรทัด:
    พิมพ์ ('++ Auth Token:% s'% line.authToken)
    พิมพ์ ('++ Timeline Token:% s'% line.tl.channelAccessToken)
    พิมพ์ ('## ----- เข้าสู่ระบบลูกค้า (สำเร็จ) ----- ##')
อื่น:
    sys.exit ('## ----- ลูกค้าเข้าสู่ระบบ (ล้มเหลว) ----- ##')
#Yepzgans
myMid = line.profile.mid
programStart = time.time ()
oepoll = OEPoll (บรรทัด)
tmp_text = []
lurking = {}
tokenz = {}
#Yepzgans
settings = livejson.File ('setting.json', จริง, เท็จ, 4)
#Yepzgans
bool_dict = {
    จริง: ['ใช่', 'ใช้งานอยู่', 'สำเร็จ', 'เปิด', 'เปิด'],
    เท็จ: ['ไม่', 'ไม่ทำงาน', 'ล้มเหลว', 'ปิด', 'ปิด']
}
# โปรไฟล์สำรอง
profile = line.getContact (myMid)
settings ['myProfile'] ['displayName'] = profile.displayName
settings ['myProfile'] ['statusMessage'] = profile.statusMessage
settings ['myProfile'] ['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail ['result'] ['objectId']
settings ['myProfile'] ['coverId'] = coverId

# ตรวจสอบข้อมูล Json
หากไม่ได้ตั้งค่า:
    พิมพ์ ('## ----- โหลดเริ่มต้น JSON ----- ##')
    ลอง:
        default_settings = line.server.getJson ('https://17hosting.id/default.json')
        settings.update (default_settings)
        พิมพ์ ('## ----- โหลด DEFAULT JSON (สำเร็จ) ----- ##')
    ยกเว้นข้อยกเว้น:
        พิมพ์ ('## ----- โหลดเริ่มต้น JSON (ล้มเหลว) ----- ##')

def restartProgram ():
    พิมพ์ ('## ----- โปรแกรมเริ่มต้นใหม่ ----- ##')
    python = sys.executable
    os.execl (python, python, * sys.argv)

def logError (ข้อผิดพลาดเขียน = True):
    errid = str (random.randint (100, 999))
    filee = open ('tmp / ข้อผิดพลาด /% s.txt'% errid, 'w') ถ้าเขียนอื่นไม่มี
    ถ้า args.traceback: traceback.print_tb (ข้อผิดพลาด. _ traceback__)
    ถ้าเขียน:
        traceback.print_tb (ข้อผิดพลาด. _ traceback__, ไฟล์ = filee)
        filee.close ()
        ด้วย open ('errorLog.txt', 'a') เป็น e:
            e.write ('\ n% s:% s'% (ผิดพลาด, str (ข้อผิดพลาด)))
    พิมพ์ ('ข้อผิดพลาด ++: {ข้อผิดพลาด}'. รูปแบบ (ข้อผิดพลาด = ข้อผิดพลาด))
คำสั่ง def (ข้อความ):
    pesan = text.lower ()
    หากการตั้งค่า ['setKey'] ['สถานะ']:
        ถ้า pesan.startswith (ตั้งค่า ['setKey'] ['สำคัญ']):
            cmd = pesan.replace (การตั้งค่า ['setKey'] ['คีย์'], '')
        อื่น:
            cmd = 'คำสั่งที่ไม่ได้กำหนด'
    อื่น:
        cmd = text.lower ()
    ผลตอบแทน cmd
   
def changeVideoAndPictureProfile (รูป, vids):
    ลอง:
        files = {'file': open (vids, 'rb')}
        obs_params = line.genOBSParams ({'oid': myMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'ชื่อ': 'Hello_World.mp4'}
        data = {'params': obs_params}
        r_vp = line.server.postContent ('{} / คุย / vp / upload.nhn'.format (str (line.server.LINE_OBS_DOMAIN)) data = data, ไฟล์ = ไฟล์)
        ถ้า r_vp.status_code! = 201:
            ส่งคืน "โปรไฟล์การอัพเดทล้มเหลว"
        line.updateProfilePicture (รูป 'vp')
        ส่งคืน "โปรไฟล์การอัพเดทสำเร็จ"
    ยกเว้นข้อยกเว้นเป็น e:
        เพิ่มข้อยกเว้น ("ข้อผิดพลาดเปลี่ยนโปรไฟล์วิดีโอและรูปภาพ% s"% str (e))
        
def changeProfileVideo (เป็น):
    ถ้าการตั้งค่า ['changevp'] ['picture'] == ไม่มี:
        return line.sendReplyMessage (msg_id, ถึง, "รูปถ่ายไม่ออก")
    การตั้งค่า elif ['changevp'] ['video'] == ไม่มี:
        return line.sendReplyMessage (msg_id, ถึง, "วิดีโอการแก้ไข")
    อื่น:
        path = settings ['changevp'] ['video']
        files = {'file': open (เส้นทาง, 'rb')}
        obs_params = line.genOBSParams ({'oid': line.getProfile (). mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent ('{} / คุย / vp / upload.nhn'.format (str (line.server.LINE_OBS_DOMAIN)) data = data, ไฟล์ = ไฟล์)
        ถ้า r_vp.status_code! = 201:
            return line.sendReplyMessage (msg_id, ถึง, "โปรไฟล์การอัปเดต Gagal")
        path_p = settings ['changevp'] ['picture']
        settings ['changevp'] ['status'] = False
        line.updateProfilePicture (path_p, 'vp')

def genImageB64 (เส้นทาง):
    ด้วย open (path, 'rb') เป็น img_file:
        encode_str = img_file.read ()
        b64img = base64.b64encode (encode_str)
        return b64img.decode ('utf-8')

def genUrlB64 (url):
    return base64.b64encode (url.encode ('utf-8')). decode ('utf-8')

def removeCmd (text, key = ''):
    ถ้าคีย์ == '':
        setKey = '' หากไม่ได้ตั้งค่า ['setKey'] ['สถานะ'] การตั้งค่าอื่น ['setKey'] ['คีย์']
    อื่น:
        setKey = สำคัญ
    text_ = text [len (setKey):]
    sep = text_.split ('')
    ส่งคืนข้อความ _ [len (sep [0] + ''):]

def multiCommand (cmd, list_cmd = []):
    ถ้าเป็น True ใน [cmd.startswith (c) สำหรับ c ใน list_cmd]:
        กลับ True
    อื่น:
        กลับเท็จ

def replaceAll (ข้อความ, dic):
    ลอง:
        rep_this = dic.items ()
    ยกเว้น:
        rep_this = dic.iteritems ()
    สำหรับฉัน, j ใน rep_this:
        text = text.replace (i, j)
    ส่งคืนข้อความ

def help ():
    key = '' หากไม่ได้ตั้งค่า ['setKey'] ['สถานะ'] การตั้งค่าอื่น ['setKey'] ['คีย์']
    ด้วย open ('help.txt', 'r') เป็น f:
        text = f.read ()
    helpMsg = text.format (key = key.title ())
    กลับมาช่วยเหลือ MS
    
def helpmsg2 ():
    หากการตั้งค่า ['setKey'] == จริง:
        key = settings ['keyCommand']
    อื่น:
        key = ''
helpMsg2 = "╭───「 Token 」" + "\ n" + \
                    "├" + แป้น + "Win10" + "\ n" + \
                    "├" + แป้น + "Iospad" + "\ n" + \
                    "├" + แป้น + "Chromeos" + "\ n" + \
                    "├" + แป้น + "Desktopwin" + "\ n" + \
                    "├" + แป้น + "Desktopmac" + "\ n" + \
                    "├────────────" + "\ n" + \
                    "├" + แป้น + "Ex: Token win10" + "\ n" + \
                    "├" + แป้น + "Jika Sudah Ketik เสร็จสิ้น" + "\ n" + \
                    "╰────────────"
    ส่งคืน helpMsg2
    
def helpmsg3 ():
    หากการตั้งค่า ['setKey'] == จริง:
        key = settings ['keyCommand']
    อื่น:
        key = ''
    helpMsg3 = "╭───「 giie 」" + "\ n" + \
                    "├" + แป้น + "ฉัน" + "\ n" + \
                    "├" + คีย์ + "โปรไฟล์" + "\ n" + \
                    "├" + คีย์ + "บล็อกลิสต์" + "\ n" + \
                    "├" + แป้น + "เลียนแบบ" + "\ n" + \
                    "├" + แป้น + "Myprofile" + "\ n" + \
                    "├" + คีย์ + "ผู้สร้าง" + "\ n" + \
                    "├────────────" + "\ n" + \
                    "├" + แป้น + "รายชื่อเพื่อน" + "\ n" + \
                    "├" + แป้น + "ออกอากาศ" + "\ n" + \
                    "╰────────────"
    ส่งคืน helpMsg3
    
def helpmsg4 ():
    หากการตั้งค่า ['setKey'] == จริง:
        key = settings ['keyCommand']
    อื่น:
        key = ''
    helpMsg4 = "╭───「กลุ่ม」" + "\ n" + \
                    "├" + แป้น + "Groupinfo" + "\ n" + \
                    "├" + แป้น + "Grouplist" + "\ n" + \
                    "├" + คีย์ + "รายชื่อสมาชิก" + "\ n" + \
                    "├" + แป้น + "Openqr" + "\ n" + \
                    "├" + แป้น + "Closeqr" + "\ n" + \
                    "├" + แป้น + "ChangeGroupName <name>" + "\ n" + \
                    "├" + แป้น + "ChangeGroupPict" + "\ n" + \
                    "├" + แป้น + "Kickall" + "\ n" + \
                    "├" + แป้น + "ยกเลิกทั้งหมด" + "\ n" + \
                    "├" + แป้น + "Tagall" + "\ n" + \
                    "├" + แป้น + "Lurk" + "\ n" + \
                    "├" + แป้น + "เตะ <พูดถึง>" + "\ n" + \
                    "├" + แป้น + "Vkick <Mention>" + "\ n" + \
                    "├" + แป้น + "Greet" + "\ n" + \
                    "├────「ระยะไกล」" + "\ n" + \
                    "├" + แป้น + "เปิด <NumberGroup>" + "\ n" + \
                    "├" + แป้น + "ปิด <NumberGroup>" + "\ n" + \
                    "╰────────────"
    ส่งคืน helpMsg4
    
def helpmsg5 ():
    หากการตั้งค่า ['setKey'] == จริง:
        key = settings ['keyCommand']
    อื่น:
        key = ''
    helpMsg5 = "╭───「การตั้งค่า」" + "\ n" + \
                    "├" + แป้น + "SetKey" + "\ n" + \
                    "├" + แป้น + "เพิ่มอัตโนมัติ" + "\ n" + \
                    "├" + แป้น + "ตอบกลับอัตโนมัติ" + "\ n" + \
                    "├" + แป้น + "AutoRespondMention" + "\ n" + \
                    "├" + แป้น + "อ่านอัตโนมัติ <เปิด / ปิด>" + "\ n" + \
                    "├" + แป้น + "CheckContact <เปิด / ปิด>" + "\ n" + \
                    "├" + แป้น + "CheckPost <เปิด / ปิด>" + "\ n" + \
                    "├" + แป้น + "CheckSticker <เปิด / ปิด>" + "\ n" + \
                    "╰────────────"
    ส่งคืน helpMsg5
def helpmsg6 ():
    หากการตั้งค่า ['setKey'] == จริง:
        key = settings ['keyCommand']
    อื่น:
        key = ''
    helpMsg6 = "╭───「สื่อ」" + "\ n" + \
                    "├" + แป้น + "Musik 「ข้อความ」" + "\ n" + \
                    "├" + แป้น + "รูปภาพ「ข้อความ」" + "\ n" + \
                    "├" + แป้น + "Gambar 「ข้อความ」" + "\ n" + \
                    "├" + แป้น + "Playvidio 「ข้อความ」" + "\ n" + \
                    "├" + แป้น + "Listoken" + "\ n" + \
                    "╰────────────"
    ส่งคืน helpMsg6

def parsingRes (res):
    ผลลัพธ์ = ''
    textt = res.split ('\ n')
    สำหรับข้อความใน textt:
        หาก True ไม่อยู่ใน [text.startswith (s) สำหรับ s ใน ['╭', '├', '│', '╰']]:
            result + = '\ n│' + ข้อความ
        อื่น:
            if text == textt [0]:
                ผลลัพธ์ + = ข้อความ
            อื่น:
                ผลลัพธ์ + = '\ n' + ข้อความ
    ส่งคืนผลลัพธ์

def กล่าวถึงสมาชิก (ถึง, mids = []):
    ถ้า myMid เป็น mids: mids.remove (myMid)
    parsed_len = len (กลาง) // 20 + 1
    ผลลัพธ์ = '╭───「พูดถึง」 \ n'
    พูดถึง = '@zeroxyuuki \ n'
    ไม่ = 0
    สำหรับจุดอยู่ในช่วง (parsed_len):
        ผู้กล่าวถึง = []
        สำหรับ mid in mids [จุด * 20: (จุด + 1) * 20]:
            ไม่มี + = 1
            ผลลัพธ์ + = '│% i % s '% (ไม่พูดถึง)
            slen = len (ผลลัพธ์) - 12
            elen = len (ผลลัพธ์) + 3
            พูดถึง. ผนวก ({'S': str (slen), 'E': str (elen - 4), 'M': mid})
            ถ้า mid == mids [-1]:
                result + = '╰───「 Self Bot 」 \ n'
        ถ้าผลลัพธ์:
            ถ้า result.endswith ('\ n'): result = result [: - 1]
            line.sendMessage (ถึง, ผลลัพธ์, {'MENTION': json.dumps ({'MENTIONEES': กล่าวถึง}}), 0)
        ผลลัพธ์ = ''
def cloneProfile (กลาง):
    contact = line.getContact (กลาง)
    profile = line.getProfile ()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile (รายละเอียด)
    หากผู้ติดต่อรูปภาพสถานะ:
        pict = line.downloadFileURL ('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture (PICT)
    coverId = line.getProfileDetail (กลาง) ['ผลลัพธ์'] ['objectId']
    line.updateProfileCoverById (coverId)

def backupProfile ():
    profile = line.getContact (myMid)
    settings ['myProfile'] ['displayName'] = profile.displayName
    settings ['myProfile'] ['pictureStatus'] = profile.pictureStatus
    settings ['myProfile'] ['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail () ['ผลลัพธ์'] ['objectId']
    settings ['myProfile'] ['coverId'] = str (coverId)

def restoreProfile ():
    profile = line.getProfile ()
    profile.displayName = settings ['myProfile'] ['displayName']
    profile.statusMessage = settings ['myProfile'] ['statusMessage']
    line.updateProfile (รายละเอียด)
    หากการตั้งค่า ['myProfile'] ['pictureStatus']:
        pict = line.downloadFileURL ('http://dl.profile.line-cdn.net/' + การตั้งค่า ['myProfile'] ['pictureStatus'])
        line.updateProfilePicture (PICT)
    coverId = settings ['myProfile'] ['coverId']
    line.updateProfileCoverById (coverId)

def executeCmd (msg, ข้อความ, txt, cmd, msg_id, ผู้รับ, ผู้ส่ง, ถึง, setKey):
    หาก cmd == '@logoutbot':
        line.sendReplyMessage (msg_id, ถึง, 'Bot จะออกจากระบบ')
        sys.exit ('## ----- โปรแกรมหยุด ----- ##')
    ถ้า cmd == "ผู้สร้าง":
        line.sendReplyMessage (msg_id, ถึง, "ติดต่อ Dibawah Ini \ nAdalah Creator Bot")
        line.sendContact (เพื่อ "u975a1d526d06a8dad7bbbb9b4e64f30b")
    ถ้า cmd == "listoken":
        helpMsg2 = helpmsg2 ()
        ty = line.getContact (ผู้ส่ง)
        a = {'MSG_SENDER_NAME': line.getContact (ผู้ส่ง) .displayName, 'MSG_SENDER_ICON': ​​'http://dl.profile.line.naver.jp' +
 STR (ty.picturePath)}
        line.sendReplyMessage (msg_id, ถึง, str (helpMsg2), contentMetadata = a)
    ถ้า cmd == "ตัวเอง":
        helpMsg3 = helpmsg3 ()
        ty = line.getContact (ผู้ส่ง)
        a = {'MSG_SENDER_NAME': line.getContact (ผู้ส่ง) .displayName, 'MSG_SENDER_ICON': ​​'http://dl.profile.line.naver.jp' +
 STR (ty.picturePath)}
        line.sendReplyMessage (msg_id, ถึง, str (helpMsg3), contentMetadata = a)
    ถ้า cmd == "กลุ่ม":
        helpMsg4 = helpmsg4 ()
        ty = line.getContact (ผู้ส่ง)
        a = {'MSG_SENDER_NAME': line.getContact (ผู้ส่ง) .displayName, 'MSG_SENDER_ICON': ​​'http://dl.profile.line.naver.jp' +
 STR (ty.picturePath)}
        line.sendReplyMessage (msg_id, ถึง, str (helpMsg4), contentMetadata = a)
    หาก cmd == "การตั้งค่า":
        helpMsg5 = helpmsg5 ()
        ty = line.getContact (ผู้ส่ง)
        a = {'MSG_SENDER_NAME': line.getContact (ผู้ส่ง) .displayName, 'MSG_SENDER_ICON': ​​'http://dl.profile.line.naver.jp' +
 STR (ty.picturePath)}
        line.sendReplyMessage (msg_id, ถึง, str (helpMsg5), contentMetadata = a)
    ถ้า cmd == "media":
        helpMsg6 = helpmsg6 ()
        ty = line.getContact (ผู้ส่ง)
        a = {'MSG_SENDER_NAME': line.getContact (ผู้ส่ง) .displayName, 'MSG_SENDER_ICON': ​​'http://dl.profile.line.naver.jp' +
 STR (ty.picturePath)}
        line.sendReplyMessage (msg_id, ถึง, str (helpMsg6), contentMetadata = a)
    elif cmd == '@logoutdevicee':
        line.logout ()
        sys.exit ('## ----- ลูกค้า LOGOUT ----- ##')
    elif cmd == 'เริ่มต้นใหม่':
        line.sendReplyMessage (msg_id ถึง 'Bot จะรีสตาร์ทโปรดรอจนกว่า bot จะสามารถทำงานได้♪')
        settings ['restartPoint'] = ถึง
        restartProgram ()
    elif cmd == 'ความช่วยเหลือ':
        line.sendReplyMessage (msg_id, ถึง, help ())
    elif cmd == 'speed':
        start = time.time ()
        line.sendReplyMessage (msg_id, ถึง, 'กำลังตรวจสอบความเร็ว')
        elapse = time.time () - เริ่ม
        line.sendReplyMessage (msg_id, ถึง, 'ข้อความที่ส่งความเร็วใช้เวลา% s วินาที'% str (ล่วงเลย))
    elif cmd == 'me':
           msg.contentType = 13
           msg.contentMetadata = {'mid': msg._from}
           line.sendReplyMessage (msg_id, ถึง, ไม่มี, contentMetadata = {'mid': msg._from}, contentType = 13)
           path = line.getContact (msg.contentMetadata ["mid"]) picturePath
    elif cmd == "changevp":
settings ["changevp"] = จริง
client.sendReplyMessage (msg_id, ถึง, "Kirim video nya")
    elif cmd == 'runtime':
        runtime = time.time () - programStart
        line.sendReplyMessage (msg_id, ถึง, 'Bot ทำงานอยู่ใน' + format_timespan (runtime))
    elif cmd == 'ผู้แต่ง':
        line.sendReplyMessage (msg_id, ถึง, 'Author is linepy')
    elif cmd == 'about':
        res = '╭───「เกี่ยวกับ」'
        res + = '\ n├ประเภท: Self Bot'
        res + = '\ n├เวอร์ชัน: 3.0.8'
        res + = '\ n├ Library: linepy'
        res + = '\ n├ขอขอบคุณเป็นพิเศษถึง'
        res + = '\ n├ทีม Hello World'
        res + = '\ n╰──────────'
        line.sendReplyMessage (msg_id, ถึง, res)
    elif cmd == 'สถานะ':
res + = '\ n├เพิ่มอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoAdd'] ['สถานะ']] [1]
        res + = '\ n├การเข้าร่วมอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoJoin'] ['สถานะ']] [1]
        res + = '\ n├ตอบกลับอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoRespond'] ['สถานะ']] [1]
        res + = '\ n├พูดถึงการตอบกลับอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoRespondMention'] ['สถานะ']] [1]
        res + = '\ n├อ่านอัตโนมัติ:' + bool_dict [การตั้งค่า ['autoRead']] [1]
        res + = '\ n├คีย์การตั้งค่า:' + bool_dict [การตั้งค่า ['setKey'] ['สถานะ']] [1]
        res + = '\ n├เลียนแบบ:' + bool_dict [การตั้งค่า ['เลียนแบบ'] ['สถานะ']] [1]
        res + = '\ n├ทักทายเข้าร่วม:' + bool_dict [การตั้งค่า ['ทักทาย'] ['เข้าร่วม'] ['สถานะ']] [1]
        res + = '\ n├ลาการทักทาย:' + bool_dict [การตั้งค่า ['ทักทาย'] ['ออก'] ['สถานะ']] [1]
        res + = '\ n├ตรวจสอบรายชื่อผู้ติดต่อ:' + bool_dict [การตั้งค่า ['checkContact']] [1]
        res + = '\ n├ตรวจสอบโพสต์:' + bool_dict [การตั้งค่า ['checkPost']] [1]
        res + = '\ n├ตรวจสอบสติ๊กเกอร์:' + bool_dict [การตั้งค่า ['checkSticker']] [1]
        res + = '\ n╰───「 Self Bot 」'
        line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
    elif cmd == 'ยกเลิก':
        aborted = เท็จ
        ถ้าจะอยู่ในการตั้งค่า ['changeGroupPicture']:
            การตั้งค่า [ 'changeGroupPicture']. ลบ (เพื่อ)
            line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนรูปภาพกลุ่มถูกยกเลิก')
            aborted = True
        หากการตั้งค่า ['changePictureProfile']:
            settings ['changePictureProfile'] = เท็จ
            line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนโปรไฟล์ภาพที่ถูกยกเลิก')
            aborted = True
        หากการตั้งค่า ['changeCoverProfile']:
            settings ['changeCoverProfile'] = เท็จ
            line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนโปรไฟล์การยกเลิก')
            aborted = True
        หากไม่ถูกยกเลิก:
            line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวล้มเหลว, ไม่มีสิ่งใดที่จะยกเลิก')
    elif cmd.startswith ('ข้อผิดพลาด'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「ข้อผิดพลาด」'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│•ข้อผิดพลาด {key}'
        res + = '\ n│• {key} บันทึกข้อผิดพลาด'
        res + = '\ n│• {key} การรีเซ็ตข้อผิดพลาด'
        res + = '\ n│• {key} รายละเอียดข้อผิดพลาด <errid>'
        res + = '\ n╰───「 Self Bot 」'
        หาก cmd == 'ข้อผิดพลาด':
line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif cond [0] .lower () == 'บันทึก':
            ลอง:
                filee = open ('errorLog.txt', 'r')
            ยกเว้น FileNotFoundError:
                return line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการแสดงบันทึกข้อผิดพลาด, ไม่พบไฟล์บันทึกข้อผิดพลาด')
            ข้อผิดพลาด = [err.strip () สำหรับข้อผิดพลาดใน filee.readlines ()]
            filee.close ()
            หากไม่ใช่ข้อผิดพลาด: ส่งคืน line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการบันทึกข้อผิดพลาดการแสดงผล, บันทึกข้อผิดพลาดที่ว่างเปล่า')
            res = '╭───「บันทึกข้อผิดพลาด」'
            res + = '\ n├รายการ:'
            parsed_len = len (ข้อผิดพลาด) // 200 + 1
            ไม่ = 0
            สำหรับจุดอยู่ในช่วง (parsed_len):
                สำหรับข้อผิดพลาดในข้อผิดพลาด [จุด * 200: (จุด + 1) * 200]:
                    ถ้าไม่ใช่ข้อผิดพลาด: ดำเนินการต่อ
                    ไม่มี + = 1
                    res + = '\ n│% i % s '% (ไม่ผิดพลาด)
                    หากข้อผิดพลาด == ข้อผิดพลาด [-1]:
                        res + = '\ n╰───「 Self Bot 」'
                ถ้า res:
                    ถ้า res.startswith ('\ n'): res = res [1:]
                    line.sendReplyMessage (msg_id, ถึง, res)
                res = ''
        elif cond [0] .lower () == 'รีเซ็ต':
            filee = open ('errorLog.txt', 'w')
            filee.write ( '')
            filee.close ()
            shutil.rmtree ('tmp / errors /', ign_errors = True)
            os.system ('mkdir tmp / ข้อผิดพลาด')
            line.sendReplyMessage (msg_id, ถึง, 'บันทึกข้อผิดพลาดการรีเซ็ตสำเร็จ')
        elif cond [0] .lower () == 'detail':
            หาก len (cond) <2:
                ส่งคืน line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
            errid = cond [1]
            หาก os.path.exists ('tmp / errors /% s.txt'% errid):
                ด้วย open ('tmp / errors /% s.txt'% errid, 'r') เป็น f:
                    line.sendReplyMessage (msg_id, ถึง, f.read ())
            อื่น:
                return line.sendReplyMessage (msg_id, ถึง, 'ข้อผิดพลาดการแสดงรายละเอียดล้มเหลว, errorid ไม่ถูกต้อง')
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif txt.startswith ('setkey'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
res = '╭───「คีย์การตั้งค่า」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['setKey'] ['สถานะ']] [1]
        res + = '\ n├ Key:' + settings ['setKey'] ['key']. title ()
        res + = '\ n├การใช้งาน:'
        res + = '\ n│•ปุ่มกด'
        res + = '\ n│• Setkey <เปิด / ปิด>'
        res + = '\ n│• Setkey <key>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า txt == 'setkey':
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['setKey'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'การเปิดใช้งานไม่สำเร็จ setkey, setkey แอ็คทีฟแล้ว')
            อื่น:
                settings ['setKey'] ['status'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'setkey การเปิดใช้งานสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['setKey'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการยกเลิกการใช้งาน setkey, setkey ใช้งานไม่ได้แล้ว')
            อื่น:
                settings ['setKey'] ['status'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'setkey ปิดการใช้งานสำเร็จ')
        อื่น:
            settings ['setKey'] ['key'] = texttl
            line.sendReplyMessage (msg_id, เป็น, 'การเปลี่ยนคีย์สำเร็จเป็น (% s)'% textt)
    elif cmd.startswith ("musik"):
        query = msg.text.replace ("musik", "")
        search = query.replace ("", "+")
        ผลลัพธ์ = requests.get ("https://api.zicor.ooo/joox.php?song= {}" .format (str (ค้นหา)))
        data = result.text
        data = json.loads (data)
        ret_ = "- ••• >> เล่นดนตรี << ••• -"
        ret_ + = "\ n- Judul: {}". format (data ["title"])
        ret_ + = "\ n- บทความ: {}". รูปแบบ (ข้อมูล ["นักร้อง"])
        ret_ + = "\ n- Lirik: \ n {}". รูปแบบ (ข้อมูล ["บทกวี"])
        line.sendImageWithURL (ถึง, ข้อมูล ["ภาพ"])
        line.sendReplyMessage (msg_id, ถึง, ret_)
        line.sendAudioWithURL (ไปยังข้อมูล ["url"])
    elif cmd.startswith ("image"):
           sep = msg.text.split ("")
           textnya = msg.text.replace (sep [0] + "", "")
           เส้นทาง = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "& chts = FFFFFF, 70 & chf = bg, s, 000000"
           line.sendImageWithURL (msg.to เส้นทาง)
    elif cmd.startswith ("playvidio"):
   # if msg._from ในผู้ดูแลระบบ:
        ลอง:
            sep = msg.text.split ("")
            textToSearch = msg.text.replace (sep [0] + "", "")
            query = urllib.parse.quote (textToSearch)
            SEARCH_URL = "https://www.youtube.com/results?search_query="
            mozhdr = {'ตัวแทนผู้ใช้': 'Mozilla / 5.0 (Windows; U; Windows NT 5.1; en-GB; rv: 1.9.0.3) Gecko / 2008092417 Firefox / 3.0.3'}
            sb_url = search_url + ข้อความค้นหา
            sb_get = requests.get (sb_url, ส่วนหัว = mozhdr)
            soupeddata = BeautifulSoup (sb_get.content, "html.parser")
            yt_links = soupeddata.find_all ("a", class_ = "yt-uix-tile-link")
            x = (yt_links [1])
            yt_href = x.get ("href")
            yt_href = yt_href.replace ("watch? v =", "")
            qx = "https://youtu.be" + str (yt_href)
            vid = pafy.new (qx)
            กระแส = vid.streams
            best = vid.getbest ()
            best.resolution, best.extension
            สำหรับในสตรีม:
me = best.url
                hasil = ""
                title = "Judul [" + vid.title + "]"
                ผู้เขียน = '\ n \ nâ ???? ผู้แต่ง: '+ str (vid.author)
                durasi = '\ nâ ???? ระยะเวลา: '+ str (vid.duration)
                suka = ​​'\ nâ ???? ไลค์: '+ str (vid.likes)
                rating = '\ nâ ???? คะแนน: '+ str (vid.rating)
                deskripsi = '\ nâ ???? คำอธิบาย: '+ str (vid.description)
                line.sendVideoWithURL (msg.to ฉัน)
                line.sendReplyMessage (msg_id, ถึง, ชื่อ + ผู้แต่ง + durasi + suka + ให้คะแนน + deskripsi)
        ยกเว้นข้อยกเว้นเป็น e:
                line.sendReplyMessage (msg_id, ถึง, str (e))
    elif cmd.startswith ("open"):
 # if msg._from ในเจ้าของ:
        แยก = text.split ("")
        หมายเลข = text.replace (แยก [0] + "", "")
        groups = line.getGroupIdsJoined ()
        ret_ = ""
        ลอง:
            กลุ่ม = กลุ่ม [int (จำนวน) -1]
            G = line.getGroup (กลุ่ม)
            G.preventedJoinByTicket = False
            line.updateGroup (G)
            ลอง:
                gCreator = G.creator.mid
                dia = line.getContact (gCreator)
                zx = ""
                zxc = ""
                zx2 = []
                xpesan = '<Sukses Open Qr> \ n •ผู้สร้าง:'
                diaa = str (dia.displayName)
                pesan = ''
                pesan2 = pesan + "@ a \ n"
                xlen = str (len (zxc) + len (xpesan))
                xlen2 = str (len (zxc) + len (pesan2) + len (xpesan) -1)
                zx = {'S': xlen, 'E': xlen2, 'M': dia.mid}
                zx2.append (ZX)
                zxc + = pesan2
            ยกเว้น:
                gCreator = "Tidak ditemukan"
            ถ้า G.invitee ไม่ใช่:
                gPending = "0"
            อื่น:
                gPending = str (len (G.invitee))
            ถ้า G.preventedJoinByTicket == จริง:
                gQr = "Tertutup"
                gTicket = "Tidak ada"
            อื่น:
                gQr = "Terbuka"
                gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(G.id)))
            timeCreated = []
            timeCreated.append (time.strftime ("% d-% m-% Y [% H:% M:% S]", time.localtime (int (G.createdTime) / 1,000)))
            ret_ + = xpesan + zxc
            ret_ + = "â ?? ​​¢ Nama: {}". รูปแบบ (G.name)
            ret_ + = "\ nâ ?? ¢กลุ่ม Qr: {}". รูปแบบ (gQr)
            ret_ + = "\ nâ ?? ¢ Pendingan: {}". รูปแบบ (gPending)
            ret_ + = "\ nâ ?? ¢ตั๋วกลุ่ม: {}". รูปแบบ (gTicket)
            ret_ + = ""
            line.sendMessage (ผู้รับ, ret_, contentMetadata = {'เมนทอล': str ('{"MENTIONEES":' + json.dumps (zx2) .replace ('', '' + + '}')}, contentType = 0 )
        ยกเว้น:
            ผ่านไป
    elif cmd.startswith ("gambar"):
            query = msg.text.replace ("gambar", "")
            r = requests.get ("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + การสืบค้น + "? offset = 1")
            ข้อมูล = r.text
            ข้อมูล = json.loads (r.text)
            ถ้าข้อมูล! = []:
                สำหรับอาหารในข้อมูล:
                    line.sendImageWithURL (msg.to, str (อาหาร ["url"]))
    elif cmd.startswith ('autoadd'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「เพิ่มอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoAdd'] ['สถานะ']] [1]
        res + = '\ n├ตอบกลับ:' + bool_dict [การตั้งค่า ['autoAdd'] ['ตอบกลับ']] [0]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoAdd'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} เพิ่มอัตโนมัติ'
        res + = '\ n│• {key} เพิ่มอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} ตอบกลับอัตโนมัติเพิ่ม <เปิด / ปิด>'
        res + = '\ n│• {key} AutoAdd <message>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'autoadd':
line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoAdd'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autoadd เรียบร้อยแล้ว')
            อื่น:
                settings ['autoAdd'] ['status'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จเปิดใช้งาน autoadd')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoAdd'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autoadd ปิดใช้งานแล้ว')
            อื่น:
                การตั้งค่า ['autoAdd'] ['สถานะ'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จปิดการใช้งาน autoadd')
        elif cond [0] .lower () == 'reply':
            หาก len (cond) <2:
                ส่งคืน line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
            ถ้า cond [1] .lower () == 'on':
                หากการตั้งค่า ['autoAdd'] ['ตอบกลับ']:
                    line.sendReplyMessage (msg_id, ถึง, 'ข้อความตอบกลับ autoadd เปิดใช้งานแล้ว')
                อื่น:
                    settings ['autoAdd'] ['reply'] = จริง
                    line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จเปิดใช้งานข้อความตอบกลับอัตโนมัติเพิ่ม')
            elif cond [1] .lower () == 'off':
                หากไม่มีการตั้งค่า ['autoAdd'] ['ตอบกลับ']:
                    line.sendReplyMessage (msg_id, ถึง, 'ข้อความตอบกลับ autoadd ปิดใช้งานแล้ว')
                อื่น:
                    settings ['autoAdd'] ['reply'] = เท็จ
                    line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จปิดการใช้งานข้อความตอบกลับอัตโนมัติเพิ่ม')
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            settings ['autoAdd'] ['message'] = textt
            line.sendReplyMessage (msg_id, ถึง, 'สำเร็จเปลี่ยนข้อความอัตโนมัติเป็น `% s`'% textt)
    elif cmd.startswith ('autojoin'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
res = '╭───「เข้าร่วมอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoJoin'] ['สถานะ']] [1]
        res + = '\ n├ตอบกลับ:' + bool_dict [การตั้งค่า ['autoJoin'] ['ตอบกลับ']] [0]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoJoin'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} AutoJoin'
        res + = '\ n│• {key} AutoJoin <เปิด / ปิด>'
        res + = '\ n│• {key} ตั๋วเข้าร่วมอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} ตอบกลับเข้าร่วมอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} AutoJoin <message>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'autojoin':
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoJoin'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autojoin แอ็คทีฟอยู่แล้ว')
            อื่น:
                การตั้งค่า ['autoJoin'] ['สถานะ'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'Success เปิดใช้งานการเข้าร่วมอัตโนมัติ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoJoin'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autojoin ปิดใช้งานแล้ว')
            อื่น:
                การตั้งค่า ['autoJoin'] ['สถานะ'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'ปิดการใช้งานอัตโนมัติเข้าสู่ความสำเร็จ')
        elif cond [0] .lower () == 'reply':
            หาก len (cond) <2:
                ส่งคืน line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
            ถ้า cond [1] .lower () == 'on':
                หากการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                    line.sendReplyMessage (msg_id, ถึง, 'ข้อความตอบกลับอัตโนมัติเข้าร่วมอยู่แล้ว')
                อื่น:
                    settings ['autoJoin'] ['reply'] = จริง
                    line.sendReplyMessage (msg_id, ถึง, 'สำเร็จเปิดใช้งานข้อความตอบกลับอัตโนมัติเข้าร่วม')
            elif cond [1] .lower () == 'off':
                หากไม่มีการตั้งค่า ['autoJoin'] ['ตอบกลับ']:
                    line.sendReplyMessage (msg_id, ถึง, 'ข้อความตอบกลับปิดการใช้งานอัตโนมัติแล้ว')
                อื่น:
                    settings ['autoJoin'] ['reply'] = เท็จ
                    line.sendReplyMessage (msg_id, ถึง, 'สำเร็จปิดการตอบข้อความอัตโนมัติเข้าร่วม')
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif cond [0] .lower () == 'ticket':
            หาก len (cond) <2:
                ส่งคืน line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
            ถ้า cond [1] .lower () == 'on':
                หากการตั้งค่า ['autoJoin'] ['ตั๋ว']:
                    line.sendReplyMessage (msg_id, ถึง, 'ตั๋วอัตโนมัติเข้าร่วมแล้ว')
                อื่น:
                    การตั้งค่า ['autoJoin'] ['ตั๋ว'] = จริง
                    line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จในการเปิดใช้งานตั๋วอัตโนมัติเข้าร่วม'
            elif cond [1] .lower () == 'off':
                หากไม่มีการตั้งค่า ['autoJoin'] ['ตั๋ว']:
                    line.sendReplyMessage (msg_id, ถึง, 'ตั๋วเข้าร่วมอัตโนมัติปิดใช้งานแล้ว')
                อื่น:
                    การตั้งค่า ['autoJoin'] ['ตั๋ว'] = เท็จ
                    line.sendReplyMessage (msg_id, ถึง, 'การปิดใช้งานตั๋วอัตโนมัติเข้าสู่ความสำเร็จ')
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            settings ['autoJoin'] ['ข้อความ'] = ข้อความ
            line.sendReplyMessage (msg_id, ถึง, 'สำเร็จเปลี่ยนข้อความอัตโนมัติเป็น `% s`'% textt)
    elif cmd.startswith ('autorespondmention'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res = '╭───「ตอบกลับอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoRespondMention'] ['สถานะ']] [1]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoRespondMention'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} AutoRespondMention'
        res + = '\ n│• {key} AutoRespondMention <เปิด / ปิด>'
        res + = '\ n│• {key} AutoRespondMention <message>'
        res + = '\ n╰───「 Self Bot 」'
        หาก cmd == 'การตอบกลับอัตโนมัติ':
line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoRespondMention'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autorespondmention ทำงานอยู่แล้ว')
            อื่น:
                settings ['autoRespondMention'] ['status'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'การเปิดใช้งานระบบตอบรับอัตโนมัติที่ประสบความสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoRespondMention'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'การตอบกลับอัตโนมัติถูกปิดใช้งานแล้ว')
            อื่น:
                settings ['autoRespondMention'] ['status'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'การปิดระบบตอบกลับอัตโนมัติที่ประสบความสำเร็จ')
        อื่น:
            settings ['autoRespondMention'] ['message'] = ข้อความ
            line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนข้อความตอบกลับอัตโนมัติเป็น'% s` '% textt ได้สำเร็จ)
    elif cmd.startswith ('autorespond'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        res = '╭───「ตอบกลับอัตโนมัติ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['autoRespond'] ['สถานะ']] [1]
        res + = '\ n├ข้อความตอบกลับ:' + การตั้งค่า ['autoRespond'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} การตอบกลับอัตโนมัติ'
        res + = '\ n│• {key} การตอบกลับอัตโนมัติ <เปิด / ปิด>'
        res + = '\ n│• {key} AutoRespond <message>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'ตอบกลับอัตโนมัติ':
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['autoRespond'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autorespond active active' แล้ว)
            อื่น:
                การตั้งค่า ['autoRespond'] ['สถานะ'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'การเปิดใช้งานระบบตอบกลับอัตโนมัติที่ประสบความสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoRespond'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Autorespond deactive เรียบร้อยแล้ว')
            อื่น:
                การตั้งค่า ['autoRespond'] ['สถานะ'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'การปิดการใช้งานอัตโนมัติที่ประสบความสำเร็จ')
        อื่น:
            การตั้งค่า ['autoRespond'] ['ข้อความ'] = ข้อความ
            line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนข้อความอัตโนมัติให้เป็น'% s` '% textt ได้สำเร็จ)
    elif cmd.startswith ('autoread'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
หากการตั้งค่า ['autoRead']:
                line.sendReplyMessage (msg_id, ถึง, 'Autoread ทำงานอยู่แล้ว')
            อื่น:
                settings ['autoRead'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'การเปิดใช้งาน Autoread สำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['autoRead']:
                line.sendReplyMessage (msg_id, ถึง, 'Autoread deactive เรียบร้อยแล้ว')
            อื่น:
                settings ['autoRead'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จปิดการใช้งาน Autoread อัตโนมัติ')
    elif cmd.startswith ('checkcontact'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['checkContact']:
                line.sendReplyMessage (msg_id, ถึง, 'Checkcontact แอ็คทีฟแล้ว')
            อื่น:
                settings ['checkContact'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'การเปิดใช้งานสำเร็จ checkcontact')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['checkContact']:
                line.sendReplyMessage (msg_id, ถึง, 'Checkcontact ปิดใช้งานแล้ว')
            อื่น:
                settings ['checkContact'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'สำเร็จการยกเลิกการใช้งาน checkcontact')
    elif cmd.startswith ('checkpost'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['checkPost']:
                line.sendReplyMessage (msg_id, ถึง, 'Checkpost active active')
            อื่น:
                settings ['checkPost'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'เครื่องหมายถูกเปิดใช้งานสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่ได้ตั้งค่า ['checkPost']:
                line.sendReplyMessage (msg_id, ถึง, 'Checkpost ปิดการใช้งานแล้ว')
            อื่น:
                settings ['checkPost'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'ด่านตรวจสอบความสำเร็จปิดการใช้งาน')
    elif cmd.startswith ('checksticker'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        ถ้า texttl == 'เปิด':
            หากการตั้งค่า ['checkSticker']:
                line.sendReplyMessage (msg_id, ถึง, 'Checksticker ทำงานแล้ว')
            อื่น:
                settings ['checkSticker'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'ตัวตรวจสอบการเปิดใช้งานสำเร็จ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['checkSticker']:
                line.sendReplyMessage (msg_id, ถึง, 'Checksticker ปิดการใช้งานแล้ว')
            อื่น:
                settings ['checkSticker'] = เท็จ
                line.sendReplyMessage (msg_id, ถึง, 'ตัวตรวจสอบความสำเร็จปิดการใช้งาน')
    elif cmd.startswith ('myprofile'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        profile = line.getProfile ()
        res = '╭───「โปรไฟล์ของฉัน」'
        res + = '\ n├ MID:' + profile.mid
        res + = '\ n├ชื่อที่แสดง:' + str (profile.displayName)
        res + = '\ n├ข้อความสถานะ:' + str (profile.statusMessage)
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} MyProfile'
        res + = '\ n│• {key} MyProfile MID'
        res + = '\ n│• {key} ชื่อ MyProfile'
        res + = '\ n│• {key} MyProfile Bio'
        res + = '\ n│• {key} MyProfile Pict'
        res + = '\ n│• {key} ใบปะหน้าของ MyProfile'
        res + = '\ n│• {key} MyProfile เปลี่ยนชื่อ <name>'
        res + = '\ n│• {key} MyProfile Change Bio <bio>'
        res + = '\ n│• {key} MyProfile Change Pict'
        res + = '\ n│• {key} MyProfile Change Cover'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'myprofile':
ถ้า profile.pictureStatus:
                line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
            cover = line.getProfileCoverURL (profile.mid)
            line.sendImageWithURL (ถึง, str (ปก))
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'mid':
            line.sendReplyMessage (msg_id, ถึง, '「 MID 」 \ n' + str (profile.mid))
        elif texttl == 'name':
            line.sendReplyMessage (msg_id, ถึง, '「ชื่อที่แสดง」 \ n' + str (profile.displayName))
        elif texttl == 'ชีวภาพ':
            line.sendReplyMessage (msg_id, ถึง, 'Message ข้อความสถานะ」 \ n' + str (profile.statusMessage)
        elif texttl == 'pict':
            ถ้า profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL (ไปยังเส้นทาง)
                line.sendReplyMessage (msg_id, ถึง, '「สถานะภาพ」 \ n' + เส้นทาง)
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถแสดงสถานะภาพ, ผู้ใช้ไม่มีสถานะภาพ')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL (profile.mid)
            line.sendImageWithURL (ถึง, str (ปก))
            line.sendReplyMessage (msg_id, ถึง, '「รูปภาพหน้าปก」 \ n' + str (ปก))
        elif texttl.startswith ('เปลี่ยน'):
            ตำรา = textt [7:]
            ตำราl = ตำรา.lower ()
            ถ้าตำรา l.startswith ('ชื่อ'):
                ชื่อ = ข้อความ [5:]
                ถ้า len (ชื่อ) <= 20:
                    profile.displayName = ชื่อ
                    line.updateProfile (รายละเอียด)
                    line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนชื่อสำเร็จแล้วเปลี่ยนเป็นชื่อ'% s` ''%)
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ชื่อที่แสดงเปลี่ยนไม่ได้, ความยาวของชื่อต้องไม่เกิน 20')
            elif ตำราl.startswith ('ชีวภาพ'):
                bio = ตำรา [4:]
                หาก len (ประวัติ) <= 500:
                    profile.statusMessage = ชีวภาพ
                    line.updateProfile (รายละเอียด)
                    line.sendReplyMessage (msg_id, เป็น, 'ข้อความสถานะการเปลี่ยนความสำเร็จเปลี่ยนเป็น `% s`'% bio)
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ข้อความสถานะการเปลี่ยนแปลงล้มเหลวความยาวของไบโอต้องไม่เกิน 500')
            elif ตำราl == 'pict':
                settings ['changePictureProfile'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'กรุณาส่งภาพเพื่อตั้งค่าในรูปโปรไฟล์พิมพ์' {key} Abort` หากต้องการยกเลิกมัน \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพ'.format (key = setKey.title ()))
            elif ตำราl == 'ปก':
                settings ['changeCoverProfile'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'กรุณาส่งภาพเพื่อตั้งค่าในหน้าปกโปรไฟล์พิมพ์' {key} Abort` หากต้องการยกเลิกมัน \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพ'.format (key = setKey.title ()))
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('profile'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        profile = line.getContact (ถึง) ถ้า msg.toType == 0 ไม่มี
        res = '╭───「โปรไฟล์ของฉัน」'
        หากโปรไฟล์:
            res + = '\ n├ MID:' + profile.mid
            res + = '\ n├ชื่อที่แสดง:' + str (profile.displayName)
            ถ้า profile.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (profile.displayNameOverridden)
            res + = '\ n├ข้อความสถานะ:' + str (profile.statusMessage)
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} โปรไฟล์'
        res + = '\ n│• {key} โปรไฟล์กลาง'
        res + = '\ n│• {key} ชื่อโปรไฟล์'
        res + = '\ n│• {key} โปรไฟล์ Bio'
        res + = '\ n│• {key} Pict ของโปรไฟล์'
        res + = '\ n│• {key} หน้าปกโปรไฟล์'
        res + = '\ n│• {key} โปรไฟล์การขโมยโปรไฟล์ <mention>'
        res + = '\ n│• {key} โปรไฟล์ขโมยกลาง <mention>'
        res + = '\ n│• {key} ชื่อขโมยของโปรไฟล์ <mention>'
        res + = '\ n│• {key} โปรไฟล์ Steal Bio <mention>'
        res + = '\ n│• {key} โปรไฟล์ Steal Pict <mention>'
        res + = '\ n│• {key} โปรไฟล์ Steal Cover <mention>'
        res + = '\ n╰───「 Self Bot 」'
        หาก cmd == 'โปรไฟล์':
หากโปรไฟล์:
                ถ้า profile.pictureStatus:
                    line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL (profile.mid)
                line.sendImageWithURL (ถึง, str (ปก))
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'mid':
            ถ้า msg.toType! = 0: return line.sendReplyMessage (msg_id, ถึง, 'ไม่แสดงกลางผู้ใช้ให้ใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            line.sendReplyMessage (msg_id, ถึง, '「 MID 」 \ n' + str (profile.mid))
        elif texttl == 'name':
            ถ้า msg.toType! = 0: return line.sendReplyMessage (msg_id, ถึง, 'ไม่แสดงกลางผู้ใช้ให้ใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            line.sendReplyMessage (msg_id, ถึง, '「ชื่อที่แสดง」 \ n' + str (profile.displayName))
        elif texttl == 'ชีวภาพ':
            ถ้า msg.toType! = 0: return line.sendReplyMessage (msg_id, ถึง, 'ไม่แสดงกลางผู้ใช้ให้ใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            line.sendReplyMessage (msg_id, ถึง, 'Message ข้อความสถานะ」 \ n' + str (profile.statusMessage)
        elif texttl == 'pict':
            ถ้า msg.toType! = 0: return line.sendReplyMessage (msg_id, ถึง, 'ไม่แสดงกลางผู้ใช้ให้ใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            ถ้า profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL (ไปยังเส้นทาง)
                line.sendReplyMessage (msg_id, ถึง, '「สถานะภาพ」 \ n' + เส้นทาง)
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถแสดงสถานะภาพ, ผู้ใช้ไม่มีสถานะภาพ')
        elif texttl == 'cover':
            ถ้า msg.toType! = 0: return line.sendReplyMessage (msg_id, ถึง, 'ไม่แสดงกลางผู้ใช้ให้ใช้คำสั่งนี้เฉพาะในการแชทส่วนตัว')
            cover = line.getProfileCoverURL (profile.mid)
            line.sendImageWithURL (ถึง, str (ปก))
            line.sendReplyMessage (msg_id, ถึง, '「รูปภาพหน้าปก」 \ n' + str (ปก))
        elif texttl.startswith ('steal'):
            ตำรา = textt [6:]
            ตำราl = ตำรา.lower ()
            หากตำรา l.startswith ('โปรไฟล์'):
                หาก 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        profile = line.getContact (พูดถึง ['M'])
                        ถ้า profile.pictureStatus:
line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL (profile.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res = '╭───「โปรไฟล์」'
                        res + = '\ n├ MID:' + profile.mid
                        res + = '\ n├ชื่อที่แสดง:' + str (profile.displayName)
                        ถ้า profile.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (profile.displayNameOverridden)
                        res + = '\ n├ข้อความสถานะ:' + str (profile.statusMessage)
                        res + = '\ n╰───「 Self Bot 」'
                        line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถขโมยโปรไฟล์, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
            elif ตำราl.startswith ('กลาง'):
                res = '╭───「 MID 」'
                ไม่ = 0
                หาก 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        mid = กล่าวถึง ['MENTIONEES'] [0] ['M']
                        return line.sendReplyMessage (msg_id, ถึง, '「 MID 」 \ n' + กลาง)
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, กลาง)
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถขโมยกลาง, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
            elif ตำราl.startswith ('ชื่อ'):
res = '╭───「ชื่อที่แสดง」'
                ไม่ = 0
                หาก 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        profile = line.getContact (กล่าวถึง ['MENTIONEES'] [0] ['M'])
                        return line.sendReplyMessage (msg_id, ถึง, '「ชื่อที่แสดง」 \ n' + str (profile.displayName))
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        profile = line.getContact (กลาง)
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, profile.displayName)
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการขโมยชื่อที่แสดง, ไม่มีผู้ใช้คนใดพูดถึง')
            elif ตำราl.startswith ('ชีวภาพ'):
                res = '╭───「ข้อความสถานะ」'
                ไม่ = 0
                หาก 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        profile = line.getContact (กล่าวถึง ['MENTIONEES'] [0] ['M'])
                        return line.sendReplyMessage (msg_id, ถึง, '「ข้อความสถานะ」 \ n' + str (profile.statusMessage))
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        profile = line.getContact (กลาง)
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่ใช่, profile.statusMessage)
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ข้อความสถานะการขโมยที่ล้มเหลว, ไม่มีผู้ใช้รายหนึ่งพูดถึง')
            elif ตำราl.startswith ('pict'):
                res = '╭───「สถานะภาพ」'
                ไม่ = 0
                หาก 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        profile = line.getContact (กล่าวถึง ['MENTIONEES'] [0] ['M'])
                        ถ้า profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL (ไปยังเส้นทาง)
                            return line.sendReplyMessage (msg_id, ถึง, '「สถานะภาพ」 \ n' + เส้นทาง)
                        อื่น:
                            return line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถขโมยสถานะภาพ, ผู้ใช้ `% s` ไม่ได้มีสถานะภาพ'% profile.displayName)
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
                        profile = line.getContact (กลาง)
                        ไม่มี + = 1
                        ถ้า profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL (ไปยังเส้นทาง)
                            res + = '\ n│% i % s '% (ไม่, เส้นทาง)
                        อื่น:
                            res + = '\ n│% i ไม่พบ '% ไม่
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการขโมยสถานะภาพ, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
            elif ตำราl.startswith ('ปก'):
                res = '╭───「รูปภาพหน้าปก」'
                ไม่ = 0
                หาก 'MENTION' ใน msg.contentMetadata.keys ():
                    mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                    หาก len (กล่าวถึง ['MENTIONEES']) == 1:
                        mid = กล่าวถึง ['MENTIONEES'] [0] ['M']
                        cover = line.getProfileCoverURL (กลาง)
                        line.sendImageWithURL (ถึง, str (ปก))
                        line.sendReplyMessage (msg_id, ถึง, '「รูปภาพหน้าปก」 \ n' + str (ปก))
                    สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                        mid = พูดถึง ['M']
ไม่มี + = 1
                        cover = line.getProfileCoverURL (กลาง)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res + = '\ n│% i % s '% (ไม่ครอบคลุม)
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                อื่น:
                    line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการขโมยภาพปก, ไม่มีผู้ใช้คนใดพูดถึง')
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('เลียนแบบ'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        เป้าหมาย = ''
        หากการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย']:
            ไม่ = 0
            สำหรับเป้าหมายสถานะในการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย'] รายการ ():
                ไม่มี + = 1
                ลอง:
                    name = line.getContact (target) .displayName
                ยกเว้น TalkException:
                    ชื่อ = 'ไม่ทราบ'
                เป้าหมาย + = '\ n│% i % s //% s '% (ไม่, ชื่อ, bool_dict [สถานะ] [1])
        อื่น:
            เป้าหมาย + = '\ n│ไม่มีอะไรเลย'
        res = '╭───「เลียนแบบ」'
        res + = '\ n├สถานะ:' + bool_dict [การตั้งค่า ['เลียนแบบ'] ['สถานะ']] [1]
        res + = '\ n├รายการ:'
        res + = เป้าหมาย
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} เลียนแบบ'
        res + = '\ n│• {key} เลียนแบบ <เปิด / ปิด>'
        res + = '\ n│• {key} เลียนแบบการตั้งค่าใหม่'
        res + = '\ n│• {key} เลียนแบบการเพิ่ม <mention>'
        res + = '\ n│• {key} ล้อเลียน Del <mention>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'เลียนแบบ':
line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl == 'เปิด':
            หากการตั้งค่า ['เลียนแบบ'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Mimic active แล้ว')
            อื่น:
                settings ['mimic'] ['status'] = จริง
                line.sendReplyMessage (msg_id, ถึง, 'การเปิดใช้งานสำเร็จแล้วเลียนแบบ')
        elif texttl == 'ปิด':
            หากไม่มีการตั้งค่า ['เลียนแบบ'] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Mimic deactive แล้ว')
            อื่น:
                settings ['mimic'] ['status'] = False
                line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จปิดใช้งานการเลียนแบบ')
        elif texttl == 'รีเซ็ต':
            settings ['mimic'] ['target'] = {}
            line.sendReplyMessage (msg_id, ถึง, 'การตั้งค่ารายการเลียนแบบสำเร็จ')
        elif texttl.startswith ('เพิ่ม'):
            res = '╭───「เลียนแบบ」'
            res + = '\ n├สถานะ: เพิ่มเป้าหมาย'
            res + = '\ n├ที่เพิ่ม:'
            ไม่ = 0
            หาก 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    settings ['mimic'] ['target'] [mid] = จริง
                    ไม่มี + = 1
                    ลอง:
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「 Self Bot 」'
                line.sendReplyMessage (msg_id, ถึง, res)
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถเพิ่มเป้าหมายเลียนแบบ, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
        elif texttl.startswith ('del'):
            res = '╭───「เลียนแบบ」'
            res + = '\ n├สถานะ: ลบเป้าหมาย'
            res + = '\ n├ถูกลบ:'
            ไม่ = 0
            หาก 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้ากลางในการตั้งค่า ['เลียนแบบ'] ['เป้าหมาย']:
                        settings ['mimic'] ['target'] [mid] = False
                    ไม่มี + = 1
                    ลอง:
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「 Self Bot 」'
                line.sendReplyMessage (msg_id, ถึง, res)
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการลอกเลียนแบบเป้าหมาย, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('ออกอากาศ'):
textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cond = textt.split ('')
        res = '╭───「 Broadcast 」'
        res + = '\ n├ประเภทการออกอากาศ:'
        res + = '\ n│ 1: เพื่อน'
        res + = '\ n│ 2: กลุ่ม'
        res + = '\ n│ 0: ทั้งหมด'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} Broadcast'
        res + = '\ n│• {key} Broadcast <type> <message>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'ออกอากาศ':
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format (key = setKey.title ()))
        elif cond [0] == '1':
            หาก len (cond) <2:
                return line.sendReplyMessage (msg_id, ถึง, 'การออกอากาศล้มเหลว, ไม่พบข้อความ')
            res = '「ออกอากาศ」 \ n'
            res + = textt [2:]
            res + = '\ n \ n 「 Self Bot 」'
            เป้าหมาย = line.getAllContactIds ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง:
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep (0.8)
            line.sendReplyMessage (msg_id, ถึง, 'การออกอากาศสำเร็จให้เพื่อนทุกคนส่งไปยัง% i friends'% len (เป้าหมาย))
        elif cond [0] == '2':
            หาก len (cond) <2:
                return line.sendReplyMessage (msg_id, ถึง, 'การออกอากาศล้มเหลว, ไม่พบข้อความ')
            res = '「ออกอากาศ」 \ n'
            res + = textt [2:]
            res + = '\ n \ n 「 Self Bot 」'
            เป้าหมาย = line.getGroupIdsJoined ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง:
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep (0.8)
            line.sendReplyMessage (msg_id, ถึง, 'การกระจายความสำเร็จไปยังทุกกลุ่มส่งไปยังกลุ่ม% i'% len (เป้าหมาย))
        elif cond [0] == '0':
            หาก len (cond) <2:
                return line.sendReplyMessage (msg_id, ถึง, 'การออกอากาศล้มเหลว, ไม่พบข้อความ')
            res = '「ออกอากาศ」 \ n'
            res + = textt [2:]
            res + = '\ n \ n 「 Self Bot 」'
            เป้าหมาย = line.getGroupIdsJoined () + line.getAllContactIds ()
            สำหรับเป้าหมายในเป้าหมาย:
                ลอง:
                    line.sendMessage (เป้าหมาย res)
                ยกเว้น TalkException:
                    targets.remove (เป้าหมาย)
                    ต่อ
                time.sleep (0.8)
            line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จในการออกอากาศไปยังกลุ่มและเพื่อนทั้งหมดส่งไปยัง% i กลุ่มและเพื่อน ๆ '% len (เป้าหมาย))
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format (key = setKey.title ()))
    elif cmd.startswith ('friendlist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cids = line.getAllContactIds ()
        cids.sort ()
        cnames = []
        ress = []
res = '╭───「รายชื่อเพื่อน」'
        res + = '\ n├รายการ:'
        ถ้า cids:
            รายชื่อ = []
            ไม่ = 0
            หาก len (cids)> 200:
                parsed_len = len (cids) // 200 + 1
                สำหรับจุดอยู่ในช่วง (parsed_len):
                    สำหรับ cid ใน cids [จุด * 200: (จุด + 1) * 200]:
                        ลอง:
                            contact = line.getContact (cid)
                            contacts.append (ติดต่อ)
                        ยกเว้น TalkException:
                            cids.remove (CID)
                            ต่อ
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, contact.displayName)
                        cnames.append (contact.displayName)
                    ถ้า res:
                        ถ้า res.startswith ('\ n'): res = res [1:]
                        if point! = parsed_len - 1:
                            ress.append (ความละเอียดสูง)
                    if point! = parsed_len - 1:
                        res = ''
            อื่น:
                สำหรับ cid ใน cids:
                    ลอง:
                        contact = line.getContact (cid)
                        contacts.append (ติดต่อ)
                    ยกเว้น TalkException:
                        cids.remove (CID)
                        ต่อ
                    ไม่มี + = 1
                    res + = '\ n│% i % s '% (ไม่, contact.displayName)
                    cnames.append (contact.displayName)
        อื่น:
            res + = '\ n│ไม่มีอะไรเลย'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} FriendList'
        res + = '\ n│• {key} ข้อมูล FriendList <num / name>'
        res + = '\ n│• {key} FriendList เพิ่ม <mention>'
        res + = '\ n│• {key} Del FriendList Del <พูดถึง / num / ชื่อ / ทั้งหมด>'
        res + = '\ n╰───「 Self Bot 」'
        ress.append (ความละเอียดสูง)
        ถ้า cmd == 'รายชื่อเพื่อน':
            สำหรับ res ใน ress:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('info'):
            ตำรา = textt [5:]. แยก (',')
            ถ้าไม่ใช่ cids:
                return line.sendReplyMessage (msg_id, ถึง, 'เพื่อนแสดงข้อมูลที่ล้มเหลว, ไม่มีเพื่อนในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL (contact.mid)
                    line.sendImageWithURL (ถึง, str (ปก))
                    res = '╭───「ข้อมูลติดต่อ」'
                    res + = '\ n├ MID:' + contact.mid
                    res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                    res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน cnames:
contact = ผู้ติดต่อ [cnames.index (ชื่อ)]
                        หากผู้ติดต่อรูปภาพสถานะ:
                            line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL (contact.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res = '╭───「ข้อมูลติดต่อ」'
                        res + = '\ n├ MID:' + contact.mid
                        res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                        ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                        res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                        res + = '\ n╰───「 Self Bot 」'
                        line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
        elif texttl.startswith ('เพิ่ม'):
            res = '╭───「รายชื่อเพื่อน」'
            res + = '\ n├สถานะ: เพิ่มเพื่อน'
            res + = '\ n├ที่เพิ่ม:'
            ไม่ = 0
            เพิ่ม = []
            หาก 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ใน cids หรือ mid ในการเพิ่ม:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.findAndAddContactsByMid (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                    added.append (กลาง)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「 Self Bot 」'
                line.sendReplyMessage (msg_id, ถึง, res)
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถเพิ่มผู้ติดต่อไปยังรายชื่อเพื่อนไม่มีผู้ใช้หนึ่งคนพูดถึง')
        elif texttl.startswith ('del'):
            ตำรา = textt [4:]. split (',')
            ถ้าไม่ใช่ cids:
                return line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถลบรายชื่อผู้ติดต่อจากรายชื่อเพื่อนไม่มีเพื่อนในรายการ')
            res = '╭───「รายชื่อเพื่อน」'
            res + = '\ n├สถานะ: เพื่อนสนิท'
            res + = '\ n├ถูกลบ:'
            ไม่ = 0
            ลบแล้ว = []
            หาก 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ไม่อยู่ใน cids หรือ mid ถูกลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.deleteContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                    deleted.append (กลาง)
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    หาก contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.deleteContact (contact.mid)
                        ชื่อ = contact.displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                    deleted.append (contact.mid)
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน cnames:
                        contact = ผู้ติดต่อ [cnames.index (ชื่อ)]
                        หาก contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                            ต่อ
                        ไม่มี + = 1
                        ลอง:
                            line.deleteContact (contact.mid)
                            ชื่อ = contact.displayName
                        ยกเว้น TalkException:
                            ชื่อ = 'ไม่ทราบ'
                        res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                        deleted.append (contact.mid)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับผู้ติดต่อในผู้ติดต่อ:
                            หาก contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                                ต่อ
                            ไม่มี + = 1
                            ลอง:
                                line.deleteContact (contact.mid)
                                ชื่อ = contact.displayName
                            ยกเว้น TalkException:
                                ชื่อ = 'ไม่ทราบ'
                            res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                            deleted.append (contact.mid)
                            time.sleep (0.8)
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'เพื่อนที่ล้มเหลวด้วยชื่อ `% s`, ชื่อไม่อยู่ในรายการ♪'% ชื่อ)
            หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
            res + = '\ n╰───「 Self Bot 」'
            line.sendReplyMessage (msg_id, ถึง, res)
        อื่น:
            สำหรับ res ใน ress:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('blocklist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        cids = line.getBlockedContactIds ()
        cids.sort ()
        cnames = []
        ress = []
        res = '╭───「รายการบล็อก」'
        res + = '\ n├รายการ:'
        ถ้า cids:
            รายชื่อ = []
            ไม่ = 0
            หาก len (cids)> 200:
                parsed_len = len (cids) // 200 + 1
                สำหรับจุดอยู่ในช่วง (parsed_len):
                    สำหรับ cid ใน cids [จุด * 200: (จุด + 1) * 200]:
                        ลอง:
contact = line.getContact (cid)
                            contacts.append (ติดต่อ)
                        ยกเว้น TalkException:
                            cids.remove (CID)
                            ต่อ
                        ไม่มี + = 1
                        res + = '\ n│% i % s '% (ไม่, contact.displayName)
                        cnames.append (contact.displayName)
                    ถ้า res:
                        ถ้า res.startswith ('\ n'): res = res [1:]
                        if point! = parsed_len - 1:
                            ress.append (ความละเอียดสูง)
                    if point! = parsed_len - 1:
                        res = ''
            อื่น:
                สำหรับ cid ใน cids:
                    ลอง:
                        contact = line.getContact (cid)
                        contacts.append (ติดต่อ)
                    ยกเว้น TalkException:
                        cids.remove (CID)
                        ต่อ
                    ไม่มี + = 1
                    res + = '\ n│% i % s '% (ไม่, contact.displayName)
                    cnames.append (contact.displayName)
        อื่น:
            res + = '\ n│ไม่มีอะไรเลย'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} BlockList'
        res + = '\ n│• {key} ข้อมูลบล็อกลิสต์ <num / name>'
        res + = '\ n│• {key} BlockList เพิ่ม <mention>'
        res + = '\ n│• {key} BlockList Del <พูดถึง / num / ชื่อ / ทั้งหมด>'
        res + = '\ n╰───「 Self Bot 」'
        ress.append (ความละเอียดสูง)
        ถ้า cmd == 'blocklist':
            สำหรับ res ใน ress:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('info'):
            ตำรา = textt [5:]. แยก (',')
            ถ้าไม่ใช่ cids:
                return line.sendReplyMessage (msg_id, ถึง, 'ข้อมูลผู้ใช้ที่ถูกบล็อคไม่แสดง, ไม่มีผู้ใช้ในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
contact = รายชื่อ [NUM - 1]
                    หากผู้ติดต่อรูปภาพสถานะ:
                        line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL (contact.mid)
                    line.sendImageWithURL (ถึง, str (ปก))
                    res = '╭───「ข้อมูลติดต่อ」'
                    res + = '\ n├ MID:' + contact.mid
                    res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                    ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                    res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                    res + = '\ n╰───「 Self Bot 」'
                    line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน cnames:
                        contact = ผู้ติดต่อ [cnames.index (ชื่อ)]
                        หากผู้ติดต่อรูปภาพสถานะ:
                            line.sendImageWithURL (ถึง, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL (contact.mid)
                        line.sendImageWithURL (ถึง, str (ปก))
                        res = '╭───「ข้อมูลติดต่อ」'
                        res + = '\ n├ MID:' + contact.mid
                        res + = '\ n├ชื่อที่แสดง:' + str (contact.displayName)
                        ถ้า contact.displayNameOverridden: res + = '\ n├แทนที่ชื่อที่แสดง:' + str (contact.displayNameOverridden)
                        res + = '\ n├ข้อความสถานะ:' + str (contact.statusMessage)
                        res + = '\ n╰───「 Self Bot 」'
                        line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ res (res))
        elif texttl.startswith ('เพิ่ม'):
            res = '╭───「รายการบล็อก」'
            res + = '\ n├สถานะ: เพิ่มบล็อก'
            res + = '\ n├ที่เพิ่ม:'
            ไม่ = 0
            เพิ่ม = []
            หาก 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ใน cids หรือ mid ในการเพิ่ม:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.blockContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                    added.append (กลาง)
                หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
                res + = '\ n╰───「 Self Bot 」'
                line.sendReplyMessage (msg_id, ถึง, res)
            อื่น:
                line.sendReplyMessage (msg_id, ถึง, 'ผู้ติดต่อบล็อกที่ล้มเหลว, ไม่มีผู้ใช้หนึ่งคนพูดถึง')
        elif texttl.startswith ('del'):
            ตำรา = textt [4:]. split (',')
            ถ้าไม่ใช่ cids:
                return line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถปลดบล็อคผู้ติดต่อ, ไม่มีผู้ใช้ในรายการ')
            res = '╭───「รายการบล็อก」'
            res + = '\ n├สถานะ: Del Block'
            res + = '\ n├ถูกลบ:'
            ไม่ = 0
            ลบแล้ว = []
            หาก 'MENTION' ใน msg.contentMetadata.keys ():
                mentions = ast.literal_eval (msg.contentMetadata ['MENTION'])
                สำหรับการกล่าวถึงในการกล่าวถึง ['MENTIONEES']:
                    mid = พูดถึง ['M']
                    ถ้า mid ไม่อยู่ใน cids หรือ mid ถูกลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
line.unblockContact (กลาง)
                        name = line.getContact (กลาง) .displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                    deleted.append (กลาง)
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    contact = รายชื่อ [NUM - 1]
                    หาก contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                        ต่อ
                    ไม่มี + = 1
                    ลอง:
                        line.unblockContact (contact.mid)
                        ชื่อ = contact.displayName
                    ยกเว้น TalkException:
                        ชื่อ = 'ไม่ทราบ'
                    res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                    deleted.append (contact.mid)
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน cnames:
                        contact = ผู้ติดต่อ [cnames.index (ชื่อ)]
                        หาก contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                            ต่อ
                        ไม่มี + = 1
                        ลอง:
                            line.unblockContact (contact.mid)
                            ชื่อ = contact.displayName
                        ยกเว้น TalkException:
                            ชื่อ = 'ไม่ทราบ'
                        res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                        deleted.append (contact.mid)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับผู้ติดต่อในผู้ติดต่อ:
                            หาก contact.mid ไม่ได้อยู่ใน cids และ contact.mid ในลบ:
                                ต่อ
                            ไม่มี + = 1
                            ลอง:
                                line.unblockContact (contact.mid)
                                ชื่อ = contact.displayName
                            ยกเว้น TalkException:
                                ชื่อ = 'ไม่ทราบ'
                            res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                            deleted.append (contact.mid)
                            time.sleep (0.8)
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถปลดบล็อกผู้ใช้ที่มีชื่อ `% s`, ชื่อไม่อยู่ในรายการ♪'% ชื่อ)
            หากไม่มี == 0: res + = '\ n│ไม่มีอะไร'
            res + = '\ n╰───「 Self Bot 」'
            line.sendReplyMessage (msg_id, ถึง, res)
        อื่น:
            สำหรับ res ใน ress:
line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd == 'tagall':
        สมาชิก = []
        ถ้า msg.toType == 1:
            room = line.getCompactRoom (ถึง)
            members = [mem.mid สำหรับ mem ใน room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup (ถึง)
            สมาชิก = [mem.mid สำหรับ mem ใน group.members]
        อื่น:
            return line.sendReplyMessage (msg_id, ถึง, 'สมาชิกที่ไม่กล่าวถึงทั้งหมด, ใช้คำสั่งนี้เฉพาะในห้องแชทหรือกลุ่ม')
        ถ้าสมาชิก:
            พูดถึงสมาชิก (ถึงสมาชิก)
    elif cmd == 'groupinfo':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id ถึง 'ข้อมูลกลุ่มการแสดงที่ล้มเหลวใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        ลอง:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        ยกเว้น:
            ccreator = ไม่มี
            gcreator = 'ไม่พบ'
        ถ้าไม่ได้เป็นกลุ่ม invitee:
            pendings = 0
        อื่น:
            pendings = len (group.invitee)
        qr = 'ปิด' ถ้า group.preventedJoinByTicket อื่น 'เปิด'
        ถ้า group.preventedJoinByTicket:
            ticket = 'ไม่พบ'
        อื่น:
            ticket = 'https://line.me/R/ti/g/' + str (line.reissueGroupTicket (group.id))
        สร้าง = time.strftime ('% d-% m-% Y% H:% M:% S', time.localtime (int (group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「ข้อมูลกลุ่ม」'
        res + = '\ n├ ID:' + group.id
        res + = '\ n├ชื่อ:' + group.name
        res + = '\ n├ผู้สร้าง:' + gcreator
        res + = '\ n├เวลาที่สร้าง:' + สร้างแล้ว
        res + = '\ n├จำนวนสมาชิก:' + str (len (group.members))
        res + = '\ n├จำนวนที่รอดำเนินการ:' + str (pendings)
        res + = '\ n├สถานะ QR:' + qr
        res + = '\ n├ตั๋ว:' + ตั๋ว
        res + = '\ n╰───「 Self Bot 」'
line.sendImageWithURL (ไปยังเส้นทาง)
        ถ้า ccreator:
            line.sendContact (ถึง, ccreator)
        line.sendReplyMessage (msg_id, ถึง, res)
    elif cmd.startswith ('grouplist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        gids = line.getGroupIdsJoined ()
        gnames = []
        ress = []
        res = '╭───「รายชื่อกลุ่ม」'
        res + = '\ n├รายการ:'
        ถ้า gids:
            groups = line.getGroups (gids)
            ไม่ = 0
            ถ้า len (กลุ่ม)> 200:
                parsed_len = len (กลุ่ม) // 200 + 1
                สำหรับจุดอยู่ในช่วง (parsed_len):
                    สำหรับกลุ่มในกลุ่ม [จุด * 200: (จุด + 1) * 200]:
                        ไม่มี + = 1
                        res + = '\ n│% i % s //% i '% (ไม่, group.name, len (group.members))
                        gnames.append (group.name)
                    ถ้า res:
                        ถ้า res.startswith ('\ n'): res = res [1:]
                        if point! = parsed_len - 1:
                            ress.append (ความละเอียดสูง)
                    if point! = parsed_len - 1:
                        res = ''
            อื่น:
                สำหรับกลุ่มในกลุ่ม:
                    ไม่มี + = 1
                    res + = '\ n│% i % s //% i '% (ไม่, group.name, len (group.members))
                    gnames.append (group.name)
        อื่น:
            res + = '\ n│ไม่มีอะไรเลย'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} GroupList'
        res + = '\ n│• {key} GroupList ปล่อยให้ <num / name / all>'
        res + = '\ n╰───「 Self Bot 」'
        ress.append (ความละเอียดสูง)
        ถ้า cmd == 'grouplist':
            สำหรับ res ใน ress:
line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('ออก'):
            ตำรา = textt [6:]. แยก (',')
            leaved = []
            ถ้าไม่ใช่ gids:
                return line.sendReplyMessage (msg_id, ถึง, 'กลุ่มออกจากไม่สำเร็จ, ไม่มีกลุ่มใดในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    ถ้า num <= len (กลุ่ม) และ num> 0:
                        group = กลุ่ม [NUM - 1]
                        ถ้ากลุ่มอยู่ในใบ:
                            line.sendReplyMessage (msg_id, ถึง, 'ออกจากกลุ่ม% s'% group.name ไปแล้ว)
                            ต่อ
                        line.leaveGroup (group.id)
                        leaved.append (group.id)
                        หากไม่ได้อยู่ในใบ:
                            line.sendReplyMessage (msg_id, ถึง, 'สำเร็จออกจากกลุ่ม% s'% group.name)
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถออกจากกลุ่มหมายเลข% i, หมายเลขนอกช่วง'% num)
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน gnames:
                        group = groups [gnames.index (ชื่อ)]
                        ถ้ากลุ่มอยู่ในใบ:
                            line.sendReplyMessage (msg_id, ถึง, 'ออกจากกลุ่ม% s'% group.name ไปแล้ว)
                            ต่อ
                        line.leaveGroup (group.id)
                        leaved.append (group.id)
                        หากไม่ได้อยู่ในใบ:
                            line.sendReplyMessage (msg_id, ถึง, 'สำเร็จออกจากกลุ่ม% s'% group.name)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับ gid ใน gids:
                            ถ้า gid ในใบไม้:
                                ต่อ
                            line.leaveGroup (GID)
                            leaved.append (GID)
                            time.sleep (0.8)
                        หากไม่ได้อยู่ในใบ:
                            line.sendReplyMessage (msg_id, ถึง, 'สำเร็จออกจากกลุ่มทั้งหมด♪')
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'ออกจากกลุ่มด้วยชื่อ `% s`, ชื่อไม่อยู่ในรายการ♪'% ชื่อ)
        อื่น:
            สำหรับ res ใน ress:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('invitlist'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        gids = line.getGroupIdsInvited ()
        gnames = []
        ress = []
        res = '╭───「รายการคำเชิญ」'
        res + = '\ n├รายการ:'
        ถ้า gids:
            groups = line.getGroups (gids)
            ไม่ = 0
            ถ้า len (กลุ่ม)> 200:
                parsed_len = len (กลุ่ม) // 200 + 1
                สำหรับจุดอยู่ในช่วง (parsed_len):
                    สำหรับกลุ่มในกลุ่ม [จุด * 200: (จุด + 1) * 200]:
                        ไม่มี + = 1
res + = '\ n│% i % s //% i '% (ไม่, group.name, len (group.members))
                        gnames.append (group.name)
                    ถ้า res:
                        ถ้า res.startswith ('\ n'): res = res [1:]
                        if point! = parsed_len - 1:
                            ress.append (ความละเอียดสูง)
                    if point! = parsed_len - 1:
                        res = ''
            อื่น:
                สำหรับกลุ่มในกลุ่ม:
                    ไม่มี + = 1
                    res + = '\ n│% i % s //% i '% (ไม่, group.name, len (group.members))
                    gnames.append (group.name)
        อื่น:
            res + = '\ n│ไม่มีอะไรเลย'
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} รายการเชิญ'
        res + = '\ n│• {key} InvitationList ยอมรับ <num / name / all>'
        res + = '\ n│• {key} การปฏิเสธรายการเชิญ <num / name / all>'
        res + = '\ n╰───「 Self Bot 」'
        ress.append (ความละเอียดสูง)
        หาก cmd == 'Invitlist':
            สำหรับ res ใน ress:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        elif texttl.startswith ('ยอมรับ'):
            ตำรา = textt [7:]. แยก (',')
            ได้รับการยอมรับ = []
            ถ้าไม่ใช่ gids:
                return line.sendReplyMessage (msg_id, ถึง, 'กลุ่มยอมรับไม่สำเร็จ, ไม่มีกลุ่มคำเชิญในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    ถ้า num <= len (กลุ่ม) และ num> 0:
                        group = กลุ่ม [NUM - 1]
                        ถ้า group.id เป็นที่ยอมรับ:
                            line.sendReplyMessage (msg_id, ถึง, 'ยอมรับกลุ่ม% s'% group.name แล้ว)
                            ต่อ
                        line.acceptGroupInvitation (group.id)
                        accepted.append (group.id)
                        line.sendReplyMessage (msg_id, ถึง, 'สำเร็จยอมรับกลุ่ม% s'% group.name)
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถรับหมายเลขกลุ่ม% i, หมายเลขนอกช่วง'% num)
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน gnames:
                        group = groups [gnames.index (ชื่อ)]
                        ถ้า group.id เป็นที่ยอมรับ:
                            line.sendReplyMessage (msg_id, ถึง, 'ยอมรับกลุ่ม% s'% group.name แล้ว)
                            ต่อ
line.acceptGroupInvitation (group.id)
                        accepted.append (group.id)
                        line.sendReplyMessage (msg_id, ถึง, 'สำเร็จยอมรับกลุ่ม% s'% group.name)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับ gid ใน gids:
                            ถ้า gid ได้รับการยอมรับ:
                                ต่อ
                            line.acceptGroupInvitation (GID)
                            accepted.append (GID)
                            time.sleep (0.8)
                        line.sendReplyMessage (msg_id, ถึง, 'สำเร็จยอมรับกลุ่มคำเชิญทั้งหมด♪')
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถรับกลุ่มที่มีชื่อ `% s`, ชื่อไม่ได้อยู่ในรายการ♪'% ชื่อ)
        elif texttl.startswith ('ปฏิเสธ'):
            ตำรา = textt [7:]. แยก (',')
            ปฏิเสธ = []
            ถ้าไม่ใช่ gids:
                return line.sendReplyMessage (msg_id, ถึง, 'กลุ่มปฏิเสธไม่สำเร็จ, ไม่มีกลุ่มคำเชิญในรายการ')
            สำหรับ texxt ในข้อความ:
                num = ไม่มี
                ชื่อ = ไม่มี
                ลอง:
                    num = int (texxt)
                ยกเว้น ValueError:
                    ชื่อ = texxt
                if num! = ไม่มี:
                    ถ้า num <= len (กลุ่ม) และ num> 0:
                        group = กลุ่ม [NUM - 1]
                        ถ้า group.id ถูกปฏิเสธ:
                            line.sendReplyMessage (msg_id, ถึง, 'เรียบร้อยแล้วปฏิเสธกลุ่ม% s'% group.name)
                            ต่อ
                        line.rejectGroupInvitation (group.id)
                        rejected.append (group.id)
                        line.sendReplyMessage (msg_id, ถึง, 'สำเร็จปฏิเสธกลุ่ม% s'% group.name)
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถปฏิเสธหมายเลขกลุ่ม% i, หมายเลขนอกช่วง'% num)
                ชื่อ elif! = ไม่มี:
                    หากชื่อใน gnames:
                        group = groups [gnames.index (ชื่อ)]
                        ถ้า group.id ถูกปฏิเสธ:
                            line.sendReplyMessage (msg_id, ถึง, 'เรียบร้อยแล้วปฏิเสธกลุ่ม% s'% group.name)
                            ต่อ
                        line.rejectGroupInvitation (group.id)
                        rejected.append (group.id)
                        line.sendReplyMessage (msg_id, ถึง, 'สำเร็จปฏิเสธกลุ่ม% s'% group.name)
                    elif name.lower () == 'ทั้งหมด':
                        สำหรับ gid ใน gids:
                            ถ้า gid ถูกปฏิเสธ:
                                ต่อ
                            line.rejectGroupInvitation (GID)
                            rejected.append (GID)
                            time.sleep (0.8)
                        line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จปฏิเสธกลุ่มคำเชิญทั้งหมด♪')
                    อื่น:
                        line.sendReplyMessage (msg_id, ถึง, 'กลุ่มปฏิเสธไม่สำเร็จด้วยชื่อ `% s`, ชื่อไม่อยู่ในรายการ♪'% ชื่อ)
        อื่น:
            สำหรับ res ใน ress:
                line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd == 'รายชื่อสมาชิก':
ถ้า msg.toType == 1:
            ห้อง = line.getRoom (ไป)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup (ถึง)
            สมาชิก = group.members
        อื่น:
            return line.sendReplyMessage (msg_id, ถึง, 'รายชื่อสมาชิกที่แสดงไม่สำเร็จ, ใช้คำสั่งนี้เฉพาะในห้องแชทหรือกลุ่ม')
        ถ้าไม่ใช่สมาชิก:
            return line.sendReplyMessage (msg_id, ถึง, 'รายชื่อสมาชิกที่แสดงไม่สำเร็จ, ไม่มีผู้ติดต่อรายเดียว')
        res = '╭───「รายชื่อสมาชิก」'
        parsed_len = len (สมาชิก) // 200 + 1
        ไม่ = 0
        สำหรับจุดอยู่ในช่วง (parsed_len):
            สำหรับสมาชิกในสมาชิก [จุด * 200: (จุด + 1) * 200]:
                ไม่มี + = 1
                res + = '\ n│% i % s '% (ไม่, member.displayName)
                ถ้าสมาชิก == สมาชิก [-1]:
                    res + = '\ n╰───「 Self Bot 」'
            ถ้า res:
                ถ้า res.startswith ('\ n'): res = res [1:]
                line.sendReplyMessage (msg_id, ถึง, res)
            res = ''
    elif cmd == 'รอดำเนินการ':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id ถึง 'ไม่แสดงรายการที่ค้างอยู่ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getGroup (ถึง)
        สมาชิก = group.invitee
        ถ้าไม่ใช่สมาชิก:
            return line.sendReplyMessage (msg_id, ถึง, 'การแสดงรายการที่ค้างอยู่, ไม่มีผู้ติดต่อรายเดียว')
        res = '╭───「รายการที่รอดำเนินการ」'
        parsed_len = len (สมาชิก) // 200 + 1
        ไม่ = 0
        สำหรับจุดอยู่ในช่วง (parsed_len):
            สำหรับสมาชิกในสมาชิก [จุด * 200: (จุด + 1) * 200]:
                ไม่มี + = 1
                res + = '\ n│% i % s '% (ไม่, member.displayName)
                ถ้าสมาชิก == สมาชิก [-1]:
                    res + = '\ n╰───「 Self Bot 」'
            ถ้า res:
                ถ้า res.startswith ('\ n'): res = res [1:]
                line.sendReplyMessage (msg_id, ถึง, res)
            res = ''
    elif cmd == 'openqr':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id ถึง, 'Failed open qr ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        group.preventedJoinByTicket = False
        line.updateGroup (กลุ่ม)
        line.sendReplyMessage (msg_id, ถึง, 'การเปิดกลุ่มที่ประสบความสำเร็จคุณต้องระวัง')
    elif cmd == 'closeqr':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id, ถึง, 'Failed close qr, ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        group.preventedJoinByTicket = True
        line.updateGroup (กลุ่ม)
        line.sendReplyMessage (msg_id, ถึง, 'Success close group qr')
    elif cmd.startswith ('changegroupname'):
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id, ถึง, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้ให้ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        gname = removeCmd (ข้อความ, setKey)
        ถ้า len (gname)> 50:
            return line.sendReplyMessage (msg_id, ถึง, 'ชื่อกลุ่มการเปลี่ยนแปลงที่ล้มเหลว, จำนวนชื่อต้องไม่เกิน 50')
        group.name = gname
        line.updateGroup (กลุ่ม)
        line.sendReplyMessage (msg_id, เป็น, 'เปลี่ยนชื่อกลุ่มสำเร็จเป็น `% s`'% gname)
    elif cmd == 'changegrouppict':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id ถึง 'ไม่สามารถเปลี่ยนรูปภาพกลุ่มใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        หากไม่อยู่ในการตั้งค่า ['changeGroupPicture']:
            การตั้งค่า [ 'changeGroupPicture']. ผนวก (เพื่อ)
            line.sendReplyMessage (msg_id, ถึง, 'กรุณาส่งภาพพิมพ์ `{key} Abort` หากต้องการยกเลิก \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัพโหลดภาพ'.format (key = setKey.title) นานเกินไป ))
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, 'คำสั่งทำงานอยู่แล้วกรุณาส่งภาพหรือพิมพ์ `{key} Abort` หากต้องการยกเลิกมัน \ nFYI: การดาวน์โหลดภาพจะล้มเหลวหากอัปโหลด image'.format (key = setKey นานเกินไป) .หัวข้อ()))
    elif cmd == 'kickall':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id ถึง 'ไม่เตะสมาชิกทั้งหมดให้ใช้คำสั่งนี้เฉพาะการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        ถ้าไม่ใช่กลุ่มสมาชิก:
            return line.sendReplyMessage (msg_id, ถึง, 'เตะสมาชิกทั้งหมดล้มเหลว, ไม่มีสมาชิกในรายการ')
        สำหรับสมาชิกใน group.members:
            ถ้า member.mid == myMid:
                ต่อ
            ลอง:
line.kickoutFromGroup (ถึง, [member.mid])
            ยกเว้น TalkException เป็น talk_error:
                return line.sendReplyMessage (msg_id, ถึง, 'เตะสมาชิกทั้งหมดไม่สำเร็จสาเหตุคือ `% s' '% talk_error.reason)
            time.sleep (0.8)
        line.sendReplyMessage (msg_id, ถึง, 'ความสำเร็จเตะสมาชิกทั้งหมด, ยอดรวม% i สมาชิก'% len (group.members))
    elif cmd == 'cancelall':
        ถ้า msg.toType! = 2: return line.sendReplyMessage (msg_id ถึง, 'ไม่สามารถยกเลิกสมาชิกที่ค้างอยู่ทั้งหมดให้ใช้คำสั่งนี้เฉพาะในการแชทเป็นกลุ่ม')
        group = line.getCompactGroup (ถึง)
        ถ้าไม่ได้เป็นกลุ่ม invitee:
            return line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการยกเลิกสมาชิกที่รอดำเนินการทั้งหมด, ไม่มีสมาชิกรอดำเนินการในรายการ')
        สำหรับสมาชิกใน group.invitee:
            ถ้า member.mid == myMid:
                ต่อ
            ลอง:
                line.cancelGroupInvitation (ถึง, [member.mid])
            ยกเว้น TalkException เป็น talk_error:
                return line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการยกเลิกสมาชิกที่รอดำเนินการทั้งหมด, เหตุผลคือ `% s`'% talk_error.reason)
            time.sleep (0.8)
        line.sendReplyMessage (msg_id, ถึง, 'ประสบความสำเร็จในการยกเลิกสมาชิกที่รอดำเนินการทั้งหมด, ยอดรวม% i ที่รอดำเนินการสมาชิก'% len (การส่ง))
    elif cmd.startswith ('lurk'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
        หาก msg.toType ใน [1, 2] และไม่อยู่ในที่ซุ่มซ่อน:
            ซุ่มซ่อน [เพื่อ] = {
                'สถานะ': เท็จ
                'เวลา': ไม่มี
                'สมาชิก': [],
                'ตอบกลับ': {
                    'สถานะ': เท็จ
                    'message': settings ['defaultReplyReader']
                }
            }
        res = '╭───「ที่ซุ่มซ่อน」'
        ถ้า msg.toType ใน [1, 2]: res + = '\ n├สถานะ:' + bool_dict [ที่ซุ่มซ่อน [ถึง] ['สถานะ']] [1]
        ถ้า msg.toType ใน [1, 2]: res + = '\ n├ผู้อ่านที่ตอบกลับ:' + bool_dict [ที่ซุ่มซ่อน [ถึง] ['ตอบ'] ['สถานะ']] [1]
        ถ้า msg.toType ใน [1, 2]: res + = '\ n├ข้อความตอบกลับของผู้อ่าน:' + ที่ซุ่มซ่อน [ถึง] ['ตอบ'] ['ข้อความ']
        res + = '\ n├การใช้งาน:'
        res + = '\ n│• {key} Lurk'
        res + = '\ n│• {key} Lurk <เปิด / ปิด>'
        res + = '\ n│• {key} ผลลัพธ์แฝงตัว'
        res + = '\ n│• {key} Lurk รีเซ็ต'
        res + = '\ n│• {key} Lurk ReplyReader <เปิด / ปิด>'
        res + = '\ n│• {key} Lurk ReplyReader <ข้อความ>'
        res + = '\ n╰───「 Self Bot 」'
        ถ้า cmd == 'lurk':
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
        ไม่ได้อยู่ใน [1, 2]:
            return line.sendReplyMessage (msg_id, ถึง, 'ล้มเหลวในการรันคำสั่งคำสั่ง, ใช้คำสั่งนี้เฉพาะในห้องหรือแชทกลุ่ม')
        elif texttl == 'เปิด':
            ถ้าซุ่มซ่อน [ถึง] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Lurking active แล้ว')
            อื่น:
                ซุ่มซ่อน [ไป] .update ({
                    'สถานะ': จริง
                    'เวลา': datetime.now (tz = pytz.timezone ('เอเชีย / จาการ์ตา')) strftime ('% Y-% m-% d% H:% M:% S'),
                    'สมาชิก': []
                })
                line.sendReplyMessage (msg_id, ถึง, 'Success lurking สำเร็จ')
        elif texttl == 'ปิด':
            หากไม่แฝงตัว [ถึง] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'Lurking deactive เรียบร้อยแล้ว')
            อื่น:
                ซุ่มซ่อน [ไป] .update ({
                    'สถานะ': เท็จ
                    'เวลา': ไม่มี
                    'สมาชิก': []
                })
line.sendReplyMessage (msg_id, ถึง, 'สำเร็จปิดการใช้งานการซุ่มโจมตี')
        elif texttl == 'ผลลัพธ์':
            หากไม่แฝงตัว [ถึง] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'การแสดงผลที่ไม่สามารถดักซุ่ม, การซุ่มซ่อนไม่ได้เปิดใช้งาน')
            อื่น:
                ถ้าไม่ซุ่มซ่อน [กับ] ['members']:
                    line.sendReplyMessage (msg_id, ถึง, 'การแสดงผลล้มเหลว, ไม่มีสมาชิกคนใดอ่าน')
                อื่น:
                    members = ซุ่มซ่อน [to] ['members']
                    res = '╭───「ที่ซุ่มซ่อน」'
                    ถ้า msg.toType == 2: res + = '\ n├ชื่อกลุ่ม:' + line.getGroup (ถึง) .name
                    parsed_len = len (สมาชิก) // 200 + 1
                    ไม่ = 0
                    สำหรับจุดอยู่ในช่วง (parsed_len):
                        สำหรับสมาชิกในสมาชิก [จุด * 200: (จุด + 1) * 200]:
                            ไม่มี + = 1
                            ลอง:
                                name = line.getContact (สมาชิก) .displayName
                            ยกเว้น TalkException:
                                ชื่อ = 'ไม่ทราบ'
                            res + = '\ n│% i % s '% (ไม่ใช่ชื่อ)
                            ถ้าสมาชิก == สมาชิก [-1]:
                                res + = '\ n│'
                                res + = '\ n├ตั้งเวลา:' + ที่ซุ่มซ่อน [ถึง] ['เวลา']
                                res + = '\ n╰───「 Self Bot 」'
                        ถ้า res:
                            ถ้า res.startswith ('\ n'): res = res [1:]
                            line.sendReplyMessage (msg_id, ถึง, res)
                        res = ''
        elif texttl == 'รีเซ็ต':
            หากไม่แฝงตัว [ถึง] ['สถานะ']:
                line.sendReplyMessage (msg_id, ถึง, 'การรีเซ็ตที่ซุ่มซ่อนไม่สำเร็จ, การซุ่มซ่อนไม่ได้เปิดใช้งาน')
            อื่น:
                ซุ่มซ่อน [ไป] .update ({
                    'สถานะ': จริง
                    'เวลา': datetime.now (tz = pytz.timezone ('เอเชีย / จาการ์ตา')) strftime ('% Y-% m-% d% H:% M:% S'),
                    'สมาชิก': []
                })
                line.sendReplyMessage (msg_id, ถึง, 'Success resetted lurking')
        elif texttl.startswith ('replyreader'):
            ตำรา = textt [12:]
            หากตำรา == 'เปิด':
                ถ้าซุ่มซ่อน [ถึง] ['ตอบ'] ['สถานะ']:
                    line.sendReplyMessage (msg_id, ถึง, 'ผู้อ่านตอบใช้งานอยู่แล้ว')
                อื่น:
                    ที่ซุ่มซ่อน [ถึง] ['reply'] ['สถานะ'] = จริง
                    line.sendReplyMessage (msg_id, ถึง, 'ผู้อ่านตอบกลับที่เปิดใช้งานสำเร็จ')
            elif ตำรา == 'ปิด':
                ถ้าไม่ซุ่มซ่อน [[]] ['ตอบ'] ['สถานะ']:
                    line.sendReplyMessage (msg_id, ถึง, 'ผู้อ่านตอบกลับใช้งานไม่ได้')
                อื่น:
                    ที่ซุ่มซ่อน [ถึง] ['reply'] ['สถานะ'] = False
                    line.sendReplyMessage (msg_id, ถึง, 'สำเร็จปิดการใช้งานเครื่องมืออ่านตอบ')
            อื่น:
                ซุ่มซ่อน [ถึง] ['reply'] ['message'] = ข้อความ
                line.sendReplyMessage (msg_id, ถึง, 'ข้อความตอบกลับของผู้อ่านที่ตั้งค่าสำเร็จเป็นข้อความ% `` s' '%)
        อื่น:
            line.sendReplyMessage (msg_id, ถึง, การแยกวิเคราะห์ (res) .format_map (SafeDict (key = setKey.title ()))
    elif cmd.startswith ('ทักทาย'):
        textt = removeCmd (ข้อความ, setKey)
        texttl = textt.lower ()
res = '╭───「ทักทายข้อความ 」'
        res += '\n├ สวัสดีเข้าร่วมสถานะ : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ ทักทายเข้าร่วมข้อความ: ' + settings['greet']['join']['message']
        res += '\n├ สวัสดีฝากสถานะ : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\n├ ทักทายเข้าร่วมข้อความ : ' + settings['greet']['leave']['message']
        res += '\n├ การใช้ : '
        res += '\n│ • {key}ทักทาย'
        res += '\n│ • {key}สวัสดีเข้าร่วม <เปิด / ปิด>'
        res += '\n│ • {key}สวัสดีเข้าร่วม <ข้อความ>'
        res += '\n│ • {key}สวัสดีปล่อยให้ <เปิด / ปิด>'
        res += '\n│ • {key}สวัสดี <ฝากข้อความ>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'greet':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    line.sendReplyMessage(msg_id, to, 'Greetings join already active')
                else:
                    settings['greet']['join']['status'] = True
                    line.sendReplyMessage(msg_id, to, 'Success activated greetings join')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    line.sendReplyMessage(msg_id, to, 'Greetings join already deactive')
                else:
                    settings['greet']['join']['status'] = False
                    line.sendReplyMessage(msg_id, to, 'Success deactivated greetings join')
            else:
                settings['greet']['join']['message'] = texts
                line.sendReplyMessage(msg_id, to, 'Success change greetings join message to `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    line.sendReplyMessage(msg_id, to, 'Greetings leave already active')
                else:
                    settings['greet']['leave']['status'] = True
                    line.sendReplyMessage(msg_id, to, 'Success activated greetings leave')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    line.sendReplyMessage(msg_id, to, 'Greetings leave already deactive')
                else:
                    settings['greet']['leave']['status'] = False
                    line.sendReplyMessage(msg_id, to, 'Success deactivated greetings leave')
            else:
                settings['greet']['leave']['message'] = texts
                line.sendReplyMessage(msg_id, to, 'Success change greetings leave message to `%s`' % texts)
        else:
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('kick '):
        if msg.toType != 2: return line.sendReplyMessage(msg_id, to, 'Failed kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                except TalkException as talk_error:
                    return line.sendReplyMessage(msg_id, to, 'Failed kick members, the reason is `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendReplyMessage(msg_id, to, 'Success kick members, totals %i members' % len(mentions['MENTIONEES']))
        else:
            line.sendReplyMessage(msg_id, to, 'Failed kick member, please mention user you want to kick')
    elif cmd.startswith('vkick '):
        if msg.toType != 2: return line.sendReplyMessage(msg_id, to, 'Failed vultra kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                except TalkException as talk_error:
                    return line.sendReplyMessage(msg_id, to, 'Failed vultra kick members, the reason is `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendReplyMessage(msg_id, to, 'Success vultra kick members, totals %i members' % len(mentions['MENTIONEES']))
        else:
            line.sendReplyMessage(msg_id, to, 'Failed vultra kick member, please mention user you want to kick')
            
    elif text.lower() == 'token chromeos':
           req = requests.get(url = 'https://api.eater.pw/token?header=CHROMEOS')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           line.sendReplyMessage(msg_id, to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           line.sendReplyMessage(msg_id, to, '{}'.format(b))
    elif text.lower() == 'token win10':
           req = requests.get(url = 'https://api.eater.pw/token?header=WIN10')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           line.sendReplyMessage(msg_id, to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           line.sendReplyMessage(msg_id, to, '{}'.format(b))
    elif text.lower() == 'token iospad':
           req = requests.get(url = 'https://api.eater.pw/token?header=IOSIPAD')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           line.sendReplyMessage(msg_id, to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           line.sendReplyMessage(msg_id, to, '{}'.format(b))
    elif text.lower() == 'token desktopwin':
           req = requests.get(url = 'https://api.eater.pw/token?header=DESKTOPWIN')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           line.sendReplyMessage(msg_id, to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           line.sendReplyMessage(msg_id, to, '{}'.format(b))
    elif text.lower() == 'token desktopmac':
           req = requests.get(url = 'https://api.eater.pw/token?header=DESKTOPMAC')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           line.sendReplyMessage(msg_id, to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           line.sendReplyMessage(msg_id, to, '{}'.format(b))  

def executeOp(op):
    try:
        print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 13:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])
        if op.type == 15:
            if settings['greet']['leave']['status']:
                if '@!' not in settings['greet']['leave']['message']:
                    line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 17:
            if settings['greet']['join']['status']:
                if '@!' not in settings['greet']['join']['message']:
                    line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendReplyMessage(msg_id, to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendReplyMessage(msg_id, to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendReplyMessage(msg_id, to, 'Success join to group ' + group.name)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendReplyMessage(msg_id, to, 'Execute command error, ' + str(talk_error))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendReplyMessage(msg_id, to, 'Execute command error, ' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    line.sendReplyMessage(msg_id, to, 'Success change picture profile')
                    settings['changePictureProfile'] = False
                elif settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    line.sendReplyMessage(msg_id, to, 'Success change cover profile')
                    settings['changeCoverProfile'] = False
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    line.sendReplyMessage(msg_id, to, 'Success change group picture')
                    settings['changeGroupPicture'].remove(to)
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = '╭───「 ข้อมูลสติกเกอร์ 」'
                    res += '\n├ สติ๊กเกอร์ ID : ' + msg.contentMetadata['STKID']
                    res += '\n├ แพ็คเกจสติกเกอร์ ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\n├ เวอร์ชั่นสติ๊กเกอร์: ' + msg.contentMetadata['STKVER']
                    res += '\n├ ลิงค์สติ๊กเกอร์: line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return line.sendReplyMessage(msg_id, to, 'Failed get details contact with mid ' + mid)
                    res = '╭───「 รายละเอียดการติดต่อ」'
                    res += '\n├ MID : ' + mid
                    res += '\n├ ชื่อที่แสดง: ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ แทนที่ชื่อที่แสดง: ' + str(contact.displayNameOverridden)
                    res += '\n├ ข้อความสถานะ: ' + str(contact.statusMessage)
                    res += '\n╰───「 Self Bot 」'
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                            contact = line.getContact(sender)
                            author = contact.displayName
                        else:
                            author = msg.contentMetadata['serviceName']
                        posturl = msg.contentMetadata['postEndUrl']
                        res = '╭───「 โพสต์รายละเอียด」'
                        res += '\n├ ผู้สร้าง : ' + author
                        res += '\n├ ลิงค์โพสต์ : ' + posturl
                        res += '\n╰───「 Self Bot 」'
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if settings['autoRead']:
                line.sendChatChecked(to, msg_id)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendReplyMessage(msg_id, to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendReplyMessage(msg_id, to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendReplyMessage(msg_id, to, 'Success join to group ' + group.name)
                if settings['mimic']['status']:
                    if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            tmp_text.append(text)
                        except:
                            pass
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendMessage(to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV2(to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendMessage(to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoRespond']['message'], [sender])
        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendReplyMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

def runningProgram():
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                executeOp(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()



