
from datetime import datetime

import requests


class Website:
    """
    Main one, represents core web site.
    """

    counter = 0

    def __init__(self, shortdomain: str, path=None):
        self.port = "80"
        self.protocol = "https"
        self.domain = f"www.{shortdomain}.com"
        self.script_lang = "php"
        self.layout_lang = "html"
        self.path = path
        Website.counter += 1


    def create_url(self):
        return r"%s://%s/%s/%s" % (self.protocol, self.domain,
                                   self.port, self.path)

    # def __new__(cls, *args, **kwargs):
    #     res = super(Website, cls).__new__(cls)
    #     cls.counter +=1
    #     return res


    @staticmethod
    def static():
        print("Class exists")

    @classmethod
    def show_amount_sites(cls):
        print(cls.counter)


class HomePage(Website):

    def __init__(self, shortdomain):
        super(HomePage, self).__init__(shortdomain, path="Random_page")
        self.date = datetime.now().strftime("%Y-%m-%d")

    def show_date(self):
        print(self.date)


class ContactPage(Website):

    def __init__(self, shortdomain, **contacts):
        super(ContactPage, self).__init__(shortdomain, path="Contact_page")
        self.contacts = contacts


    def names_n_numbers(self):
        self.names = [name for name in self.contacts.values()]
        self.numbers = [number for number in self.contacts.keys()]


class NewsPage(Website):
    import requests

    def __init__(self, shortdomain, url):
        super(NewsPage, self).__init__(shortdomain, path="News_page")
        self.title = requests.request("GET", url).content[2461:2519]

    def show_title(self):
        print(self.title)


home_page = HomePage("Home")
print(home_page.create_url())

dct = {
    "Swaroop": "+34523566756",
    "Ge": "+98765789087",
    "Man": "+876546789",
    "HamApp": "8765456789"
}

contact_page = ContactPage("contacts", **dct)
news_page = NewsPage("news", "https://www.bbc.com/news/uk-61052643")
# Website("asdf")
Website.show_amount_sites()
