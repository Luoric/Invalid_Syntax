#class definition
class SugleAccount(object):
    def __init__(self, username, full_name):
        self.username = username
        self.personal_info = {'name': full_name, 'email': '', 'favourite_food': ''}
        self.news = []

    def add_news(self, news_update):
        self.news.append(news_update)
    def print_news(self):
        print(self.username + "'s update")
        for item in self.news:
            print(item)

#object instantiation
my_account = SugleAccount('Luoric', 'Ruicheng Luo')
friend_account = SugleAccount("xxXproXxx", "Thomas Jefferson")
my_account.add_news('I LOVE MONDAY')
my_account.add_news('I LOVE tuesday')
my_account.add_news('I LOVE everyday')
my_account.print_news()
