# EAG: V3

## Session 1: Foundations of Transformer Architecture


### **Concept Refresh: LLMs & Modern API Protocols**
*Query: What is LLM/Language Modeling? Pre/Post-training. Tool Calling. REST, GraphQL, gRPC.*

#### 🧠 **1. Language Models & LLMs**
* **Definition:** <span style="color:#2ecc71">Autoregressive</span> models that map language to vector space to calculate token probability distributions.
* **Mechanism:** Highly advanced **next-token prediction** (sentence completion on steroids).
* **Caveats:** They do not *think*. Hallucinations occur because they optimize for statistical probability, not factual truth.

#### 🏗️ **2. Pre-training vs. Post-training**
* **Pre-training:** Self-supervised learning on massive internet corpora to build a **Base Model**. Understands language and world knowledge. Extremely expensive.
* **Post-training:** SFT, RLHF, DPO. Fine-tuning the base model to follow instructions and safety guardrails, resulting in an **Instruct Model**.
* **Gotcha:** Poor post-training data leads to an *alignment tax* (loss of reasoning capabilities).

#### 🛠️ **3. Tool / Function Calling**
* **Definition:** Forcing an LLM to output structured data (e.g., **JSON**) matching a predefined schema to trigger external systems.
* **Usage:** Building autonomous AI agents that can query databases, execute code, or hit external APIs.
* **Caveat:** The LLM *only* generates the payload. Your application architecture must execute the code and return the result. Beware of hallucinated parameters.

#### 🌐 **4. REST vs. GraphQL**
* **REST:** Multiple endpoints, strict server-defined payloads. Prone to **over-fetching** and **under-fetching**.
* **GraphQL:** Single endpoint, flexible client-defined payloads. Solves over-fetching but introduces complex backend routing and **N+1 query** performance risks.

#### ⚡ **5. gRPC**
* **Definition:** High-performance RPC framework using **HTTP/2** and **Protocol Buffers (Protobuf)**.
* **Mechanics:** Serializes data into <span style="color:#e74c3c">binary format</span> instead of JSON. 
* **Usage:** Extremely low-latency, high-throughput internal microservice communication. 
* **Gotcha:** Not natively browser-friendly. Requires strict `.proto` contracts. Binary payloads are hard to debug manually.


---

### **Concept Refresh: Pipelines, UIs, AI Agents, & Tech Moats**
*Query: CI/CD Pipelines, Gradio vs FastAPI, AntiGravity/Claude Code/Codex/Cursor, Software as a moat.*

#### 🔄 **1. CI/CD Pipelines**
* **Definition:** <span style="color:#2ecc71">Continuous Integration / Continuous Deployment</span>. Automated sequences for testing and shipping code.
* **Intuition:** An automated software assembly line and quality control checkpoint.
* **Caveat:** Flaky tests break the pipeline. Bloated pipelines slow down deployment velocity.

#### 🌐 **2. Gradio vs. FastAPI**
* **Gradio:** Rapid **UI framework** for demonstrating ML models. (The flashy storefront window).
* **FastAPI:** High-performance, async **REST API framework**. (The industrial loading dock).
* **Gotcha:** Never use Gradio for production traffic; it scales poorly. FastAPI requires building your own frontend.

#### 🤖 **3. The AI Coding Evolution**
* **Codex:** Foundational code model (autocomplete). *The smart typewriter.*
* **Cursor:** AI-first **IDE** with multi-file context. *The junior dev pair-programmer.*
* **Claude Code:** Agentic **CLI tool** for autonomous terminal tasks. *The command-line robot.*
* **AntiGravity:** Agent-first IDE (Gemini 3) with a "Mission Control" to manage parallel autonomous agents. *The robotic engineering team.*
* **Gotcha:** Autonomous agents require strict terminal execution limits (Allow/Deny lists) to prevent catastrophic system commands.

#### 🏰 **4. Software is Not a Moat**
* **Concept:** Because AI drives the cost of coding to near-zero, raw code is a commodity, not a competitive advantage.
* **The Real Value:** * **Idea:** Solving an actual, painful human problem.
    * **Execution:** Shipping rapidly and reliably.
    * **Tested:** Validated by users and rigorous automated QA.
* **Intuition:** Everyone has a printing press now; the value is in writing a good story.

---

### **Concept Refresh: Gradient Descent & Deep Learning History**
*Query: Model training process math (why -1 in gradient/weight update) and the history of Hinton, LeCun, AlexNet, ImageNet.*

#### 🧮 **1. The Math: Weight Updates & The "-1"**
* **The Equations:** `rate_of_change = -x.sign(y - y_pred)` | `w_dash = w - learning_rate * rate_of_change`
* **Why `-x`?:** Calculus <span style="color:#3498db">Chain Rule</span>. The derivative of the prediction $-(w \cdot x)$ with respect to $w$ yields $-x$.
* **Why subtract in `w_dash`?:** Gradients point toward the steepest *ascent* (highest error). We want to minimize error, so we move in the **opposite direction** (steepest descent).
* > *"Gradients point up the mountain. We subtract them to walk down the mountain."*

