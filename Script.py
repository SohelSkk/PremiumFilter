class script(object):
    START_TXT = """<b>Hello {}</b>

Iam A Simple Auto Filter + Movie Search + Manual Filter Bot. I Can Provide Movies In Telegram Groups. You Can Search Movies Via Inline. I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group And Enjoy

<b>Made With ❤ BY @Archie_bots</b>"""

    HELP_TXT = """<b>Hᴇʏ {} Fʀɪᴇɴᴅ Hᴇʀᴇ Yᴏᴜʀ Bᴜᴛᴛᴏɴs 👇</b>"""

    PRIVATEBOT_TXT = """<b>Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ

- ›› Mᴜsᴛ Aᴅᴅ Mᴇ Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ Oɴ Tʜɪs Gʀᴏᴜᴘ

- ›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect

- ›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ

- ›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>
"""

    MODS_TXT = """I Hᴀᴠᴇ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs"""

    PONGD_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""
    
    PONG_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: FilmyzillaBot
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Archie_Bots>Archie Bots</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""

    SOURCES_TXT = """Tʜɪs Is Aɴ Oᴩᴇɴ-Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Bʏ @Tamilan_BotsZ

- 100﹪ Cᴏᴅᴇᴅ Bʏ <a href=https://t.me/SharathItsIsme>sʜᴀʀᴀᴛʜ</a>

- & Rᴇᴩᴏ Lɪɴᴋ 👇 Hᴇʀᴇ"""

    SOURCE_TXT = """Tʜɪs Is Aɴ Oᴩᴇɴ-Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Bʏ @Tamilan_BotsZ</b>

- 100﹪ Cᴏᴅᴇᴅ Bʏ <a href=https://t.me/SharathItsIsme>sʜᴀʀᴀᴛʜ</a></b>

- Rᴇᴩᴏ Lɪɴᴋ 👇 Hᴇʀᴇ"""

    FONT_TXT = """I Cᴀɴ Gᴇɴᴇʀᴀᴛᴇ Aᴛᴛʀᴀᴄᴛɪᴠᴇ Fᴏɴᴛs Fᴏʀ Yᴏᴜʀ Tᴇxᴛ Sᴇɴᴅ Lɪᴋᴇ Tʜɪs 👇

ᴇɢ :- /font hi da"""

    CARBON_TXT = """/carbon ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /carbon hi"""

    SHARE_TXT = """/share ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /share hi da"""

    VIDEO_TXT ="""Dᴏᴡɴʟᴏᴀᴅ Aɴʏ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏ Fʀᴏᴍ Tʜᴇ Vɪᴅᴇᴏ Lɪɴᴋ

• Hᴏᴡ Tᴏ Usᴇ
• Tʏᴘᴇ /video 𝘈𝘯𝘥 (YᴏᴜTᴜʙᴇ Vɪᴅᴇᴏ Lɪɴᴋ)
• Exᴀᴍᴘʟᴇ:
• /video https://youtu.be/kB9TkCscX0"""

    TELE_TXT = """▫️Hᴇʟᴘ: ▪️ Tᴇʟᴇɢʀᴀᴘʜ ▪️
     Tᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ
    Usᴀɢᴇ
    🤧 /telegraph - Sᴇɴᴅ Mᴇ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ (5ᴍʙ)"""

    MANUELFILTER_TXT = """<b>Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Usɪɴɢ Tʜɪs Bᴏᴛ</b> 😌 🔋

<b>Fɪʀsᴛ Jᴏɪɴ Tʜɪs Gʀᴏᴜᴩ » <a href=https://t.me/+bgKgAUWN1pw2Nzll>@FilmyzillaBotChat</a></b>

<b>Sᴇɴᴅ Yᴏᴜ Wᴀɴᴛ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴩᴇʟʟɪɴɢ</b>

<b>Aɴᴅ Bᴏᴛ Wɪʟʟ Sᴇɴᴅ Yᴏᴜ Asᴋᴇᴅ Fɪʟᴇ</b>

<b>Hᴏᴡ Tᴏ Oᴩᴇɴ Bᴏᴛ Sᴇɴᴅᴇᴅ Fɪʟᴇ Lɪɴᴋ. » <a href=https://t.me/Filmyzilla_Updates>ᴛᴜᴛᴏʀɪᴀʟ</a>.﹤/b>"""

    CONTACT_TXT = """<b>
<b>»» ° Oɴʟʏ Cᴏɴᴛᴀᴄᴛ Fᴏʀ Pᴀɪᴅ Wᴏʀᴋs / Pʀᴏʙʟᴇᴍ / Dᴏᴜʙᴛ / Cᴏʟʟᴀʙ / Hᴇʟᴩ °</b>

<b>»» Iғ U Cᴏɴᴛᴀᴄᴛ Mᴇ Sᴇᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs 😙</b>
"""

    STATUS_TXT = """<b><u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</b></u>
    
<b>📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code>
🗄️ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code></b>
"""
    LOG_TEXT_G = """<b> #NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} </b>
"""
    LOG_TEXT_P = """<b> #NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} </b>
"""
