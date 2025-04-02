import os

def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def update_window(board: list[list[str]]) -> None:
    clear_terminal()
    print_board(board)

def print_board(board: list[list[str]]) -> None:
    if board is None: return
    r: str = 'A'
    bar: str = " ---|---|---"
    col_nums: str = "  1   2   3"

    print()
    for row in board:
        print(r + " " + row[0] + " | " + row[1] + " | " + row[2])
        print(col_nums if r == 'C' else bar)
        r = chr(ord(r) + 1)

def is_board_full(board: list[list[str]]) -> bool:
    if board is None: return False
    for row in board:
        for piece in row:
            if piece == ' ':
                return False
    return True

def get_winner(board: list[list[str]]) -> str:
    if board is None: return '\0'

    for row in board:
        if row[0] == row[1] and row[0] == row[2]:
            return row[0]

    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    return ' '

def can_make_move(board: list[list[str]], row: int, col: int) -> bool:
    if board is None: return False
    return board[row][col] == ' '

def make_move(board: list[list[str]], piece: str, row: int, col: int) -> None:
    if board is None: return
    board[row][col] = piece

def parse_coordinates(coords: str, positions: list[int]) -> None:
    if coords is None or positions is None or len(coords) != 2:
        return

    match coords[0]:
        case 'A' | 'a': positions[0] = 0
        case 'B' | 'b': positions[0] = 1
        case 'C' | 'c': positions[0] = 2
        case _ : raise ValueError("Invalid coordinates")

    match coords[1]:
        case '1': positions[1] = 0
        case '2': positions[1] = 1
        case '3': positions[1] = 2
        case _ : raise ValueError("Invalid coordinates")

def main():
    board: list = [[' '] * 3 for _ in range(3)]
    positions: list = [0, 0]

    update_window(board)

    is_X_turn: bool = True
    while (winner := get_winner(board)) == ' ' and not is_board_full(board):
        coords: str = input("\nEnter move for " + ("X: " if is_X_turn else "O: "))
        parse_coordinates(coords, positions)

        if can_make_move(board, positions[0], positions[1]):
            if is_X_turn:
                piece: str = 'X'
                is_X_turn = False
            else:
                piece: str = 'O'
                is_X_turn = True
            make_move(board, piece, positions[0], positions[1])

        update_window(board)

    if winner == ' ':
        print("\nDraw!")
    else:
        print("\nThe winner is " + winner)

if __name__ == "__main__":
    main()