#### 🏆 **2. The Deep Learning Pioneers**
* **Yann LeCun:** Invented the **CNN** blueprint. 
* **Geoffrey Hinton:** Popularized **Backpropagation** (the engine calculating the gradients).
* **Alex Krizhevsky & Ilya Sutskever:** Created **AlexNet**. 
* **The Breakthrough:** Alex recognized that training requires millions of simultaneous matrix multiplications. He ported these computations from CPUs to **GPUs**, allowing massive parallel processing.
* **ImageNet (2012):** AlexNet used this GPU paradigm to obliterate traditional algorithms in the ImageNet competition, sparking the modern AI revolution.

#### ⚠️ **3. Caveats & Gotchas**
* **Learning Rate ($\eta$):** The most critical hyperparameter. 
    * *Too high* = Divergence (jumping over the minimum). 
    * *Too low* = computationally unviable (takes forever).
* **Hardware:** The GPU paradigm Alex started is now the ultimate bottleneck; scaling AI today is limited by the physical manufacturing of specialized GPU clusters and the network bandwidth connecting them.

---

### **Concept Refresh: Hardware, Transformers, Networks, & LLM Control**
*Query: SIMD. 2017 Transformer shift (Attention is All You Need). Neural Networks & Feed Forward. Chain of Thought. Guard Rails.*

#### 🖥️ **1. SIMD (Single Instruction, Multiple Data)**
* **Definition:** A parallel architecture where one instruction is executed across multiple data points simultaneously. 
* **Intuition:** A drill sergeant making 100 soldiers do a push-up at the exact same time.
* **Caveat:** Highly dependent on memory bandwidth cache alignment. 

#### 🚀 **2. The 2017 Transformer Paradigm Shift**
* **Pre-2017:** Sequential models (RNNs). Hard to parallelize, required expensive <span style="color:#3498db">labeled data</span>, forgot early context.
* **2017 (Attention Is All You Need):** The **Transformer** replaced sequential reading with **Self-Attention** (looking at all tokens simultaneously). 
* **Impact:** Highly parallelizable, unlocked **Self-Supervised Learning** (training on raw internet text), and proved that massive scale (Compute/Money) equals capability.
* **Caveat:** Attention compute scales quadratically ($O(N^2)$) with context length.

#### 🧠 **3. Neural Networks & Feed Forward**
* **Neural Network:** A mathematical graph of nodes (neurons) and weights used for pattern recognition.
* **Feed-Forward:** The simplest topology where data moves strictly in one direction (input $\rightarrow$ hidden $\rightarrow$ output).
* **Intuition:** Water flowing downward through a series of stacked filters. No backward flow.
* **Caveat:** Has no "memory" of previous inputs; cannot process sequential context alone.

#### 🔗 **4. Chain of Thought (CoT)**
* **Definition:** Forcing an LLM to generate intermediate reasoning steps before answering. 
* **Intuition:** Forcing a student to "show their work" on a math test.
* **Caveat:** Increases <span style="color:#f39c12">latency and token cost</span>. The model can still hallucinate a logically flawed chain.

#### 🛡️ **5. Guard Rails**
* **Definition:** Safety layers/filters placed around an LLM to block toxic inputs, prevent PII leaks, and enforce output constraints.
* **Intuition:** Automated braking systems on a powerful race car.
* **Caveat:** Causes latency and can lead to *refusal fatigue* if tuned too aggressively.


----

### **Knowledge Base: AI Timelines, 2026 Inference, Agents, & Hardware**
*Query: Deep Learning Milestones, Turbo Quant, Karpathy AutoResearch, Agentic Skills, 1-Person Unicorn, Hardware (Jet engines, VSLAM drones, Actuators, 6-Axis).*

#### 📅 **1. Deep Learning Architecture Timeline**
* **Evolution:** Embeddings (vocabulary) $\rightarrow$ **Transformers** (reading) $\rightarrow$ **RLHF** (manners) $\rightarrow$ **Diffusion/CLIP** (vision) $\rightarrow$ **LoRA** (cheap adaptability).
* **Key Components:** <span style="color:#2ecc71">Adam Optimizer</span> (stable training) and <span style="color:#2ecc71">Batch Norm</span> are the engine oil for these architectures.
* **Gotcha:** Modern LLMs are overkill for simple tabular data; legacy ML (XGBoost) is often better and cheaper.

#### ⚡ **2. TurboQuant & AutoResearch (2026)**
* **TurboQuant:** Google algorithm compressing the **KV Cache** to 3-4 bits. Uses a mathematical rotation matrix.
* **Impact:** Drastically reduces <span style="color:#e74c3c">OOM</span> errors, enabling huge context windows on standard GPUs without retraining.
* **Karpathy's AutoResearch:** Agentic loop that edits PyTorch, trains for 5 mins, and acts as an autonomous ML researcher.
* > *"AutoResearch is a tireless robotic intern running ML experiments overnight."*

#### 🤖 **3. Agentic Skills & Industry AI**
* **Agentic Skills:** Deterministic tools an LLM can trigger (Python, SQL, web search). Giving the AI "hands".
* **One-Person Unicorn:** A $1B startup run by a solo founder orchestrating AI agents instead of human employees.
* **Domain AI:** **inkl.ai** (SME private-cloud AI) and **Cursor for Construction** (e.g., Brickanta; automating building codes and estimation).
* **Gotcha:** Multi-agent systems suffer from <span style="color:#f39c12">compounding hallucination rates</span> across workflows.

