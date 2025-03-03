import telebot
import os
import random
import requests
from telebot import types 
from bot_logic import gen_pass, gen_emodji, get_duck_image_url, timers, flip_coin, jokes, get_dog_image_url # Импортируем функции из bot_logic
# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("no")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Какую команду вы выберете? /hello, /bye, /pass, /emodji, /jokes, /coin, /timers, /heh, /dog, /ping, /poll, /mem, /animals")
    bot.reply_to(message, "Команды по экологии: /find-узнать куда девать сортированный мусор, /what-узнать сколько разлагаются отходы, /ecomems-отдохнуть от душных тем и посмотреть мемы про экологию")
    bot.reply_to(message, "/ecopoll,/ecopoll2,/ecopoll3,/ecopoll4,/ecopoll5,/ecopoll6,/ecopoll7-мини опрос про экологию")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['jokes'])
def send_jokes(message):
    joke = jokes()
    bot.reply_to(message, f"Шутка: {joke}")   

@bot.message_handler(commands=['timers'])
def send_timers(message):
    timer = timers()
    bot.reply_to(message, f"Время: {timer}")  

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Понг!")

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "Мнение")
    answer_options = ["да", "нет", "ДА", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Вам нравится кодланд?",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass

# Обработчик команды /picture
@bot.message_handler(commands=['dog'])
def send_dog(message):
    with open('lavar/lava.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 


@bot.message_handler(commands=['mem'])
def send_mem(message):
    file_list = os.listdir("images")
    img_name = random.choice(file_list)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['dogs'])
def dogs(message):
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)
 
@bot.message_handler(commands=['animals'])
def animals(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("уткены")
    btn2 = types.KeyboardButton("собакены")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери категорию".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['find'])
def find(message):
    bot.reply_to(message, "Вы тоже не понимаете куда девать сортированный мусор?")
    with open('images/meme.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
    bot.reply_to(message, "Сегодня я об этом расскажу.Ищите сайты которые расскажут о местах перерабатывания мусора.Ресурсы для поиска информации о переработчиках: •  Recyclemap.ru: Один из самых известных проектов в России. Пользователи могут добавлять на карту точки приема вторсырья.Greenpeace Map: Карта Greenpeace, на которой отмечены пункты приема вторсырья, экоцентры и другие полезные места для экологичной жизни.ЭкоВики: Сообщество ЭкоВики ведет базу данных пунктов приема вторсырья, которую можно найти на их сайте.2Гис (онлайн-карта): Если ввести запрос прием вторсырья  или  переработка отходов в вашем городе, можно найти компании, занимающиеся переработкой.")

@bot.message_handler(commands=['what'])
def find(message):
    bot.reply_to(message, "Мистер пес вам расскажет как разлагается мусор")
    with open('lavar/lava.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
    bot.reply_to(message, "Остатки пищевых продуктов перегнивают под воздействием микроорганизмов в течение 1 месяца. Исключением является апельсиновая кожура: на её переработку окружающей среде требуется от 4 до 6 месяцев. Обычная бумага и картон разлагаются за 1-2 месяца, а вот книгам или печатной продукции может потребоваться до двух лет. Дольше всего длится процесс переработки глянцевых журналов: на их уничтожение природа затратит около 5 лет. Остатки одежды из хлопка, льна, бамбукового волокна или вискозы полностью переработаются под воздействием влаги и микроорганизмов за 3 года. При этом шерстяные изделия менее устойчивы, и для их разложения понадобится не более 1 года. А вот для того, чтобы переработать одежду из синтетических материалов и старую обувь, нужно около 50 лет. Выброшенная на свалку древесина разлагается около 3-10 лет, а вот покрытые лакокрасочными материалами деревянные изделия могут гнить до 13 лет.Брошенная на землю жевательная резинка исчезнет только через 30 лет. Батарейки и аккумуляторы для бытовых приборов разлагаются в природе около 100 лет. На разложение полиэтиленового пакета потребуется от 30 до 200 лет. Пл. бутылки Разлагаются от 450 до 1000 лет, в зависимости от климата и состава пластика. На их исчезновение понадобится от 80 до 500 лет. На то, чтобы переработать этот вид отходов, у природы уходит до 100 лет. Срок разложения стекла в природе может превышать 1000 лет. ")

@bot.message_handler(commands=['ecomems'])
def send_ecomems(message):
    file_list = os.listdir("meme")
    img_name = random.choice(file_list)
    with open(f'meme/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=["ecopoll"])
def create_poll(message):
    bot.send_message(message.chat.id, "Экотест")
    answer_options = ["да", "нет", "ДА", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Нужно ли сортировать мусор?",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass      

@bot.message_handler(commands=["ecopoll2"])
def create_poll2(message):
    answer_options = ["пластик", "бумага", "стекло", "алюминиевая банка"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Какой мусор разлагается дольше всего?",
        options=answer_options,
        type="quiz",
        correct_option_id=0,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass     

@bot.message_handler(commands=["ecopoll3"])
def create_poll3(message):
    answer_options = ["Нет", "Да,есть сайты,которые помогут их найти", "Что", "Да, но нет средств, которые помогут их найти"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="В России есть места для переработки мусора?",
        options=answer_options,
        type="quiz",
        correct_option_id=1,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass    

@bot.message_handler(commands=["ecopoll4"])
def create_poll4(message):
    answer_options = ["биосфера", "литосфера", "гидросфера", "атмосфера"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Как называется активная оболочка Земли, которая населена живыми организмами?",
        options=answer_options,
        type="quiz",
        correct_option_id=0,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass    

@bot.message_handler(commands=["ecopoll5"])
def create_poll5(message):
    answer_options = ["книги", "газеты", "бумажные полотенца"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Какая бумага не подлежит переработке?",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass    

@bot.message_handler(commands=["ecopoll6"])
def create_poll6(message):
    answer_options = ["водоросли", "мхи", "горы и ледники"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Что выделяет больше кислорода?",
        options=answer_options,
        type="quiz",
        correct_option_id=0,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass   

@bot.message_handler(commands=["ecopoll7"])
def create_poll7(message):
    answer_options = ["выкинуть в мусорный бак", "сдать в специальный пункт приёма", "закопать в землю"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Что следует сделать со старыми батарейками?",
        options=answer_options,
        type="quiz",
        correct_option_id=1,
        is_anonymous=False,
    )

@bot.poll_answer_handler()
def handle_poll(poll):
    pass   

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "уткены"):
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)
    elif(message.text == "собакены"):
        image_url = get_dog_image_url()
        bot.reply_to(message, image_url)  

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Запускаем бота
bot.polling()