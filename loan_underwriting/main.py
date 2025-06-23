#!/usr/bin/env python3
"""
Main entry point for the Loan Underwriting Agent application.

This script allows you to run the application in different modes:
- part1: Query Understanding
- part2: Basic Tools  
- part3: Memory

Usage:
    python main.py [mode]
    
Examples:
    python main.py part1
    python main.py part2
    python main.py part3
"""

import sys
import argparse
from app import create_demo

def main():
    """Main function to run the application."""
    parser = argparse.ArgumentParser(description="Loan Underwriting Agent Application")
    parser.add_argument(
        "mode", 
        nargs="?", 
        default="part1",
        choices=["part1", "part2", "part3"],
        help="Mode to run the application in (default: part1)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=7860,
        help="Port to run the application on (default: 7860)"
    )
    parser.add_argument(
        "--host", 
        default="0.0.0.0",
        help="Host to run the application on (default: 0.0.0.0)"
    )
    
    args = parser.parse_args()
    
    print(f"Starting Loan Underwriting Agent in {args.mode} mode...")
    print(f"Access the application at: http://localhost:{args.port}")
    
    # Create and launch the demo
    demo = create_demo(args.mode)
    demo.launch(
        server_name=args.host,
        server_port=args.port,
        share=False,
        show_error=True
    )

if __name__ == "__main__":
    main() 