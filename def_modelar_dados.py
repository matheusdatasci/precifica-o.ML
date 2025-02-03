def modelar_dados(dados_desejados, df_original):
  df_original = df_original[df_original['price'] <= 334]
  media_por_bairro = df_original.groupby('bairro')['price'].mean()
  media_por_bairro_group = df_original.groupby('bairro_group')['price'].mean()
  media_por_host_name = df_original.groupby('host_name')['price'].mean()

  dados_desejados['media_por_bairro'] = dados_desejados['bairro'].map(media_por_bairro)
  dados_desejados['media_por_bairro_group'] = dados_desejados['bairro_group'].map(media_por_bairro_group)
  dados_desejados['media_por_host_name'] = dados_desejados['host_name'].map(media_por_host_name)

  dados_desejados[['host_id', 'nome','host_name','bairro_group','bairro', 'room_type']] = dados_desejados[['host_id','nome','host_name','bairro_group','bairro', 'room_type']].astype('category')

  dados_desejados = dados_desejados.drop(columns = ['ultima_review', 'reviews_por_mes', 'id', 'minimo_noites', 'latitude', 'longitude', 'disponibilidade_365'], axis = 1)

  return dados_desejados