import asyncio
from aiogram import Dispatcher, Bot, filters, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()


class Card(StatesGroup):
    card_number = State()
    card_number_2 = State()


class Card_1(StatesGroup):
    card_number = State()
    card_number_2 = State()


contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)

til = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Uzb 🇺🇿")],
    [KeyboardButton(text="Rus 🇷🇺")]
], resize_keyboard=True)

til_1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="O'zbek tili 🇺🇿")],
    [KeyboardButton(text="Русский язык 🇷🇺")]
], resize_keyboard=True)

kb = [
    [KeyboardButton(text="🌭 Hot dog"), KeyboardButton(text="🌯 Lavash menu")],
    [KeyboardButton(text="🍔 Burger menu"), KeyboardButton(text="🍹 Ichimliklar")],
    [KeyboardButton(text="🍟 Qo'shimcha"), KeyboardButton(text="🎂 Shirinliklar"), KeyboardButton(text="🔙 Orqaga")]
]
mb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

kb_1 = [
    [KeyboardButton(text="🔍 Menu"), KeyboardButton(text="🛒 Savat"), KeyboardButton(text="Ma'lumot")],
    [KeyboardButton(text="📲 My info"), KeyboardButton(text="Yordam"), KeyboardButton(text="Tilni o'zgartirish")]
]
mb_1 = ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True)

savat_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sotib olish"), KeyboardButton(text="🚮 Savatni tozalash")],
    [KeyboardButton(text="🗑 Savatni ko'rish"), KeyboardButton(text="🔙 Orqaga")]
], resize_keyboard=True)

mb_hd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌭 Classic Hot dog", callback_data="Classic_Hot_dog"),
     InlineKeyboardButton(text="🌭 Combo Hot dog", callback_data="Combo_Hot_dog")],
    [InlineKeyboardButton(text="🌭 Sirli Hot dog", callback_data="Sirli_Hot_dog"),
     InlineKeyboardButton(text="🌭 Double Hot dog", callback_data="Double_Hot_dog")],
])

mb_burger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍔 Mini burger", callback_data="Mini_burger"),
     InlineKeyboardButton(text="🍔 Gamburger", callback_data="Gamburger")],
    [InlineKeyboardButton(text="🍔 Cheese burger", callback_data="Cheese_burger"),
     InlineKeyboardButton(text="🍔 Chicken burger", callback_data="Chicken_burger")],
    [InlineKeyboardButton(text="🍔 Combo burger", callback_data="Combo_burger")],
])

mb_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌯 Lavash", callback_data="Lavash"),
     InlineKeyboardButton(text="🌯 Combo Tandir Lavash", callback_data="Combo_Tandir_Lavash")],
    [InlineKeyboardButton(text="🌯 Tandir Lavash", callback_data="Tandir_Lavash"),
     InlineKeyboardButton(text="🌯 Combo Lavash", callback_data="Combo_Lavash")],
])

mb_i = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="☕ Capuccino", callback_data="Coffee_1"),
     InlineKeyboardButton(text="🍹 Tropic", callback_data="Tropic_1")],
    [InlineKeyboardButton(text="💧 Hydrolife", callback_data="Hydrolife_1"),
     InlineKeyboardButton(text="🍸 Moxito", callback_data="Moxito_1")]
])

mb_q = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍟 Free", callback_data="Free"),
     InlineKeyboardButton(text="🍪 Smayliki", callback_data="Smayliki")],
    [InlineKeyboardButton(text="🥫 Ketchup", callback_data="Ketchup"),
     InlineKeyboardButton(text="🥫 Mayanez", callback_data="Mayanez")],
])

mb_sh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍹 Kokteyl", callback_data="Kokteyl"),
     InlineKeyboardButton(text="🍰 Tort", callback_data="Tort")],
    [InlineKeyboardButton(text="🍩 Bulochka", callback_data="Bulochka"),
     InlineKeyboardButton(text="🍦 Muzqaymoq", callback_data="Muzqaymoq")],
])

pay_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_2")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_3")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_4")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_5")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_6")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_7")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_8")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_9")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_10")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_11")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_12")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_13")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_14")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_15")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_16 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_16")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_17 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_17")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_18 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_18")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_19 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_19")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_20 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_20")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_21 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_21")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_22 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_22")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_23 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_23")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_24 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_24")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_25 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_25")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

cart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Uzcard", callback_data="Uzcard")],
    [InlineKeyboardButton(text="💳 Humo", callback_data="Humo")],
])

balance = 50000
orders = []


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(f"\n \n Salom {message.from_user.full_name}, botga xush kelibsiz !!!", reply_markup=til)


@dp.callback_query(F.data == "Menu")
async def start_function(call: types.CallbackQuery):
    await call.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgcHamCzJt-qENl1BBA1OhlKsl3Bubsg-feg&s",
        caption="\n \n  EVOS menusi bilan tanishing. \n 1 Hot_dog \n 2 Gamburger \n 3 Lavash_menu \n 4 Ichimliklar \n 5 Qo'shimcha \n 6 Shirinliklar \n \n \n",
        reply_markup=mb)


