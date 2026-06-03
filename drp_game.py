import time
import random

class DRPGame:
    def __init__(self):
        self.turn = 1
        self.inventory = 100
        self.customer_satisfaction = 80
        self.ai_optimized = False
        self.raw_data = "MESSY_DATA_COLUMNS_UNCLEANED_09123"
        self.demand_forecast = 0
        self.supplier_lead_time = 5 # days
        self.hidden_insights = []

    def clear_screen(self):
        print("\n" * 50)

    def display_status(self):
        print(f"--- TURN {self.turn} ---")
        print(f"Inventory: {self.inventory} units")
        print(f"Customer Satisfaction: {self.customer_satisfaction}%")
        print(f"Data Status: {'[STRUCTURED]' if self.ai_optimized else '[MESSY]'}")
        if self.ai_optimized:
            print(f"Real-time Demand Analysis: {self.demand_forecast} units/turn")
        print("-" * 20)

    def process_data_with_ai(self):
        print("\n[AI] Organizing data and structuring columns...")
        time.sleep(1)
        self.ai_optimized = True
        print("[AI] Data processed. You are now providing value as an engineer instead of wasting time on formatting.")

    def play_turn(self):
        self.clear_screen()
        self.display_status()

        if not self.ai_optimized:
            print("1. Use AI to structure and organize data")
            print("Q. Quit")
        else:
            print("1. Analyze real-time demand & find 'Hidden Sales'")
            print("2. Reinforce Supplier Agreements (Maintain Lead Time)")
            print("3. Ship to Customers (Provide Added Value)")
            print("Q. Quit")

        choice = input("\nChoose action: ").strip().lower()

        if choice == 'q':
            return False

        if not self.ai_optimized:
            if choice == '1':
                self.process_data_with_ai()
            else:
                print("Invalid choice.")
        else:
            if choice == '1':
                self.analyze_demand()
            elif choice == '2':
                self.reinforce_suppliers()
            elif choice == '3':
                self.ship_to_customers()
            else:
                print("Invalid choice.")

        input("\nPress Enter to continue...")
        self.turn += 1
        return True

    def analyze_demand(self):
        print("\n[AI] Scanning market trends and search data...")
        time.sleep(1)
        self.demand_forecast = random.randint(10, 50)

        # Hidden Sales Prediction
        if random.random() > 0.6:
            hidden_sales = random.randint(20, 40)
            print(f"!!! [INSIGHT] AI discovered hidden sales! Predicted surge of +{hidden_sales} units.")
            self.demand_forecast += hidden_sales
        else:
            print(f"[AI] Demand prediction stabilized at {self.demand_forecast} units.")

    def reinforce_suppliers(self):
        print("\n[AI] Reviewing supplier performance...")
        time.sleep(1)
        if self.supplier_lead_time > 2:
            self.supplier_lead_time -= 1
            print(f"[AI] Agreements reinforced. Lead time reduced to {self.supplier_lead_time} turns.")
        else:
            print("[AI] Lead time is already optimized to the maximum.")

        # Maintain Lead Time
        print("[AI] Supplier coordination active. Lead time stabilized.")

    def ship_to_customers(self):
        if self.demand_forecast == 0:
            print("\n[ERROR] You need to analyze demand before shipping!")
            return

        print(f"\n[ENGINEER] Fulfilling orders (Target: {self.demand_forecast})...")

        shipped = min(self.inventory, self.demand_forecast)
        self.inventory -= shipped

        if shipped >= self.demand_forecast:
            print(f"[VALUE] All customers satisfied! Shipped {shipped} units.")
            self.customer_satisfaction = min(100, self.customer_satisfaction + 5)
        else:
            backlog = self.demand_forecast - shipped
            print(f"[VALUE] Stockout! Could not fulfill {backlog} units.")
            self.customer_satisfaction = max(0, self.customer_satisfaction - 10)

        # Supplier refill based on lead time
        print(f"[INFO] New shipment arriving in {self.supplier_lead_time} turns.")
        # Simplified restocking for simulation (could be improved further, but for now just acknowledging lead time)
        self.inventory += 30
        self.demand_forecast = 0 # Reset for next turn

def main():
    game = DRPGame()
    print("Welcome to DRP AI: The Supply Chain Frontier")
    print("Evolutionizing DRP with Intelligence.")
    input("Press Enter to Start...")

    running = True
    while running:
        running = game.play_turn()

if __name__ == "__main__":
    main()
