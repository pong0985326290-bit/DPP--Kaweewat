def checkmate(board: str) -> None:
    try:
        # แปลง board เป็น list ของ list
        rows = [list(line) for line in board.strip().splitlines() if line.strip() != ""]
        
        if not rows:
            return  # empty board → ไม่ทำอะไร

        height = len(rows)
        width = len(rows[0])

        # ตรวจว่าเป็นสี่เหลี่ยมจัตุรัส
        for row in rows:
            if len(row) != width:
                return  # ไม่ใช่ square → silent fail

        # หาตำแหน่ง King และตรวจว่ามีแค่ตัวเดียว
        king_pos = None
        for y in range(height):
            for x in range(width):
                if rows[y][x] == 'K':
                    if king_pos is not None:
                        return  # มี King มากกว่า 1 ตัว
                    king_pos = (x, y)

        if king_pos is None:
            return  # ไม่มี King

        kx, ky = king_pos

        # ฟังก์ชันช่วยตรวจทิศทาง (สำหรับ Rook, Bishop, Queen)
        def is_attacked_in_direction(dx: int, dy: int, pieces: set) -> bool:
            x, y = kx + dx, ky + dy
            while 0 <= x < width and 0 <= y < height:
                piece = rows[y][x]
                if piece != '.' and piece != ' ':  # มีชิ้นส่วน
                    return piece in pieces
                x += dx
                y += dy
            return False

        # 1. ตรวจ Pawn (โจมตีทแยงขึ้น)
        for dx in (-1, 1):
            px, py = kx + dx, ky - 1  # ขึ้นไป 1 แถว
            if 0 <= px < width and 0 <= py < height:
                if rows[py][px] == 'P':
                    print("Success")
                    return

        # 2. ตรวจ Rook + Queen (แนวนอน + แนวตั้ง)
        rook_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in rook_dirs:
            if is_attacked_in_direction(dx, dy, {'R', 'Q'}):
                print("Success")
                return

        # 3. ตรวจ Bishop + Queen (ทแยง)
        bishop_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in bishop_dirs:
            if is_attacked_in_direction(dx, dy, {'B', 'Q'}):
                print("Success")
                return

        # ไม่ถูกโจมตี
        print("Fail")

    except Exception:
        # กัน error ทุกอย่าง → ไม่ crash
        return