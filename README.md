# emoX-text
Explorations into the subject of linguistic expressions of emotional events documented in the Empathetic Dialogues dataset (ED; Rashkin et al., [2019](https://arxiv.org/pdf/1811.00207.pdf)). As its name suggests, the ED dataset is often used as a benchmark dataset for developing empatheic dialog systems. 
At the same time, the ED dataset also has a particularly interesting feature that can allow us to probe into the psycholinguistic aspects of emotions. 
In particular, the creators of the ED dataset provided people with an emotion word, and had them describe a situation (henceforth referred to as "emotional situation instance") associated with that word. Similar to word assocation tests within the domain of psychology and cognitive science, the emotion-situation relation in ED can provide us with some clues about the associative links between episodic memory and emotion concepts (i.e., how emotion words trigger memories of events/situations).

Some information on the dataset: 

There are a total of 32 "emotion classes". Details pertaining to these classes specific to the ED dataset is in Figure 3 of Rashkin et al. ([2019](https://arxiv.org/pdf/1811.00207.pdf)). 

There are a total of n emotional situation instance, split into the conventional train, validation, test sets.

**Some thoughts about "emotion classes"**: This phrases is in parentheses because the state of emotion research, at this juncture, do not permit a precise formulation of the space and structure governing the emotion concept. A thorough review is beyond the scope of this README. Nonetheless, the following are starting points to understand how we can think about emotion and its related concept: 

**TODO: write short summary of these papers**

- Cowen and Keltner ([2021](https://linkinghub.elsevier.com/retrieve/pii/S136466132030276X))
- Ong, Zaki, and Goodman ([2015](https://linkinghub.elsevier.com/retrieve/pii/S136466132030276X))
- Ortony et al., ([1987](http://doi.wiley.com/10.1207/s15516709cog1103_4))

Given the heterogeniety in people's conceptualisations of what emotions are, and the disparate worlds of thoughts by which emotion researchers inhabit, I adopt a "unsupervised" approach towards the task of exploring the relatonship amongst various situational instances that people described. Through these "data-driven" explorations, I hope to develop testable hypotheses concerning the links between an emotion concept and situation instances.

These methods used in this project are roughly similar to standard NLP/ML pipelines.
1) Obtain a distributed representation of each emotional situation instance with an off-the-shelf encoder (e.g., [SBERT](https://www.sbert.net/). 
Project the set of high-dimensional emotion situation vectors onto a lower dimensional space via dimensionality reduction techniques such as PCA, T-SNE, or UMAP
2) Topic models *TODO*
3) ... 
