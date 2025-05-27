import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
import argparse

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def calculate_and_save_drawdowns(data, ticker, frequency):
    # Create nested directory structure
    base_dir = "drawdowns"
    ticker_dir = os.path.join(base_dir, ticker)
    frequency_dir = os.path.join(ticker_dir, frequency)
    ensure_directory(frequency_dir)
    
    # Resample data based on frequency
    if frequency == 'monthly':
        price_series = data['Close'].resample('ME').last()
    elif frequency == 'quarterly':
        price_series = data['Close'].resample('QE').last()
    else:  # daily
        price_series = data['Close']
    
    rolling_max = price_series.expanding().max()
    drawdown = (price_series - rolling_max) / rolling_max * 100

    # Convert datetime index to date only
    dates = price_series.index.date

    df = pd.DataFrame({
        'Date': dates,
        'Drawdown': drawdown
    })
    df.to_csv(os.path.join(frequency_dir, 'drawdown_data.csv'), index=False)

    # Create and save standard view
    plt.figure(figsize=(12, 8))
    plt.plot(dates, df['Drawdown'], 'r')
    plt.title(f'{ticker} Historical Drawdown ({frequency.capitalize()}, Standard)')
    plt.xlabel('Date')
    plt.ylabel('Drawdown %')
    plt.grid(True)
    plt.savefig(os.path.join(frequency_dir, 'drawdown_standard.png'))
    plt.close()

    # Create and save flipped view
    plt.figure(figsize=(12, 8))
    plt.plot(dates, df['Drawdown'], 'r')
    plt.title(f'{ticker} Historical Drawdown ({frequency.capitalize()}, Flipped)')
    plt.xlabel('Date')
    plt.ylabel('Drawdown %')
    plt.grid(True)
    ymin, ymax = plt.ylim()
    plt.ylim(max(0, ymax), min(ymin, -100))
    plt.savefig(os.path.join(frequency_dir, 'drawdown_flipped.png'))
    plt.close()

    return drawdown.min(), dates[drawdown.argmin()]

def process_ticker(ticker, frequencies=None):
    if frequencies is None:
        frequencies = ['daily', 'monthly', 'quarterly']
    
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="max")
        
        if len(data) == 0:
            raise Exception("No data found for this ticker")

        print(f"\nGenerating drawdown analysis for {ticker}...")
        
        results = {}
        for freq in frequencies:
            if freq not in ['daily', 'monthly', 'quarterly']:
                print(f"Warning: Skipping invalid frequency '{freq}'")
                continue
            max_dd, max_dd_date = calculate_and_save_drawdowns(data, ticker, freq)
            results[freq] = {'drawdown': max_dd, 'date': max_dd_date}

        # Print results
        print("\nResults Summary:")
        for freq in results:
            print(f"\n{freq.capitalize()} Analysis:")
            print(f"Maximum drawdown: {results[freq]['drawdown']:.2f}%")
            print(f"Date of maximum drawdown: {results[freq]['date']}")
            print(f"Files saved in: drawdowns/{ticker}/{freq}/")
            print("- drawdown_data.csv (data)")
            print("- drawdown_standard.png (standard view)")
            print("- drawdown_flipped.png (flipped view)")

    except Exception as e:
        print(f"Error processing {ticker}: {str(e)}")
        print("Please check the ticker symbol and try again.")

def main():
    parser = argparse.ArgumentParser(description='Calculate and visualize drawdowns for stock tickers')
    parser.add_argument('tickers', nargs='*', help='One or more ticker symbols (e.g., AAPL MSFT SPY)')
    parser.add_argument('-f', '--frequencies', nargs='+', choices=['daily', 'monthly', 'quarterly'],
                      help='Frequencies to analyze (default: all)')
    args = parser.parse_args()

    # If no tickers provided via command line, ask interactively
    if not args.tickers:
        ticker = input("Enter ticker symbol (e.g. AAPL, MSFT, SPY): ")
        tickers = [ticker]
    else:
        tickers = args.tickers

    # Process each ticker
    for ticker in tickers:
        process_ticker(ticker.upper(), args.frequencies)

if __name__ == "__main__":
    main() 