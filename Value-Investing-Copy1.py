
# coding: utf-8

# Programm zur Value-Investing Bewertung
# 
# pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, parse_cols=None, usecols=None, squeeze=False, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skip_footer=0, skipfooter=0, convert_float=True, mangle_dupe_cols=True, **kwds)

# In[2]:


#Input sind Gewinn, Umsatz, Kassenbestand, Multiplikator von 12,5 Anzahl frei im Umlauf befindlicher Aktien


# In[41]:


import pandas as pd
df = pd.read_excel('Daten-Value-Bewertung.xlsx', sheet_name=2)


# In[42]:


df


# In[43]:


jahr = df["Jahr"]
gewinn = df["Gewinn"]
umsatz = df["Umsatz"]
aktien = df["Aktien"]
kasse = df["Kasse"]


# In[44]:


#m ist der Multiplikator
m = gewinn/umsatz
print(m)


# In[45]:


#.mean Function errechnet den Durchschnitt des m Dataframes
m.mean()


# In[47]:


M = 12.5
G = m.mean()*umsatz[9]
V = M*G
V_kas = V+kasse[9]
V_aktie = V_kas/aktien[9]
V_aktie_50 = V_aktie*0.5
V_aktie_40 = V_aktie*0.6
V_aktie_30 = V_aktie*0.7
V_aktie_20 = V_aktie*0.8
print(V_aktie)
print(V_aktie_20)
print(V_aktie_30)
print(V_aktie_40)
print(V_aktie_50)


# BMW

# In[48]:


df1 = pd.read_excel('Daten-Value-Bewertung.xlsx', sheet_name=1)
df1


# In[49]:


jahr1 = df1["Jahr"]
gewinn1 = df1["Gewinn"]
umsatz1 = df1["Umsatz"]
aktien1 = df1["Aktien"]
kasse1 = df1["Kasse"]


# In[51]:


m1 = gewinn1/umsatz1
m1


# In[53]:


M = 12.5
G1 = m1.mean()*umsatz1[9]
V1 = M*G1
V_kas1 = V+kasse1[9]
V_aktie1 = V_kas1/aktien1[9]
V_aktie1_50 = V_aktie1*0.5
V_aktie1_40 = V_aktie1*0.6
V_aktie1_30 = V_aktie1*0.7
V_aktie1_20 = V_aktie1*0.8
print(V_aktie1)
print(V_aktie1_20)
print(V_aktie1_30)
print(V_aktie1_40)
print(V_aktie1_50)


# Deutz AG

# In[55]:


df2 = pd.read_excel('Daten-Value-Bewertung.xlsx', sheet_name=0)
df2
jahr2 = df2["Jahr"]
gewinn2 = df2["Gewinn"]
umsatz2 = df2["Umsatz"]
aktien2 = df2["Aktien"]
kasse2 = df2["Kasse"]
m2 = gewinn2/umsatz2
print(m2)
m2.mean()
G2 = m2.mean()*umsatz2[9]
V2 = M*G2
V_kas2 = V+kasse2[9]
V_aktie2 = V_kas2/aktien2[9]
V_aktie2_50 = V_aktie2*0.5
V_aktie2_40 = V_aktie2*0.6
V_aktie2_30 = V_aktie2*0.7
V_aktie2_20 = V_aktie2*0.8
print(V_aktie2)
print(V_aktie2_20)
print(V_aktie2_30)
print(V_aktie2_40)
print(V_aktie2_50)


# In[28]:


print(m2.mean())


# In[27]:


df2

