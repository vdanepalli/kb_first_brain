# Hands-On Large Language Models ~ Jay Alammar, Maarten Grootendorst

## 1. Intro to LLM

NPC - nonplayable character
Language AI - tech capable to understand, process, generate language

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0101.png)


**Tokenization** - Words or SubWords
**Vocabulary** - Unique list of tokens. 

**Bag of Words, 2000:** so each sentence can be represented as a vector of vocabulary size where the value represents the frequency of the token in the sentence. 

**word2vec, 2013:** say a neural network trained on data to learn **embeddings** - vector representations of data. attempt to capture meaning. semantic representation. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0106.png)

the dimension of the embedding is the size of the embedding vector. to simplify each dimension can be considered as an attribute or property of the word it represents. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0110.png)


word2vec creates **static embeddings**. The word **bank** has the same representation irrespective of the context it was used in. 

**RNN Recurrent Neural Networks** attempt to encode this positional info. Modeling sequences. 


![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0111.png)

**Autoregressive** when generating next token, it needs all previous tokens. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0112.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0113.png)

So, in 2014 came **Attention**, a way to attend to the other words or tokens. It selectively determines which words are important. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0115.png)


But this sequential nature makes it impossible for parallelization. 

In 2017, there came a paper **Attention is all you need.** Authors proposed an architecture called **Transformer** - solely based on attention, and removes the recurrence network. Transformer can be trained in parallel. 

Transformer has **encoder** and **decoder** parts. 

The **encoder** part has **self-attention** and **feed forward neural network**

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0116.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0117.png)


decoder pays attention to the output of the encoder. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0119.png)

**self-attention** in decoder **masks** future positions to avoid information leak. 


The encoder-decoder model served well for translation tasks but couldn't be easily used for other tasks, like text classification. 

2018, a new architecture **Bidirectional Encoder Representations from Transformers - BERT** 

BERT is encoder only. Removes decoder part. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0121.png)

BERT trains the encoder stack by using something called **Masked language modeling.** Mask part of the input for the model to predict. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0122.png)

BERT like models are commonly used for **Transfer learning** First **pretraining** to model language, and then **fine-tuning** it for specific task

BERT models are used for classification, clustering, semantic search. 

encoder only models = **representation models**
decoder only models = **generative models**


<br/><br/>

In 2018, another architecture was prorposed. It's called **GPT - Generative Pre-trained Transformer** 

GPT 1 -- 7000 books -- 117 Million Parameters. 
GPT 2 -- 1.5B Params
GPT 3 -- 175B Params


![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0124.png)


Generate LLMS -- seq to seq machines. attempt to autocomplete input. Completion models.

By fine-tuning, we can make these models follow instructions. 

**Context length/window** represents max tokens the model can process. Current context length increases with each prediction. 

Open source base models are referred to as **Foundation models**

New architectures emerged in addition to **Transformers** such as **MAMBA** and **RWKV**


<br/><br/>

In machine learning, you take data, and train a model for one specific task (say classification)


Creating LLMS: 
1. Language Modeling - Pretraining. Predicts next word. Results in Foundational or Base model. 
2. Fine-tuning - Post-tuning. Training the desired behavior. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0130.png)


Caution:

1. Bias and fairness. 
2. Transparency and accountability. 
3. Generating harmful content
4. Intellectual property
5. Regulation

**VRAM** Video Random Access Memory. GPU RAM. 


```py
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
```

we can encapsulate the model, tokenizer, and text generation process for simplicity. 

```py
from transformers import pipeline

# Create a pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=500,
    do_sample=False
)
```

```py
# The prompt (user input / query)
messages = [
    {"role": "user", "content": "Create a funny joke about chickens."}
]

# Generate output
output = generator(messages)
print(output[0]["generated_text"])

# [{'generated_text': ' Why did the chicken join the band? Because it had the drumsticks!'}]
```


## 2. Tokens and Embeddings 

