import heapq

class PickleballWaitlist:
    def __init__(self):
        self.waitlist = []  # Priority queue based on FIFO order
        self.counter = 0  # Used to maintain order

    def add_paddle(self, player_name):
        """Adds a player's paddle to the queue."""
        heapq.heappush(self.waitlist, (self.counter, player_name))
        self.counter += 1
        print(f"{player_name} has been added to the waitlist.")

    def assign_court(self):
        """Assigns the next player(s) in the queue to a court."""
        if not self.waitlist:
            print("No players in the waitlist.")
            return None
        _, player = heapq.heappop(self.waitlist)
        print(f"{player} has been assigned to a court!")
        return player

    def peek_next(self):
        """Returns the next player to be assigned a court without removing them."""
        if not self.waitlist:
            print("No players in the waitlist.")
            return None
        _, player = self.waitlist[0]
        print(f"Next player in line: {player}")
        return player

    def print_waitlist(self):
        """Prints the entire waitlist in order."""
        if not self.waitlist:
            print("The waitlist is empty.")
            return
        print("Current Waitlist:")
        for order, (_, player) in enumerate(sorted(self.waitlist), start=1):
            print(f"{order}. {player}")

# Example usage
if __name__ == "__main__":
    waitlist = PickleballWaitlist()
    waitlist.add_paddle("Alice")
    waitlist.add_paddle("Bob")
    waitlist.add_paddle("Charlie")
    waitlist.peek_next()
    waitlist.print_waitlist()
    waitlist.assign_court()
    waitlist.print_waitlist()