@dp.message(F.text == "🔍 Menu")
async def start_function(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgcHamCzJt-qENl1BBA1OhlKsl3Bubsg-feg&s",
        caption="\n \n EVOS menusi bilan tanishing. \n 1 Hot_dog \n 2 Gamburger \n 3 Lavash_menu \n 4 Ichimliklar \n 5 Qo'shimcha \n 6 Shirinliklar \n \n \n",
        reply_markup=mb)


@dp.message(F.text == "🔙 Orqaga")
async def ortga_function(message: types.Message):
    await message.answer("Siz ortga qaytdiz", reply_markup=mb_1)


@dp.message(F.text == "📲 My info")
async def info_function(message: types.Message):
    await message.answer(
        f"\n\nSizning ismingiz: {message.from_user.full_name} 😊\nSizning username'ingiz: @{message.from_user.username} 📱\nSizning ID raqamingiz: {message.from_user.id} 🔑\n\n",
    reply_markup=mb_1)


@dp.message(F.text == "Uzb 🇺🇿")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Xush kelibsiz\nIsmingizni kiriting: ")


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Endi familyangizni kiriting: ")


@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Yaxshi endi number kiriting: ", reply_markup=contact_button)


@dp.message(Registration.number)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Ajoyib !\nIsmingiz: {data['first_name']}\nFamilyangiz: {data['last_name']}\nTelefon nomeringiz: {data['number']}",
        reply_markup=mb_1)
    await state.clear()


@dp.message(F.text == "🌭 Hot dog")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoCkyHT7mIKrR2Xom0fs6oNsn80JzatgdNGA&s",
        caption=f"\n \n{message.from_user.full_name} siz Hot doglar bo'limini tanladingiz.", reply_markup=mb_hd)


@dp.callback_query(F.data == "Classic_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://yukber.uz/image/cache/catalog/classic%20hot%20dog-600x600.jpg",
        caption="\n \n Classic Hot dog 14 000 so'm \n \n",
        reply_markup=pay_1)


@dp.callback_query(F.data == "random")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Classic_Hot_dog narxi: 14000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !", reply_markup=mb)


@dp.callback_query(F.data == "Sirli_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgJJEGYB0GJ8HJA6Fxms7GP7Z3Env4TzR2AA&s",
        caption="\n \n Sirli Hot dog 16 000 so'm ",
        reply_markup=pay_2)


@dp.callback_query(F.data == "random_2")
async def send_random_value(callback: types.CallbackQuery):
    orders.append("Sirli_Hot_dog narxi: 16000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !!!", reply_markup=mb)


@dp.callback_query(F.data == "Double_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjlWcPo8tTY6AGrUqieI1oxcq63s-MQwzKbw&s",
        caption="\n \n Double Hot dog 22 000 so'm \n \n",
        reply_markup=pay_3)


@dp.callback_query(F.data == "random_3")
async def send_random_value(callback: types.CallbackQuery):
    orders.append("Double_Hot_dog narxi: 22000")
    global balance
    balance = balance - 22000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsIYZQXcdBH2ZabeWDRlKzhqkxeUMWBeGXbw&s",
        caption="\n \n Combo Hot dog 26 000 so'm \n \n",
        reply_markup=pay_4)


@dp.callback_query(F.data == "random_4")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Hot_dog narxi: 26000")
    global balance
    balance = balance - 26000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🍔 Burger menu")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK9LBKz0IZ1JAQUIckQwRJfk5c9_b0FsBXuw&s",
        caption=f"\n \n {message.from_user.full_name} siz Burgerlar bo'limini tanladingiz.",
        reply_markup=mb_burger)


@dp.callback_query(F.data == "Mini_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa5ZtGioOE49mUVh1bc3EPwmzIB4l9RaG0cw&s",
                                    caption="\n \n Mini_burger 16 000 so'm \n \n",
                                    reply_markup=pay_5)


@dp.callback_query(F.data == "random_5")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Mini_burger narxi: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Gamburger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtSUy5NmnPvAeaH-DdVnUaVciikPOG0DmfoA&s",
        caption="\n \n Gamburger 20 000 so'm \n \n",
        reply_markup=pay_6)


@dp.callback_query(F.data == "random_6")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Gamburger narxi: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Cheese_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://evos.com/wp-content/uploads/2016/10/burger_2009.jpg",
                                    caption="\n \n Cheese_burger 24 000 so'm \n \n",
                                    reply_markup=pay_7)


@dp.callback_query(F.data == "random_7")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Cheese_burger narxi: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Chicken_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_iVcFzROXn21H7lG5H4vFcML9NhRa4nGB8A&s",
        caption="\n \n Chicken_burger 28 000 so'm \n \n",
        reply_markup=pay_8)


