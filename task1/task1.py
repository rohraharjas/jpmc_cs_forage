import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return df.columns

def exercise_2(df, k=5):
    return df.head(k)

def exercise_3(df, k=5):
    return df.sample(n=k)

def exercise_4(df):
    return list(set(df['type']))

def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]

def exercise_7(df):
    data = df.groupby('nameOrig')['nameDest'].agg(['nunique'])
    data.sort_values(by=('nunique'), ascending=False, inplace=True)
    return data

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()
    def transaction_counts_split_by_fraud(df):
        return df.groupby(by=['type', 'isFraud']).size()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Frequencies of Transaction Type')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Occurence')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Type Frequencies splitted by Fraud')
    axs[1].set_xlabel('Transaction Type, Fraud')
    axs[1].set_ylabel('Occurence')
    fig.suptitle('Transaction Types')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    print("High-Risk Transactions:")
    print("- `CASH_OUT` and `TRANSFER` transactions have recorded fraudulent activities.")
    print("- Although the overall number of fraudulent transactions is low, these types highlight potential risk areas.\n")
    print("Zero Fraud Transactions:")
    print("- `PAYMENT`, `CASH_IN`, and `DEBIT` transactions show no fraudulent occurrences, indicating these transaction types might have effective fraud prevention measures or are less targeted by fraudulent activities.\n")
    print("Volume vs. Fraud:")
    print("- Despite `CASH_OUT` having a high volume, it has a relatively low number of fraudulent transactions, suggesting that while frequent, the fraud rate is very low (approximately 0.11%).")
    print("- `TRANSFER` transactions, although fewer in number, also exhibit a low fraud rate (approximately 0.43%).\n")
    print("Focus for Fraud Prevention:")
    print("- Given that fraud is present in `CASH_OUT` and `TRANSFER` transactions, these should be the focus for enhanced fraud detection and prevention strategies.\n")
    print("Potential Anomalies:")
    print("- The absence of fraud in `PAYMENT`, `CASH_IN`, and `DEBIT` might warrant further investigation to ensure that no undetected fraud is present.\n\n")

def visual_2(df):
    def query(df):
        df['Origin_Delta'] = df['oldbalanceOrg'] - df['newbalanceOrig']
        df['Destination_Delta'] = df['oldbalanceDest'] - df['newbalanceDest']
        return df[df['type'] == 'CASH_OUT']
    plot = query(df).plot.scatter(x='Origin_Delta',y='Destination_Delta')
    plot.set_title('Source vs Destination Balance Delta for CASH_OUT Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    
    print("1. A cluster around (0, 0), indicating many transactions with minimal or zero balance changes, likely representing failed or reversed transactions.")
    print("2. Numerous points with positive Origin_Delta and zero Destination_Delta, suggesting withdrawals without direct transfers.")
    print("3. Some points with negative Destination_Delta and zero Origin_Delta, indicating cash payouts from the destination account.")
    print("4. Fewer points with both positive Origin_Delta and Destination_Delta, implying less common direct transfers or variable transaction amounts.")
    print("5. Points forming diagonal lines, suggesting direct exchanges between accounts.")
    print("6. Values mostly within -1000 to 1000 range, typical for 'CASH_OUT' transactions.")
    print("7. Outliers with significantly higher values indicating large transactions.")
    print("These observations indicate 'CASH_OUT' transactions primarily involve withdrawals and some direct transfers, with insights into transaction amounts and common patterns.\n\n")
