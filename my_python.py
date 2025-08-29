#!/usr/bin/env python3
"""
Simple Python program example
"""

def main():
    print("🚀 Starting Python Program!")
    print(f"Python version: 3.x")
    
    # Get user input
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # Simple calculation
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers!")
    
    print("✅ Program completed successfully!")

if __name__ == "__main__":
    main()