@dp.callback_query(F.data == "random_8")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Chicken_burger narxi: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://telegra.ph/file/1e381adadd8b099f91158.jpg",
        caption="\n \n Combo_burger 32 000 so'm \n \n",
        reply_markup=pay_9)


@dp.callback_query(F.data == "random_9")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_burger narxi: 32 000")
    global balance
    balance = balance - 32000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🌯 Lavash menu")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU4676EF_T-dzQep4TBNxClYGPPRJfSu7NTw&s",
        caption=f"\n \n{message.from_user.full_name} siz Lavashlar bo'limini tanladingiz.",
        reply_markup=mb_lavash)


@dp.callback_query(F.data == "Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.express24.uz/r/600/600/OZpGZ7bkt6pXPFINvsIZq.jpg",
        caption="\n \n Lavash 20 000 so'm \n \n",
        reply_markup=pay_10)


@dp.callback_query(F.data == "random_10")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Lavash narxi: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Tandir_Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.express24.uz/r/600/600/lOuoAH0_ereI7jcnSjj_D.jpg",
        caption="\n \n Tandir Lavash 24 000 so'm \n \n",
        reply_markup=pay_11)


@dp.callback_query(F.data == "random_11")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Tandir_Lavash narxi: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThJaF81P-HOIEQG9yzG2UapRmBEAUm5YP46A&s",
        caption="\n \n Combo Lavash 28 000 so'm \n \n",
        reply_markup=pay_12)


@dp.callback_query(F.data == "random_12")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Lavash narxi: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_Tandir_Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.express24.uz/r/600/600/ysAeQlYdx3lKbf6L3D-OF.jpg",
        caption="\n \n Combo Tandir Lavash 30 000 so'm \n \n",
        reply_markup=pay_13)


@dp.callback_query(F.data == "random_13")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Tandir_Lavash narxi: 30 000")
    global balance
    balance = balance - 30000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🍹 Ichimliklar")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD6a7C94aHN0EAfJobwSOyZ54axXIHUcvkxQ&s",
                               caption=f"\n \n{message.from_user.full_name} siz Ichimliklar bo'limini tanladingiz.",
                               reply_markup=mb_i)


@dp.callback_query(F.data == "Coffee")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://latte.ru/wa-data/public/site/img/capp.jpeg",
                                    caption="\n \n Ichimlik Capucino 18 000 so'm \n \n",
                                    reply_markup=pay_14)


@dp.callback_query(F.data == "random_14")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Capucino narxi: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Hydrolife")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXMT5WbaId475mO1C-caqZb0JfU9KJVLm9IlU3o5TEHXKh3LrVR1JoFJJaMPprlLWFDkI&usqp=CAU",
                                    caption="\n \n Ichimlik Hydrolife 12 000 so'm \n \n",
                                    reply_markup=pay_15)


@dp.callback_query(F.data == "random_15")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Hydrolife narxi: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Ice_tea")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://devel.prom.uz/upload/product_logos/78/d3/78d3fd0d9b6216c60ebad53ea18096bd.jpeg",
                                    caption="\n \n Ichimlik Ice tea 6 000 so'm \n \n",
                                    reply_markup=pay_16)


@dp.callback_query(F.data == "random_16")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Ice tea narxi: 6 000")
    global balance
    balance = balance - 6000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Moxito")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.gazeta.uz/media/img/2021/05/hxSClG16221972734019_l.jpg",
                                    caption="\n \n Ichimlik Moxito 16 000 so'm \n \n",
                                    reply_markup=pay_17)


@dp.callback_query(F.data == "random_17")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Moxito narxi: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🍟 Qo'shimcha")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ01yt2f5IaMNhsj67ORWNFhBXdJjgBaJo4AQ&s",
                               caption=f"\n \n{message.from_user.full_name} siz Qo'shimchalar bo'limini tanladingiz.",
                               reply_markup=mb_q)


@dp.callback_query(F.data == "Free")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://media.express24.uz/r/600/600/StlAff2G-YemVPT4A-CzX.jpg",
                                    caption="\n \n Qo'shimchalar bo'limidan Free 12 000 so'm \n \n",
                                    reply_markup=pay_18)


@dp.callback_query(F.data == "random_18")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Free narxi: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Smayliki")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3qQkPXKGIYuWazr3FWgj-WXhdVODC74UGMQ&s",
        caption="\n \n Qo'shimchalar bo'limidan Smayliki 14 000 so'm \n \n",
        reply_markup=pay_19)


@dp.callback_query(F.data == "random_19")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Smayliki narxi: 14 000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Ketchup")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/1463280/72cadbb7f9f543a225f53b4adcc53121/M_height",
                                    caption="\n \n Qo'shimchalar bo'limidan Ketchup 2 000 so'm \n \n",
                                    reply_markup=pay_20)


