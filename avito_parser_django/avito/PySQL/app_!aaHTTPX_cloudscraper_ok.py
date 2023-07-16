import cloudscraper
import httpx


#
#

def cloudget():
    s = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0'})
    url = 'https://www.avito.ru/web/1/main/items'
    params = {
        'forceLocation': False,
        'locationId': 653040,
        'lastStamp': 1683748131,
        'limit': 30,
        'offset': 89,
        'categoryId': 4
    }
    r = s.get(url, params=params)
    print(r.url, '\n', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    print(r.text)


def cloudcoocie():
    #url = "https://example.com"
    url = "https://www.avito.ru/web/1/main/items"
    postData = "postData"
    second_postData = "second_postData"

    # Отправка первого POST-запроса
    response = httpx.post(url, data=postData, headers={"Content-Type": "text/xml"})
    responseData = response.text
    print(responseData)

    # Отправка второго POST-запроса
    response = httpx.post(url, data=second_postData, headers={"Content-Type": "text/xml"})
    responseData = response.text
    print(responseData)

def cloudhttpx():

    url = 'https://www.avito.ru/web/1/main/items'
    params = {
        'forceLocation': False,
        'locationId': 653040,
        'lastStamp': 1683748131,
        'limit': 30,
        'offset': 89,
        'categoryId': 4
    }
    # Создание экземпляра cloudscraper для сохранения cookie в контейнере
    scraper = cloudscraper.create_scraper()

    # Получение cookie из cloudscraper
    cookies = scraper.cookies

    # Создание экземпляра httpx.Client с использованием cookie из контейнера
    session = httpx.Client(cookies=cookies)

    # URL для GET-запроса
    url = "https://www.example.com"

    # Выполнение GET-запроса с использованием httpx и cookie из контейнера
    response = session.get(url)
    print(response.text)

    # Закрытие сессии
    session.close()


class ScraperClient:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.session = httpx.Client(cookies=self.scraper.cookies)

    def get(self, url, params):
        response = self.session.get(url, params=params)  # Исправленное использование параметров
        return response.text

    def close(self):
        self.scraper.close()
        self.session.close()


# Использование класса ScraperClient
if __name__ == '__main__':  # Исправленное условие
    #cloudcoocie()
    cloudget()
    #cloudhttpx()
    print('############################################')

    client = ScraperClient()
    url = 'https://www.avito.ru/web/1/main/items'
    params = {
        'forceLocation': False,
        'locationId': 653040,
        'lastStamp': 1683748131,
        'limit': 30,
        'offset': 89,
        'categoryId': 4
    }
    #response = client.get(url, params)
    #print(response)
    client.close()

# cloudget()


#########################
#
'''
создать одну сессию и использовать ее для отправки запросов через cloudscraper или httpx

import cloudscraper
import httpx

scraper = cloudscraper.create_scraper()
session = httpx.Client()

url = "https://www.example.com"

# Использование cloudscraper для получения контента страницы
response_cloudscraper = scraper.get(url)
print(response_cloudscraper.text)

# Использование httpx для отправки запроса
response_httpx = session.get(url)
print(response_httpx.text)

# Закрытие сессий
scraper.close()
session.close()
'''

'''
Есть задача обратиться к серверу, получить ответ, затем в той же сессии 
ещё раз обратиться к серверу. 
Это необходимо, так как таким образом выполняется авторизация. 
Мой код выдаёт ошибку на втором GetRequestStream о том, 
что поток недоступен для записи. Что нужно сделать, чтобы сессия 
сохранялась и я мог отправить второй запрос в рамках этой сессии? 
Первый ответ сервера корректный, говорящий о том, что я успешно авторизовался.

    public ActionResult Regs()
    {
        string url = "url";
        string postData = "postData";
        HttpWebRequest webRequest = (HttpWebRequest)WebRequest.Create(url);
        webRequest.Method = "POST";
        webRequest.ContentType = "text/xml";
        using (StreamWriter requestWriter2 = new StreamWriter(webRequest.GetRequestStream()))
        {
            requestWriter2.Write(postData);
        }
        HttpWebResponse resp = (HttpWebResponse)webRequest.GetResponse();

        string responseData = string.Empty;

        using (StreamReader responseReader = new StreamReader(webRequest.GetResponse().GetResponseStream()))
        {
            responseData = responseReader.ReadToEnd();
        }
        postData = "second_postData";
        using (StreamWriter requestWriter2 = new StreamWriter(webRequest.GetRequestStream()))
        {
            requestWriter2.Write(postData);
        }
        resp = (HttpWebResponse)webRequest.GetResponse();

        using (StreamReader responseReader = new StreamReader(webRequest.GetResponse().GetResponseStream()))
        {
            responseData = responseReader.ReadToEnd();
        }
        ViewBag.RD = responseData;
        return PartialView();
    }

    asp.nethttppostс ессияrequest

Поделиться
Улучшить вопрос
Отслеживать
задан 1 ноя 2018 в 9:19
Дмитрий Лосинец's user avatar
Дмитрий Лосинец
4155 бронзовых знаков
Добавить комментарий
1 ответ
Сортировка:
0

Оказалось, проблема решается просто. Делаю куки контейнер:

CookieContainer cookieContainer = new CookieContainer();

Привязываю его к первому запросу:

webRequest.CookieContainer = cookieContainer;

Затем после получения ответа создаю второй запрос и привязываю тот же контейнер к нему:

HttpWebRequest webRequest1 = (HttpWebRequest)WebRequest.Create(url);
webRequest1.CookieContainer = cookieContainer;

Всё отрабатывает штатно, ответы корректные.

'''
