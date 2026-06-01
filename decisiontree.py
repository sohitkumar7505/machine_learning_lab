import pandas as pd
import math

data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

def entrophy(df):
    target = df['PlayTennis']
    total = len(target)
    value_counts = target.value_counts()
    entropy = 0
    for val in value_counts:
        p = val / total
        entropy -= p * math.log2(p)
    return entropy

def information_gain(df):
    dic = {}
    base_entropy = entrophy(df)

    for col in df.columns:
        if col == 'PlayTennis':
            continue

        weighted_entropy = 0
        for val in df[col].unique():
            df1 = df[df[col] == val]
            weighted_entropy += (len(df1) / len(df)) * entrophy(df1)

        dic[col] = base_entropy - weighted_entropy

    return dic


def decision_tree(df, depth=0):
    target = df['PlayTennis']
    if len(target.unique()) == 1:
        print("  " * depth + "→", target.iloc[0])
        return
    if len(df.columns) == 1:
        print("  " * depth + "→", target.mode()[0])
        return

    dic = information_gain(df)
    selected_column = max(dic, key=dic.get)

    print("  " * depth + selected_column)

    for val in df[selected_column].unique():
        print("  " * depth + f"{selected_column} = {val}")

        tempdf = df[df[selected_column] == val].drop(columns=[selected_column])
        decision_tree(tempdf, depth + 1)


decision_tree(df)