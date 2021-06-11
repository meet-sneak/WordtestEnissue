# -*- coding:utf-8 -*-
import requests,datetime,json,yaml,os
from playsound import playsound

file_name='allocation.yaml'
yaml_Path = os.path.dirname(os.path.realpath(__file__))
with open(yaml_Path+'/../wordtest/'+file_name, 'rb') as f:
    temp = yaml.load(f.read(),Loader=yaml.FullLoader)
temp=temp['environment']    #配置文件数据

user_data={"email":str(temp['user']),"password":temp['password']}
api_address=temp['api_address']


if api_address:
    login_url = '{}/api/auth'.format(api_address)

    fastoverList_url='{}/api/quiz/BensonSpeakingLevel'.format(api_address)  #闯关列表
    fastover_url='{}/api/quiz/BensonSpeakingRecord'.format(api_address)     #闯关作答


else:
    print('url环境配置错误')


headers = {

'Accept': 'application/json, text/plain, */*',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
'Content-Type': 'application/json;charset=UTF-8',
'Origin':'https://test.sis.07future.com',
'Referer': 'https://test.sis.07future.com/',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Host':'test.api.07future.com',
'Connection': 'keep-alive',
'Content-Length': '7010',
         }


#登录

class Loin():

    def __init__(self):
        pass

    def login(self,user_data=user_data):

        session = requests.session()
        resing = session.request('POST',login_url,headers=headers,json=user_data)
        print(resing.text)

        return session


class FastGameover():

    def __init__(self):
        pass

    def fastgameover(self,session):

        res = session.request('GET',fastoverList_url)
        res_date = json.loads(res.text)
        res_dateList=[]

        for i in range(len(res_date['spContent'])):
            res_dateList.append(res_date['spContent'][i]['_id'])

        if len(res_dateList):
            for j in res_dateList:
                quiz={
    "score": 100,
    "answerDuration": 37,
    "answerGradeAuto": {
        "grade": 100
    },
    "speakingLevel": j, #关卡ID
    "answerUrl": "https://soe-1253364609.cos.ap-shanghai.myqcloud.com/1258234461/default/20210610/audio/2d514c5d-49d6-4496-bfec-83250edf0b76.mp3",
    "stage": "recording",
    "autoGradeReport": "{\"passCount\":0,\"pronAccuracy\":23,\"pronCompletion\":34,\"pronFluency\":32,\"word\":[{\"score\":0,\"word\":\"in\"},{\"score\":7,\"word\":\"just\"},{\"score\":-1,\"word\":\"moments\"},{\"score\":-1,\"word\":\"sixteen\"},{\"score\":-1,\"word\":\"complete\"},{\"score\":-1,\"word\":\"strangers\"},{\"score\":-1,\"word\":\"from\"},{\"score\":-1,\"word\":\"across\"},{\"score\":-1,\"word\":\"america\"},{\"score\":-1,\"word\":\"will\"},{\"score\":-1,\"word\":\"move\"},{\"score\":-1,\"word\":\"into\"},{\"score\":-1,\"word\":\"this\"},{\"score\":-1,\"word\":\"house\"},{\"score\":-1,\"word\":\"with\"},{\"score\":-1,\"word\":\"one\"},{\"score\":-1,\"word\":\"goal\"},{\"score\":8,\"word\":\"in\"},{\"score\":-1,\"word\":\"mind\"},{\"score\":-1,\"word\":\"to\"},{\"score\":-1,\"word\":\"be\"},{\"score\":75,\"word\":\"the\"},{\"score\":76,\"word\":\"last\"},{\"score\":54,\"word\":\"houseguest\"},{\"score\":58,\"word\":\"standing\"},{\"score\":86,\"word\":\"and\"},{\"score\":92,\"word\":\"win\"},{\"score\":94,\"word\":\"the\"},{\"score\":84,\"word\":\"half\"},{\"score\":95,\"word\":\"million\"},{\"score\":92,\"word\":\"dollar\"},{\"score\":81,\"word\":\"grand\"},{\"score\":70,\"word\":\"prize\"},{\"score\":-1,\"word\":\"but\"},{\"score\":-1,\"word\":\"it\"},{\"score\":-1,\"word\":\"won\\u0027t\"},{\"score\":-1,\"word\":\"be\"},{\"score\":-1,\"word\":\"easy\"},{\"score\":-1,\"word\":\"for\"},{\"score\":-1,\"word\":\"the\"},{\"score\":-1,\"word\":\"next\"},{\"score\":65,\"word\":\"three\"},{\"score\":64,\"word\":\"months\"},{\"score\":70,\"word\":\"they\\u0027ll\"},{\"score\":87,\"word\":\"be\"},{\"score\":-1,\"word\":\"completely\"},{\"score\":-1,\"word\":\"cut\"},{\"score\":-1,\"word\":\"off\"},{\"score\":77,\"word\":\"from\"},{\"score\":95,\"word\":\"the\"},{\"score\":96,\"word\":\"outside\"},{\"score\":97,\"word\":\"world\"},{\"score\":-1,\"word\":\"no\"},{\"score\":68,\"word\":\"internet\"},{\"score\":49,\"word\":\"no\"},{\"score\":55,\"word\":\"tv\"},{\"score\":86,\"word\":\"no\"},{\"score\":95,\"word\":\"cell\"},{\"score\":52,\"word\":\"phones\"},{\"score\":-1,\"word\":\"only\"},{\"score\":-1,\"word\":\"these\"},{\"score\":57,\"word\":\"cameras\"},{\"score\":-1,\"word\":\"and\"},{\"score\":-1,\"word\":\"microphones\"},{\"score\":-1,\"word\":\"to\"},{\"score\":-1,\"word\":\"capture\"},{\"score\":-1,\"word\":\"every\"},{\"score\":-1,\"word\":\"emotionally\"},{\"score\":-1,\"word\":\"charged\"},{\"score\":-1,\"word\":\"moment\"},{\"score\":-1,\"word\":\"like\"},{\"score\":-1,\"word\":\"never\"},{\"score\":-1,\"word\":\"before\"},{\"score\":-1,\"word\":\"it\\u0027s\"},{\"score\":-1,\"word\":\"summertime\"},{\"score\":-1,\"word\":\"america\"},{\"score\":-1,\"word\":\"and\"},{\"score\":-1,\"word\":\"that\"},{\"score\":-1,\"word\":\"can\"},{\"score\":-1,\"word\":\"only\"},{\"score\":-1,\"word\":\"mean\"},{\"score\":-1,\"word\":\"one\"},{\"score\":-1,\"word\":\"thing\"},{\"score\":-1,\"word\":\"it\\u0027s\"},{\"score\":-1,\"word\":\"time\"},{\"score\":-1,\"word\":\"for\"},{\"score\":-1,\"word\":\"big\"},{\"score\":-1,\"word\":\"brother\"}]}"
}
                res = session.request('PUT',fastover_url,json=quiz)
                print('作答结果',res.text)


if __name__ == '__main__':

    session=Loin().login()

    FastGameover().fastgameover(session)