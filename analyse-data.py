import os
import json
import pickle
import pandas as pd
import seaborn as sns
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from umap import UMAP

DATA_PATH = "datasets/empathetic-dialogues/context-only"
full_data = pd.read_csv(os.path.join(DATA_PATH, 'train-with-embeddings-ekman-emotions-pca-components.csv'), encoding='utf-8')

embeddings = full_data.loc[:, full_data.columns.str.startswith('e_')].iloc[:,:10]
embeddings['ekman_emotions'] = full_data.ekman_emotions

pair_plot = sns.pairplot(embeddings, hue= 'ekman_emotions', palette='Spectral')
fig = pair_plot.fig
fig.savefig('visuals/first-10-dim-sentence-embeddings-correlation-matrix.png')

embeddings = full_data.loc[:, full_data.columns.str.startswith('e_')]
reducer = UMAP(random_state=42, verbose=True)
reducer.fit(embeddings)

umap_embeddings = reducer.transform(embeddings)

umap_components = pd.DataFrame(umap_embeddings, columns = [f'umap_{num}' for num in range(1, 3)])
data_with_umap = pd.concat([full_data, umap_components], axis=1)

data_with_umap = data_with_umap.loc[:,~data_with_umap.columns.str.startswith('Unnamed')]
data_with_umap.to_csv('train-with-embeddings-ekman-emotions-pca-components.csv', index=False)

fig = px.scatter(
        data_with_umap, x='umap_1', y='umap_2',color='ekman_emotions',
        hover_name = 'situation', hover_data = ['emotion'],
        labels={'color': 'ekman_emotions'},
        color_discrete_map={
            "anger": "red",
            "disgust": "green",
            "fear": "purple",
            "sadness": "grey",
            "surprise": "pink",
            "joy": "yellow",
            "mixed": "blue",
            "others": "saddlebrown"
            }
    )

fig.write_html("visuals/ED-contexts-UMAP.html")