1. Tokenization methods: **BPE Byte Pair Encoding** and **WordPiece**, **SentencePiece**, **Unigram**
2. Tokenizer design choices | parameters -- vocab size, special tokens (begining, ending, padding, unk, classification, masking, <work>, <StartRef>), Capitalization
3. Train the tokenizer on dataset. 

**Word Tokens** used in recommendation systems. minimal differences between tokens (say, like, liked, likes). Doens't represent new tokens in dataset after training. 
**Subword Tokens** More expressive. Can represent new words as combination of smaller tokens. Often Average at 3 characters per token.
**Character Tokens** 
**Byte Tokens** Tokenization free encoding. Individual bytes used to represent unicode characters. 

Some subword tokenizers also include bytes as tokens in their vocabulary. Ex: GPT-2 and RoBERTa


Token Embeddings: numeric representation, capture meanings and patterns in language. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0207.png)


**Text Embedding**

```py
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

# Convert text to text embeddings
vector = model.encode("Best movie ever!")
```

Using pretrained Word Embeddings

```py
import gensim.downloader as api

# Download embeddings (66MB, glove, trained on wikipedia, vector size: 50)
# Other options include "word2vec-google-news-300"
# More options at https://github.com/RaRe-Technologies/gensim-data
model = api.load("glove-wiki-gigaword-50")

model.most_similar([model['king']], topn=11)
```

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0214.png)


**Skip-gram** method of selecting neighboring words, and negative sampling, adding negative examples by random sampling from dataset. 

## 3. Looking inside LLM 

A model generates one token at a time. 
Each token is a result of one complete forward pass. 


**Autoregressive models:** models consume earlier predictions to make later predictions. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0304.png)

Tokenizer is followed by neural network. 

**LM Head** translates the output of the stack into probability scores for what the next most likely token is. LM Head is a simple neural network by itself. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0305.png)


**MLP** Multilayer Perceptron

**Decoding Strategy** method of choosing a single token from the probability distribution. 
**Greedy Decoding** Choosing the highest scoring token everytime. => `temperature = 0`

**Context length** How many tokens can a model process at once. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0309.png)


**kv cache** keys and values. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0310.png)

```py
%%timeit -n 1
# Generate the text
generation_output = model.generate(
  input_ids=input_ids,
  max_new_tokens=100,
  use_cache=False # kv cache disabled. 
)
```

Each **Transformer** block has two components. 1. **Attention** and 2. **Feed Forward Neural Network**


What should the model do? **Instruction tuning, Human preference, Feedback fine tuning.**

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0314.png)


Attention involves two steps. 
1. **Relevance Score**: how relevant each of the tokens are to the current token
2. **Combine Information** combine tokens using the score. 

The attention mechanism is duplicated and parallelized and each are conducted into **Attention Head**. This allows the model to model complex patterns in input sequence. Attending to different patterns at once. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0318.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0319.png)


Q.K => Softmax => Relevance Scores. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0320.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0321.png)

Attention is the most expensive computation. 

**Local/Sparse Attention** limits context / the number of tokens a model can attend to.
**Sliding Window Attention**

Efficient attention ~ transformer blocks alternate between full attention and sparse attention. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0323.png)


**Grouped-Query Attention** Builds on multi-query attention. Multiple groups of attention heads, share the KV matrices
**Multi-Query Attention** Shares KV between all attention heads leaving only the Queries as unique among all heads. Ideally, each attention head has its own QKV matrices. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0325.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0326.png)


![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0327.png)


![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0328.png)


**Flash Attention** speeds up attention calculation by optimizing what values are loaded and moved between a GPUs shared memory (SRAM) and **High Bandwidth Memory HBM**



![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0329.png)


**RMSNorm** Root Mean Square  is simpler than the **LayerNorm** used in Original Transformer. 

**SwiGLU** over **ReLU** activation function used in original Transformer. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0330.png)

**RoPE** Rotary Positional Encoding 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0331.png)

