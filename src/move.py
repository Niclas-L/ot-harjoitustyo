# THIS IS CURRENTLY VERY MESSY BUT IT WORKS, I DON'T HAVE THE TIME RIGHT NOW TO REFACTOR IT


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
        h = i + 4  # BELOW NEIGHBOUR
        j = i - 4  # ABOVE NEIGHBOUR
        k = i - 8  # TWO ROWS ABOVE NEIGHBOUR
        try:
            if board.dict[i].get_value() == 0:
                board.dict[i].set_value(board.dict[h].get_value())
                board.dict[h].reset()
                if board.dict[j].get_value() == 0:
                    board.dict[j].set_value(board.dict[i].get_value())
                    board.dict[i].reset()
                    if board.dict[k].get_value() == 0:
                        board.dict[k].set_value(board.dict[j].get_value())
                        board.dict[j].reset()
                    else:
                        board.merge_squares(j, k)
                        continue
                else:
                    board.merge_squares(i, j)
                    continue
            else:
                board.merge_squares(h, i)
                continue
        except KeyError:
            # NO SUCH NEIGHBOUR EXISTS (EDGE OF MATRIX)
            continue

    control_help(control, board)


def down(board):
    # MAKING COPY OF BOARD.LIST TO LATER CONTROL IF SQUARES MOVED OR NOT
    control = board.list.copy()

    for i in reversed(board.dict):
        g = i + 8  # TWO ROWS BELOW NEIGHBOUR
        h = i + 4  # BELOW NEIGHBOUR
        j = i - 4  # ABOVE NEIGHBOUR
        try:
            if board.dict[i].get_value() == 0:
                board.dict[i].set_value(board.dict[j].get_value())
                board.dict[j].reset()
                if board.dict[h].get_value() == 0:
                    board.dict[h].set_value(board.dict[i].get_value())
                    board.dict[i].reset()
                    if board.dict[g].get_value() == 0:
                        board.dict[g].set_value(board.dict[h].get_value())
                        board.dict[h].reset()
                    else:
                        board.merge_squares(h, g)
                        continue
                else:
                    board.merge_squares(i, h)
                    continue
            else:
                board.merge_squares(j, i)
                continue
        except KeyError:
            # NO SUCH NEIGHBOUR EXISTS (EDGE OF MATRIX)
            continue

    control_help(control, board)


def left(board):
    # MAKING COPY OF BOARD.LIST TO LATER CONTROL IF SQUARES MOVED OR NOT
    control = board.list.copy()

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
            board.dict[i + 1].get_value() == 0 and board.dict[i +
                                                              2].get_value() == 0
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
            board.dict[i - 1].get_value() == 0 and board.dict[i -
                                                              2].get_value() == 0
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
