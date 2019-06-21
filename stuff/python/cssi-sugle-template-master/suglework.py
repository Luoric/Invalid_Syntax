class SugleAccount(object):

    def __init__(self, username, name):
        self.username = username
        self.personal_info = {'name': name, 'email': '', 'favourite_food': ''}
        self.friends = {}
        self.news_list = []
        self.messages = []

    def add_friend(self, friend_account):
        self.friends[friend_account.username] = friend_account

    def remove_friend(self, friend_username):
        if friend_username in self.friends:
            del self.friends[friend_username]
            return True
        else:
            return False

    def add_news(self, new_news):
        self.news_list.append(new_news)

    def get_latest_news(self):
        latestNews = self.news_list[-1]
        return latestNews

    def get_all_news(self):
        return self.news_list

    def add_to_inbox(self,from_user, message):
        thing = from_user, message
        self.messages.append(thing)

    def read_inbox(self):
        return self.messages

if __name__ == "__main__":
    luoric = SugleAccount('luoric', 'Ruicheng Luo')
    donald = SugleAccount('donald', 'Donald Duck')
    oka = SugleAccount('oka', 'oka K')
    print(luoric.personal_info)
    luoric.add_friend(donald)
    luoric.add_friend(oka)
    luoric.add_news("I love mondays")
    luoric.add_news("I love tuesdays")
    print(luoric.get_all_news())
    luoric.add_to_inbox("donald", "self my friend!")
    luoric.add_to_inbox("luoric", "self my friend!")
    print(luoric.read_inbox())
