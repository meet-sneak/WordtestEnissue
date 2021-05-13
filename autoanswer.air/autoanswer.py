# -*- encoding=utf8 -*-
__author__ = "test010"
import datetime
#from playsound import playsound
from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

lins="此次系统更新添加了以下问题：一、系统新增校刊功能，学生及校刊管理员可以发布及管理校刊。二、校刊支持文章、新闻、视频等常见信息载体形式。三、其他功能体验优化"
text(lins)


#开始-------------------------------------------------
#SAT核心词汇 1600，List55-Tough P219-223
today = datetime.date.today() #今天日期

namelist={'01':'测试看英写中','09':'测试看中写英补考百分比间隔7分1次','02':'测试看中写英不补考','03':'测试听英写中','04':'测试听英写英（固三）','05':'测试看英选中同题','06':'测试看中选英近义','07':'测试单词连线','08':'测试单词跟读'}

i="04" #~~~~~~

listype=i #作答类型 01---看英写中，02---看中写英，03---听英写中，04---听英写英，05---看英选中，06---看中选英，07---单词连线，08---单词跟读
name="{0}.{1}---{2}".format(today.month,today.day,namelist[i]) #小测名

lisEn=["surfeit","surreptitious","surrogate","tactless","tangential","temerity","tendentious","tirade","torpor","transgression","traverse","trepidation","trifling","tumultuous","turpitude","unassailable","unseemly","urbane","usurp","veracity","verisimilar","vicissitude","vilify","vintage","virtuoso","voluminous","voracious","wanton","warranted","wary","whereas","whet","wily","writhe","zany"]

lisZh=["过量、过度（尤指饮食）、（饮食过度引起的）不适","鬼鬼崇祟的、私下的、秘密的","代理、代表、代用品、代替、代孕者、代用人物、遗嘱检验法庭、代理的","不得体的、不圆通的、粗鲁的、不替别人着想的","间接相关的、次要的、外围的、略为触及题目的","鲁莽、冒失","有偏见的、（指演说、文章等）宣传性的、淘气的、倔强的","激烈的长篇指责或演说","麻木、迟钝、麻痹、（动物的）冬眠","违反、违法、罪过","横越、横贯、通过","颤抖、害怕、不安、震颤","微不足道的、轻浮的、无聊的、懒散的","骚乱的、吵闹的、狂暴的、激烈的","邪恶、恶劣、堕落","攻不破的","（举止）不得体的、不合时宜的、易遣非议的","都市化的、彬彬有礼的、温文尔雅的","篡夺、盗用、侵占、霸占、夺取、强夺","诚实、真实","好像真实的","变迁兴衰","中伤、诽谤","美酒、葡萄产量、酒产年、酒产地、制造年份","艺术大师、演奏能手、名家、艺术名家、学者、古董收藏家","大的、多卷的、著作多的、宽松的","贪婪的、如饥似渴的、贪吃的、渴求的","荒唐的、繁茂的、变化无常的、行为不检的","（制造商）担保的、保证的","谨慎的、小心翼翼的、警戒的、警惕的","然而、鉴于、反之","（在石头上）磨（刀、斧等）、引起、刺激（食欲、欲望、兴趣等）","狡诈的、狡猾的、足智多谋的、诡计多端的","（因极度痛苦而）扭动或翻滚、痛苦、苦恼、蠕动、蜿蜒移动","滑稽的、荒唐的、笨的、可笑的"]

