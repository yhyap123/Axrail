class VendingMachine:
    items = {
        "A": ("Coca-Cola", 10),
        "B": ("Pepsi", 15),
        "C": ("Sprite", 20),
        "D": ("Water", 7),
    }

    notes = [100, 50, 20, 10, 5, 1]

    def list_items(self):
        """
        Print all the drinks
        """
        for choice, (drink, price) in self.items.items():
            print(f"{choice}: Drinks - {drink}, Price - ${price:.2f}")

    def select_items(self, choice):
        """
        Find and return the selected drinks
        """
        for key in self.items:
            if choice.lower() == key.lower():
                return self.items[key]
        print("This item is not available")
        return None

    def purchase(self, price, amount_paid):
        """
        Calculate the amount of change and number of notes
        """
        change_amount = amount_paid - price
        remaining = change_amount
        change_note = {}
        for note in self.notes:
            if remaining == 0:
                break
            note_amount = remaining // note
            remaining %= note
            change_note[note] = note_amount
        return change_note, change_amount


if __name__ == "__main__":
    vm = VendingMachine()
    
    while True:
        vm.list_items()
        choice = input("Please select your drinks from the menu (A/B/C/D): ").strip()

        item = vm.select_items(choice)
        if item is None:
            continue
        drinks = item[0]
        price = item[1]

        try:
            amount_paid = int(input("Please pay the money: "))
        except Exception as e:
            print("Please enter a valid amount")
            continue
        if amount_paid < price:
            print("Insufficient amount")
            continue

        change_note, change_amount = vm.purchase(price, amount_paid)
        print(f"Please take your drinks and change with a total amount of {change_amount:.2f}")
        for note, amount in change_note.items():
            if amount > 0:
                print(f"{amount} ${note}")

        next = input("Do you want to purchase another drinks? (yes/no)").strip()
        if next.lower() == 'no':
            break