# Stock Drawdown Analysis Tool

A Python tool for analyzing and visualizing historical drawdowns of stocks and indices. The tool calculates maximum drawdowns across different time frequencies (daily, monthly, quarterly) and generates both standard and flipped visualizations.

## Beginner's Installation Guide

### For macOS Users

1. **Install Python**:
   - Visit the official Python website: https://www.python.org/downloads/
   - Click the big yellow "Download Python" button
   - Open the downloaded file (it will be named something like "python-3.x.x-macos.pkg")
   - Follow the installation wizard, clicking "Continue" and "Install"

2. **Open Terminal**:
   - Press `Command (⌘) + Space` to open Spotlight Search
   - Type "Terminal" and press Enter
   - You'll see a black or white window with text - this is your Terminal

3. **Download this tool**:
   - Copy and paste this command into Terminal and press Enter:
     ```bash
     git clone https://github.com/finnjclancy/drawdowns.git
     ```
   - Then enter this command:
     ```bash
     cd drawdowns
     ```

4. **Install required packages**:
   - Copy and paste this command and press Enter:
     ```bash
     pip install -r requirements.txt
     ```
   - Wait for the installation to complete

### For Windows Users

1. **Install Python**:
   - Visit https://www.python.org/downloads/
   - Click the big yellow "Download Python" button
   - Open the downloaded file (named like "python-3.x.x-amd64.exe")
   - **IMPORTANT**: Check the box that says "Add Python to PATH" before clicking Install
   - Click "Install Now"

2. **Open Command Prompt**:
   - Press `Windows key + R`
   - Type "cmd" and press Enter
   - You'll see a black window with text - this is your Command Prompt

3. **Download this tool**:
   - First, install Git:
     - Visit https://git-scm.com/download/win
     - Download and run the installer (use all default options)
   - In Command Prompt, copy and paste:
     ```bash
     git clone https://github.com/finnjclancy/drawdowns.git
     ```
   - Then type:
     ```bash
     cd drawdowns
     ```

4. **Install required packages**:
   - Copy and paste this command:
     ```bash
     pip install -r requirements.txt
     ```
   - Wait for the installation to complete

## How to Use the Tool

### Basic Usage (For Beginners)

1. **Start the program**:
   - If you're on macOS (in Terminal) or Windows (in Command Prompt), type:
     ```bash
     python drawdown.py
     ```
   - Press Enter

2. **Enter a stock symbol**:
   - Type a stock symbol when asked (for example: AAPL for Apple, MSFT for Microsoft, GOOGL for Google)
   - Press Enter
   - The program will create files in a new 'drawdowns' folder

3. **Find your results**:
   - Look for a new folder called 'drawdowns' in your File Explorer/Finder
   - Inside, you'll find folders named after the stocks you analyzed
   - Each stock folder contains:
     - Daily analysis
     - Monthly analysis
     - Quarterly analysis
   - Each analysis includes:
     - A CSV file (can be opened in Excel)
     - Two PNG image files showing the drawdown graphs

### Advanced Usage

Once you're comfortable with the basic usage, you can try these advanced commands:

1. Analyze a single stock directly:
```bash
python drawdown.py AAPL
```

2. Analyze multiple stocks at once:
```bash
python drawdown.py AAPL MSFT SPY
```

3. Choose specific time periods:
```bash
python drawdown.py AAPL -f daily monthly
```

## Common Stock Symbols

- Apple: AAPL
- Microsoft: MSFT
- Google: GOOGL
- Amazon: AMZN
- S&P 500 Index: ^GSPC
- Tesla: TSLA
- Netflix: NFLX

## Troubleshooting

### Common Issues and Solutions

1. **"Python not found" error**:
   - macOS: Reinstall Python from python.org
   - Windows: Make sure you checked "Add Python to PATH" during installation

2. **"Git not found" error**:
   - macOS: Install Git using the instructions at https://git-scm.com/download/mac
   - Windows: Install Git using the instructions at https://git-scm.com/download/win

3. **"No module named..." error**:
   - Run this command again:
     ```bash
     pip install -r requirements.txt
     ```

4. **"Invalid ticker symbol" error**:
   - Make sure you're using the correct stock symbol
   - Try using the common symbols listed above

Need more help? Feel free to open an issue on GitHub!

## Dependencies

- yfinance: Gets stock market data
- pandas: Handles data processing
- matplotlib: Creates the graphs
- Python 3.x: The programming language used

## Notes

- Data comes from Yahoo Finance
- Different stocks have different amounts of historical data available
- Some special symbols need specific formatting (like ^GSPC for the S&P 500)

