import os
import telebot
from telebot import types

# تعيين توكن البوت الخاص بك هنا
token = "7232454111:AAEDr1hfeacm8C6ZjoYZOsumIPMY5mntkW8"
bot = telebot.TeleBot(token)

# دالة بداية البوت واستقبال أمر /start
@bot.message_handler(commands=["start"])
def start(message):
    # إعداد الأزرار
    markup = types.InlineKeyboardMarkup()
    
    # إضافة الأزرار المطلوبة
    button1 = types.InlineKeyboardButton("ᴍᴏʜᴏᴍᴍᴇᴅ", url="https://t.me/KOK0KK")
    markup.add(button1)
    button2 = types.InlineKeyboardButton("ملفات 𝐏𝐘𝐓𝐇𝐎𝐍", url="https://t.me/Your_uncle_Muhammad")
    markup.add(button2)

    # إرسال الصورة مع الرسالة والأزرار
    bot.send_photo(
        message.chat.id,
        "https://t.me/B_6ODA/2151",
        caption="""
        **╭⦿  ꜱᴏᴜꝛᴄᴇ.ɴᴧᴍᴇ: ᴍᴏʜᴧᴍᴍᴇᴅ
        │᚜⦿ ꜱʏꜱᴛᴇᴍ: ᴘʏᴛʜᴏɴ
        │᚜⦿ ʟᴧɴɢᴜᴧɢᴇ: ɪꜱ ᴧꝛᴧʙɪᴄ
        │᚜⦿ ᴅᴧᴛᴇ ᴄʀᴇᴧᴛᴇᴅ: 2024-10-26
        ╰⦿  ᴏᴡɴᴇʀ ᴏꜰ ᴍᴏʜᴧᴍᴍᴇᴅ: [ᴍᴏʜᴧᴍᴍᴇᴅ](https://t.me/KOK0KK)**
        """,
        reply_markup=markup,
        parse_mode='Markdown'
    )

# دوال تنسيق الاسم بزخارف متعددة
def stylish_name(name):
    styles = [
        ("𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭", "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝗲𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"),  
        ("𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩", "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓝𝓸𝓹𝓾𝓼𝓽𝓸𝓿𝔀𝔵"),  
        ("𝔄𝔅𝔇𝔈𝔉𝔊𝔏𝔐𝔑𝔒𝔔𝔙", "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔠"),  
        ("𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁", "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"),  
        ("𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕺𝕽𝕾𝕿𝕾𝕻𝕻𝕾𝕺𝕿", "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"),  
        ("𝔸𝔹ℂ𝔻ℰ𝔽𝔾𝔻ℋ𝔼𝔻ℐ𝔻ℋ𝔼𝔽𝔼𝔸𝔻ℕ", "𝔞𝔟𝔠𝔡𝔢𝔣𝔞𝔡𝔦𝔠𝔱𝔲𝔹"),  
        ("ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿˢᵀᵁᵛᵂᵡᵞᶻ", "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴾʳsᴛᴜᴠᴡxʏᴢ"),  
        ("ᴀʙᴄᴅᴇᴈɢʜɪᴊᴋʟᴍɴᴏᴾʳsᴛᴜᴠᴡᴥʏᴢ", "ᴀʙᴄᴅᴇᴈɢʜɪᴊᴋʟᴍɴᴏᴾʳsᴛᴜᴠᴡᴥʏᴢ"),  
        ("ᵃᵇᶜᵈᵉᶠᵍʰᶤʲᵏˡᵐᶰᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ", "ᵃᵇᶜᵈᵉᶠᵍʰᶤʲᵏˡᵐᶰᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ"),  
        ("𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟", "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"),  
        ("ꪖ᥇ᥴᦔꫀᠻᧁꫝ𝓲𝓳𝘬ꪶꪑꪀꪮρ𝘲𝘳𝘴𝓽ꪊꪜ᭙᥊ꪗɀ", "ꪖ᥇ᥴᦔꫀᠻᧁꫝ𝓲𝓳𝘬ꪶꪑꪀꪮρ𝘲𝘳𝘴𝓽ꪊꪜ᭙᥊ꪗɀ"),  
        ("ᴬᴮᶜᵈᵉꜻᶜʜᴵᴶᴷᴸᴹᴺᴼᵖᵠᴿˢᵀᵁᵛᶻ", "ᴬᴮᶜᵈᵉꜻᶜʜᴵᴶᴷᴸᴹᴺᴼᵖᵠᴿˢᵀᵁᵛᶻ"),
        ("ᴧʙᴄᴅᴇꜰɢʜɪʲᴋʟᴍɴᴏᴘᵠꝛsᴛᴜᴠᴡхʏᴢ", "ᴧʙᴄᴅᴇꜰɢʜɪʲᴋʟᴍɴᴏᴘᵠꝛsᴛᴜᴠᴡхʏᴢ"),
    ][style_name(name, *style) for style in styles]

def style_name(name, upper_style, lower_style):
    name = name.upper()
    stylish = ''.join([upper_style[ord(c) - ord('A')] if 'A' <= c <= 'Z' else c for c in name])
    return stylish

# استقبال النصوص من المستخدم وتطبيق الزخرفة
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    name = message.text.strip()
    decorated_names = stylish_name(name)
    decorated_message = '\n'.join(decorated_names)
    bot.send_message(message.chat.id, decorated_message)

# تشغيل البوت وتحديد المنفذ
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    bot.polling(none_stop=True, timeout=60)