@dp.callback_query(F.data == "random_20")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Ketchup narxi: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Mayanez")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/3595513/cea153fdc41e7f0f642449d0e9ad4506/M_height",
                                    caption="\n \n Qo'shimchalar bo'limidan Mayanez 2 000 so'm \n \n",
                                    reply_markup=pay_21)


@dp.callback_query(F.data == "random_21")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Mayanez narxi: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🎂 Shirinliklar")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz3nWDtmXxN-1Uuo6e0PeRff2AILYqxzjl_w&s",
        caption=f"\n \n{message.from_user.full_name} siz Shirinliklar bo'limini tanladingiz.",
        reply_markup=mb_sh)


@dp.callback_query(F.data == "Kokteyl")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://barline.club/upload/iblock/1c6/1c6bb56a28d51ad03dc17dad9a0a20ee.png",
                                    caption="\n \n Shirinlik Kokteyl 18 000 so'm \n \n",
                                    reply_markup=pay_22)


@dp.callback_query(F.data == "random_22")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Kokteyl narxi: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Bulochka")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-sprav-products/5236693/2a0000018a742bb08ea403c2535a2052d8a9/M_height",
        caption="\n \n Shirinlik Bulochka 8 000 so'm \n \n",
        reply_markup=pay_23)


@dp.callback_query(F.data == "random_23")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Bulochka narxi: 8 000")
    global balance
    balance = balance - 8000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Tort")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJT0klruHveaX5bFgsSLhLQZtCJnm2YygcTw&s",
        caption="\n \n Shirinlik Tort 24 000 so'm \n \n",
        reply_markup=pay_24)


@dp.callback_query(F.data == "random_24")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Tort narxi: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Muzqaymoq")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ6tuELckH3UvYliR7QvKkUML2vjdmrFHb5w&s",
                                    caption="\n \n Shirinlik Muzqaymoq 15 000 so'm \n \n",
                                    reply_markup=pay_25)


@dp.callback_query(F.data == "random_25")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Muzqaymoq narxi: 15 000")
    global balance
    balance = balance - 15000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Uzcard")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz to'lovni Uzcard kartasi orqali omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=mb_1)
    else:
        await message.answer("Boshidan urinib ko'ring !!!")
    await state.clear()


@dp.callback_query(F.data == "Humo")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number_2)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz Humo kartasi orqali to'lovni omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=mb_1)
    else:
        await message.answer("Boshidan urinib ko'ring !!!")
    await state.clear()


@dp.callback_query(F.data == "random")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !!!", reply_markup=mb)


@dp.callback_query(F.data == "random_uz")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text="\n \n Siz buyurtma qilmadingiz!", reply_markup=mb)


@dp.message(F.text == "Sotib olish")
async def savat_function(message: types.Message):
    await message.answer("To'lov turini tanlang Uzcard yoki Humo orqali to'lash", reply_markup=cart)


@dp.message(F.text == "🛒 Savat")
async def savat_function(message: types.Message):
    await message.answer("Siz savat bo'limini tanladingiz !", reply_markup=savat_button)


@dp.message(F.text == "🗑 Savatni ko'rish")
async def orders_function(message: types.Message):
    await message.answer(f"Sizda bor narsalar ro'yxati !!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=mb_1)


@dp.message(F.text == "🚮 Savatni tozalash")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Siz barcha mahsulotlarni o'chirib yubordingiz !!!", reply_markup=mb_1)


@dp.message(F.text == "Yordam")
async def balance_function(message: types.Message):
    await message.answer(
        f"Siz yordam bo'limini tanladingiz. 😊\nAgar sizda muammo bo'lsa, quyidagi raqamlarga murojaat qilishingiz mumkin: 📞\n\nTelefon raqam: +998 93 514-06-10"
,    reply_markup=mb_1)


@dp.message(F.text == "Ma'lumot")
async def balance_function(message: types.Message):
    await message.answer(
        f"{message.from_user.full_name}, siz ma'lumot bo'limini tanladingiz 😊\nBu bo'limda siz botimiz haqida batafsil ma'lumot olishingiz mumkin 📚\nBu bot orqali siz taomlar buyurtma qilishingiz mumkin 🍽️\nShuningdek, bu bot sizga o'zingiz haqingizda ma'lumot taqdim etadi 👤\nVa, eng muhimi, bu bot yordamida o'z telegram raqamingizni topishingiz mumkin 📱.",
    reply_markup=mb_1)


@dp.message(F.text == "Tilni o'zgartirish")
async def balance_function(message: types.Message):
    await message.answer(f"Siz tilni oʻzgartirishni tanladingiz \nTilni oʻzgartiring", reply_markup=til_1)


@dp.message(F.text == "O'zbek tili 🇺🇿")
async def balance_function(message: types.Message):
    await message.answer(f"Siz O'zbek tilga o'zgartirdingiz", reply_markup=mb_1)


class Registration_1(StatesGroup):
    first_name = State()
    last_name = State()
    number_one = State()
    cart_1_numb1er = State()


contact_button_1 = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт", request_contact=True)]
], resize_keyboard=True)

