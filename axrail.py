class VendingMachine:
    items = {
        "A": ("Coca-Cola", 10),
        "B": ("Pepsi", 15),
        "C": ("Sprite", 20),
        "D": ("Water", 7),
    }

    notes = {
        100: 0, 
        50: 1, 
        20: 2, 
        10: 3, 
        5: 10, 
        1: 10
    }

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

    def purchase(self, change_amount):
        """
        Calculate the amount of change and number of notes
        """
        remaining = change_amount
        change_note = {}
        for note in self.notes.keys():
            change_note[note] = 0
        for note, note_available in self.notes.items():
            if remaining == 0:
                break
            note_amount_required = remaining // note
            note_count = min(note_amount_required, note_available)
            if note_count > 0:
                remaining -= note * note_count
                note_available -= note_count
                self.notes[note] = note_available
            change_note[note] = note_count

        for ic_note, ic_note_count in change_note.items():
            for note, note_available in self.notes.items():
                if note < ic_note and note_available > 0:
                    no_required = ic_note // note
                    note_available_count = note_available // no_required 
                    while note_available - no_required > 0 and ic_note_count > 0:
                        ic_note_count -= 1
                        change_note[ic_note] = ic_note_count
                        change_note[note] += no_required
                        note_available -= no_required
                        self.notes[note] = note_available
                        self.notes[ic_note] += 1

        if remaining > 0:
            print("Vending machine has insufficient amount of note")
            return None
        
        return change_note


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
        change_amount = amount_paid - price
        change_note = vm.purchase(change_amount)
        if change_note is None:
            continue
        print(f"Please take your drinks and change with a total amount of {change_amount:.2f}")
        for note, amount in change_note.items():
            if amount > 0:
                print(f"{amount} ${note}")

        next = input("Do you want to purchase another drinks? (yes/no)").strip()
        if next.lower() == 'no':
            break