# Texas-Hold-em-Poker
**A simulation of Texas Hold'em Poker game developed in Python using Test-Driven Development(TDD).**

Texas hold 'em (also known as Texas holdem, hold 'em, and holdem) is one of the most popular variants of the card game of poker. Two cards, known as hole cards, are dealt face down to each player, and then five community cards are dealt face up in three stages. The stages consist of a series of three cards ("the flop"), later an additional single card ("the turn" or "fourth street"), and a final card ("the river" or "fifth street"). Each player seeks the best five card poker hand from any combination of the seven cards; the five community cards and their two hole cards. Players have betting options to check, call, raise, or fold. Rounds of betting take place before the flop is dealt and after each subsequent deal. The player who has the best hand and has not folded by the end of all betting rounds wins all of the money bet for the hand, known as the pot. In certain situations, a "split-pot" or "tie" can occur when two players have hands of equivalent value. This is also called a "chop-pot". 

# *Rules*

## Betting structures

Hold 'em is normally played using small and big blind bets—forced bets by two players. Antes (forced contributions by all players) may be used in addition to blinds, particularly in later stages of tournament play. A dealer button is used to represent the player in the dealer position; the dealer button rotates clockwise after each hand, changing the position of the dealer and blinds. The small blind is posted by the player to the left of the dealer and is usually equal to half of the big blind. The big blind, posted by the player to the left of the small blind, is equal to the minimum bet. In tournament poker, the blind/ante structure periodically increases as the tournament progresses. After one round of betting is done, the next betting round will start by the person in the small blind.

A standard hold 'em game showing the position of the blinds relative to the dealer button: 
![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Texas_Hold%27em_Poker_Table_with_Blinds.svg/700px-Texas_Hold%27em_Poker_Table_with_Blinds.svg.png)

When only two players remain, special "head-to-head" or "heads up" rules are enforced and the blinds are posted differently. In this case, the person with the dealer button posts the small blind, while their opponent places the big blind. The dealer acts first before the flop. After the flop, the dealer acts last and continues to do so for the remainder of the hand.

The three most common variations of hold 'em are limit hold 'em, no-limit hold 'em and pot-limit hold 'em. Limit hold 'em has historically been the most popular form of hold 'em found in casino live action games in the United States. In limit hold 'em, bets and raises during the first two rounds of betting (pre-flop and flop) must be equal to the big blind; this amount is called the small bet. In the next two rounds of betting (turn and river), bets and raises must be equal to twice the big blind; this amount is called the big bet.

No-limit hold 'em has grown in popularity and is the form most commonly found in televised tournament poker and is the game played in the main event of the World Series of Poker. In no-limit hold 'em, players may bet or raise any amount over the minimum raise up to all of the chips the player has at the table (called an all-in bet). The minimum raise is equal to the size of the previous bet or raise. If someone wishes to re-raise, they must raise at least the amount of the previous raise. For example, if the big blind is $2 and there is a raise of $6 to a total of $8, a re-raise must be at least $6 more for a total of $14. If a raise or re-raise is all-in and does not equal the size of the previous raise (or half the size in some casinos), the initial raiser cannot re-raise again (in case there are other players also still in the game). In pot-limit hold 'em, the maximum raise is the current size of the pot (including the amount needed to call).

Some casinos that offer hold 'em also allow the player to the left of the big blind to post an optional live straddle, usually double the amount of the big blind. This causes that player to act as the big blind and the player has an option to raise when it comes to their turn again. (Some variations allow for straddle on the button). No-limit games may also allow multiple re-straddles, in any amount that would be a legal raise.

## Play of the hand

Following a shuffle of the cards, play begins with each player being dealt two cards face down, with the player in the small blind receiving the first card and the player in the button seat receiving the last card dealt. (As in most poker games, the deck is a standard 52-card deck containing no jokers.) These cards are the players' hole or pocket cards. These are the only cards each player will receive individually, and they will (possibly) be revealed only at the showdown, making Texas hold 'em a closed poker game.

Each player is dealt two private cards in hold 'em, which are dealt first:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Texas_Hold_%27em_Hole_Cards.jpg/440px-Texas_Hold_%27em_Hole_Cards.jpg)

The hand begins with a "pre-flop" betting round, beginning with the player to the left of the big blind (or the player to the left of the dealer, if no blinds are used) and continuing clockwise. A round of betting continues until every player has folded, put in all of their chips, or matched the amount put in by all other active players. See betting for a detailed account. Note that the blinds are considered "live" in the pre-flop betting round, meaning that they are counted toward the amount that the blind player must contribute. If all players call around to the player in the big blind position, that player may either check or raise.

After the pre-flop betting round, assuming there remain at least two players taking part in the hand, the dealer deals a flop: three face-up community cards. The flop is followed by a second betting round. This and all subsequent betting rounds begin with the player to the dealer's left and continue clockwise.

After the flop betting round ends, a single community card (called the turn or fourth street) is dealt, followed by a third betting round. A final single community card (called the river or fifth street) is then dealt, followed by a fourth betting round and the showdown, if necessary. In the third and fourth betting rounds, the stakes double.

## The showdown

If a player bets and all other players fold, then the remaining player is awarded the pot and is not required to show their hole cards. If two or more players remain after the final betting round, a showdown occurs. On the showdown, each player plays the best poker hand they can make from the seven cards comprising their two hole cards and the five community cards. A player may use both of their own two hole cards, only one, or none at all, to form their final five-card hand. If the five community cards form the player's best hand, then the player is said to be playing the board and can only hope to split the pot, because each other player can also use the same five cards to construct the same hand.

If the best hand is shared by more than one player, then the pot is split equally among them, with any extra chips going to the first players after the button in clockwise order. It is common for players to have closely valued, but not identically ranked hands. Nevertheless, one must be careful in determining the best hand; if the hand involves fewer than five cards, (such as two pair or three of a kind), then kickers are used to settle ties (see the second example below). The card's numerical rank is of sole importance; suit values are irrelevant in hold 'em.

## Hand values

The following table shows the possible hand values in increasing order. 

| Name        | Description           | Example  |
| ------------- |:-------------:| -----:|
| Highcard      | Simple value of the card. Lowest: 2 – Highest: Ace (King in example) | ![](/Flush/Flush.png) |
| Pair      | Two cards of the same rank      |    |
| Two pairs | Two times two cards with the same rank     |     |
| Three of a kind | Three cards with the same rank      |     |
| Straight | Sequence of 5 cards in increasing value (Ace can precede 2 and follow up King)      |     |
| Flush | 5 cards of the same suit      |  <img src = "images/Flush.png" width = 200>   |
| Full house | Combination of three of a kind and a pair      |     |
| Four of a kind | Four cards of the same rank      |     |
| Straight flush | Straight of the same suit      |     |
| Royal flush | Straight flush that ends with Ace      |     |