**Packing** efficiently organizing short training documents into context. minimize padding. group multiple documents together

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0332.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0333.png)

during attention, apply positioanl encoding to Q, K before multiplication.


## 4. Text Classification

Classification with representation models: 
1. Task Specific Models
2. Embedding Models

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0403.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0404.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0405.png)

```py
from transformers import pipeline

# Path to our HF model
model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# Load model into pipeline
pipe = pipeline(
    model=model_path,
    tokenizer=model_path,
    return_all_scores=True,
    device="cuda:0"
)
```

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0408.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0409.png)

**Accuracy:** Of all the predictions, how many are actually right. TP + TN / Total
**Precision:** Of all positivde predictions, how many are actually positive. TP / TP + FP. Hates FP. 
**Recall:** Of all positives, how many did model predict correctly. TP / TP + FN. Of all scam out there, how much did the model catch? 
**F1 Score:** 2 * Precision * Recall / Precision + Recall. Harmonic Mean. 


When dealing with rates, we use harmonic mean, as regular average often fails which doesn't account for the denominator. Haramonic mean drags the final score towards the lowest value. 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0410.png)

```py
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

# Convert text to embeddings
train_embeddings = model.encode(data["train"]["text"], show_progress_bar=True)
test_embeddings = model.encode(data["test"]["text"], show_progress_bar=True)
```

```py
from sklearn.linear_model import LogisticRegression

# Train a logistic regression on our train embeddings
clf = LogisticRegression(random_state=42)
clf.fit(train_embeddings, data["train"]["label"])

y_pred = clf.predict(test_embeddings)
```

To create embeddings, we can use external API offerings form Cohere or OpenAI to remove GPU dependency. 

**Zero-shot classification with Embeddings**

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0415.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0416.png)

```py
from sklearn.metrics.pairwise import cosine_similarity

# Find the best matching label for each document
sim_matrix = cosine_similarity(test_embeddings, label_embeddings)
y_pred = np.argmax(sim_matrix, axis=1)
```


**Prompt Engineering** iteratively improving prompt to get desired output. 

**T5 Model** Text-to-Text Transfer Transformer Model 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0419.png)

1. pretrain using masked language modeling (masking more than 1 token, or sets of tokens)
2. fine-tuning the base model 

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0421.png)

Preference tuning and Instruction tuning

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0422.png)

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0423.png)

```py
import openai

# Create client
client = openai.OpenAI(api_key="YOUR_KEY_HERE")
```

## 5. Text Clustering and Topic Modeling

**Text Clustering**
1. Convert input documents into embeddings with embedding model
2. Reduce dimensionality of the embeddings with dimensionality reduction model. Compression Technique
3. Find groups of semantically similar models with a cluster model 

Dimensionality Reduction
1. **PCA** Principal Component Analysis
2. **UMAP** Uniform Manifold Approximation and Projection

```py
from umap import UMAP

# We reduce the input embeddings from 384 dimensions to 5 dimensions
umap_model = UMAP(
    n_components=5, min_dist=0.0, metric='cosine', random_state=42
)
reduced_embeddings = umap_model.fit_transform(embeddings)
```

setting a `random_state` in UMAP will make the results reproducible across sessions but will disable parallelism and therefore slow down training.

![Image Name](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098150952/files/assets/holl_0507.png)

**HDBSCAN** Hierarchical Density-Based Spatial Clustering of Applications with Noise
**DBSCAN** Allows micro clusters to be found without having to explictly specify number of clusters. 

```py
from hdbscan import HDBSCAN

# We fit the model and extract the clusters
hdbscan_model = HDBSCAN(
    min_cluster_size=50, metric="euclidean", cluster_selection_method="eom"
).fit(reduced_embeddings)
clusters = hdbscan_model.labels_
```

**Topic modeling** finding themes or latent topics in a collection of textual data. keywords or phrases that capture the meaning of the topic 

**Latent** hidden, underlying, not directly observable. 

thomas cruz david lopez brittany fowler garret holder