# til = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Uzb 🇺🇿")],
#     [KeyboardButton(text="Rus 🇷🇺")]
# ], resize_keyboard=True)

kb = [
    [KeyboardButton(text="🌭 Hotdog"), KeyboardButton(text="🌯 Lavash Меню")],
    [KeyboardButton(text="🍔 Burger Меню"), KeyboardButton(text="🍹 Напитоки")],
    [KeyboardButton(text="🍟 Дополнительный"), KeyboardButton(text="🎂 Сладость"), KeyboardButton(text="🔙 Назад")]
]
mb1 = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

kb1_1 = [
    [KeyboardButton(text="🔍 Меню"), KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="📲 Ваша информация"), KeyboardButton(text="Поддерживать"),
     KeyboardButton(text="Изменить язык")]
]
mb1_2 = ReplyKeyboardMarkup(keyboard=kb1_1, resize_keyboard=True)

savat_button_1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Покупка"), KeyboardButton(text="🚮 Очистить корзину")],
    [KeyboardButton(text="🗑 Посмотреть корзину"), KeyboardButton(text="🔙 Назад")]
], resize_keyboard=True)

mb1_hd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌭 Classic Hotdog", callback_data="Classic_Hot_dog_1"),
     InlineKeyboardButton(text="🌭 Comb1o Hotdog", callback_data="Comb1o_Hot_dog_1")],
    [InlineKeyboardButton(text="🌭 Sirli Hotdog", callback_data="Sirli_Hot_dog_1"),
     InlineKeyboardButton(text="🌭 Double Hotdog", callback_data="Double_Hot_dog_1")],
])

mb1_burger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍔Mini burger", callback_data="Mini_burger_1"),
     InlineKeyboardButton(text="🍔Gamburger", callback_data="Gamb1urger_1")],
    [InlineKeyboardButton(text="🍔Cheese burger", callback_data="Cheese_burger_1"),
     InlineKeyboardButton(text="🍔Chicken burger", callback_data="Chicken_burger_1")],
    [InlineKeyboardButton(text="🍔Combo burger", callback_data="Comb1o_burger_1")],
])

mb1_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌯Lavash", callback_data="Lavash_1"),
     InlineKeyboardButton(text="🌯Combo Tandir Lavash", callback_data="Comb1o_Tandir_Lavash_1")],
    [InlineKeyboardButton(text="🌯Tandir Lavash", callback_data="Tandir_Lavash_1"),
     InlineKeyboardButton(text="🌯Combo Lavash", callback_data="Comb1o_Lavash_1")],
])

mb1_i = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="☕ Capuccino", callback_data="Coffee_1"),
     InlineKeyboardButton(text="🍹 Tropic", callback_data="Tropic_1")],
    [InlineKeyboardButton(text="💧 Hydrolife", callback_data="Hydrolife_1"),
     InlineKeyboardButton(text="🍸 Moxito", callback_data="Moxito_1")]

])

mb1_q = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍟Free", callback_data="Free_1"),
     InlineKeyboardButton(text="🍖Smayliki", callback_data="Smayliki_1")],
    [InlineKeyboardButton(text="🥫Ketchup", callback_data="Ketchup_1"),
     InlineKeyboardButton(text="🥫Mayanez", callback_data="Mayanez_1")],
])

mb1_sh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍹Kokteyl", callback_data="Kokteyl_1"),
     InlineKeyboardButton(text="🍰Tort", callback_data="Tort_1")],
    [InlineKeyboardButton(text="🍩Bulochka", callback_data="Bulochka_1"),
     InlineKeyboardButton(text="🍦 Мороженое", callback_data="Мороженое_1")],
])

pay1_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_2")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_3")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_4")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_5")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_6")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_7")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_8")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_9")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_10")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_11")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_12")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_13")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_14")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_15")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_16 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_16")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_17 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_17")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_18 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_18")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_19 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_19")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_20 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_20")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_21 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_21")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_22 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_22")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_23 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_23")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_24 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_24")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_25 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_25")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

cart_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳Uzcard", callback_data="Uzcard_1")],
    [InlineKeyboardButton(text="💳Humo", callback_data="Humo_1")],
])


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(
        f"\n \n Salom {message.from_user.full_name}, botga xush kelibsiz !!! \n \n Здравствуйте, {message.from_user.full_name}, добро пожаловать в бот !!!",
        reply_markup=til)


