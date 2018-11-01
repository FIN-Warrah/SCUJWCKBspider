import requests
import http.cookiejar
import urllib.request
import json
import re

username=input("Please enter your account:")
password=input("Please enter your password:")

data={
    'j_username':username,
    'j_password':password,
    'j_captcha1':'error'
}

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Pragma': 'no-cache',
    'Referer': 'http://zhjw.scu.edu.cn/login'
}

url0='http://zhjw.scu.edu.cn/login'
url='http://zhjw.scu.edu.cn/j_spring_security_check'

#s=requests.session()
#r=s.post(url,data,headers=headers)
s=requests.session()
cookie=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
r=opener.open(url0)
print(cookie)
for item in cookie:
    print ('Name = '+item.name)
    print ('Value = '+item.value)
s.cookies=cookie
s.headers=headers
r=s.post(url,data,headers=headers)
print(r)
r1=s.get('http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/index',headers=headers)
print(r1)
r2=s.get(url='http://zhjw.scu.edu.cn/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback',headers=headers)
jsobj=json.loads(r2.text)
#print(jsobj)

# for i in jsobj:
#     print(i)




filename=data['j_username']+'.txt'
f=open(filename,'w')
f.write(str(jsobj))
f.close()

filename2=data['j_username']+'_2.txt'
f2=open(filename2,'w')

for item in jsobj['xkxx']:
    for item2,value2 in item.items():
        for item3,value3 in value2.items():
            f2.write(str(item3)+"\n")
            f2.write(str(value3)+"\n")
        f2.write("\n\n\n")

f2.close()

filename3=data['j_username']+'_3.txt'
f3=open(filename3,'w')

for item in jsobj['xkxx']:
    print(item)
    print(type(item))
    for item2,value2 in item.items():
        numbers=re.split('_',item2)
        # print(numbers[0])
        # print(numbers[1])
        f3.write('number1:'+numbers[0]+"\n")
        f3.write('number2:'+numbers[1]+"\n")
        f3.write('courseName:'+value2['courseName']+"\n")
        f3.write('points:'+str(value2['unit'])+"\n")
        f3.write('coursePropertiesName:'+value2['coursePropertiesName']+"\n")
        f3.write('courseCategoryName:'+value2['courseCategoryName']+"\n")
        f3.write('examTypeName:'+value2['examTypeName']+"\n")
        f3.write('attendClassTeacher:'+value2['attendClassTeacher']+"\n")
        f3.write('studyModeName:'+value2['studyModeName']+"\n")
        f3.write('selectCourseStatusName:'+value2['selectCourseStatusName']+"\n")
        f3.write('weekDescription:'+value2['timeAndPlaceList'][0]['weekDescription']+"\n")
        f3.write('classDay:'+str(value2['timeAndPlaceList'][0]['classDay'])+"\n")
        f3.write('classSessions:'+str(value2['timeAndPlaceList'][0]['classSessions'])+"\n")
        f3.write('continuingSession:'+str(value2['timeAndPlaceList'][0]['continuingSession'])+"\n")
        f3.write('campusName:'+value2['timeAndPlaceList'][0]['campusName']+"\n")
        f3.write('teachingBuildingName:'+value2['timeAndPlaceList'][0]['teachingBuildingName']+"\n")
        f3.write('classroomName:'+value2['timeAndPlaceList'][0]['classroomName']+"\n")
        f3.write("\n\n")
f3.close()


# print(str)
# allUnits=re.search(r"'allUnits':(.+\..+), 'xkxx",str)
# print()
# print(allUnits.groups().__len__())
# print(allUnits.groups())
# attendClassTeachers=re.search(r" {'attendClassTeacher': '(.*)', 'courseCategoryCode'",str)
# print(attendClassTeachers.groups())