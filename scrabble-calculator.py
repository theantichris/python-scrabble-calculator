letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]


letters_to_points = {letter: point for letter, point in zip(letters, points)}

player_to_words = {}
player_to_points = {}

def add_player(player):
    player_to_words[player] = []

def score_word(word):
    points = 0
    for char in word:
        points += letters_to_points.get(char.upper(), 0)
    return points

def play_word(player, word):
    try:
        player_to_words[player].append(word)
    except KeyError:
        print(player + " is not part of this game.")

def update_point_totals():
    for player, words in player_to_words.items():
        points = 0
        for word in words:
            points += score_word(word)
        player_to_points[player] = points


add_player("Christopher")
play_word("Christopher", "butts")
update_point_totals()
print(player_to_points)