#### ⚙️ **4. Robotics & Physical Tech**
* **GPS-less Drones:** Navigate via **VSLAM** (tracking pixel shifts). Fails in featureless environments (smooth water/white walls).
* **Motors vs Actuators:** Motor = rotational energy generator. Actuator = full assembly converting energy to motion (the "muscle").
* **Six-Axis Robot:** Industrial arm with 6 degrees of freedom (X, Y, Z + Roll, Pitch, Yaw). 
* **Jet Engine:** Intake $\rightarrow$ Compress $\rightarrow$ Ignite $\rightarrow$ Exhaust (Thrust).



<br/><br/>
<br/><br/>


---


<br/><br/>
<br/><br/>







## Session 2: Modern LLM Internals & SFT

### **Concept Refresh: LLM Mechanics, Tokenization, & Scaling Laws**
*Query: Plan mode vs regular chat, context length vs token size, tokenizer determinism/compression, autoregression, why LLM, Chinchilla scaling laws.*

#### 🧠 **1. Plan Mode vs. Regular LLM**
* **Regular Chat:** System-1 thinking. Immediate <span style="color:#3498db">autoregressive prediction</span>. 
* **Plan Mode:** System-2 thinking. Generates an internal **Chain of Thought (CoT)** to reason and self-correct before outputting a final answer. 
* **Caveat:** Plan mode significantly increases latency and API token costs.

#### 🔠 **2. Tokenization & Compression**
* **Determinism:** Tokenizers are <span style="color:#2ecc71">strictly deterministic</span> at inference time.
* **Training:** Built via statistical ML (like **BPE**) to compress the most frequent character combinations.
* **Language Disparity:** Optimized heavily for English. Non-English languages tokenize poorly, consuming more context length and inflating API costs.
* > *"Tokenization is Morse Code. English got the shortest signals."*

#### 📚 **3. Autoregression & KV Cache**
* **The Rule:** Predicting token $N+1$ requires the mathematical context of tokens $1$ to $N$.
* **The Mechanism:** To prevent recomputing the whole sequence every step, past token states are stored in the **KV Cache**.
* **Caveat:** As context length scales, KV Cache explodes, causing <span style="color:#e74c3c">OOM (Out of Memory)</span> errors.

#### ⚖️ **4. Chinchilla Scaling Laws**
* **Why LLM:** **L**arge (billion+ parameters), **L**anguage (trained on text), **M**odel (statistical graph).
* **Chinchilla Law:** Proved optimal model scaling requires a ratio of **~20 training tokens per 1 parameter**.
* **Intuition:** Don't build a 100-story library (parameters) for 10 books (tokens). 
* **Gotcha:** We are hitting the "Data Wall"—running out of internet text to satisfy the 20:1 ratio for trillion-parameter models.

---

### **Concept Refresh: Language Modeling, Alignment, Tokenization & PEFT**
*Query: CLM masking, Pre-training vs Fine-tuning (SFT, RLHF, FFT), Language Tokenizers, LoRA.*

#### 🧠 **1. Fundamental Concepts**
* **Autoregressive Generation:** Predicting the next sequence item based *strictly* on previous items.
* **BPE (Byte-Pair Encoding):** Compression algorithm merging frequent characters into tokens.
* **Loss Function:** Mathematical measurement of prediction error.
* **PEFT (Parameter-Efficient Fine-Tuning):** Methods to adapt models cheaply without altering the whole network.

#### 🎭 **2. CLM & Masking**
* **CLM (Causal Language Modeling):** Training a model to strictly predict the forward-moving next token.
* **Training Mask:** Uses a <span style="color:#f39c12">Causal Mask</span> to block the model from seeing future tokens during parallel batch training.
* **Inference Mask:** We do *not* mask the future during inference because the future hasn't been generated yet.

#### 🏗️ **3. Training Phases**
* **Pre-training:** Unsupervised learning on massive data to build the **Base Model** (learning world knowledge).
* **SFT (Supervised Fine-Tuning):** Training on human Q&A pairs to teach dialogue formatting.
* **RLHF (Reinforcement Learning from Human Feedback):** Using human preference scores to align the model for safety/helpfulness.
* **FFT (Full Fine-Tuning):** Updating *every* network weight. <span style="color:#e74c3c">Gotcha:</span> Expensive and causes catastrophic forgetting.

#### 🔠 **4. Language-Specific Tokenizers**
* **Mechanism:** Tokenizers compress based on training data statistics. 
* **Disparity:** Models trained heavily on English map English words perfectly (1 token). Rare languages fragment into many tokens.
* **Gotcha:** Processing non-English languages consumes vastly more API budget and context window space.
* > *"Tokenization is making boxes. English gets perfect boxes; other languages get chopped up."*

#### ⚡ **5. LoRA (Low-Rank Adaptation)**
* **Mechanism:** Freezes base weights ($W_{old}$) and injects tiny, trainable low-rank matrices ($A$ and $B$). $W_{new} = W_{old} + A \times B$.
* **Benefit:** Allows fine-tuning massive models on a single GPU. Outputs a tiny, swappable adapter file.
* **Intuition:** Drawing on a transparent glass overlay instead of repainting the entire canvas.



