import types

from aiogram import F

from bot import dp
from keyboards import product_button


@dp.callback_query(F.data == "Cheese_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://recipes.av.ru//media/recipes/100608_picture_XNlaEKL.jpg",
                                    caption="\n \n Mahsulotlardan birini tanlang", reply_markup=product_button)

