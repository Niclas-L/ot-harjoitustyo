# THIS IS CURRENTLY VERY MESSY BUT IT WORKS, I DON'T HAVE THE TIME RIGHT NOW TO REFACTOR IT
# I HAVE NOW SPENT SOME MORE TIME LOOKING AT THIS AND I HAVE DECIDED TO LEAVE IT AS IT IS
# I CANNOT SEEM TO MAKE IT WORK IN A MORE SIMPLE OR CLEAR WAY


def control_help(control, board):
    # IF ANY SQUARES MOVED, SPAWN NEW NUMBERS. NO CHANGE = INVALID MOVE, NO NEW NUMBER
    board.update_list()
    if control != board.list:
        board.spawn_square()


def up(board):  # pylint: disable=invalid-name
    # MAKING COPY OF BOARD.LIST TO LATER CONTROL IF SQUARES MOVED OR NOT
    control = board.list.copy()

    for i in board.dict:
        # SQUARE NEIGHBOURS
        below, above, two_above = i + 4, i - 4, i - 8
        try:
            if board.dict[i].get_value() == 0:
                board.dict[i].set_value(board.dict[below].get_value())
                board.dict[below].reset()
                if board.dict[above].get_value() == 0:
                    board.dict[above].set_value(board.dict[i].get_value())
                    board.dict[i].reset()
                    if board.dict[two_above].get_value() == 0:
                        board.dict[two_above].set_value(board.dict[above].get_value())
                        board.dict[above].reset()
                    else:
                        board.merge_squares(above, two_above)
                        continue
                else:
                    board.merge_squares(i, above)
                    continue
            else:
                board.merge_squares(below, i)
                continue
        except KeyError:
            # NO SUCH NEIGHBOUR EXISTS (EDGE OF MATRIX)
            continue

    control_help(control, board)


def down(board):
    # MAKING COPY OF BOARD.LIST TO LATER CONTROL IF SQUARES MOVED OR NOT
    control = board.list.copy()

    for i in reversed(board.dict):
        two_below, below, above = i + 8, i + 4, i - 4
        two_below = i + 8  # TWO ROWS BELOW NEIGHBOUR
        below = i + 4  # BELOW NEIGHBOUR
        above = i - 4  # ABOVE NEIGHBOUR
        try:
            if board.dict[i].get_value() == 0:
                board.dict[i].set_value(board.dict[above].get_value())
                board.dict[above].reset()
                if board.dict[below].get_value() == 0:
                    board.dict[below].set_value(board.dict[i].get_value())
                    board.dict[i].reset()
                    if board.dict[two_below].get_value() == 0:
                        board.dict[two_below].set_value(board.dict[below].get_value())
                        board.dict[below].reset()
                    else:
                        board.merge_squares(below, two_below)
                        continue
                else:
                    board.merge_squares(i, below)
                    continue
            else:
                board.merge_squares(above, i)
                continue
        except KeyError:
            # NO SUCH NEIGHBOUR EXISTS (EDGE OF MATRIX)
            continue

    control_help(control, board)


def left(board):
    # MAKING COPY OF BOARD.LIST TO LATER CONTROL IF SQUARES MOVED OR NOT
    control = board.list.copy()

    # I ITERATES THROUGH THE MATRIX IN STEPS OF 4
    # TO COMPARE SQUARES IN THE SAME ROW
    for i in range(0, 13, 4):
        square_control = board.dict[i].get_value()
        board.merge_squares(i + 1, i)
        if (
            board.dict[i + 1].get_value() == 0
            and board.dict[i + 2].get_value() == 0
            and board.dict[i + 3].get_value() == square_control
        ):
            board.merge_squares(i + 3, i)
        if (
            board.dict[i + 1].get_value() == 0
            and board.dict[i + 2].get_value() == square_control
        ):
            board.merge_squares(i + 2, i)
        if (
            board.dict[i + 1].get_value() == 0 and board.dict[i + 2].get_value() == 0
        ) and board.dict[i + 3].get_value() == square_control:
            board.merge_squares(i + 3, i)
        elif board.dict[i + 1].get_value() == board.dict[i + 2].get_value():
            board.merge_squares(i + 2, i + 1)
        elif (
            board.dict[i + 2].get_value() == 0
            and board.dict[i + 1].get_value() == board.dict[i + 3].get_value()
        ):
            board.merge_squares(i + 3, i + 1)
        elif board.dict[i + 2].get_value() == board.dict[i + 3].get_value():
            board.merge_squares(i + 3, i + 2)
        for _ in range(3):
            if board.dict[i + 2].get_value() == 0:
                board.dict[i + 2].set_value(board.dict[i + 3].get_value())
                board.dict[i + 3].reset()
            if board.dict[i + 1].get_value() == 0:
                board.dict[i + 1].set_value(board.dict[i + 2].get_value())
                board.dict[i + 2].reset()
            if board.dict[i].get_value() == 0:
                board.dict[i].set_value(board.dict[i + 1].get_value())
                board.dict[i + 1].reset()

    control_help(control, board)


def right(board):
    # MAKING COPY OF BOARD.LIST TO LATER CONTROL IF SQUARES MOVED OR NOT
    control = board.list.copy()

    # I ITERATES THROUGH THE MATRIX IN STEPS OF 4
    # TO COMPARE SQUARES IN THE SAME ROW
    for i in range(3, 16, 4):
        square_control = board.dict[i].get_value()
        board.merge_squares(i - 1, i)
        if (
            board.dict[i - 1].get_value() == 0
            and board.dict[i - 2].get_value() == 0
            and board.dict[i - 3].get_value() == square_control
        ):
            board.merge_squares(i - 3, i)
        if (
            board.dict[i - 1].get_value() == 0
            and board.dict[i - 2].get_value() == square_control
        ):
            board.merge_squares(i - 2, i)
        if (
            board.dict[i - 1].get_value() == 0 and board.dict[i - 2].get_value() == 0
        ) and board.dict[i - 3].get_value() == square_control:
            board.merge_squares(i - 3, i)
        elif board.dict[i - 1].get_value() == board.dict[i - 2].get_value():
            board.merge_squares(i - 2, i - 1)
        elif (
            board.dict[i - 2].get_value() == 0
            and board.dict[i - 1].get_value() == board.dict[i - 3].get_value()
        ):
            board.merge_squares(i - 3, i - 1)
        elif board.dict[i - 2].get_value() == board.dict[i - 3].get_value():
            board.merge_squares(i - 3, i - 2)
        for _ in range(3):
            if board.dict[i - 2].get_value() == 0:
                board.dict[i - 2].set_value(board.dict[i - 3].get_value())
                board.dict[i - 3].reset()
            if board.dict[i - 1].get_value() == 0:
                board.dict[i - 1].set_value(board.dict[i - 2].get_value())
                board.dict[i - 2].reset()
            if board.dict[i].get_value() == 0:
                board.dict[i].set_value(board.dict[i - 1].get_value())
                board.dict[i - 1].reset()

    control_help(control, board)
