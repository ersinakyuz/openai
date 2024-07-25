#!/usr/bin/python3
import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    max_retries=0
)

def is_stock_related(user_input):

    stock_keywords = [
        # Turkish Keywords
        "borsa", "hisse", "şirket", "yatırım", "piyasa", "endeks", "fon", "portföy",
        "ticaret", "alım-satım", "iskonto", "kâr", "zarar", "karar alma", "tahvil",
        "bono", "sermaye", "risk", "volatilite", "analiz", "grafik", "yatırımcı",
        "vadeli işlem", "opsiyon", "dividant", "ekonomi", "makroekonomi", "mikroekonomi",
        "finansal rapor", "hisse senedi",
        
        # English Keywords
        "stock exchange", "stock", "company", "investment", "market", "index", "fund",
        "portfolio", "trading", "buy-sell", "discount", "profit", "loss", "decision making",
        "bond", "treasury bill", "capital", "risk", "volatility", "analysis", "chart",
        "investor", "futures", "options", "dividend", "economy", "macroeconomics",
        "microeconomics", "financial report", "stock share",

        # Company Names Simplified
        "Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms", "Tesla",
        "PayPal", "Intel", "Cisco Systems", "Netflix", "Adobe", "Broadcom", "Salesforce",
        "Advanced Micro Devices", "Qualcomm", "Costco Wholesale", "PepsiCo", "Starbucks",
        "T-Mobile US", "ServiceNow", "Autodesk", "Zoom Video Communications", "Okta",
        "Atlassian", "Electronic Arts", "Symantec", "Illumina", "DocuSign", "Shopify",
        "MongoDB", "CrowdStrike", "Snowflake", "Roku", "Palantir Technologies", "Splunk",
        "Marvell Technology", "RingCentral", "Wix", "Datadog", "Veeva Systems", "Five Below",
        "Fastly", "Elastic", "Twilio", "Beyond Meat", "HubSpot", "Squarespace", "F5 Networks",
        
        # NASDAQ Big Stocks
        "aapl", "msft", "googl", "goog", "amzn", "nvda", "meta", "tsla", "pypl",
        "intc", "csco", "nflx", "adbe", "avgo", "crm", "amd", "qcom", "cost",
        "pep", "sbux", "tmus", "now", "adsk", "zm", "okta", "team", "ea",
        "symc", "ilmn", "docu", "shop", "mdb", "crwd", "snow", "roku", "pltr",
        "splk", "mrvl", "rng", "wix", "ddog", "veeva", "five", "fsly", "estc",
        "twlo", "bynd", "hubs", "sqsp", "ffiv"
    ]
    return any(keyword.lower() in user_input.lower() for keyword in stock_keywords)


@app.route('/process', methods=['POST'])

def process():

    data = request.json
    user_input = data.get('user_input')
    print(user_input)
    is_only_stock_queries = True #if is_stock_related(user_input)
    # This option is reserved

    if is_only_stock_queries:

        # Call the OpenAI API
        response = client.with_options(max_retries=2).chat.completions.create(
        messages=[
            {
            "role": "user", "content": user_input
            }
        ],
        model="gpt-4o-mini",
        stream = False
        )

        answer = response.choices[0].message.content
        print(answer)
        return jsonify({'result': answer})
    else:
        return jsonify({'result': 'Sorry, I can only answer questions about the stock market..'})

if __name__ == '__main__':
    app.run(debug=True)

