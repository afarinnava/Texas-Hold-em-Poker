from poker.validators import FiveCardsInARowValidator


class StraightFlushValidator(FiveCardsInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"

    def is_valid(self):
        return len(self._straight_flush_card_batches) >= 1

    def valid_cards(self):
        return self._straight_flush_card_batches[0]

    @property
    def _straight_flush_card_batches(self):
        return [
            five_cards
            for five_cards in self._collections_of_five_straight_cards_in_row
            if len({card.suit for card in five_cards}) == 1
        ]