# lisLg={'1': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuussussupussuper127.mp3', '2': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronssursurresurreptitious.mp3', '3': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronssursurrosurrogate.mp3', '4': 'https://test.sis.07future.com/CambridgeDictWithSound/us_proneeuseus74eus74472.mp3', '5': 'https://test.sis.07future.com/CambridgeDictWithSound/us_proneeuseus74eus74482.mp3', '6': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuustustelusteleg021.mp3', '7': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuustustenustenab003.mp3', '8': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronttirtiradtirade.mp3', '9': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuustustorustorme011.mp3', '10': 'https://test.sis.07future.com/CambridgeDictWithSound/qHHkA3JvR.mp3', '11': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronttratravetraverse.mp3', '12': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronttretrepitrepidation.mp3', '13': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronttritrifltrifling.mp3', '14': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronttumtumultumultuous.mp3', '15': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuustusturusturk_011.mp3', '16': 'https://test.sis.07future.com/CambridgeDictWithSound/us_proneeuseus28eus28263.mp3', '17': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuunsunseeunseemly.mp3', '18': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuurburbanurbane.mp3', '19': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuusuusurpusurp.mp3', '20': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuusvusvenusvenez014.mp3', '21': 'https://test.sis.07future.com/CambridgeDictWithSound/nSaX4IS5_.mp3', '22': 'https://test.sis.07future.com/CambridgeDictWithSound/YxmFiVu4bJ.mp3', '23': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronvvilvilifvilify.mp3', '24': 'https://test.sis.07future.com/CambridgeDictWithSound/us_proneeuseus74eus74856.mp3', '25': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronvvirvirtuvirtuoso.mp3', '26': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronuusvusvivusvivac022.mp3', '27': 'https://test.sis.07future.com/CambridgeDictWithSound/us_proneeuseus74eus74900.mp3', '28': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronwwanwantowanton.mp3', '29': 'https://test.sis.07future.com/CambridgeDictWithSound/hfpfHMeOY.mp3', '30': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronwwarwary_wary.mp3', '31': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronwwhewherewhereas.mp3', '32': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronwwhewhet_whet.mp3', '33': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronwwilwily_wily.mp3', '34': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronwwriwrithwrithe.mp3', '35': 'https://test.sis.07future.com/CambridgeDictWithSound/us_pronzzanzany_zany.mp3'}

#作答类型分类
lisAs=[['01','03'],['02','04','09'],['05'],['06'],['07'],['08']] #09及以上题目为重复题型

slidexy=-0.74000    #滑动距离

for i in namelist:
    if i  not in ['08']:    #部分不支持的类型不作答
        listype=i
        answer_mode='text'
        if listype in lisAs[0]: #相识度判断
            lis=lisZh  #答案
            answer_mode='text'  #作答方式
        elif listype in lisAs[1]:
            lis=lisEn
            answer_mode='text'
        elif listype in lisAs[2]:
            lis=lisZh
            answer_mode='choice'
        elif listype in lisAs[3]:
            lis=lisEn
            answer_mode='choice'
        elif listype in lisAs[5]:
            lis=lisLg
            answer_mode='speak'
        elif listype in lisAs[4]:
            answer_mode='online'
            lis=lisEn   #连线题目
        else:
            print("题目类型错误")
            lis=lisZh
            answer_mode='text'

        fin=len(lis)%5 #最后剩余题数

        name="{0}.{1}---{2}".format(today.month,today.day,namelist[i]) #小测名
        pass

        #答题----------------------------------------------------
        print(name,listype)
        keyevent("HOME")
        poco("com.pad.lingqiweilai:id/tv_study").click()
        try:
            poco(text=name).click() #小测作答名称
        except:
            print(name,'小测名错误')
        poco("com.pad.lingqiweilai:id/tv_start_exam").click()

        if answer_mode=='text' and i !='04':
            for i in range(0,len(lis)-fin,5):
                try:
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.LinearLayout")[0].child("com.pad.lingqiweilai:id/et_input").set_text(lis[i])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.LinearLayout")[1].child("com.pad.lingqiweilai:id/et_input").set_text(lis[i+1])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.LinearLayout")[2].child("com.pad.lingqiweilai:id/et_input").set_text(lis[i+2])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.LinearLayout")[3].child("com.pad.lingqiweilai:id/et_input").set_text(lis[i+3])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.LinearLayout")[4].child("com.pad.lingqiweilai:id/et_input").set_text(lis[i+4])
                    poco("com.pad.lingqiweilai:id/rv_question").swipe([-0.03000, slidexy])
                except:
                    print(i+4,"作答循环错误")
                    poco("com.pad.lingqiweilai:id/rv_question").swipe([-0.03000, slidexy])
            for j in range(fin):
                poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.LinearLayout")[4-j].child("com.pad.lingqiweilai:id/et_input").set_text(lis[i+5])
                print("打印-------------------&&&&&-----------------------------------打印")
        elif i =='04':
            poco("com.pad.lingqiweilai:id/tv_next").click()
            for i in range(0,len(lis)-fin,5):
                try:
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/nsvp_exam").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.RelativeLayout")[0].offspring("com.pad.lingqiweilai:id/et_input").set_text(lis[i])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/nsvp_exam").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.RelativeLayout")[1].offspring("com.pad.lingqiweilai:id/et_input").set_text(lis[i+1])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/nsvp_exam").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.RelativeLayout")[2].offspring("com.pad.lingqiweilai:id/et_input").set_text(lis[i+2])
                    poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/nsvp_exam").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.RelativeLayout")[3].offspring("com.pad.lingqiweilai:id/et_input").set_text(lis[i+3])
                    poco("com.pad.lingqiweilai:id/rv_question").swipe([-0.03000, slidexy])
                except:
                    print(i+4,"作答循环错误")
                    poco("com.pad.lingqiweilai:id/rv_question").swipe([-0.03000, slidexy])
            for j in range(fin):
                 poco("android.widget.LinearLayout").offspring("com.pad.lingqiweilai:id/nsvp_exam").offspring("com.pad.lingqiweilai:id/rv_question").child("android.widget.RelativeLayout")[3-j].offspring("com.pad.lingqiweilai:id/et_input").set_text(lis[i+4])
            print("打印--------04---------&&&&&-----------------04----------------打印")
        elif answer_mode=='choice':
            for i in range(0,len(lis)-fin,1):
                try:
                    poco(text=lis[i]).click()
                    poco("com.pad.lingqiweilai:id/elv").swipe([0.0007, -0.4000])
                except:
                    print(i,"作答循环错误")
                    poco("com.pad.lingqiweilai:id/elv").swipe([0.0007, -0.4000])
            for j in range(fin):
                poco(text=lis[i]).click()
                poco("com.pad.lingqiweilai:id/elv").swipe([0.0007, -0.4000])
            print("打印--------Choice---------&&&&&-----------------Choice----------------打印")
