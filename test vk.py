from spotipy.oauth2 import SpotifyOAuth
from colorama import Fore
import spotipy
import typing
import vk_api
import time

quote = ['Я не волшебник, я всего лишь учусь','Это не баг — это незадокументированная фича.','Удаленный код — отлаженный код.','Чтобы понять рекурсию, нужно сперва понять рекурсию.', 'Самая сложная часть в дизайне… держаться подальше от фич.', 'Если сразу не получилось хорошо, назовите это версией 1.0.', 'format c: - лучший антивирус', 'Куплюклавиатурусработающимпробелом', 'Чудеса случаются.', 'Предположим, что у тебя есть 1000 рублей... Ну, для круглого счета возьмем 1024...', '99% ошибок компьютера сидит в полуметре от монитора.', 'Невозможно победить того, кто не сдается', 'Моё "люблю" очень дорогого стоит. Говорю это редко и мало кому.', 'Миллионы людей не заменят тебя. Никогда.', 'Ничего в этой жизни не дается легко', 'Безумец всегда говорит и поступает так, как будто он прав.', 'Я не ухожу, просто иногда меня нет', 'Самостоятельность не означает одиночество', 'Не ждите, пока кто-то другой сделает первый шаг. Что вы можете потерять, кроме своего одиночества?', 'Я — человек, для которого уединение жизнено необходимо', 'Я не боюсь одиночества. Я уже в нем…', 'То, во что ты веришь, становится твоим миром', 'Факт о человеческой лени №212682340236: Вы слишком ленивы, чтобы прочитать это число', 'Простить — да. Забыть — никогда.', 'Бывают минуты, за которые можно отдать месяцы и годы.', 'Влюбиться не значит любить. Влюбиться можно и ненавидя', 'Скучать по кому-то — самое прекрасное из всех грустных чувств']


class Config:
    MAIN_STATUS = "♡ 02.05.2k21 - 19:18:36 ♡  \n \n Sadddd ×︵♡ \n \n [RSq] Taë <З "
    STATUS = "Sp♡tify:  ♫ {track} -by- {artist} ♪ \n\n ♡ 02.05.2k21 - 19:18:36 ♡ \n \n ×︵♡ \n \n  [RSq] Taë <З"
    CLIENT_ID = "e0475cf903d44052a9be5af15067eaf1"
    CLIENT_SECRET = "e71f8c5c779b47f9aa3b84281f6293a4"
    REDIRECT_URI = "http://localhost:8888/callback"
    USERNAME = "Funtazygg"
    SCOPE = "user-read-playback-state user-library-read"
    VK_TOKEN='e2fd679aa7fe68c73e4e5347b4a2627466daaa9e4883d5a8d8e19775055071e614d7d85af1f4ff1b9678f'
vk = vk_api.VkApi(token=Config.VK_TOKEN).get_api()

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=Config.SCOPE,
        client_id=Config.CLIENT_ID,
        client_secret=Config.CLIENT_SECRET,
        redirect_uri=Config.REDIRECT_URI,
        username=Config.USERNAME,
    )
)

current_playing = typing.List[typing.Union[str, str, str]]

def update_status_to_standard():

    if vk.users.get(fields="status")[0]["status"] != Config.MAIN_STATUS:
        vk.status.set(text=Config.MAIN_STATUS)
    print(Fore.RED + f"Sad not one song is not playing'")



def update_status(_current_playing: typing.List[typing.Union[str, str, str]]) -> typing.List[typing.Union[str, str, str]]:
    current = spotify.current_user_playing_track()
    track, album, artist = current["item"]["name"], \
                           current["item"]["album"]["name"], \
                           current["item"]["artists"][0]["name"]
    if _current_playing != [track, album, artist]:
        vk.status.set(text=Config.STATUS.format(track=track, album=album, artist=artist))
        print(Fore.GREEN + f"WoW song played now: * {track} -by-  {artist}")
    if _current_playing is None:
        raise
    return [track, album, artist]



while True:
    try:
        current_playing = update_status(current_playing)
    except (KeyboardInterrupt, SystemExit, Exception):
        update_status_to_standard()
        time.sleep(45)
        pass