@dp.callback_query(F.data == "Меню")
async def start_function(call: types.CallbackQuery):
    await call.answer_photo(
        photo="https://avatars.mds.yandex.net/get-altay/9728306/2a0000018a6fc3054db52240e707fb55e28f/L_height",
        caption="\n \n Привет, feed up. Познакомься с меню. \n 1 Hot_dog \n 2 Gamb1urger \n 3 Lavash_Меню \n 4 Напитокиlar \n 5 Дополнительный \n 6 Сладостьlar \n \n \n",
        reply_markup=mb1)


@dp.message(F.text == "🔍 Меню")
async def start_function(message: types.Message):
    await message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-altay/9728306/2a0000018a6fc3054db52240e707fb55e28f/L_height",
        caption="\n \n Привет, feed up. Познакомься с меню. \n 1 Hot_dog \n 2 Gamb1urger \n 3 Lavash_Меню \n 4 Напитокиlar \n 5 Дополнительный \n 6 Сладостьlar \n \n \n",
        reply_markup=mb1)


@dp.message(F.text == "🔙 Назад")
async def ortga_function(message: types.Message):
    await message.answer("Вы вернулись", reply_markup=mb1_2)


@dp.message(F.text == "📲 Ваша информация")
async def info_function(message: types.Message):
    await message.answer(
        f"\n \n Ваше имя {message.from_user.full_name} \nВаше user name {message.from_user.username} \nВаше id {message.from_user.id} \n \n",
        reply_markup=mb1_2)


@dp.message(F.text == "Rus 🇷🇺")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration_1.first_name)
    await message.answer("Добро пожаловать\nВведите свое имя: ")


@dp.message(Registration_1.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration_1.last_name)
    await message.answer("Хорошо, теперь введите фамилия: ")


@dp.message(Registration_1.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration_1.number_one)
    await message.answer("Хорошо, теперь введите номер: ", reply_markup=contact_button_1)


@dp.message(Registration_1.number_one)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(numb1er=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Нет проблем!\nВаше имя: {data['first_name']}\nВаша фамилия: {data['last_name']}\nВаш номер: {data['number']}",
        reply_markup=mb1_2)
    await state.clear()


@dp.message(F.text == "🌭 Hotdog")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://sun9-16.userapi.com/impf/c852024/v852024787/1b00ec/nh17wVjmwIw.jpg?size=640x333&quality=96&sign=ac5dcb5df8feb82b1ccbf2f81e56adec&c_uniq_tag=AoaV9UZx--Xsue7NGHnjIh8QJc7P0U9saxrGdxWqU5A&type=album",
        caption=f"\n \n Здравствуйте, {message.from_user.full_name}! Вы выбрали раздел «Хот-доги».",
        reply_markup=mb1_hd)


@dp.callback_query(F.data == "Classic_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3490335/46368596e993177dbd46616cefc0f3d1/M_height",
        caption="\n \n Classic Hot dog 14 000 so'm", reply_markup=pay1_1)


@dp.callback_query(F.data == "1_random")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Classic_Hot_dog расходы: 14000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Sirli_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3506707/10f01c187799f1ea0345822dbe475f59/M_height",
        caption="\n \n Sirli Hot dog 16 000 so'm", reply_markup=pay1_2)


@dp.callback_query(F.data == "1_random_2")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Sirli_Hot_dog расходы: 16000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Double_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://img.iamcook.ru/2022/upl/recipes/byusers/misc/9661/mobile/48e7636ccc941eb606c5b0b3bf824cb8-2022.jpg",
        caption="\n \n Double Hot dog 22 000 so'm", reply_markup=pay1_3)


@dp.callback_query(F.data == "1_random_3")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Double_Hot_dog расходы: 22000")
    global balance
    balance = balance - 22000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3793239/39f9a17282975e92a218e17cc006980c/M_height",
        caption="\n \n Comb1o Hot dog 26 000 so'm", reply_markup=pay1_4)


@dp.callback_query(F.data == "1_random_4")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Comb1o_Hot_dog расходы: 26000")
    global balance
    balance = balance - 26000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🍔 Burger Меню")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://img.freepik.com/premium-vector/vector-burger-media-social-feed-design-template_844390-50.jpg",
        caption=f"Здравствуйте, {message.from_user.full_name}, вы выбрали Бургеры.", reply_markup=mb1_burger)


@dp.callback_query(F.data == "Mini_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://img.delo-vcusa.ru/2015/07/86.jpg",
                                    caption="\n \n Mini_burger 16 000 so'm", reply_markup=pay1_5)


@dp.callback_query(F.data == "1_random_5")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Mini_burger расходы: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Gamb1urger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_46.png&w=640&q=75",
        caption="\n \n Gamb1urger 20 000 so'm", reply_markup=pay1_6)


@dp.callback_query(F.data == "1_random_6")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Gamb1urger расходы: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Cheese_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://recipes.av.ru//media/recipes/100608_picture_XNlaEKL.jpg",
                                    caption="\n \n Cheese_burger 24 000 so'm", reply_markup=pay1_7)


