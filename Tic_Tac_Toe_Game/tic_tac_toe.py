"""
Tic-Tac-Toe Game - A classic two-player game
"""

import random


class TicTacToe:
    """Tic-Tac-Toe game implementation."""

    def __init__(self):
        """Initialize the game."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.moves_count = 0

    def display_board(self):
        """Display the current game board."""
        board_display = f"""
        {self.board[0]} | {self.board[1]} | {self.board[2]}
       ---+---+---
        {self.board[3]} | {self.board[4]} | {self.board[5]}
       ---+---+---
        {self.board[6]} | {self.board[7]} | {self.board[8]}
        """
        return board_display

    def display_board_with_positions(self):
        """Display board positions for reference."""
        return """
        Position Reference:
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        """

    def make_move(self, position):
        """Make a move at the given position (1-9)."""
        if not 1 <= position <= 9:
            return False, "Invalid position. Choose 1-9."

        index = position - 1
        if self.board[index] != " ":
            return False, "Position already taken. Choose another."

        self.board[index] = self.current_player
        self.moves_count += 1

        # Check for winner or draw
        if self.check_winner():
            self.game_over = True
            self.winner = self.current_player
            return True, f"🎉 Player {self.current_player} wins!"

        if self.moves_count == 9:
            self.game_over = True
            return True, "🤝 It's a draw!"

        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"
        return True, f"Player {self.current_player}'s turn"

    def check_winner(self):
        """Check if there's a winner."""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] ==
                    self.board[combo[2]] != " "):
                return True
        return False

    def reset_game(self):
        """Reset the game to initial state."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.moves_count = 0
        return "Game reset! Player X starts."

    def get_available_moves(self):
        """Get list of available positions."""
        return [i + 1 for i in range(9) if self.board[i] == " "]

    def ai_move(self):
        """Simple AI to make a move (random from available)."""
        available = self.get_available_moves()
        if available:
            # Try to win or block
            move = self._find_best_move()
            if move:
                return self.make_move(move)
            # Random move
            return self.make_move(random.choice(available))
        return False, "No moves available"

    def _find_best_move(self):
        """Find the best move for AI (basic strategy)."""
        # Check if AI can win
        for pos in self.get_available_moves():
            test_board = self.board.copy()
            test_board[pos - 1] = self.current_player
            if self._would_win(test_board, self.current_player):
                return pos

        # Block opponent's win
        opponent = "X" if self.current_player == "O" else "O"
        for pos in self.get_available_moves():
            test_board = self.board.copy()
            test_board[pos - 1] = opponent
            if self._would_win(test_board, opponent):
                return pos

        # Take center if available
        if 5 in self.get_available_moves():
            return 5

        # Take a corner
        corners = [1, 3, 7, 9]
        available_corners = [c for c in corners if c in self.get_available_moves()]
        if available_corners:
            return random.choice(available_corners)

        return None

    def _would_win(self, board, player):
        """Check if the given board state would be a win for player."""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False


def play_two_player():
    """Play a two-player game."""
    game = TicTacToe()

    print("\n🎮 Two Player Mode")
    print(game.display_board_with_positions())

    while not game.game_over:
        print(game.display_board())
        print(f"Player {game.current_player}'s turn")

        try:
            position = int(input("Enter position (1-9): "))
            success, message = game.make_move(position)
            print(f"\n{message}")
        except ValueError:
            print("\n❌ Invalid input. Please enter a number 1-9.")

    print(game.display_board())
    return game.winner


def play_vs_ai():
    """Play against AI."""
    game = TicTacToe()

    print("\n🤖 Play vs AI Mode")
    print("You are X, AI is O")
    print(game.display_board_with_positions())

    while not game.game_over:
        print(game.display_board())

        if game.current_player == "X":
            print("Your turn!")
            try:
                position = int(input("Enter position (1-9): "))
                success, message = game.make_move(position)
                print(f"\n{message}")
            except ValueError:
                print("\n❌ Invalid input. Please enter a number 1-9.")
                continue
        else:
            print("AI is thinking...")
            _, message = game.ai_move()
            print(f"\n{message}")

    print(game.display_board())
    return game.winner


def main():
    """Main function to run the Tic-Tac-Toe game."""
    scores = {"X": 0, "O": 0, "Draw": 0}

    print("=" * 50)
    print("       Welcome to Tic-Tac-Toe Game")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("1. Two Player Mode")
        print("2. Play vs AI")
        print("3. View Scores")
        print("4. Reset Scores")
        print("5. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            winner = play_two_player()
            if winner:
                scores[winner] += 1
            else:
                scores["Draw"] += 1

        elif choice == "2":
            winner = play_vs_ai()
            if winner:
                scores[winner] += 1
            else:
                scores["Draw"] += 1

        elif choice == "3":
            print("\n🏆 Scoreboard:")
            print(f"   Player X: {scores['X']} wins")
            print(f"   Player O: {scores['O']} wins")
            print(f"   Draws: {scores['Draw']}")

        elif choice == "4":
            scores = {"X": 0, "O": 0, "Draw": 0}
            print("\n✅ Scores reset!")

        elif choice == "5":
            print("\nThanks for playing Tic-Tac-Toe! Goodbye! 🎮")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
