import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(position, maximising_player, alpha, beta):
    if position.current_winner:
        if position.current_winner == 'X':
            return (None, 1*(position.num_empty_squares() + 1))
        else:
            return (None, -1*(position.num_empty_squares() + 1))
    elif not position.empty_squares():
        return (None, 0)

    if maximising_player:
        max_eval = -math.inf
        best_move = None
        for move in position.available_moves():
            position.make_move(move, 'X')
            eval, _ = minimax(position, False, alpha, beta)
            position.board[move] = ' '
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in position.available_moves():
            position.make_move(move, 'O')
            eval, _ = minimax(position, True, alpha, beta)
            position.board[move] = ' '
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Instructions: Enter a number between 0-8 to place your move on the board.")
    TicTacToe.print_board_nums()
    print("Let's start the game!")
    game = TicTacToe()
    game.print_board()

    while game.empty_squares():
        if game.current_winner:
            break
        if game.num_empty_squares() == 1:
            move = game.available_moves()[0]
        else:
            if game.num_empty_squares() % 2 == 0:
                _, move = minimax(game, True, -math.inf, math.inf)
            else:
                _, move = minimax(game, False, -math.inf, math.inf)
        game.make_move(move, 'X' if game.num_empty_squares() % 2 == 0 else 'O')
        game.print_board()
        if game.current_winner:
            if game.current_winner == 'X':
                print("X wins!")
            else:
                print("O wins!")
            break
        elif not game.empty_squares():
            print("It's a tie!")

if __name__ == "__main__":
    play_game()
