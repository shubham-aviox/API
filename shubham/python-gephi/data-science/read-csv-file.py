import pandas as pd

df = pd.read_csv('legal_data_2022-05-12.csv')

# remove_special_chr_list = []
# for i in df['advogados_reclamado']:
# 	remove_special_chr_list.append(i.replace('[','').replace(']','').replace("'",""))

# new_df = pd.DataFrame({'advogados_reclamado': remove_special_chr_list})
# new_df.to_csv('new_data.csv')

# data = df['advogados_reclamado'].replace("'[^A-Za-z0-9,\s']+", "", regex=True)
# data.to_csv('data.csv')
# print(data)

# df = pd.DataFrame(df['advogados_reclamado'][0])
print(type(','.join(df['advogados_reclamado'])))