from linebot.models import *


class Response(object):
    '''
    This class control how to response to messages from users.
    '''

    _greeting = TextSendMessage(
        text='Hi！我是William，很高興認識您！您想要問些什麼呢？\n' + 
             '1. 自我介紹\n' +
             '2. 實習動機\n' + 
             '3. 工作經驗\n' +
             '4. Side Projects\n' + 
             '5. 研究領域\n'
    )

    _response = {
        '自我介紹': TextSendMessage(text='你好！我是目前就讀台大資工系大三的高偉倫，' +
                                        '平時的興趣是聽團和玩音樂，喜歡嘗試各種新事物。' +
                                        '希望未來能夠成為LINE TECH FRESH的一員，還請多多指教！\n\n' + 
                                        'Github連結：https://github.com/william881218\n' +
                                        'LinkedIn連結：https://www.linkedin.com/in/wei-lun-kao-0341191a3/'),
                                        
        '實習動機': TextSendMessage(text='我一直認為實習是快速認識自己的最佳方法。\n' +
                                        'Data Engineer, Backend Devloper, DevOps...' + 
                                        '因為不確定自己未來的路，若有幸能成為Line Tech Fresh的一員，' + 
                                        '我非常希望在發揮自己專長對Line帶來一些貢獻之餘，' +
                                        '也趁機讓自己更確定未來的職涯發展。'),

        '工作經驗': TextSendMessage(text='1. 台大數位學習中心 Intern\n' + 
                                        '(Oct 2020 ~ Present)\n'
                                        '從0開始開發上課錄影投影片換頁偵測的功能。' + 
                                        '需要自己去survey和prototype各種做法，' + 
                                        '並且定期和成員開會更新進度並報告。\n\n' + 
                                        '2. 華碩AI研發中心 Intern\n' + 
                                        '(Jul 2020 ~ Sep 2020)\n'+
                                        '(1). 利用Data Augmentation增進已上線模型的準確率(從89.1%到91.2%)\n' +
                                        '(2). 協助重構現有的前處理函式庫\n' +
                                        '(3). 開發PoC，負責資料分析/prototyping/訓練baseline model'),

        'Side Projects': TextSendMessage(text='1. Adversarial Attack on ASR\n' + 
                                              '我使用pytorch和flask搭建了一個web-based的demo。' + 
                                              '使用者可以輸入原始音檔和想要攻擊的target transcription，' +
                                              '此網頁便能回傳一個加了惡意噪音的音檔，可用以攻擊同網頁的語音辨識系統。\n' +
                                              'Github連結: https://github.com/william881218/Adversarial-ASR-Attack\n'
                                              'Demo: http://140.112.90.203:9999'),

        '研究領域': TextSendMessage(text='我在2020二月加入了台大人工智慧安全實驗室做專題，' + 
                                        '研究主題是語音辨識模型的惡意攻擊與防禦。' + 
                                        '2020十月開始和同實驗室的博士生進行另一個有關語音驗證碼(Audio Captcha)的研究。'),
    }


    @classmethod
    def response_to_message(cls, message):
        """
        Given a message from user, return the most appropriate response.
        If no appropriate response can be found, raise an error.
        """

        for key_word in cls._response.keys():
            if message in key_word:
                return cls._response[key_word]

        raise UnknownMessageError


    @classmethod
    def unknown_message(cls, message):
        """
        Return response for unknown messages.
        """

        return TextSendMessage(
            text=f'不好意思，我不了解「{message}」是什麼意思QQ。您可以嘗試下列指令：\n' + 
                '1. 自我介紹\n' +
                '2. 實習動機\n' + 
                '3. 工作經驗\n' +
                '4. Side Projects\n' + 
                '5. 研究領域\n' + 
                '謝謝！'
        )


# A self-defined exception for unrecognizable user message.
class UnknownMessageError(Exception):
    pass