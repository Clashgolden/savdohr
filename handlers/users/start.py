from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.tugmalar import boshmenyu,boshlash,orqa,raqam,yashaydimi,tuman,darajasi,oilasi,tilbiladi,kasblar
from aiogram.dispatcher import FSMContext
from states.xodim import ishchi
from loader import dp,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo(photo='https://t.me/jdasbhbhsd/2',caption=f"<b>Assalomu alaykum,\n\nHurmatli {message.from_user.full_name} - Avvalambor bor bizning Kompaniyamizga qiziqish bildirganinggizdan xursandmiz😊\n\nIsh bo'yicha tanishib chiqish, yoki ishlash qaroringgiz qat'iy bo'lsa✍️\n\nBizning Kompaniyamiz ish faoliyati bilan tanishib chiqishinggizni so'raymiz!☝️\n\nTanishish uchun: <a href='https://telegra.ph/Talim-Rivoj-01-18'>Bu Yerga Bosing!</a>\n\nTanishib chiqqaninggizdan keyin pastdagi - ✅ Roziman tugmasini bosing!👇</b>",reply_markup=boshmenyu)

@dp.message_handler(text="✅ Roziman")
async def sotuv(message: types.Message):
    await message.answer('''<b>SIZNI QADRLAYDIGAN JAMOADA SOTUVGA DOIR BILIMLARNI O'RGANISHNI VA ISHLASHNI XOXLAYSIZMI?</b>

Unda siz uchun - <b>AJOYIB IMKONIYAT!</b>

✅<b> " Ta’lim Rivoj " </b>- kompaniyasi jamoasiga <b>"SOTUV MENEJERI"</b>  lavozimiga ishga taklif qiladi.

✳️<b> ISH NIMADAN IBORAT:</b>
• O’qish yuzasidan qo’ng’iroq qilgan abituriyent, maktab bitiruvchilari, kollej bitiruvchilari, va univeristet bo’yicha to’liq ma’lumotga ega bo’lmoqchi bo’lgan har qanday insonlar bilan;
• Telefon orqali suxbat qilish;
• Yuzma yuz suxbat qilish;
• Ijtimoiy tarmoqlar orqali suxbat qilish; 
• Kompaniyamiz va universitet bo’yicha to’liq ma’lumot berish;
• Bajarilgan ishlarni hisobotini muntazam yuritib borish;
• Sotuv rejasini amalga oshirish;
• Mijozlar bilan shartnomalar tuzish;

✅ <b>BIZ, AYNAN SIZNI TANLAYMIZ AGAR SIZ:</b>
• 19-25 yoshdagi qiz bo’lsangiz;
• Jamoada ishlash maxorati;
• Har qanday shevada xususan sof o’zbek tilida suxbatlasha olsangiz;
• Insonlar bilan samimiy munosabat qura olsangiz xushmuomala qilishingiz;
• Eshitishni va fikringizni yetqaza olishni bilishingiz;

🎯 <b>SHAXSIY SIFATLAR:</b>

• Masulyatli;
• Tashabbus;
• Samaradorlik;
• Sabrli;
• Halollik;
• Axborotga e'tiborlilik;
• Vaqtni qadrlash;
• Energiyaga to’la;
• Maqsadli shijoatlilik;
• Quvnoq xazilkash;

🔆<b> SIZNI QANDAY IMKONIYATLAR KUTIB TURIBDI ?</b>
• Sotuvga doir barcha bilim ko’nikmalarni o’rganish;
• Insonlar bilan muloqat qilishni o’rganish;
• Tog’ri maqsad qo’yish va bosqichma boshqich maqsadga tog’ri harakat qilish va natijaga erishish o'rganasiz;
• Zamonaviy texnologiyalarga to’la atmasfera;
• Raqobatdosh ish haqi;
• Yuqori maosh;
• Birdamlikda harakat qiluvchi jamoa;
• Korparativ ta’lim Rivojlanish;
• Professianal o’sish va o’zini ko’rsata ish;
• Karyera markazi;

- Agar siz <b>Karyerangizga</b> qadam tashlash niyatida bo’lsangiz,
Moliyaviy erkinlikga chiqish qaroringiz <b>Qa’tiy Bo’lsa,</b> 
Biznes va zamonaviy kasblarga doir bilimlarni egallash va mutaxxasis bo’lish maqsadingiz qa’tiy bo’lsa...

<b>Siz bizni safimizdasiz ✔</b>️

Tayyor bo’lsangiz, siz haqingizda bizga qisqacha ma’lumotlar kerak, Ish ma'qul bo’lgan bo’lsa - <b>✅ Boshlash</b> tugmasini bosing!''',reply_markup=boshlash)

