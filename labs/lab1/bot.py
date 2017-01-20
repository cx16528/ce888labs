from sopel import module
from emo.wdemotions import EmotionDetector
ave = None
emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    global ave
    a = 0.01
    print(str(trigger))
    print (ave)
    if(ave is None):
        ave = (emo.detect_emotion_in_raw_np(str(trigger)))
    else:
        ave = ave + a * (emo.detect_emotion_in_raw_np(str(trigger)) - ave)

    #ave_love = ave[2]
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + ave + trigger.nick)
    print(ave)