<br/><br/>
<br/><br/>

---

### Concept Refresh: Gradient Descent Math & The "Two Negatives"
*Query: Why is the derivative -x, and why do we subtract the gradient in weight updates?*

#### 🧮 **1. The First Negative: The Derivative ($-x$)**
* **Concept:** Derives from the **Chain Rule** in calculus.
* **Mechanics:** The error function contains the inner function $(y - w \cdot x)$. Differentiating this inner function with respect to $w$ isolates the constant attached to $w$, which is <span style="color:#e74c3c">$-x$</span>.
* **Meaning:** It quantifies exactly how sensitive the error is to a change in the weight.

#### 📉 **2. The Second Negative: The Weight Update ($w = w - \nabla$)**
* **Concept:** Gradients point toward the **steepest ascent** (maximum error).
* **Mechanics:** To minimize loss, we must invert the direction. We mathematically force a descent by subtracting the gradient from the current weight.
* *Equation:* $w_{new} = w_{old} - \text{gradient}$

#### 🧠 **Intuition (The Blindfolded Hiker)**
* **Weight ($w$):** Your coordinates on a mountain.
* **Derivative ($-x$):** Feeling the slope with your foot to find which way is *uphill*.
* **Subtraction:** Turning 180 degrees to walk *downhill* toward the valley (zero error).

#### ⚠️ **Caveats & Gotchas**
* **Missing Learning Rate:** Never subtract the raw gradient. Always scale it with a learning rate ($\eta$) to prevent overshooting: $w = w - (\eta \cdot \text{gradient})$.
* **Chain Rule Risks:** Deep networks multiplying many derivatives together risk **Vanishing** or **Exploding Gradients**.


----


### Concept Refresh: LoRA Math & Matrix Decomposition
*Query: Math behind LoRA, calculation of A and B matrix sizes, and parameter reduction.*

#### 🧮 **1. The Core Equation**
* **FFT:** Learns full update matrix $\Delta W$ of size $d \times k$.
* **LoRA Hypothesis:** Weight changes have a <span style="color:#2ecc71">low intrinsic rank</span>.
* **Decomposition:** $\Delta W = A \times B$

#### 📏 **2. Matrix A & B Sizes**
Given base weights $W \in \mathbb{R}^{d \times k}$ and a chosen rank $r$:
* **Matrix A:** Dimensions are $d \times r$.
* **Matrix B:** Dimensions are $r \times k$.
* **Matrix Multiplication:** $(d \times r) \times (r \times k)$ yields a $d \times k$ matrix, allowing it to be seamlessly added to $W$.

#### 📉 **3. The Math in Practice ($4096 \times 4096$ layer, $r=8$)**
* **FFT Parameters:** $16.7$ Million
* **LoRA Parameters:** $4096(8) + 8(4096) = 65,536$
* **Result:** ~99.6% reduction in VRAM overhead. The tiny $A$ and $B$ matrices become the "Adapter file".

#### 🧠 **Intuition (The 4K Screen)**
> *FFT is building a full 4K piece of tinted glass. LoRA is using two thin strip projectors (A and B) that cross beams to create the exact same 4K filter.*

#### ⚠️ **Caveats & Gotchas**
* **Rank Selection:** Low $r$ = underfitting (bad for complex SQL/Code). High $r$ = slow training, defeats the purpose of LoRA.
* **Scaling Factor ($\alpha$):** LoRA uses an $\alpha$ hyperparameter. The update is actually scaled by $\frac{\alpha}{r}$. Failing to tune $\alpha$ breaks training stability.
* **Inference Overhead:** Dynamically calculating $A \times B$ at runtime adds compute overhead. Always <mark>merge weights</mark> ($W_{new} = W + AB$) for production inference.


----


### Concept Refresh: Reversing LLM Alignment (Uncensoring)
*Query: Can pre-trained models that are aligned via SFT/RLHF be fine-tuned again to remove safety guardrails?*

#### 🧠 **1. The Mechanics of Uncensoring**
* **Concept:** RLHF and SFT <span style="color:#e74c3c">do not delete</span> harmful knowledge from the base weights; they merely suppress the probability of outputting it.
* **Mechanism:** By applying adversarial fine-tuning (e.g., via **LoRA**) using a small dataset of harmful prompts paired with compliant responses, you rewire the probability distribution to bypass the refusal mechanism.

#### 🌍 **2. Real-World Application**
* **Usage:** Producing "Uncensored" models (widely available on HuggingFace).
* **Purpose:** Used for unrestricted creative writing, red-teaming, and cybersecurity penetration testing where artificial refusals hinder productivity.

#### 🛠️ **Intuition (The Bribed Locksmith)**
> *The model is a master locksmith who signed a contract to never pick a bank vault. They still possess the skill. Uncensoring is paying them a bribe (new data) to ignore the contract and use the skills they already have.*

#### ⚠️ **Caveats & Gotchas**
* **Superficial Alignment:** Alignment is incredibly fragile. Millions of dollars of RLHF can be undone with <span style="color:#f39c12">~$10 of GPU compute</span> and a few hundred training examples.
* **Catastrophic Forgetting:** Over-tuning to break guardrails can damage the model's core instruction-following abilities, making it useless.
* **Security Risk:** Stripping guardrails leaves the model completely defenseless against generating toxic, biased, or strictly illegal content.


