import random

BLANK = ' '
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'
TRAINING_EPOCHS = 40000
TRAINING_EPSILON = .4
REWARD_WIN = 10
REWARD_LOSE = -100
REWARD_TIE = -10


class Player:

    @staticmethod
    def show_board(board):
        print('|'.join(board[0:3]))
        print('|'.join(board[3:6]))
        print('|'.join(board[6:9]))


class HumanPlayer(Player):

    def reward(self, value, board):
        pass

    def make_move(self, board):

        while True:
            try:
                self.show_board(board)
                move = input('Your next move (cell index 1-9):')
                move = int(move)

                if not (move - 1 in range(9)):
                    raise ValueError
            except ValueError:
                print('Invalid move; try again:\n')
            else:
                return move-1


class AIPlayer(Player):

    def __init__(self, epsilon=0.4, alpha=0.3, gamma=0.9, default_q=1):
        # this is the epsilon parameter of the model: the probability of exploration
        self.EPSILON = epsilon
        # learning rate
        self.ALPHA = alpha
        # discount parameter for future reward (rewards now are better than rewards in the future)
        self.GAMMA = gamma
        # if the given move at the given state is not defined yet: we have a default Q value
        self.DEFAULT_Q = default_q
        # Q(s,a) function is a dict in this implementation. This is the Q function - Q: SxA -> R
        # return a value for s state and a action (s,a) pair
        self.q = {}
        # previous move during the game
        self.move = None
        # board in the previous iteration
        self.board = (' ',) * 9

    # these are available or empty cells on the grid (board)
    def available_moves(self, board):
        return [i for i in range(9) if board[i] == ' ']

    # Q(s,a) -> Q value for (s,a) pair - if no Q value exists then create a new one with the
    # default value (=1) and otherwise we return the q value present in the dict
    def get_q(self, state, action):
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = self.DEFAULT_Q

        return self.q[(state, action)]

    # make a random move with epsilon probability (exploration) or pick the action with the
    # highest Q value (exploitation)
    def make_move(self, board):

        self.board = tuple(board)
        actions = self.available_moves(board)

        # action with epsilon probability
        if random.random() < self.EPSILON:
            # this is in index (0-8 board cell related index)
            self.move = random.choice(actions)
            return self.move

        # take the action with highest Q value
        q_values = [self.get_q(self.board, a) for a in actions]
        max_q_value = max(q_values)

        # if multiple best actions, choose one at random
        if q_values.count(max_q_value) > 1:
            best_actions = [i for i in range(len(actions)) if q_values[i] == max_q_value]
            best_move = actions[random.choice(best_actions)]
        # there is just a single best move (best action)
        else:
            best_move = actions[q_values.index(max_q_value)]

        self.move = best_move
        return self.move

    # let's evaluate a given state: so update the Q(s,a) table regarding s state and a action
    def reward(self, reward, board):
        if self.move:
            prev_q = self.get_q(self.board, self.move)
            max_q_new = max([self.get_q(tuple(board), a) for a in self.available_moves(self.board)])
            self.q[(self.board, self.move)] = prev_q + self.ALPHA * (reward + self.GAMMA * max_q_new - prev_q)


class TicTacToe:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.first_player_turn = random.choice([True, False])
        self.board = [' '] * 9

    def play(self):

        # this is the "game loop"
        while True:
            if self.first_player_turn:
                player = self.player1
                other_player = self.player2
                player_tickers = (AI_PLAYER, HUMAN_PLAYER)
            else:
                player = self.player2
                other_player = self.player1
                player_tickers = (HUMAN_PLAYER, AI_PLAYER)

            # check the state of the game (win, lose or draw)
            game_over, winner = self.is_game_over(player_tickers)

            # game is over: handle the rewards
            if game_over:
                if winner == player_tickers[0]:
                    player.show_board(self.board[:])
                    print('\n %s won!' % player.__class__.__name__)
                    player.reward(REWARD_WIN, self.board[:])
                    other_player.reward(REWARD_LOSE, self.board[:])
                if winner == player_tickers[1]:
                    player.show_board(self.board[:])
                    print('\n %s won!' % other_player.__class__.__name__)
                    other_player.reward(REWARD_WIN, self.board[:])
                    player.reward(REWARD_LOSE, self.board[:])
                else:
                    player.show_board(self.board[:])
                    print('Tie!')
                    player.reward(REWARD_TIE, self.board[:])
                    other_player.reward(REWARD_TIE, self.board[:])
                break

            # next player's turn in the next iteration
            self.first_player_turn = not self.first_player_turn

            # actual player's best move (based on Q(s,a) table for AI player)
            move = player.make_move(self.board)
            self.board[move] = player_tickers[0]

    def is_game_over(self, player_tickers):

        # consider both players (X and O players - these are the tickers)
        for player_ticker in player_tickers:

            # check horizontal dimension (so the rows)
            for i in range(3):
                if self.board[3 * i + 0] == player_ticker and\
                        self.board[3 * i + 1] == player_ticker and\
                        self.board[3 * i + 2] == player_ticker:
                    return True, player_ticker

            # check vertical dimension (so the columns)
            for j in range(3):
                if self.board[j + 0] == player_ticker and \
                        self.board[j + 3] == player_ticker and \
                        self.board[j + 6] == player_ticker:
                    return True, player_ticker

            # check diagonal dimensions (top left to bottom right + top right to bottom left)
            if self.board[0] == player_ticker and self.board[4] == player_ticker and\
                    self.board[8] == player_ticker:
                return True, player_ticker

            if self.board[2] == player_ticker and self.board[4] == player_ticker and self.board[6] == player_ticker:
                return True, player_ticker

        # finally we can deal with the 'draw' cases
        if self.board.count(' ') == 0:
            return True, None
        else:
            return False, None


if __name__ == '__main__':

    ai_player_1 = AIPlayer()
    ai_player_2 = AIPlayer()

    print('Training the AI player(s)...')

    ai_player_1.EPSILON = TRAINING_EPSILON
    ai_player_2.EPSILON = TRAINING_EPSILON

    for _ in range(TRAINING_EPOCHS):
        game = TicTacToe(ai_player_1, ai_player_2)
        game.play()

    print('\nTraining is Done')
    # epsilon=0 means no exploration - it will use the Q(s,a) function to make the moves
    ai_player_1.EPSILON = 0
    human_player = HumanPlayer()
    game = TicTacToe(ai_player_1, human_player)
    game.play()
