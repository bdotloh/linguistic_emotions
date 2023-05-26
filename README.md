# Emotions in language space

Explorations into the subject of linguistic expressions of emotional events documented in the Empathetic Dialogues dataset (ED; Rashkin et al., [2019](https://arxiv.org/pdf/1811.00207.pdf)). As its name suggests, the ED dataset is often used as a benchmark dataset for developing empatheic dialog systems. 
At the same time, the ED dataset also has a particularly interesting feature that can allow us to probe into the psycholinguistic aspects of emotions. 
In particular, the creators of the ED dataset provided people with an emotion word, and had them describe a situation (henceforth referred to as "emotional situation instance") associated with that word. Similar to word assocation tests within the domain of psychology and cognitive science, the emotion-situation relation in ED can provide us with some clues about the associative links between episodic memory and emotion concepts (i.e., how emotion words trigger memories of events/situations).

Some information on the dataset: 

There are a total of 32 "emotion classes". Details pertaining to these classes specific to the ED dataset is in Figure 3 of Rashkin et al. ([2019](https://arxiv.org/pdf/1811.00207.pdf)). 

There are a total of n emotional situation instance, split into the conventional train, validation, test sets.

**Some thoughts about the "emotions"**: Emotion reseach in its current form do not permit a precise formulation of the space and structure governing the emotion concept. A thorough review is beyond the scope of this README. Nonetheless, the following are starting points to understand how we can think about emotion and its related concept: 

- Cowen and Keltner ([2021](https://linkinghub.elsevier.com/retrieve/pii/S136466132030276X)) : A data-driven technique to showcase multidimensional space of emotion-evoking stimuli.  
- Ong, Zaki, and Goodman ([2015](https://linkinghub.elsevier.com/retrieve/pii/S136466132030276X)) : A probabilistic graphical model of emotion reasoning 
- Ortony et al., ([1987](http://doi.wiley.com/10.1207/s15516709cog1103_4)) : Componential Analysis to derive a taxonomy of putative emotion words

Taken together, these papers showcase the value of computational approaches in elucidating the latent space of emotions. This work seeks to adopt a similar approach. In particular, given the heterogeniety in people's conceptualisations of what emotions are, I a "unsupervised" approach towards the task of exploring the relatonship amongst various situational instances that people described. 

