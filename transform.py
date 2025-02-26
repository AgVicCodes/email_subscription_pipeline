from staging import df

df["first_name"] = df['first_name'].str.lower()
df["last_name"] = df['last_name'].str.lower()
df["email"] = df['email'].str.lower()

print(df.head())