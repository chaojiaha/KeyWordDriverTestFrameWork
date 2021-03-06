from datetime import datetime, date
from config.VarConfig import *

class DirAndTime(object):
    @staticmethod
    def getCurrentDate():
        '''
        获取当前日期
        :return:
        '''
        try:
            currentDate = date.today()
        except Exception as e:
            raise e
        else:
            return str(currentDate)
    @staticmethod
    def getCurrentTime():
        '''
        获取当前时间
        :return:
        '''
        try:
            Time = datetime.now()
            currentTime = Time.strftime('%H_%M_%S')
        except Exception as e:
            raise e
        else:
            return currentTime
    @staticmethod
    def CreatePicturePath():
        '''
        创建图片存放路径路径
        :return:
        '''
        try:

            picturePath = os.path.join(exceptionPath , DirAndTime.getCurrentDate())
            if not os.path.exists(picturePath):
                os.makedirs(picturePath) # 生成多级目录
        except Exception as e:
            raise e
        else:
            return picturePath

if __name__=='__main__':
    print(DirAndTime.getCurrentDate())
    print(DirAndTime.getCurrentTime())
    print(DirAndTime.CreatePicturePath())