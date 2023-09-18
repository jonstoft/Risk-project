import random
import numpy as np

import network

class CardMissing(Exception):
    """Error if there are too few terretories compared with the number of cards needed in a game"""

class Card():
    def __init__(self, terretory: str, card_type: str):
        self.terretory = terretory
        self.card_type = card_type

    def getInfo(self):
        return (self.card_type, self.terretory)
    
    def getCardType(self):
        return self.card_type

class CardDeck():
    def __init__(self, terretories: list, nr_players) -> None:
        self.deck = self.createDeck(terretories, len(terretories), nr_players)
        
    def createDeck(self, terretories: list, num_terretories: int, nr_players) -> set:
        deck = set()
        # Check if there is an adequet number of terretories for the number of players, 
        # so all players can have 5 cards at the same time
        if (num_terretories + 2) < (nr_players * 5):
            raise ValueError("There are too few terretories for the number of players on the map")
        # Create list of the three card types and shuffle them
        card_types = ['Infantry', 'Cavelary', 'Canon'] 
        # Create a ballanced card set with a random card type for every terretory
        for i, terretory in enumerate(random.shuffle(terretories)):
            new_card = Card(terretory, card_types[i%3])
            deck.add(new_card)

        # Add 2 joker cards, which count as any card, but not any terretory
        for _ in range(2):
            deck.add(Card("None", "Joker"))
        return deck


    def drawCard(self) -> Card:
        """Method to draw a card from the deck. Include error if deck is empty."""
        if len(self.deck) == 0:
            raise CardMissing("There are no more cards to draw")
        return self.deck.pop()
    
    def returnCards(self, cards: list) ->  None:
        self.deck.update(cards)




class CardManager():
    def __init__(self) -> None:
        self.card_type_to_idx_dict = {'Infantry' : 0, 
                                      'Cavelary' : 1, 
                                      'Canon' : 2, 
                                      'Joker' : 3}
        

    def findPosibleCardUses(self, cards: [Card]) -> None:
        # If the player don't have any cards
        if len(cards) == 0:
            return None
        
        # Counting number of cards as an array
        num_cards = [0]*4
        for card in cards:
            num_cards[self.card_type_to_idx_dict[card.getCardType]] += 1
        
        # Create vector with posible combinations: 
        #[infantry_posible, cavelary_posible, Canon_posible, mix_posible]
        posible_combinations = [0]*4

        # Adding the joker count to all other combinations
        # Combination of having 3 of the same card:
        for type in range(3):
            if num_cards[type] + num_cards[3] >= 3:
                posible_combinations[type] = 1

        # Adding the posibility of one of all the cards
        if np.count_nonzero(num_cards) >= 3:
            posible_combinations[3] = 1
        
        return posible_combinations
    

    def findCombinationValue(self, posible_combinations: list) -> []:
        # If no combination of cards can be played
        if sum(posible_combinations) == 0:
            return None
        
        points_for_combinations = []

        for combination_number, combination in enumerate(posible_combinations):
            if combination

            




class RiskPlayer:
    """Class for a player in risk: Tracks the state of a player, control the action 
    of the player, and is each players interface with the game. The player class 
    have the following fields and methods: 
    
    Fields: 
        - terretories: [Terretory]: A list of terretories that the player controls
        - total_terretories: int: The number of terretories the player control
        - total_troups
        - turn: bool: True if it is players turn, False if it is not players turn
        - turn_type: Turntype: The type of turn it is for the player, used in diffirent gamemodes
        - colour: Colour: The colour of the player
        - troups_to_mobilize: The number of troups the player can mobilize in a turn
        - alive: bool: True if player is still alive, False if player is dead

    Public methods:

    -- init(terretories: [Terretory]): Initializes the player with the initial state of the player.
    -- takeTurn(turn_type: [Turntype], mobilize: int): 

     """
    

    def __init__(self, terretories: [Terretory], colour: Colour, 
                 starting_troups: int, card_pointer: Card, map_pointer: Map,
                 ComboMagager: ComboMagager) -> None:
        self.terretories: [Terretory] = terretories
        self.total_terretories: int = len(terretories)
        self.total_troups: int = starting_troups
        self.turn: bool = False
        self.alive: bool = True
        self.colour = colour
        self.cards = []
        self.card_pointer = card_pointer
        self.map_pointer = map_pointer
        self.ComboMagager = ComboMagager



    def takeTurn(self, turn_type: [Turntype], troups_to_mobilize: int = 0):
        
        self.turn = True
        terretorries_captured_in_turn = 0

        # If the turn include moblization
        if 'mobilize' in turn_type:
            self.mobilize(troups_to_mobilize)

        # If turn include attacking
        if 'attack' in turn_type:
            terretorries_captured_in_turn = self.attack()

        # If turn include fortifying    
        if 'fortify' in turn_type:
            self.fortify()
        
        # If turn include grabbing terretorie:
        if 'grab' in turn_type:
            self.grab()


        # Add other types of turns for other game-modes at appropriate places

        self.end_turn(terretorries_captured_in_turn)


    def end_turn(self, terretorries_captured_in_turn):
        """ Method for ending a turn for a player. This includes drawing a risk card 
        if terretories were captured, but can include other actions depending on 
        gamemode or expantion to visual media"""
        if terretorries_captured_in_turn > 0:
            self.draw_card()

        self.turn = False

        return
    
    def draw_card(self):
        """Class to draw a card."""
        self.cars.append(self.card_pointer.draw())
        return
    
    def mobilize(self, troups_to_mobilize: int):
        """Method to mobilize troups. This covers two actions: Placing in troups and 
        activating cards. """

        if len(self.cards) >= 5:
            must_activate_cards = True

        end_mobilization = False
        while not end_mobilization:
            action = input("Write the number of the action do you want to take:\n1: See your risk cards\n2: Use your risk cards\n3: Add troups to a terretory\n4: End mobilization")

            if action == "1":
                self.view_risk_cards()
            
            elif action == "2":
                self.useRiskCards()



        
    def view_risk_cards(self) -> None:
        """Method for the player to see their cards"""

        print("\n\n" + "-" * 80)

        if len(self.cards) == 0:
            print("You don't have any cards")
            return
        
        print(f"Your {len(self.cards)} cards are:")
        for card in self.cards:
            print(f"Type: {card[0]}, Terretory: {card[1]}")
        # Create seperation of cards, so its clear where the cards starts and end
        print("\n\n" + "-" * 80)
        return
    

    def useRiskCards(self):
        possible_combinations = self.ComboMagager.findPosibleCardUses(self.cards)
        if possible_combinations is None:
            print("You don't have any card comboes")
            return
        
        for possibility in possible_combinations:
            print(possibility)




