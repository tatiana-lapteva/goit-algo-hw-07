"""
Завдання 4
Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, 
які, в свою чергу, також могли мати відповіді, формуючи таким чином ієрархічну структуру.

Реалізуйте клас Comment, що представляє собою окремий коментар. Він має зберігати текст коментаря, автора та список відповідей.
Метод класу add_reply має додавати нову відповідь до коментаря.
Метод класу remove_reply має видаляти відповідь із коментаря. Це має змінювати текст коментаря на стандартне повідомлення 
(наприклад, "Цей коментар було видалено.") і встановлювати прапорець is_deleted в True.
Метод display має рекурсивно виводити коментар та всі його відповіді, використовуючи відступи для відображення ієрархічної структури.
"""

class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.reply = reply
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.author = ""
        self.is_deleted = True

    def display(self, level=0):
        indent = " " * (level * 4)
        if self.author:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}{self.text}")
        for reply in self.replies:
            reply.display(level + 1)



if __name__ == "__main__":

    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
