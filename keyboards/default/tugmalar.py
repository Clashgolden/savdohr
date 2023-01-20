from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

boshmenyu = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
boshmenyu.add(KeyboardButton("✅ Roziman"))


# ==========================================================================

boshlash = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
boshlash.add(KeyboardButton("✅ Boshlash"))

# ==========================================================================

orqa = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
orqa.add(KeyboardButton("◀️Orqaga"))

# ==========================================================================

raqam = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
raqam.add(KeyboardButton("📲 Telefon raqamimni jo'natish",request_contact=True))

# ==========================================================================

yashaydimi = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
yashaydimi.add(KeyboardButton("Ha"))
yashaydimi.add(KeyboardButton("Yo'q"))
yashaydimi.add(KeyboardButton("◀️Orqaga"))

# ==========================================================================

tuman = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
tuman.add(KeyboardButton("Urganch"))
tuman.insert(KeyboardButton("Hazorasp"))
tuman.add(KeyboardButton("Xonqa"))
tuman.insert(KeyboardButton("Qo'shko'pir"))
tuman.add(KeyboardButton("Shovot"))
tuman.insert(KeyboardButton("Bog'ot"))
tuman.add(KeyboardButton("Gurlan"))
tuman.insert(KeyboardButton("Xiva Tumani"))
tuman.add(KeyboardButton("Urganch Tumani"))
tuman.insert(KeyboardButton("Yangiariq"))
tuman.add(KeyboardButton("Xiva Shahri"))
tuman.insert(KeyboardButton("Yangibozor"))
tuman.add(KeyboardButton("Tuproqqal'a"))

# ===========================================================================

darajasi = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
darajasi.add(KeyboardButton("O'rta"))
darajasi.insert(KeyboardButton("Oliy"))
darajasi.insert(KeyboardButton("Magistr"))

# ===========================================================================

oilasi = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
oilasi.add(KeyboardButton("Oilali"))
oilasi.add(KeyboardButton("Bo'ydoq/Turmushga chiqmagan"))
oilasi.add(KeyboardButton("Ajrashgan"))

# ===========================================================================

tilbiladi = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
tilbiladi.add(KeyboardButton("0%"))
tilbiladi.insert(KeyboardButton("25%"))
tilbiladi.add(KeyboardButton("50%"))
tilbiladi.insert(KeyboardButton("75%"))
tilbiladi.add(KeyboardButton("100%"))

# ===========================================================================

kasblar = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kasblar.add(KeyboardButton("Sotuv Bo'limi Rahbari"))
kasblar.insert(KeyboardButton("Sotuv Menejeri"))
kasblar.add(KeyboardButton("Sotuv Operatori"))
kasblar.insert(KeyboardButton("Administrator"))
kasblar.add(KeyboardButton("Oddiy Xodim"))