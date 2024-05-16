import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import random as rand
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import download

def main():
    stockList = stocksSelector()
    print(stockList)
    for stock in stockList:
        print(f"On {stock} go {"LONG" if sentiment(stock) >= 0 else "SHORT"} and has a sentiment of {sentiment(stock)}, the random choice for this stock is {"LONG" if rand.random() >= .5 else "SHORT"}")

def stocksSelector():
    keyList = list(stocks.keys())
    stockList = []
    for i in range(50):
        choice  = keyList[rand.randint(0, len(keyList)-1)]
        stockList.append(choice)
        keyList.remove(choice)
    return stockList

def fetch_news(stock_symbol):
    url = f'https://www.google.com/search?q={stock_symbol}+stock+news'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h')
    return [headline.get_text() for headline in headlines]

def analyze_sentiment(headlines):
    sentiment_scores = [sia.polarity_scores(headline)['compound'] for headline in headlines]
    return sentiment_scores

def sentiment(stock_symbol):
    headlines = fetch_news(stock_symbol)
    sentiment_scores = analyze_sentiment(headlines)
    average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    return average_sentiment


stocks = {
    "MSFT": "Microsoft Corporation",
    "AAPL": "Apple Inc",
    "NVDA": "NVIDIA Corporation",
    "GOOG": "Alphabet Inc.",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com, Inc.",
    "META": "Meta Platforms, Inc.",
    "BRK.B": "Berkshire Hathaway Inc.",
    "LLY": "Eli Lilly and Company",
    "AVGO": "Broadcom Inc.",
    "JPM": "JPMorgan Chase & Co.",
    "V": "Visa Inc.",
    "TSLA": "Tesla, Inc.",
    "XOM": "Exxon Mobil Corporation",
    "WMT": "Walmart Inc.",
    "UNH": "UnitedHealth Group Incorporated",
    "MA": "Mastercard Incorporated",
    "PG": "The Procter & Gamble Company",
    "JNJ": "Johnson & Johnson",
    "COST": "Costco Wholesale Corporation",
    "HD": "The Home Depot, Inc.",
    "MRK": "Merck & Co., Inc.",
    "ORCL": "Oracle Corporation",
    "CVX": "Chevron Corporation",
    "BAC": "Bank of America Corporation",
    "ABBV": "AbbVie Inc.",
    "KO": "The Coca-Cola Company",
    "CRM": "Salesforce, Inc.",
    "NFLX": "Netflix, Inc.",
    "PEP": "PepsiCo, Inc.",
    "AMD": "Advanced Micro Devices, Inc.",
    "TMO": "Thermo Fisher Scientific Inc.",
    "ADBE": "Adobe Inc.",
    "WFC": "Wells Fargo & Company",
    "LIN": "Linde plc",
    "QCOM": "QUALCOMM Incorporated",
    "MCD": "McDonald's Corporation",
    "CSCO": "Cisco Systems, Inc.",
    "DIS": "The Walt Disney Company",
    "ACN": "Accenture plc",
    "TMUS": "T-Mobile US, Inc.",
    "DHR": "Danaher Corporation",
    "ABT": "Abbott Laboratories",
    "INTU": "Intuit Inc.",
    "GE": "GE Aerospace",
    "CAT": "Caterpillar Inc.",
    "AXP": "American Express Company",
    "AMAT": "Applied Materials, Inc.",
    "TXN": "Texas Instruments Incorporated",
    "VZ": "Verizon Communications Inc.",
    "AMGN": "Amgen Inc.",
    "MS": "Morgan Stanley",
    "PFE": "Pfizer Inc.",
    "PM": "Philip Morris International Inc.",
    "CMCSA": "Comcast Corporation",
    "IBM": "International Business Machines Corporation",
    "NEE": "NextEra Energy, Inc.",
    "UNP": "Union Pacific Corporation",
    "NOW": "ServiceNow, Inc.",
    "BX": "Blackstone Inc.",
    "GS": "The Goldman Sachs Group, Inc.",
    "COP": "ConocoPhillips",
    "RTX": "RTX Corp",
    "NKE": "NIKE, Inc.",
    "UBER": "Uber Technologies, Inc.",
    "ISRG": "Intuitive Surgical, Inc.",
    "MU": "Micron Technology, Inc.",
    "SPGI": "S&P Global Inc.",
    "SCHW": "The Charles Schwab Corporation",
    "HON": "Honeywell International Inc.",
    "LOW": "Lowe's Companies, Inc.",
    "ETN": "Eaton Corporation plc",
    "INTC": "Intel Corporation",
    "BKNG": "Booking Holdings Inc.",
    "UPS": "United Parcel Service, Inc.",
    "PGR": "The Progressive Corporation",
    "ELV": "Elevance Health Inc.",
    "SYK": "Stryker Corporation",
    "T": "AT&T Inc.",
    "C": "Citigroup Inc.",
    "LRCX": "Lam Research Corporation",
    "BLK": "BlackRock, Inc.",
    "DE": "Deere & Company",
    "LMT": "Lockheed Martin Corporation",
    "TJX": "The TJX Companies, Inc.",
    "MDT": "Medtronic plc",
    "VRTX": "Vertex Pharmaceuticals Incorporated",
    "BA": "The Boeing Company",
    "BSX": "Boston Scientific Corporation",
    "REGN": "Regeneron Pharmaceuticals, Inc.",
    "ADI": "Analog Devices, Inc.",
    "CB": "Chubb Limited",
    "ADP": "Automatic Data Processing, Inc.",
    "MMC": "Marsh & McLennan Companies, Inc.",
    "PLD": "Prologis, Inc.",
    "CI": "Cigna Corporation",
    "PANW": "Palo Alto Networks, Inc.",
    "ANET": "Arista Networks, Inc.",
    "KLAC": "KLA Corporation",
    "MDLZ": "Mondelez International, Inc.",
    "ABNB": "Airbnb, Inc.",
    "BMY": "Bristol-Myers Squibb Company",
    "FI": "Fiserv, Inc.",
    "CMG": "Chipotle Mexican Grill, Inc.",
    "SBUX": "Starbucks Corporation",
    "SO": "The Southern Company",
    "AMT": "American Tower Corporation",
    "SNPS": "Synopsys, Inc.",
    "WM": "Waste Management, Inc.",
    "GILD": "Gilead Sciences, Inc.",
    "HCA": "HCA Healthcare, Inc.",
    "GD": "General Dynamics Corporation",
    "SHW": "The Sherwin-Williams Company",
    "DUK": "Duke Energy Corporation",
    "CL": "Colgate-Palmolive Company",
    "CDNS": "Cadence Design Systems, Inc.",
    "ZTS": "Zoetis Inc.",
    "MO": "Altria Group, Inc.",
    "APH": "Amphenol Corporation",
    "CME": "CME Group Inc.",
    "ICE": "Intercontinental Exchange, Inc.",
    "FCX": "Freeport-McMoRan Inc.",
    "ITW": "Illinois Tool Works Inc.",
    "TGT": "Target Corporation",
    "EOG": "EOG Resources, Inc.",
    "TT": "Trane Technologies plc",
    "MCO": "Moody's Corporation",
    "TDG": "TransDigm Group Incorporated",
    "MCK": "McKesson Corporation",
    "EQIX": "Equinix, Inc.",
    "PH": "Parker-Hannifin Corporation",
    "CVS": "CVS Health Corporation",
    "NOC": "Northrop Grumman Corporation",
    "CTAS": "Cintas Corporation",
    "SLB": "Schlumberger Limited",
    "BDX": "Becton, Dickinson and Company",
    "MAR": "Marriott International, Inc.",
    "NXPI": "NXP Semiconductors N.V.",
    "CEG": "Constellation Energy Corporation",
    "PYPL": "PayPal Holdings, Inc.",
    "CSX": "CSX Corporation",
    "ECL": "Ecolab Inc.",
    "EMR": "Emerson Electric Co.",
    "FDX": "FedEx Corporation",
    "USB": "U.S. Bancorp",
    "PNC": "The PNC Financial Services Group, Inc.",
    "AON": "Aon plc",
    "MPC": "Marathon Petroleum Corporation",
    "PSX": "Phillips 66",
    "MSI": "Motorola Solutions, Inc.",
    "ORLY": "O'Reilly Automotive, Inc.",
    "WELL": "Welltower Inc.",
    "RSG": "Republic Services, Inc.",
    "CARR": "Carrier Global Corporation",
    "MNST": "Monster Beverage Corporation",
    "PCAR": "PACCAR Inc",
    "APD": "Air Products and Chemicals, Inc.",
    "ROP": "Roper Technologies, Inc.",
    "OXY": "Occidental Petroleum Corporation",
    "MMM": "3M Company",
    "COF": "Capital One Financial Corporation",
    "AJG": "Arthur J. Gallagher & Co.",
    "AIG": "American International Group, Inc.",
    "CPRT": "Copart, Inc.",
    "TFC": "Truist Financial Corporation",
    "NSC": "Norfolk Southern Corporation",
    "HLT": "Hilton Worldwide Holdings Inc.",
    "MET": "MetLife, Inc.",
    "GM": "General Motors Company",
    "EW": "Edwards Lifesciences Corporation",
    "VLO": "Valero Energy Corporation",
    "AZO": "AutoZone, Inc.",
    "MCHP": "Microchip Technology Incorporated",
    "DXCM": "DexCom, Inc.",
    "TRV": "The Travelers Companies, Inc.",
    "AFL": "Aflac Incorporated",
    "HES": "Hess Corporation",
    "DHI": "D.R. Horton, Inc.",
    "SRE": "Sempra",
    "NEM": "Newmont Corporation",
    "PSA": "Public Storage",
    "WMB": "The Williams Companies, Inc.",
    "F": "Ford Motor Company",
    "AEP": "American Electric Power Company, Inc.",
    "O": "Realty Income Corporation",
    "SPG": "Simon Property Group, Inc.",
    "EL": "The Estée Lauder Companies Inc.",
    "STZ": "Constellation Brands, Inc.",
    "OKE": "ONEOK, Inc.",
    "MRNA": "Moderna, Inc.",
    "ADSK": "Autodesk, Inc.",
    "URI": "United Rentals, Inc.",
    "GWW": "W.W. Grainger, Inc.",
    "SMCI": "Super Micro Computer, Inc.",
    "KDP": "Keurig Dr Pepper Inc.",
    "KMB": "Kimberly-Clark Corporation",
    "FTNT": "Fortinet, Inc.",
    "ALL": "The Allstate Corporation",
    "GEV": "GE Vernova Inc.",
    "TEL": "TE Connectivity Ltd.",
    "ROST": "Ross Stores, Inc.",
    "LEN": "Lennar Corporation",
    "COR": "Cencora",
    "PAYX": "Paychex, Inc.",
    "JCI": "Johnson Controls International plc",
    "AMP": "Ameriprise Financial, Inc.",
    "DLR": "Digital Realty Trust, Inc.",
    "KHC": "The Kraft Heinz Company",
    "D": "Dominion Energy, Inc.",
    "BK": "The Bank of New York Mellon Corporation",
    "A": "Agilent Technologies, Inc.",
    "CCI": "Crown Castle Inc.",
    "HSY": "The Hershey Company",
    "PRU": "Prudential Financial, Inc.",
    "KMI": "Kinder Morgan, Inc.",
    "IQV": "IQVIA Holdings Inc.",
    "LULU": "Lululemon Athletica Inc.",
    "FIS": "Fidelity National Information Services, Inc.",
    "LHX": "L3Harris Technologies, Inc.",
    "DOW": "Dow Inc.",
    "IDXX": "IDEXX Laboratories, Inc.",
    "NUE": "Nucor Corporation",
    "CNC": "Centene Corporation",
    "HUM": "Humana Inc.",
    "CMI": "Cummins Inc.",
    "CTVA": "Corteva, Inc.",
    "KR": "The Kroger Co.",
    "CHTR": "Charter Communications, Inc.",
    "ODFL": "Old Dominion Freight Line, Inc.",
    "GIS": "General Mills, Inc.",
    "AME": "AMETEK, Inc.",
    "PWR": "Quanta Services, Inc.",
    "KVUE": "Kenvue Inc.",
    "OTIS": "Otis Worldwide Corporation",
    "YUM": "Yum! Brands, Inc.",
    "FAST": "Fastenal Company",
    "MSCI": "MSCI Inc.",
    "PCG": "PG&E Corporation",
    "EXC": "Exelon Corporation",
    "SYY": "Sysco Corporation",
    "MLM": "Martin Marietta Materials, Inc.",
    "GEHC": "GE HealthCare Technologies Inc.",
    "ACGL": "Arch Capital Group Ltd.",
    "PEG": "Public Service Enterprise Group Incorporated",
    "CSGP": "CoStar Group, Inc.",
    "IR": "Ingersoll Rand Inc.",
    "RCL": "Royal Caribbean Cruises Ltd.",
    "FANG": "Diamondback Energy, Inc.",
    "VMC": "Vulcan Materials Company",
    "VRSK": "Verisk Analytics, Inc.",
    "NDAQ": "Nasdaq, Inc.",
    "LVS": "Las Vegas Sands Corp.",
    "DAL": "Delta Air Lines, Inc.",
    "MPWR": "Monolithic Power Systems, Inc.",
    "XYL": "Xylem Inc.",
    "IT": "Gartner, Inc.",
    "EA": "Electronic Arts Inc.",
    "CTSH": "Cognizant Technology Solutions Corporation",
    "ED": "Consolidated Edison, Inc.",
    "LYB": "LyondellBasell Industries N.V.",
    "FICO": "Fair Isaac Corporation",
    "DD": "DuPont de Nemours, Inc.",
    "HAL": "Halliburton Company",
    "HWM": "Howmet Aerospace Inc.",
    "BIIB": "Biogen Inc.",
    "GRMN": "Garmin Ltd.",
    "VST": "Vistra Corp.",
    "BKR": "Baker Hughes Company",
    "RMD": "ResMed Inc.",
    "PPG": "PPG Industries, Inc.",
    "MTD": "Mettler-Toledo International Inc.",
    "DVN": "Devon Energy Corporation",
    "ADM": "Archer-Daniels-Midland Company",
    "ON": "ON Semiconductor Corporation",
    "DFS": "Discover Financial Services",
    "EXR": "Extra Space Storage Inc.",
    "XEL": "Xcel Energy Inc.",
    "DG": "Dollar General Corporation",
    "ROK": "Rockwell Automation, Inc.",
    "VICI": "VICI Properties Inc.",
    "EFX": "Equifax Inc.",
    "HIG": "The Hartford Financial Services Group, Inc.",
    "CDW": "CDW Corporation",
    "HPQ": "HP Inc.",
    "WAB": "Westinghouse Air Brake Technologies Corporation",
    "GLW": "Corning Incorporated",
    "TSCO": "Tractor Supply Company",
    "ANSS": "ANSYS, Inc.",
    "EIX": "Edison International",
    "GPN": "Global Payments Inc.",
    "AVB": "AvalonBay Communities, Inc.",
    "CBRE": "CBRE Group, Inc.",
    "FTV": "Fortive Corporation",
    "WEC": "WEC Energy Group, Inc.",
    "DLTR": "Dollar Tree, Inc.",
    "FITB": "Fifth Third Bancorp",
    "KEYS": "Keysight Technologies, Inc.",
    "WST": "West Pharmaceutical Services, Inc.",
    "EBAY": "eBay Inc.",
    "AWK": "American Water Works Company, Inc.",
    "CHD": "Church & Dwight Co., Inc.",
    "WTW": "Willis Towers Watson PLC",
    "RJF": "Raymond James Financial, Inc.",
    "MTB": "M&T Bank Corporation",
    "DOV": "Dover Corporation",
    "EQR": "Equity Residential",
    "TROW": "T. Rowe Price Group, Inc.",
    "TRGP": "Targa Resources Corp.",
    "BRO": "Brown & Brown, Inc.",
    "ZBH": "Zimmer Biomet Holdings, Inc.",
    "IFF": "International Flavors & Fragrances Inc.",
    "PHM": "PulteGroup, Inc.",
    "TTWO": "Take-Two Interactive Software, Inc.",
    "NVR": "NVR, Inc.",
    "CAH": "Cardinal Health, Inc.",
    "DTE": "DTE Energy Company",
    "ETR": "Entergy Corporation",
    "VLTO": "Veralto Corporation",
    "BR": "Broadridge Financial Solutions, Inc.",
    "BF.B": "Brown-Forman Corporation",
    "IRM": "Iron Mountain Incorporated",
    "WDC": "Western Digital Corporation",
    "STT": "State Street Corporation",
    "FE": "FirstEnergy Corp.",
    "AXON": "Axon Enterprise, Inc.",
    "STE": "STERIS plc",
    "WY": "Weyerhaeuser Company",
    "APTV": "Aptiv PLC",
    "ROL": "Rollins, Inc.",
    "HPE": "Hewlett Packard Enterprise Company",
    "NTAP": "NetApp, Inc.",
    "LYV": "Live Nation Entertainment, Inc.",
    "GPC": "Genuine Parts Company",
    "DECK": "Deckers Outdoor Corporation",
    "ES": "Eversource Energy",
    "HUBB": "Hubbell Incorporated",
    "PPL": "PPL Corporation",
    "PTC": "PTC Inc.",
    "BALL": "Ball Corporation",
    "STLD": "Steel Dynamics, Inc.",
    "INVH": "Invitation Homes Inc.",
    "K": "Kellanova Co",
    "SBAC": "SBA Communications Corporation",
    "ARE": "Alexandria Real Estate Equities, Inc.",
    "TSN": "Tyson Foods, Inc.",
    "CPAY": "Corpay, Inc.",
    "CTRA": "Coterra Energy Inc.",
    "WAT": "Waters Corporation",
    "WBD": "Warner Bros. Discovery, Inc.",
    "MOH": "Molina Healthcare, Inc.",
    "BLDR": "Builders FirstSource, Inc.",
    "TYL": "Tyler Technologies, Inc.",
    "ALGN": "Align Technology, Inc.",
    "FSLR": "First Solar, Inc.",
    "MKC": "McCormick & Company, Incorporated",
    "HBAN": "Huntington Bancshares Incorporated",
    "WRB": "W. R. Berkley Corporation",
    "LDOS": "Leidos Holdings, Inc.",
    "AEE": "Ameren Corporation",
    "PFG": "Principal Financial Group, Inc.",
    "STX": "Seagate Technology Holdings plc",
    "HRL": "Hormel Foods Corporation",
    "TER": "Teradyne, Inc.",
    "ULTA": "Ulta Beauty, Inc.",
    "CBOE": "Cboe Global Markets, Inc.",
    "VTR": "Ventas, Inc.",
    "CNP": "CenterPoint Energy, Inc.",
    "OMC": "Omnicom Group Inc.",
    "CMS": "CMS Energy Corporation",
    "CINF": "Cincinnati Financial Corporation",
    "TDY": "Teledyne Technologies Incorporated",
    "COO": "The Cooper Companies, Inc.",
    "CCL": "Carnival Corporation & plc",
    "SYF": "Synchrony Financial",
    "RF": "Regions Financial Corporation",
    "AVY": "Avery Dennison Corporation",
    "BAX": "Baxter International Inc.",
    "DPZ": "Domino's Pizza, Inc.",
    "ILMN": "Illumina, Inc.",
    "UAL": "United Airlines Holdings, Inc.",
    "LH": "Laboratory Corporation of America Holdings",
    "CE": "Celanese Corporation",
    "DRI": "Darden Restaurants, Inc.",
    "ATO": "Atmos Energy Corporation",
    "HOLX": "Hologic, Inc.",
    "NTRS": "Northern Trust Corporation",
    "CLX": "The Clorox Company",
    "JBHT": "J.B. Hunt Transport Services, Inc.",
    "EQT": "EQT Corporation",
    "J": "Jacobs Engineering Group Inc.",
    "NRG": "NRG Energy, Inc.",
    "L": "Loews Corporation",
    "IEX": "IDEX Corporation",
    "VRSN": "VeriSign, Inc.",
    "TXT": "Textron Inc.",
    "LUV": "Southwest Airlines Co.",
    "FDS": "FactSet Research Systems Inc.",
    "EG": "Everest Group, Ltd.",
    "EXPD": "Expeditors International of Washington, Inc.",
    "ESS": "Essex Property Trust, Inc.",
    "CFG": "Citizens Financial Group, Inc.",
    "ZBRA": "Zebra Technologies Corporation",
    "BBY": "Best Buy Co., Inc.",
    "PKG": "Packaging Corporation of America",
    "MAA": "Mid-America Apartment Communities, Inc.",
    "NDSN": "Nordson Corporation",
    "MAS": "Masco Corporation",
    "ALB": "Albemarle Corporation",
    "DGX": "Quest Diagnostics Incorporated",
    "WBA": "Walgreens Boots Alliance, Inc.",
    "FOXA": "Fox Corporation",
    "FOX": "Fox Corporation",
    "ENPH": "Enphase Energy, Inc.",
    "GEN": "Gen Digital Inc.",
    "AMCR": "Amcor plc",
    "BG": "Bunge Limited",
    "SWKS": "Skyworks Solutions, Inc.",
    "MRO": "Marathon Oil Corporation",
    "SNA": "Snap-on Incorporated",
    "CAG": "Conagra Brands, Inc.",
    "NWSA": "News Corporation",
    "NWS": "News Corporation",
    "POOL": "Pool Corporation",
    "EXPE": "Expedia Group, Inc.",
    "AES": "The AES Corporation",
    "AKAM": "Akamai Technologies, Inc.",
    "KEY": "KeyCorp",
    "JBL": "Jabil Inc.",
    "TRMB": "Trimble Inc.",
    "SWK": "Stanley Black & Decker, Inc.",
    "DOC": "Healthpeak Properties, Inc.",
    "PNR": "Pentair plc",
    "CPB": "Campbell Soup Company",
    "CF": "CF Industries Holdings, Inc.",
    "IP": "International Paper Company",
    "VTRS": "Viatris Inc.",
    "WRK": "WestRock Company",
    "LNT": "Alliant Energy Corporation",
    "RVTY": "Revvity, Inc.",
    "HST": "Host Hotels & Resorts, Inc.",
    "TECH": "Bio-Techne Corporation",
    "NI": "NiSource Inc.",
    "UDR": "UDR, Inc.",
    "INCY": "Incyte Corporation",
    "MGM": "MGM Resorts International",
    "KIM": "Kimco Realty Corporation",
    "EVRG": "Evergy, Inc.",
    "AOS": "A. O. Smith Corporation",
    "BEN": "Franklin Resources, Inc.",
    "TAP": "Molson Coors Beverage Company",
    "SJM": "The J. M. Smucker Company",
    "LW": "Lamb Weston Holdings, Inc.",
    "JKHY": "Jack Henry & Associates, Inc.",
    "DVA": "DaVita Inc.",
    "LKQ": "LKQ Corporation",
    "EMN": "Eastman Chemical Company",
    "IPG": "The Interpublic Group of Companies, Inc.",
    "KMX": "CarMax, Inc.",
    "CRL": "Charles River Laboratories International, Inc.",
    "PODD": "Insulet Corporation",
    "CPT": "Camden Property Trust",
    "JNPR": "Juniper Networks, Inc.",
    "APA": "APA Corporation",
    "REG": "Regency Centers Corporation",
    "EPAM": "EPAM Systems, Inc.",
    "ALLE": "Allegion plc",
    "WYNN": "Wynn Resorts, Limited",
    "SOLV": "Solventum Corporation",
    "RL": "Ralph Lauren Corporation",
    "BBWI": "Bath & Body Works, Inc.",
    "UHS": "Universal Health Services, Inc.",
    "PAYC": "Paycom Software, Inc.",
    "FFIV": "F5, Inc.",
    "CTLT": "Catalent, Inc.",
    "HII": "Huntington Ingalls Industries, Inc.",
    "CHRW": "C.H. Robinson Worldwide, Inc.",
    "AAL": "American Airlines Group Inc.",
    "BXP": "Boston Properties, Inc.",
    "TFX": "Teleflex Incorporated",
    "DAY": "Dayforce Inc",
    "MOS": "The Mosaic Company",
    "QRVO": "Qorvo, Inc.",
    "HSIC": "Henry Schein, Inc.",
    "TPR": "Tapestry, Inc.",
    "AIZ": "Assurant, Inc.",
    "PARA": "Paramount Global",
    "PNW": "Pinnacle West Capital Corporation",
    "BWA": "BorgWarner Inc.",
    "GNRC": "Generac Holdings Inc.",
    "FRT": "Federal Realty Investment Trust",
    "HAS": "Hasbro, Inc.",
    "FMC": "FMC Corporation",
    "MTCH": "Match Group, Inc.",
    "BIO": "Bio-Rad Laboratories, Inc.",
    "GL": "Globe Life Inc.",
    "MKTX": "MarketAxess Holdings Inc.",
    "CZR": "Caesars Entertainment, Inc.",
    "MHK": "Mohawk Industries, Inc.",
    "RHI": "Robert Half International Inc.",
    "ETSY": "Etsy, Inc.",
    "CMA": "Comerica Incorporated",
    "IVZ": "Invesco Ltd.",
    "NCLH": "Norwegian Cruise Line Holdings Ltd."
}

download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
main()