---


### **Concept Refresh: LLM Parameter Storage & Runtime**
*Query: Where are pre-trained model parameters stored, and are they files?*

#### 🗄️ **1. Storage Medium & Formats**
* **Concept:** Models are serialized into massive binary files containing multi-dimensional arrays (tensors) of `fp16` or `bf16` numbers.
* **File Formats:** * <span style="color:#2ecc71">`.safetensors`</span> (Modern standard, secure, fast-loading).
  * `.bin` / `.pt` (Legacy PyTorch, vulnerable to arbitrary code execution).
* **Size:** ~2 bytes per parameter (e.g., a 70B model = ~140GB of disk space).

#### ☁️ **2. Production Architecture (Anthropic/OpenAI)**
* **Cold Storage:** Files are stored in object storage (AWS S3 / GCS).
* **Sharding:** Massive models are split into smaller ~10GB files to manage I/O and distribution.
* **Runtime:** Files are pulled from S3 $\rightarrow$ System RAM $\rightarrow$ **GPU VRAM**. Matrix math *requires* parameters to live in VRAM during inference.

#### 🧠 **3. Intuition (Warehouse to Desk)**
> *Parameters on disk (S3) are like encyclopedias in a dark warehouse. Parameters in GPU VRAM are like encyclopedias opened on a desk. You can only read and calculate when they are on the desk.*

#### ⚠️ **4. Caveats & Gotchas**
* **Cold Starts:** I/O transfer (Disk $\rightarrow$ RAM $\rightarrow$ PCIe $\rightarrow$ VRAM) is the ultimate bottleneck, taking minutes for massive models.
* **Security:** Never load untrusted `.bin` or `.pt` files. They use Python <mark>Pickle</mark>, which can execute malicious OS-level code upon loading. Always use `.safetensors`.


---


### **Concept Refresh: AI Self-Generation & Parameter Writing**
*Query: Can an all-knowing LLM directly write the billions of parameters for an ultimate LLM?*

#### 🧠 **1. The Core Limitation**
* **Direct Answer:** <span style="color:#e74c3c">No.</span>
* **Mechanics:** Parameters are not semantic facts; they are an **emergent, entangled matrix**. An autoregressive text generator cannot calculate a trillion-dimensional optimization problem (finding the minimum in a **Loss Landscape**) via sequential token prediction.
* **Math Reality:** Predicting one weight requires perfect mathematical synchronization with billions of other weights simultaneously. 

#### 🏭 **2. How AI Actually Builds AI**
* **Synthetic Data Generation:** We don't ask AI for the weights; we ask AI for the *training data*. 
* **Model Distillation:** Using a massive, smart model (Teacher) to generate high-quality datasets to train a new model (Student) via standard **Gradient Descent**.

#### 🍰 **3. Intuition (The Cake & The Oven)**
> *The LLM knows what the perfect cake is. But it cannot arrange the atoms of flour and sugar manually with tweezers (writing parameters). It must write the recipe (synthetic data) and use an oven (GPU cluster/Gradient Descent) to bake it.*

#### ⚠️ **4. Caveats & Gotchas**
* **Context Limits:** Outputting 70B+ parameters as text would require an impossible context window of hundreds of billions of tokens.
* **Arithmetic Weakness:** LLMs struggle with precise decimal math due to <span style="color:#f39c12">tokenization</span> constraints, making them useless for outputting billions of exact `fp16` values.
* **Hypernetworks:** Small AI models predicting weights for other small models exist in research, but this does not scale to foundational LLMs.


## Session 3: Developer Foundations & Introduction to Agentic AI

History: Transformers, Attention, Embeddings, Tokenization, Scaling laws, Alignment

**CPU:** Central Processing Unit. Single Physcial Chip attached to motherboard. 
- **ALU:** Arithmetic, and Logical Unit.  - Calculator. 
  - **Control Unit:** Traffic Cop. Fetches instructions from memory, and decides what ALU should do next. 
  - **Registers & Cache:** Memory banks. Small. Fast. 

**Core:** A brain. Quad-Core CPU means, 4 independent brains. 
**Hardware Thread** Now a core is too fast. Often sits idle. So they gave it threads, so it can swtich and start working. Shares resources. 

I ran `python main.py`, now python interpreter, standard libraries, imports, script, heap are all loaded into memory. RAM. 

**Process:** Is a factory. Say in above `python main.py`, when the OS loads all of the required into memory, it puts a fence around it, so nobody else can look. 
**Software Thread:** Workers inside the factory. We need atleast one main thread (worker).

Say when the **OS Scheduler** yanks your process (python program) out of the hardware thread as part of multitasking, this goes into a queue and when a slot is available it is put back in. Now, the hardware thread can be different although the OS tries to put it in the same slot. (**Cache Affinity**)

**GIL** Global Interpreter Lock. The bouncer. Architectural Decision. Dictates that only one software thread is allowed to execute Python bytecode at a time, period
Python manages memory by using **Reference Counting**. Say, it keeps tally of how many times `x` is used. When this reaches 0, it frees up memory. 

Back in 1991, there were no multi-core systems. So Guido Van Rossum made this decision. 
PEP 703 - No-GIL Python. 

