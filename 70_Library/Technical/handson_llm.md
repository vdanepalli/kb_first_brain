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



4646
4909 - -new  station 8

station 10 