#         elif i =='08':
#             for i in range(0,len(lis)-fin,1):
#                 try:
#                     poco("com.pad.lingqiweilai:id/iv_start_record").click()
#                     poco("com.pad.lingqiweilai:id/rv_question").swipe([0.0000, -0.4200])
#                 except:
#                     print(i,"作答循环错误")
#                     poco("com.pad.lingqiweilai:id/rv_question").swipe([0.0000, -0.4200]
#             for j in range(fin):
#                 poco("com.pad.lingqiweilai:id/iv_start_record").click()
#                 poco("com.pad.lingqiweilai:id/rv_question").swipe([0.0000, -0.4200])
#             print("打印--------Speak---------&&&&&-----------------Speak----------------打印")
        elif answer_mode=='online':
            for i in range(0,len(lis)-fin,5):
                try:
                    poco(text=lis[i]).click()
                    poco(text=lisZh[i]).click()
                    poco(text=lis[i+1]).click()
                    poco(text=lisZh[i+1]).click()
                    poco(text=lis[i+2]).click()
                    poco(text=lisZh[i+2]).click()
                    poco(text=lis[i+3]).click()
                    poco(text=lisZh[i+3]).click()
                    poco(text=lis[i+4]).click()
                    poco(text=lisZh[i+4]).click()
                    poco(text="下一页").click()
                except:
                    print(i,"作答循环错误")
                    poco(text="下一页").click()
            if fin > 0:
                for i in range(fin+5):
                    poco(text=lis[i]).click()
                    poco(text=lisZh[i]).click()
                poco(text="下一页").click()
            print("打印--------online---------&&&&&-----------------online----------------打印")
        else:
            print('其他类型')
            continue

        #答题结束-------------------------------------------------------------
        try:
            poco(text="下一页").click()
            poco(text="确认").click()
        except:
            print('无下一页或确认')
        #相识度判断开始-------------------------------------------------------
        if listype in lisAs[0]:
            try:
                snapshot(msg="相识度判断")
                poco(text="移动、运动").click()
            except:
                print(name,"相识度选择失败")
        #提交作答--------------------------------------------------------------    
        try:
            poco(text="下一页").click()
            poco(text="确认").click()
        except:
            print("无确认")
        poco(text="提交").click()
        poco(text="确认交卷").click()
        poco(text="确认").click()
        #断言-----------------------------------------------------------------
        assert_exists(Template(r"tpl1617624684946.png", record_pos=(-0.122, 0.194), resolution=(1920, 1200)), "{}简单答题完成".format(name))