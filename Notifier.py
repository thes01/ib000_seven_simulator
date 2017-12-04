class Notifier:
    notify_level = 1

    def notify(self, text: str, level=1):
        if self.notify_level < level:
            return

        print(text)

    def notifyCards(self, cards, message="Cards: ", level=1):
        if self.notify_level < level:
            return

        translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]

        for card_code in cards:
            message += translate_table[card_code] + ", "

        print(message[:-2])  # cut the ending comma and space