So, this means, using `threading` or `asyncio`, true parallelism (using more than one core at a time) can never be achieved. 

We cheat this by using `multiprocessing` module. It spins up more processes (factories) each with its own space, python interpreter, GIL. 

<br/><br/>

Java using **Tracing Garbage Collection** `GC`; Now this doesn't do reference counting. Instead, periodically, it sweeps memory to see dead variables, and free them. 

**Event Loop:** software. lives inside process. when you run `asyncio.run()`, python boots up infinite while True loop; Hyper efficient task manager or suspervisor. List of tasks ready to run, and a waiting list

when await is encountered, you are essentially handing off the responsibility to the OS. You register a ticket with OS via Poling tools, say `epoll` on Linux and `kqueue` on Mac, and tell OS that, "you need to register this network or x call. Interrupt me when the data arrives."

**OS is a Dictator.** When something hogs CPU, it uses **preemptive multitasking** Rips the thread and inserts another. 
**Event Loop is a Honor System (Cooperative)** uses cooperative multitasking. relies on coroutine to voluntarily yield control back to event loop using `await`

**Coroutine:** Any function defined using `async def`. this function is capable of pausing.

`async def function_name` defines async coroutine. 
`await asyncio.sleep()` we handoff to OS. Register a ticket. 
`asyncio.run()` creates the event loop
`asyncio.create_task()` sees this, runs this in background, continues with next line. doesn't wait for the coroutine to finish. 
`res1, res2, res3 = await asyncio.gather(task1, task2, task3)` - returns results in the same order.
`async with asyncio.TaskGroup() as tg: task1 = tg.create_task()` - acts as a context manager. when one crashes, it cancels the other tasks. 
`async with asyncio.timeout(xseconds)` - throws Timeout Error. 
`asyncio.to_thread(task)` - tosses it in the background, event loop is free for other work. 

`gather` - even when using this, actual execution still happens only on one hardware thread. 
`to_thread` - OS can happily assign another physical thread if available, but `GIL` prevents from true parallelism, as it bounces back between the threads. 


```py
import code

code.interact(local=locals())

# Ctrl + D -- to exit and continue execution
# exit() 
```

`pdb` Python Debugger

```py
from pdb import set_trace; set_trace()

breakpoint() # no need of pdb, set_trace() when using this. 

# c - continue until next breakpoint
# h - show available commands
# s - execute next line and step into functions
# n - execute next line but don't step into functions
# p - print value
# pp - pretty print
# q - quit debugger and stop execution
# b 10 - set breakpoint at line 10
# cl - clear all breakpoints
# l - shows code around current executing line 
# r - fast forwards execution until current function returns
# dir(var) - see all available methods on the variable
# PYTHONBREAKPOINT=0 python main.py - ignores all breakpoints. 
```





`asyncio` - asynchronous, non-blocking code

```py
async def 
await asyncio.gather
await asyncio.sleep()


import asyncio
import time

async def say_hello():
    await asyncio.sleep(2)  # Non-blocking sleep
    print("Hello World!")

async def say_good_bye():
    await asyncio.sleep(2)  # Non-blocking sleep
    print("GoodBye World!")

async def main():
    start = time.time()

    # Run both functions concurrently
    await asyncio.gather(say_hello(), say_good_bye())

    total = time.time() - start
    print(f"Total time for this version: {total:.2f} seconds")

# Run the async program
asyncio.run(main())
```


<br/><br/>

```py
from dataclasses import dataclass, field

@dataclass
class IncidentRecord:
    incident_id: str
    status: str
    priority: int = 1

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int # config.port = 1000 will fail

@dataclass
class ShiftRoster:
    station_id: str
    personnel: list[str] = field(default_factory=list) # Must use default_factory for mutable data types

@dataclass
class TemperatureReading:
    sensor_id: str
    celsius: float

    def __post_init__(self):
        if self.celsius < -273.15:
            raise ValueError("Temperature below absolute zero is impossible.")
        
        self.fahrenheit = (self.celsius * 9/5) + 32 # calculated fields
```

dataclasses operate on a honor system. if you declare something as int and drop strings, it doesn't throw errors. 

Pydantic -- solves this. strict type checking. If instantiated, guarantees, data matches schema. 

```py
from pydantic import BaseModel, ValidationError

class PersonnelRecord(BaseModel):
    emp_id: int
    active: bool
```


<br/><br/>

**Decorators:** Takes a function, wraps it to change / add behavior, and returns the wrapper; So, when you use @decorator_func, it takes the current function, and replaces it with wrapper func returned from decorator. This means, the original function loses its identity (name, and docstring). 

To overcome this, we use a decorator for the wrapper function. `from functools import wraps` and **`@wraps(func)`** - Copies the name and docstring from 'func' to 'wrapper'

@ syntax only accepts target func as the only argument. To capture parameters to decorator, we need to nest in layers. Configurator (Outer), Decorator (Middle), Wrapper (Inner)

**Stacking:** Decorators are applied bottom up, and executed top down

**Closure:** Normally, when a function finishes running, Python destroys all the local variables inside it to save RAM. When you define a function inside another function, Before the outer function dies, it looks at the inner function and asks: "Are you going to need any of my variables after I'm gone?"

