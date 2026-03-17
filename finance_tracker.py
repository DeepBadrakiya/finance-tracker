#!/usr/bin/env python3
"""Personal Finance Tracker - Manage expenses, income, and budgets."""

import json
import os
from datetime import datetime
from pathlib import Path


class FinanceTracker:
    """A simple personal finance tracker."""
    
    def __init__(self, data_file="finances.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self):
        """Load financial data from file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {"transactions": [], "budget": {}}
    
    def save_data(self):
        """Save financial data to file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_income(self, amount, category, description=""):
        """Add income transaction."""
        transaction = {
            "type": "income",
            "amount": float(amount),
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.data["transactions"].append(transaction)
        self.save_data()
        print(f"✓ Income of ${amount} added ({category})")
    
    def add_expense(self, amount, category, description=""):
        """Add expense transaction."""
        transaction = {
            "type": "expense",
            "amount": float(amount),
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.data["transactions"].append(transaction)
        self.save_data()
        print(f"✓ Expense of ${amount} added ({category})")
    
    def set_budget(self, category, limit):
        """Set budget limit for a category."""
        self.data["budget"][category] = float(limit)
        self.save_data()
        print(f"✓ Budget set for {category}: ${limit}")
    
    def get_balance(self):
        """Calculate current balance."""
        income = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "expense")
        return income - expenses
    
    def get_summary(self):
        """Get financial summary."""
        income = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "expense")
        balance = income - expenses
        
        print("\n" + "="*50)
        print("FINANCIAL SUMMARY")
        print("="*50)
        print(f"Total Income:    ${income:.2f}")
        print(f"Total Expenses:  ${expenses:.2f}")
        print(f"Balance:         ${balance:.2f}")
        print("="*50 + "\n")
    
    def show_transactions(self, limit=10):
        """Show recent transactions."""
        print("\n" + "="*70)
        print("RECENT TRANSACTIONS")
        print("="*70)
        recent = self.data["transactions"][-limit:]
        for i, t in enumerate(reversed(recent), 1):
            symbol = "+" if t["type"] == "income" else "-"
            print(f"{i}. [{t['date']}] {symbol}${t['amount']:.2f} - {t['category']} ({t['description']})")
        print("="*70 + "\n")
    
    def category_breakdown(self):
        """Show breakdown by category."""
        expenses_by_cat = {}
        for t in self.data["transactions"]:
            if t["type"] == "expense":
                cat = t["category"]
                expenses_by_cat[cat] = expenses_by_cat.get(cat, 0) + t["amount"]
        
        print("\n" + "="*50)
        print("EXPENSE BREAKDOWN BY CATEGORY")
        print("="*50)
        for cat, amount in sorted(expenses_by_cat.items(), key=lambda x: x[1], reverse=True):
            budget = self.data["budget"].get(cat, "No limit")
            status = f" / ${budget}" if isinstance(budget, (int, float)) else ""
            print(f"{cat:20} ${amount:8.2f}{status}")
        print("="*50 + "\n")


def main():
    """Main application loop."""
    tracker = FinanceTracker()
    
    while True:
        print("\n📊 PERSONAL FINANCE TRACKER")
        print("-" * 30)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Transactions")
        print("5. Category Breakdown")
        print("6. Set Budget")
        print("7. Exit")
        print("-" * 30)
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == "1":
            amount = input("Income amount: $")
            category = input("Category (e.g., Salary, Bonus): ")
            desc = input("Description (optional): ")
            try:
                tracker.add_income(amount, category, desc)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "2":
            amount = input("Expense amount: $")
            category = input("Category (e.g., Food, Transport): ")
            desc = input("Description (optional): ")
            try:
                tracker.add_expense(amount, category, desc)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "3":
            tracker.get_summary()
        
        elif choice == "4":
            tracker.show_transactions()
        
        elif choice == "5":
            tracker.category_breakdown()
        
        elif choice == "6":
            category = input("Category to set budget for: ")
            limit = input("Budget limit: $")
            try:
                tracker.set_budget(category, limit)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "7":
            print("👋 Thank you for using Finance Tracker!")
            break
        
        else:
            print("❌ Invalid option!")


if __name__ == "__main__":
    main()
    