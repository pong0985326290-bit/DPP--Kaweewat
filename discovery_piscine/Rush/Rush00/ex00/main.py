from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1 (ควรได้ Success)
    board1 = """\
R...
.K..
..P.
....
"""
    checkmate(board1)

    # ตัวอย่างที่ 2 (ควรได้ Fail)
    board2 = """\
..
.K
"""
    checkmate(board2)

if __name__ == "__main__":
    main()