class RiskPlayer:
    """Class for a player in risk: Tracks the state of a player, control the action 
    of the player, and is each players interface with the game. The player class 
    have the following fields and methods: 
    
    Fields: 
        - terretories: [Terretory]: A list of terretories that the player controls
        - total_terretories: int: The number of terretories the player control
        - total_troups
        - turn: bool: True if it is players turn, False if it is not players turn
        - turn_type: Turntype: The type of turn it is for the player, used in diffirent gamemodes
        - colour: Colour: The colour of the player
        - troups_to_mobilize: The number of troups the player can mobilize in a turn
        - alive: bool: True if player is still alive, False if player is dead

    Public methods:

    -- init(terretories: [Terretory]): Initializes the player with the initial state of the player.
    -- takeTurn(turn_type: [Turntype], mobilize: int): 

     """
    

    def __init__(self, terretories: [Terretory], colour: Colour, 
                 starting_troups: int, card_pointer: Card, map_pointer: Map,
                 ComboMagager: ComboMagager) -> None:
        self.terretories: [Terretory] = terretories
        self.total_terretories: int = len(terretories)
        self.total_troups: int = starting_troups
        self.turn: bool = False
        self.alive: bool = True
        self.colour = colour
        self.cards = []
        self.card_pointer = card_pointer
        self.map_pointer = map_pointer
        self.ComboMagager = ComboMagager



    def takeTurn(self, turn_type: [Turntype], troups_to_mobilize: int = 0):
        
        self.turn = True
        terretorries_captured_in_turn = 0

        # If the turn include moblization
        if 'mobilize' in turn_type:
            self.mobilize(troups_to_mobilize)

        # If turn include attacking
        if 'attack' in turn_type:
            terretorries_captured_in_turn = self.attack()

        # If turn include fortifying    
        if 'fortify' in turn_type:
            self.fortify()
        
        # If turn include grabbing terretorie:
        if 'grab' in turn_type:
            self.grab()


        # Add other types of turns for other game-modes at appropriate places

        self.end_turn(terretorries_captured_in_turn)


    def end_turn(self, terretorries_captured_in_turn):
        """ Method for ending a turn for a player. This includes drawing a risk card 
        if terretories were captured, but can include other actions depending on 
        gamemode or expantion to visual media"""
        if terretorries_captured_in_turn > 0:
            self.draw_card()

        self.turn = False

        return
    
    def draw_card(self):
        """Class to draw a card."""
        self.cars.append(self.card_pointer.draw())
        return
    
    def mobilize(self, troups_to_mobilize: int):
        """Method to mobilize troups. This covers two actions: Placing in troups and 
        activating cards. """

        if len(self.cards) >= 5:
            must_activate_cards = True

        end_mobilization = False
        while not end_mobilization:
            action = input(f"You have {troups_to_mobilize} troups to mobilize, write the number of the action do you want to take:\n1: See your risk cards\n2: Use your risk cards\n3: Add troups to a terretory\n4: End mobilization")

            # Option to view risk cards.
            if action == "1":
                self.view_risk_cards()
            
            # Option to use risk cars
            elif action == "2":
                self.useRiskCards()

            # Adds troups to a terretory. Can be any number from 0 to the number of troups to mobilize
            elif action == "3": 
                troups_to_mobilize -= self.addTroupsToTerretory(troups_to_mobilize)

            elif action == "4":
                # Don't end mobilization if the player have 5 or more cards.
                if must_activate_cards: 
                    print("You must activate your cards before you end mobilization")
                
                # Don't end mobilization if the player have more troups to mobilize
                elif troups_to_mobilize != 0:
                    
                    print("You must mobilize all your troups before you end your mobilization")

                # End mobilization if the player don't have any more troups and don't need to 
                # mobilize more troups
                else: 
                    end_mobilization = True

                

            else:
                print(f"Your input {action} is not one of the posible actions, please select one of the appropreat optins.") 
        
        # When the mobilization is done 
        return

        
    def view_risk_cards(self) -> None:
        """Method for the player to see their cards"""

        print("\n\n" + "-" * 80)

        if len(self.cards) == 0:
            print("You don't have any cards")
            return
        
        print(f"Your {len(self.cards)} cards are:")
        for card in self.cards:
            print(f"Type: {card[0]}, Terretory: {card[1]}")
        # Create seperation of cards, so its clear where the cards starts and end
        print("\n\n" + "-" * 80)
        return
    

    def useRiskCards(self):
        possible_combinations = self.ComboMagager.findPosibleCardUses(self.cards)
        if possible_combinations is None:
            print("You don't have any card comboes")
            return
        
        for possibility in possible_combinations:
            print(possibility)
        
        combo_not_chosen = True
        while combo_not_chosen:
            combo_chosen = input("Which of the combinations do you want to play")
            

        

