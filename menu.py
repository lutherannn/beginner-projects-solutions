from decimal import Decimal
import sys
import os
import time


def main():
    while True:
        menu = {
            "1. Chicken Strips": "$3.50",
            "2. French Fries": "$2.50",
            "3. Hamburger": "$4.00",
            "4. Hot Dog": "$3.50",
            "5. Salad": "$3.75",
            "6. Small Drink": "$1.25",
            "7. Medium Drink": "$1.50",
            "8. Large Drink": "$1.75",
            "9. Milkshake": "$2.25",
        }
        total = 0.00
        itemsOrdered = []
        fmtOrdered = []
        os.system("cls" if os.name == "nt" else "clear")
        for k, v in menu.items():
            print(k, v)
        order = input("> ")
        if len(order) < 1:
            sys.exit()
        for x in order:
            if x.isalpha() or x == "0":
                sys.exit()
            total += float(str(list(menu.values())[int(x) - 1])[1:])
            itemsOrdered.append(str(list(menu.keys())[int(x) - 1])[3:])
        for x in itemsOrdered:
            if f"{x}: {itemsOrdered.count(x)}" not in fmtOrdered:
                fmtOrdered.append(f"{x}: {itemsOrdered.count(x)}")
        print("\n".join(fmtOrdered))
        print(f"${format(total, ".2f")}")
        time.sleep(5)


main()