@dp.message_handler(text = "✅ Boshlash",state=None)
async def stateda(message:types.Message):
    text = f"<b>[1/13] - Ism Familyanggizni kiriting:</b>"
    await message.answer(text,reply_markup=orqa)
    await ishchi.name.set()

@dp.message_handler(text="◀️Orqaga",state="*")
async def orqaga(message:types.Message, state: FSMContext):
    text = f"bosh menyuga qaytdinggiz"
    await message.answer(text,reply_markup=boshmenyu)
    await state.finish()

@dp.message_handler(state=ishchi.name)
async def ismi(message:types.Message,state:FSMContext):
    name = message.text
    await state.update_data({'name':name})
    text = f"<b>[2/13] - Pastdagi tugmani bosib telefon raqaminggizni jo'nating:</b>"
    await message.answer(text,reply_markup=raqam)
    await ishchi.next()

@dp.message_handler(state=ishchi.phone,content_types=types.ContentType.CONTACT)
async def telefon(message:types.Message,state:FSMContext):
    phone = message.contact.phone_number
    await state.update_data({'phone':phone})
    text = f"<b>[3/13] - Yoshinggizni kiriting:</b>"
    await message.answer(text)
    await ishchi.next()

@dp.message_handler(state=ishchi.age)
async def yoshi(message:types.Message,state:FSMContext):
    age = message.text
    await state.update_data({'age':age})
    text = f"<b>[4/13] - Siz Xorazmda yashaysizmi?</b>"
    await message.answer(text,reply_markup=yashaydimi)
    await ishchi.next()

@dp.message_handler(state=ishchi.xorazm)
async def qayerida(message:types.Message,state:FSMContext):
    xorazm = message.text
    await state.update_data({'xorazm':xorazm})
    text = f"<b>[5/13] - Xorazmning qaysi xududida yashaysiz?</b>"
    await message.answer(text,reply_markup=tuman)
    await ishchi.next()

@dp.message_handler(state=ishchi.where)
async def hududi(message:types.Message,state:FSMContext):
    where = message.text
    await state.update_data({'where':where})
    text = f"[6/13] - <b>Malumotinggiz qanday?</b>"
    await message.answer(text,reply_markup=darajasi)
    await ishchi.next()

@dp.message_handler(state=ishchi.info)
async def bilim(message:types.Message,state:FSMContext):
    info = message.text
    await state.update_data({'info':info})
    text = f"<b>[7/13] - Oilaviy holatinggiz qanday?</b>"
    await message.answer(text,reply_markup=oilasi)
    await ishchi.next()

@dp.message_handler(state=ishchi.family)
async def semya(message:types.Message,state:FSMContext):
    family = message.text
    await state.update_data({'family':family})
    text = f"<b>[8/13] - Oldin qaysi Kompaniya yoki Tashkilotda ishlagansiz?</b>"
    await message.answer(text)
    await ishchi.next()

@dp.message_handler(state=ishchi.worked_before)
async def oldin(message:types.Message,state:FSMContext):
    worked_before = message.text
    await state.update_data({'worked_before':worked_before})
    text = f"<b>[9/13] - Oldingi Kompaniyanggizda qaysi lavozimda ishlagansiz?</b>"
    await message.answer(text,reply_markup=kasblar)
    await ishchi.next()

