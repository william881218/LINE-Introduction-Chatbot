from collections import OrderedDict

from linebot.models import *


class Response(object):
    '''
    This class control how to response to messages from users.
    '''

    _greeting = TextSendMessage(
        text='Hi！我是William，很高興認識您！您想要知道關於我的哪些事呢？'
    )

    _finish_responing = TextSendMessage(
        text='謝謝您的提問！您還想知道哪些事呢？'
    )

    _response = OrderedDict([
        ('自我介紹', [
            TextSendMessage(text='你好！我是目前就讀台大資工系大三的高偉倫，' +
                                 '平時的興趣是聽團和玩音樂，喜歡嘗試各種新事物。' +
                                 '希望未來能夠成為LINE TECH FRESH的一員，還請多多指教！\n\n' + 
                                 'Github連結：\nhttps://github.com/william881218\n' + 
                                 'LinkedIn連結：\nhttps://www.linkedin.com/in/wei-lun-kao-0341191a3/\n')
        ]),
                                        
        ('實習動機', [
            TextSendMessage(text='我一直認為實習是快速認識自己的最佳方法。' +
                                 '在參加過LINE TECHPULSE之後，我對許多領域都很有興趣：' + 
                                 'Data Engineer, Backend Devloper, DevOps...' + 
                                 '因為不確定自己未來的職涯選擇，若有幸能成為Line Tech Fresh的一員，' + 
                                 '我非常希望在發揮自己專長對Line帶來一些貢獻之餘，' +
                                 '也讓自己更確定未來走的路。')
        ]),

        ('專業技能', [
            TextSendMessage(text='我熟悉C/C++/Python，對ML的framework和相關技術原理也非常嫻熟，' + 
                                 '接觸過的應用domain有CV, NLP (transformer/BERT), ASR (Deepspeech/Kaldi)。'),
            TextSendMessage(text='我習慣在Linux的環境下開發，知道基本的後端與CI/CD的知識，平常開發也習慣使用Git當作版本控制工具。'),
            TextSendMessage(text='我也是一個喜歡自學新東西的Fast-Learner，預計寒假會在Udemy上把全端開發的基本框架（前後端 + Database)學完，' + 
                                 '補足自己不足的知識，希望能讓自己更適合成為LINE TECH FRESH的一員！')
        ]),

        ('工作經驗', [
            TextSendMessage(text='1. 台大數位學習中心 Intern\n' + 
                                '工作內容：\n' +
                                '從0開始開發上課錄影投影片換頁偵測的功能。' + 
                                '需要自己去survey和prototype各種做法，' + 
                                '並且定期和成員開會更新進度並報告。'),
            TextSendMessage(text='2. 華碩AI研發中心 Intern\n' + 
                                 '工作內容：\n' + 
                                 '(1) 利用Data Augmentation增進已上線模型的準確率(從89.1%到91.2%)。\n' + 
                                 '(2) 協助重構現有的資料處理函式庫。\n' + 
                                 '(3) 開發PoC，負責資料分析和訓練baseline model。')
        ]),

        ('專案展示', [
            TextSendMessage(text='1. Adversarial Attack on ASR\n' + 
                                  '我使用pytorch和flask搭建了一個web-based的demo。' + 
                                  '使用者可以輸入原始音檔和想要攻擊的target transcription，' +
                                  '此網頁便能回傳一個加了惡意噪音的音檔，可用以攻擊在同個頁面上的語音辨識系統。\n' + 
                                  'Github連結: https://github.com/william881218/Adversarial-ASR-Attack\n' +
                                  'Demo: http://140.112.90.203:9999'),
            TextSendMessage(text='2. Simple Bulleting and Video Streaming Sharing\n' + 
                                  '這是一個課堂project，留言版功能的部分僅使用python的socket programming；' + 
                                  '影片分享的功能主要是利用flask達到影片串流的功能。' + 
                                  '使用者可以直接在留言欄輸入使用者和留言內容；' + 
                                  '也可以在影片串流的頁面分享自己的影片，讓所有人看到一樣的影片串流。\n' + 
                                  'Github連結: https://github.com/william881218/Simple-Bulletin-and-Multimedia-Streaming\n' + 
                                  'Demo: http://140.112.90.200:9527'),
            TextSendMessage(text='3. Chinese Article Summarization\n' +
                                 '這也是一個課堂project，主要是利用Seq2seq + Attention的模型架構去做中文文章摘要。\n' + 
                                 'Github連結: https://github.com/william881218/Article-Summarization')
        ]),

        ('研究領域', [
            TextSendMessage(text='2020二月，我加入台大人工智慧安全實驗室跟著教授一起做專題，' + 
                                 '專題內容主要是探討語音辨識模型的惡意攻擊與防禦'),
            TextSendMessage(text='2020十月，開始和同實驗室的博士生進行另一個有關語音驗證碼(Audio Captcha)的研究。')
        ]),
    ])


    @classmethod
    def response_to_message(cls, message):
        """
        Given a message from user, return the most appropriate response.
        If no appropriate response can be found, raise an error.
        """

        for key_idx, key_word in enumerate(cls._response.keys()):
            if message in key_word or str(key_idx+1) == message:
                return cls._response[key_word] + [cls._finish_responing]

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
                '3. 專業技能\n' +
                '4. 工作經驗\n' +
                '5. 專案展示\n' + 
                '6. 研究領域\n' +
                '謝謝！'
        )


        @classmethod
        def greeting_new_follower(cls):
            """
            Return greeting message for new followers.
            """
            return cls._greeting


# A self-defined exception for unrecognizable user message.
class UnknownMessageError(Exception):
    pass