@dp.callback_query(F.data == "1_random_7")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Cheese_burger расходы: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Chicken_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_11.png&w=640&q=75",
        caption="\n \n Chicken_burger 28 000 so'm", reply_markup=pay1_8)


@dp.callback_query(F.data == "1_random_8")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Chicken_burger расходы: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_4.png&w=640&q=75",
        caption="\n \n Comb1o_burger 32 000 so'm", reply_markup=pay1_9)


@dp.callback_query(F.data == "1_random_9")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Comb1o_burger расходы: 32 000")
    global balance
    balance = balance - 32000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🌯 Lavash Меню")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://s.yimg.com/ny/api/res/1.2/2vDhmS8Igz2.CsalAiOsSg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://media.zenfs.com/en/food_wine_804/7452b51d817330b4071c7aff64de72f4",
        caption=f"Здравствуйте, {message.from_user.full_name}, вы выбрали раздел Лаваш..", reply_markup=mb1_lavash)


@dp.callback_query(F.data == "Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fbbq1.png&w=640&q=75",
        caption="\n \n Lavash 20 000 so'm", reply_markup=pay1_10)


@dp.callback_query(F.data == "1_random_10")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Lavash расходы: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Tandir_Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Flavash_gavyadina_sir.png&w=640&q=75",
        caption="\n \n Tandir Lavash 24 000 so'm", reply_markup=pay1_11)


@dp.callback_query(F.data == "1_random_11")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Tandir_Lavash расходы: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fbbq_komb1o.png&w=640&q=75",
        caption="\n \n Comb1o Lavash 28 000 so'm", reply_markup=pay1_12)


@dp.callback_query(F.data == "1_random_12")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Lavash расходы: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_Tandir_Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_31.png&w=640&q=75",
        caption="\n \n Comb1o Tandir Lavash 30 000 so'm", reply_markup=pay1_13)


@dp.callback_query(F.data == "1_random_13")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Comb1o_Tandir_Lavash расходы: 30 000")
    global balance
    balance = balance - 30000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🍹 Напитоки")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://storage.kun.uz/source/4/Pgv76ozIYAq6G2_Q1MWhy8Fw0-HOeiuZ.jpg",
                               caption=f"Здравствуйте, {message.from_user.full_name}! Вы выбрали «Напитки».",
                               reply_markup=mb1_i)


@dp.callback_query(F.data == "Coffee_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://exportal.io/files/images/items/0/393vf513f2da.jpg",
                                    caption="\n \n Напитоки Capucino 18 000 so'm", reply_markup=pay1_14)


@dp.callback_query(F.data == "1_random_14")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Capucino расходы: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Hydrolife_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK3368/3368-600x600.jpg",
                                    caption="\n \n Напитоки Hydrolife 12 000 so'm", reply_markup=pay1_15)


@dp.callback_query(F.data == "1_random_15")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Hydrolife расходы: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Tropic_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK0182/YK0182_1-600x600.jpg",
                                    caption="\n \n Напитоки Ice tea 6 000 so'm", reply_markup=pay1_16)


@dp.callback_query(F.data == "1_random_16")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Ice tea расходы: 6 000")
    global balance
    balance = balance - 6000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Moxito_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.gazeta.uz/media/img/2021/05/hxSClG16221972734019_l.jpg",
                                    caption="\n \n Напитоки Moxito 16 000 so'm", reply_markup=pay1_17)


@dp.callback_query(F.data == "1_random_17")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Moxito расходы: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🍟 Дополнительный")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://img.freepik.com/free-vector/fast-food-icon-set_1284-4716.jpg",
                               caption=f"Здравствуйте, {message.from_user.full_name}! Вы выбрали дополнения..",
                               reply_markup=mb1_q)


@dp.callback_query(F.data == "Free_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://media-cdn.tripadvisor.com/media/photo-p/13/f2/7b/59/photo0jpg.jpg",
                                    caption="\n \n Дополнительный из отдела Free 12 000 so'm", reply_markup=pay1_18)


@dp.callback_query(F.data == "1_random_18")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Free расходы: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Smayliki_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3qQkPXKGIYuWazr3FWgj-WXhdVODC74UGMQ&s",
        caption="\n \n Дополнительный из отдела Smayliki 14 000 so'm", reply_markup=pay1_19)


@dp.callback_query(F.data == "1_random_19")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Smayliki расходы: 14 000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Ketchup_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://images.prom.ua/2127414866_w400_h400_krahmal-dlya-sousov.jpg",
                                    caption="\n \n Дополнительный из отдела Ketchup 2 000 so'm", reply_markup=pay1_20)


@dp.callback_query(F.data == "1_random_20")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Ketchup расходы: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Mayanez_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://images.prom.ua/4235079938_w640_h640_chasnikovij-sous-dlya.jpg",
                                    caption="\n \n Дополнительный из отдела Mayanez 2 000 so'm", reply_markup=pay1_21)


