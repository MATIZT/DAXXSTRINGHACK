from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """𝙃𝙚𝙮 {}
𝗜 𝗔𝗺 **{}** 𝘼 𝘽𝙤𝙩 𝙁𝙤𝙧 𝙃𝙖𝙘𝙠 𝙏𝙂 𝙐𝙨𝙚𝙧 𝘼𝙘𝙘𝙤𝙪𝙣𝙩. 𝙑𝙞𝙖 𝙐𝙨𝙚𝙧 𝙎𝙚𝙨𝙨𝙞𝙤𝙣.

» ɪ sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ sᴇssɪᴏɴ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ
» ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ I ᴄᴀɴ ᴅᴏ ғᴏʀ ʏᴏᴜ.
"""

HACK_TEXT = """
"A" : [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]

"B" : [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsʀɴᴀᴍᴇ... ᴇᴛᴄ]

"C" : [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]

"D" : [ᴋɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ ᴏᴘᴛɪᴏɴ B ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ Aᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]

"E" : [Jᴏɪɴ A Gʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

"F" : [Lᴇᴀᴠᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

"G" : [Dᴇʟᴇᴛᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ]

"H" : [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]

"I" : [ᴛᴇʀᴍɪɴᴀᴛᴇ Aʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ Yᴏᴜʀ SᴛʀɪɴɢSᴇssɪᴏɴ]

"J" : [ᴅᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ]

"K" :~ [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

"L" :~ [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]
"""
info = """❥︎ ɴᴀᴍᴇ : {}
❥︎ ᴜsᴇʀ ɪᴅ : {}
❥︎ ᴘʜᴏɴᴇ ɴᴏ : +{}
❥︎ ᴜsᴇʀɴᴀᴍᴇ : @{}"""

PM_BUTTON = IKM([[IKB("•─╼⃝𖠁 𝐇𝐀𝐂𝐊 𖠁⃝╾─•", callback_data="hack_btn")]])



HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),          
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
                   
    ],
    [
        IKB("J", callback_data="J"),
        IKB("K", callback_data="K"),
        IKB("L", callback_data ="L"),                           
    ],
    ],    
    )



LOG_TEXT = """
     ● ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ●

 ❥︎ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ 
 ❥︎ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.
 ❥︎ ᴏᴡɴᴇʀ : Matin
"""