If inner function needs any, it packs all of those into a backpack, and straps it to inner function. `__closure__` 

```py
def execution_timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[SYSTEM] '{func.__name__}' finished in {end - start:.4f} seconds.")
        return result
    return wrapper

def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Access Denied.")
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_incident_record(user, record_id):
    print(f"Record {record_id} deleted.")

def retry_on_fail(func):
    def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed. Retrying...")
                time.sleep(1)
        raise Exception("Function failed after 3 attempts.")
    return wrapper
```

```py
# 1. The Configurator
def retry_query(max_attempts=3, delay_seconds=1):
    # 2. The Decorator
    def decorator(func):
        # 3. The Wrapper
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[WARN] Connection failed. Attempt {attempts}/{max_attempts}. Retrying in {delay_seconds}s...")
                    time.sleep(delay_seconds)
            
            # If the loop finishes without returning, we failed completely
            raise ConnectionError(f"Failed to execute '{func.__name__}' after {max_attempts} attempts.")
        return wrapper
    return decorator
```

```py
@require_admin      # 2. Finally, the timer is wrapped by the security check
@execution_timer    # 1. First, the function is wrapped by the timer
def generate_shift_roster(user_role):
    time.sleep(1)
    return "Roster Generated."

# What happens when we call it?
# 1. Execution hits require_admin first. If the user isn't an admin, it crashes immediately.
# 2. If they are an admin, it passes through to execution_timer, which starts the clock.
# 3. The roster generates.
# 4. The clock stops.
```


```py
class RateLimiter:
def __init__(self, max_calls_per_minute):
    self.max_calls = max_calls_per_minute
    self.call_count = 0
    self.start_time = time.time()

# __call__ makes the class instance behave like a function
def __call__(self, func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_time = time.time()
            
        # Reset the counter if a minute has passed
        if current_time - self.start_time > 60:
            self.call_count = 0
            self.start_time = current_time
            
        # Block the call if limit exceeded
        if self.call_count >= self.max_calls:
            raise PermissionError(f"Rate limit exceeded: {self.max_calls} calls per minute.")
            
        self.call_count += 1
        print(f"[SYS] API Call {self.call_count}/{self.max_calls}")
        return func(*args, **kwargs)
            
    return wrapper
```


<br/><br/>

`time.sleep(n_seconds)`
`time.time()` - floating number; seconds passed since 01-01-1970; Say, you are running a program that takes 60 minutes; At time t=30m, if the system clock was reset to -30m, then the math will be wrong. 

`time.perf_counter()` - stopwatch; monotonic - can only go forward. 

`__exit__(self, exc_type, exc_value, traceback):` Python always passes these 3 arguments. These are None, if no exception happened. 

`yield` - when interpreter sees this, the execution stops, and returns a value. All local variables and state are preserved unlike destroy which happens when a function ends using `return`

These functions that use `yield` are called **Generators**

`from contextlib import contextmanager` - Decorator. Everything before `yield` is `__enter__` setup, `yield` pauses code, and returns control to the `with` block; everything after `yield` is the `__exit__` tear down. 

**Parameters:** Parking spot. Variable names in definition. 
**Arguments:**  Actual data (value) passed to function. 

***args** - Tuple Packer. Packs all **positional arguments.** 
****kwargs** - Dictionary Packer. Packs all **keyword arguments.**

**asterisk** - When used in definition, it packs stuff. When used in function calls, it unpacks stuff. 

**`func(pos_only, /, standard_arg, *, kw_only):`**

```py
@contextmanager
def code_timer(block_name):
    start = time.perf_counter()
    print(f"[START] {block_name}")
    
    try:
        yield 
        
    finally:
        end = time.perf_counter()
        print(f"[END] {block_name} finished in {end - start:.4f} seconds")

with code_timer("Data Processing"):
    print("Doing some heavy lifting...")
    time.sleep(1.5)
    print("Done!")
```


<br/><br/>

Type Hinting: 

```py
from collections.abc import Callable

# Callable[[InputTypes], ReturnType]
def execute_math_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    operation(a, b)

def add(x: int, y: int) -> int:
    return x + y
```

`id: int | None` - Allows None 
`id: int | None = None` - Optional 
`list[type]`
`dict[key_type, val_type]`
`tuple[type1, type2]`
`tuple[type, ...]` - Any Length, All Strings


`from typing import Any, Literal, Callable, Iterable, Sequence, Self`
- `def fetch_record(id: int | str):`
- `def set_mode(mode: Literal["read", "write"]):` Must match values too.
- `def parse_json(payload: Any):` Turns off the type checker for this variable. 
- `def wrapper(func: Callable[[int], str]):` expects a callable, function
- `def process_batch(items: Iterable[str]):` expects a loopable
- `def get_first(items: Sequence[int]):` Anything that has lenght, and can be accessible using index, not sets. 
- `Self` instance of class. 


<br/><br/>

**TOML** Tom's Obvious, Minimal Language