@dp.message_handler(state=ishchi.wordked_as)
async def oldinlavozim(message:types.Message,state:FSMContext):
    worked_as = message.text
    await state.update_data({'worked_as':worked_as})
    text = f"<b>[10/13] - Oldin ishxonanggizda qancha maosh olgansiz?</b>"
    await message.answer(text)
    await ishchi.next()

@dp.message_handler(state=ishchi.salary_before)
async def oldinmaosh(message:types.Message,state:FSMContext):
    salary_before = message.text
    await state.update_data({'salary_before':salary_before})
    text = f"<b>[11/13] - O'zinggizning sotuvchilik mahoratinggizga 10 ballik sistemada necha ball bergan bo'lar edinggiz?</b>"
    await message.answer(text)
    await ishchi.next()

@dp.message_handler(state=ishchi.ball)
async def bahosi(message:types.Message,state:FSMContext):
    ball = message.text
    await state.update_data({'ball':ball})
    text = f"<b>[12/13] - O'zbek tilidagi nutqinggiz ravonligini ko'rsating</b>"
    await message.answer(text,reply_markup=tilbiladi)
    await ishchi.next()

@dp.message_handler(state=ishchi.language)
async def tili(message:types.Message,state:FSMContext):
    language = message.text
    await state.update_data({'language':language})
    text = f"<b>[13/13] - Iltimos o'zinggizning hozirgi kundagi rasminggizni yuboring?</b>"
    await message.answer(text)
    await ishchi.next()

@dp.message_handler(state=ishchi.photo,content_types=types.ContentType.PHOTO)
async def rasmi(message:types.Message,state:FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data({'photo':photo})
    await message.answer_photo(photo='https://t.me/jdasbhbhsd/2',caption=f"<b>Hurmatli - {message.from_user.full_name}. Tabriklaymiz siz omadli ro'yxatdan o'tdinggiz!\n\nAnketanggiz nazoratchilarimiz tomonidan ma'qul topilsa, menejerlarimiz siz bilan bog'lanishadi!</b>")
    await message.answer("<b>Bizning manzil\n\nManzil: </b>Urganch shahar, IT Texnikum\n<b>Mo’ljal:</b> Xalq bank yon tomoni, IT Park.\n\n<b>Bizning ijtimoiy tarmoqlar:</b> \n<a href='https://www.youtube.com/@TalimRivoj'>Youtube</a> | <a href='https://www.instagram.com/talimrivoj/'>Instagram</a> | <a href='https://t.me/TalimRivoj'>Telegram</a>\n\n<b>Biz bilan bog’lanish: +998 90 077 00 67</b>",reply_markup=boshmenyu)
    data = await state.get_data()
    photo = data.get('photo')
    await bot.send_photo(chat_id=-1001841490315,photo=photo,caption=f"<b>Yangi Nomzod:</b>\n\n"
                                                                    f"<b>Ismi:</b>  <i> {data['name']}</i>\n"
                                                                    f"<b>Raqami:</b>   <i>{data['phone']}</i>\n"
                                                                    f"<b>Yoshi:</b>   <i>{data['age']}</i>\n"
                                                                    f"<b>Xorazmdanmi:</b>   <i>{data['xorazm']}</i>\n"
                                                                    f"<b>Qayeridan:</b>   <i>{data['where']}</i>\n"
                                                                    f"<b>Ma'lumoti:</b>   <i>{data['info']}</i>\n"
                                                                    f"<b>Oilasi:</b>   <i>{data['family']}</i>\n"
                                                                    f"<b>Oldingi kompaniya:</b>   <i>{data['worked_before']}</i>\n"
                                                                    f"<b>Oldingi lavozimi:</b>   <i>{data['worked_as']}</i>\n"
                                                                    f"<b>Oldingi maoshi:</b>   <i>{data['salary_before']}</i>\n"
                                                                    f"<b>Sotuvchiligiga:</b>  <i>10/{data['ball']} ball</i>\n"
                                                                    f"<b>O'zbek tili darajasi:</b>  <i>{data['language']}</i>")
    await state.finish()