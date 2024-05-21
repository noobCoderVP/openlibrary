from . import db

class Battles:
    TABLENAME = "battles"
    PRIMARY_KEY = ["id"]

    @classmethod
    def add(cls, submitted_by, book1, book2, comment, winner):
        """Add the battle details into the database

        Args:
            submitted_by (text): username
            book1 (text): book1 id (ex: OL37079411M)
            book2 (text): book2 id (ex: OL32377611M)
            comment (text): comment about the battle
            winner (text): winner of the battle (OL37079411M or OL32377611M)
        """
        oldb = db.get_db()

        return oldb.insert(
            'battles',
            submitted_by=submitted_by,
            book1=book1,
            book2=book2,
            comment=comment,
            winner=winner
        )

    @classmethod
    def get_patron_battles(cls, username, book1 = None, book2 = None):
        pass

    @classmethod
    def get_patron_battle_count(cls, username, book = None):
        pass

    @classmethod
    def get_battle_comparison(cls, book1, book2):
        pass

    @classmethod
    def get_battle_history_for_book(cls, book):
        pass