@dp.callback_query(F.data == "1_random_21")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Mayanez расходы: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🎂 Сладость")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.tastingtable.com/img/gallery/ranking-fast-food-desserts-from-worst-to-best/l-intro-1682970849.jpg",
        caption=f"Здравствуйте, {message.from_user.full_name}! Вы выбрали Сладости.", reply_markup=mb1_sh)


@dp.callback_query(F.data == "Kokteyl_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.projuice.co.uk/app/uploads/2023/02/strawberry.jpg",
                                    caption="\n \n Сладость Kokteyl 18 000 so'm", reply_markup=pay1_22)


@dp.callback_query(F.data == "1_random_22")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Kokteyl расходы: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Bulochka_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL3BsYXlcLzUzZTdmMTQ0LTZkNDItNGQzZi04ZjA1LTBlOWMzMWFmODg2ZS0xMjEwLTY4MC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjgyOH19fQ==",
        caption="\n \n Сладость Bulochka 8 000 so'm", reply_markup=pay1_23)


@dp.callback_query(F.data == "1_random_23")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Bulochka расходы: 8 000")
    global balance
    balance = balance - 8000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Tort_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJT0klruHveaX5bFgsSLhLQZtCJnm2YygcTw&s",
        caption="\n \n Сладость Tort 24 000 so'm", reply_markup=pay1_24)


@dp.callback_query(F.data == "1_random_24")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Tort расходы: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Мороженое_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://i.pinimg.com/736x/6d/f2/7b/6df27b2153f813f033d124c0bb30a86f.jpg",
                                    caption="\n \n Сладость Мороженое 15 000 so'm", reply_markup=pay1_25)


@dp.callback_query(F.data == "1_random_25")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Мороженое расходы: 15 000")
    global balance
    balance = balance - 15000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Uzcard_1")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card_1.card_number)
    await call.message.answer("Введите номер карты: ")


@dp.message(Card_1.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"Спасибо {message.from_user.full_name}, вы произвели оплату картой Uzcard. \nСпасибо, что делаете покупки у нас!!! \nЕсли вы хотите купить еще раз, перейдите в раздел «Меню».",
            reply_markup=mb1_2)
    else:
        await message.answer("Попробуйте с начала!!!")
    await state.clear()


@dp.callback_query(F.data == "Humo_1")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card_1.card_number_2)
    await call.message.answer("Введите номер карты: ")


@dp.message(Card_1.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"Спасибо {message.from_user.full_name}, вы произвели оплату картой Humo. \nСпасибо, что делаете покупки у нас!!! \nЕсли вы хотите купить еще раз, перейдите в раздел «Меню».",
            reply_markup=mb1_2)
    else:
        await message.answer("Попробуйте с начала!!!")
    await state.clear()


@dp.callback_query(F.data == "1_random")
async def send_1_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Спасибо за заказ!!!", reply_markup=mb1)


@dp.callback_query(F.data == "1_random_uz")
async def send_1_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text="Вы не заказывали!", reply_markup=mb1)


@dp.message(F.text == "Покупка")
async def savat_function(message: types.Message):
    await message.answer("Вы приобрели товар \nСпасибо за покупку", reply_markup=cart_1)


@dp.message(F.text == "🛒 Корзина")
async def savat_function(message: types.Message):
    await message.answer("Вы выбрали раздел «Корзина»!", reply_markup=savat_button_1)


@dp.message(F.text == "🗑 Посмотреть корзину")
async def orders_function(message: types.Message):
    await message.answer(f"Список того, что у вас есть!!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=mb1_2)


@dp.message(F.text == "🚮 Очистить корзину")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Вы удалили все товары!!!", reply_markup=mb1_2)


@dp.message(F.text == "Поддерживать")
async def balance_function(message: types.Message):
    await message.answer(
        f"Здравствуйте, вы выбрали раздел помощи \nЕсли у вас возникли проблемы, вы можете позвонить по номерам ниже \n \n Телефон: +998 93 514-06-10",
        reply_markup=mb1_2)


@dp.message(F.text == "О нас")
async def balance_function(message: types.Message):
    await message.answer(
        f"Здравствуйте, вы выбрали информационный раздел\nВ этом разделе вы можете получить информацию об этом боте \n Через этого бота вы можете заказать еду \n Этот бот может предоставить информацию о себе. \n Через этого бота вы можете узнать свой номер телеграма.",
        reply_markup=mb1_2)


@dp.message(F.text == "Изменить язык")
async def balance_function(message: types.Message):
    await message.answer(f"Вы выбрали смену языка\nИзменить язык", reply_markup=til_1)


@dp.message(F.text == "Русский язык 🇷🇺")
async def balance_function(message: types.Message):
    await message.answer(f"Вы пер ешли на русский", reply_markup=mb1_2)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())