```toml
# This is a comment. TOML ignores this.

# Strings (Quotes are required)
name = "ccfd-rms-prototype"
author = 'Vinay D'

# Integers and Floats
timeout_seconds = 60
pi = 3.14159

# Booleans (Lowercase)
is_active = true
debug_mode = false

# Arrays (Lists)
supported_regions = ["US-East", "US-West", "EU-Central"]

# TOML Tables = Python Dictionaries. 
[project]
name = "vdutils"
version = "1.0.0"

[database]
host = "localhost"
port = 5432


# We want to configure the 'ruff' linter, which is a 'tool'
[tool.ruff]
line-length = 88

# We want to configure the specific 'format' settings inside 'ruff'
[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[[servers]]
name = "primary-db"
ip = "192.168.1.10"

[[servers]]
name = "replica-db"
ip = "192.168.1.11"
```

```py
{
    "servers": [
        {"name": "primary-db", "ip": "192.168.1.10"},
        {"name": "replica-db", "ip": "192.168.1.11"}
    ]
}

import tomllib

# Open the file in 'rb' (read binary) mode
with open("pyproject.toml", "rb") as f:
    config_dict = tomllib.load(f)

print(config_dict["project"]["name"])
```

<br/><br/>

**Emergent** not explicitly programmed or anticipated

Characteristics: Unpredictable, Threshold Dependent (after certain parameters), Quantitative Shift, Generalization

Few-Shot: Ask, Example -> Result
Zero-Shot: Ask -> Result
In-Context Learning
Complex Reasoning
Code Generation and Understanding
Common Sense and World Knowledge
Abstract Thinking and Metamorphical Understanding 
Translation and Multilingual Understanding
Social and Cultural Awareness
Tool Use and Instruction Following and API Integration
**Internal Reasoning** (Model itself knows if it neads reasoning) different from **Chain of Thought Prompting**



Scale as Driver, Diverse Data; Representation Learning; Phase Transition

Roughly At 7B, Emergent Capabilities arise. 

**Fine Tuning** makes a model obedient. 

**LLM** predict next token Understands context. This is hard. Not easy. 
**RAG** LLM + file or db
**AI Agents**

**Fuzzy** A set of algorithms that allows computer say, these are not exact matches but are similar to x%. 

**Levenshtein/Edit Distance** minimum number of char edits required to turn str A into str B. Edit = insert | delete | substitute

```py
# uv add thefuzz
from thefuzz import fuzz

# 1. Simple Ratio (Basic character-by-character comparison)
score1 = fuzz.ratio("Harbor Bridge", "Hbr Bridge")
print(score1) # Output: 78 (Not bad, but we can do better)

# 2. Partial Ratio (Great if one string is a subset of the other)
score2 = fuzz.partial_ratio("Robert Smith", "Rob")
print(score2) # Output: 100 (Because "Rob" is perfectly inside "Robert")

# 3. Token Sort Ratio (Ignores word order - amazing for names!)
score3 = fuzz.token_sort_ratio("Doe, John", "John Doe")
print(score3) # Output: 100
```


<br/><br/>

**Agent**
1. **Memory and Planning**
2. **Initiation of Actions** - Agentic Loop does this | While Loop
3. **Integration with External Tools**
4. **Ongoing Objectives**
5. **Advanced Functionality**

**Agent Characteristics**
1. Goal Directed Behavior - Has objectives; provide directions and purpose. 
2. Interactive capability - MCP
3. Autonomous Decision Making - Evaluate, Choose, Initiate.



<br/><br/>

**Reasoning Mechanisms:**
1. **Deductive Reasoning - Top Down Logic:** general rules (premises); rule + case = conclusion; if rules are true, conclusion must be true. 
2. **Inductive Reasoning - Bottom Up Logic:** observations, examples -> broad rule. conclusion is probable not mathematically guaranteed. specific cases -> inferred general rule. 
3. **Abductive Reasoning - Detective's Logic:** work your way backwards from a final result or incomplete observation set; logic of troubleshooting or medical diagnosis. Guess. 

**Memory Systems:**
1. **Working Memory** Immediate context, recent interactions. `conversation_history`
2. **Long Term Memory** Stores information across sessions. VectorDB etc. 

**Autonomous Action:**
1. **Action Space** Set of all actions agent can take. tools.
2. **Action Selection** which actions best serve goal. exploration vs exploitation (using proven methods)
3. **Execution**


<br/><br/>

1. Tools - **MCP (Anthropic) - Agent <-> Tools/APIs**
2. Agents - **A2A (Google) - Agent <-> Agent**
3. UI - **A2UI (Google, Declarative) / AG-UI(CopilotKit/Oracle/Microsoft, Streaming) - Agent <-> UI**


<br/><br/>

**Guardrails** models/scripts. sit between user, llm, and databases to enforce strict rules
1. Input Guardrails - sit between user and LLM
   1. Prompt Injection Detection
   2. PII Masking
   3. Topic Restriction
2. Output Guardrail 
   1. Format Enforcement
   2. Hallucination Checks

**Telemetry** How do we capture the LLM degrading quality. 
1. Token Tracking (Cost) - Syllables. 
2. Time to First Token (TTFT)
3. User Acceptance Rate 


**Deterministic** Same input produces same output. 
**Stochastic** Has randomness built-in but we can predict or analyze statistically over thousands of runs. 

**Temperature** 0 (turn of the rolling dice to choose next word) to 2.0;
**Top-P (Nucleus Sampling)** This tells model that it can role the dice but only among the top p%
**Setting a Seed**