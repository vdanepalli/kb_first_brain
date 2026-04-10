## Session 1: Introduction

### Coresets & Data Efficiency
#### Intuition
A "smart" representative subset of a massive dataset. It aims to reduce data volume while preserving the statistical integrity and loss surface of the full dataset.
#### Technical Details
- **Selection:** Uses <font color="#FF5733">sensitivity scoring</font> to identify "important" points (e.g., points near decision boundaries).
- **Weighting:** Each point in the coreset is weighted to represent the density of the original points it replaced.
- **Benefit:** Drastic reduction in *training time* and *computational cost*.

### Multi-GPU ImageNet Training
#### Intuition
Distributing the massive ImageNet workload across multiple accelerators to reduce training time from weeks to hours or minutes.
#### Technical Details
- **Distributed Data Parallel (DDP):** Each GPU processes a unique shard of the data. 
- **All-Reduce:** A communication primitive where all GPUs <font color="#33FF57">sum/average gradients</font> before updating weights.
- **Linear Scaling:** The goal is to achieve $N\times$ speedup with $N$ GPUs, though limited by *interconnect bandwidth*.

### Quantization Aware Training (QAT)
#### Intuition
Training a model while simulating the "rounding errors" it will face when converted to 8-bit integers for deployment.
#### Technical Details
- **Fake Quantization:** Simulates <font color="#3357FF">INT8 precision</font> during the forward pass while maintaining FP32 for gradient updates.
- **STE (Straight-Through Estimator):** Allows gradients to bypass the non-differentiable rounding operation.
- **Outcome:** Minimizes "quantization gap" (accuracy drop) compared to Post-Training Quantization (PTQ).

---

**Initial Query:** *what are coresets - data efficiency multi-gpu imagenet training qat - quantization aware training*

#### 1. <span style="color:#2ecc71">Coresets (Data Efficiency)</span>
* **Concept:** A highly optimized, weighted subset of data that mathematically approximates the full dataset.
* **Goal:** Train models significantly faster by removing redundant data *without* dropping accuracy.
* **Key Mechanic:** Uses heuristic algorithms to identify representative points; acts as a smart filter rather than just random sampling.
* **Gotcha:** Finding the coreset can be computationally expensive; risk of under-representing minority classes (bias).
* > *Layman Example:* Instead of reading 1,000 varying reviews of a restaurant to understand its quality, you read 5 perfectly selected reviews that summarize every unique point made by the larger group.

#### 2. <span style="color:#3498db">Multi-GPU ImageNet Training (Distributed Training)</span>
* **Concept:** Splitting a massive dataset (like ImageNet) across multiple GPUs (Distributed Data Parallelism) to train a model in a fraction of the time.
* **Goal:** Reduce training time from weeks to hours/minutes.
* **Key Mechanic:** Each GPU calculates gradients on its own data chunk. Gradients are then averaged across all GPUs (via **Ring All-Reduce**) before updating the model weights.
* **Gotcha:** Network communication bottleneck. High global batch sizes require specialized learning rate scaling (like the **LARS optimizer**) to maintain generalization.
* > *Layman Example:* Instead of one painter painting a massive mural, 8 painters take different sections. They pause every hour to look at each other's progress and ensure their styles and colors perfectly match before continuing.

#### 3. <span style="color:#e74c3c">QAT (Quantization Aware Training)</span>
* **Concept:** Simulating lower precision (e.g., INT8) during the FP32 training process using "fake quantization" nodes.
* **Goal:** Prepare a model for low-precision edge deployment without sacrificing accuracy.
* **Key Mechanic:** Forward pass simulates the rounding/clipping of INT8. Backward pass computes gradients in FP32 using the **Straight-Through Estimator**. The model learns to be robust against precision loss.
* **Gotcha:** Complex to engineer. Slows down training time. Always try **Post-Training Quantization (PTQ)** first; only use QAT if PTQ breaks the model.
* > *Layman Example:* Practicing a speech with marbles in your mouth (simulated limitation). By the time you actually have to give the speech with marbles (edge deployment), you've already adapted your pronunciation to sound perfectly clear.


<br/><br/>
<br/><br/>

---



### LoRA (Low-Rank Adaptation)
#### Intuition
Adapting massive models by adding small, trainable "rank decomposition" matrices instead of updating all weights.
#### Technical Details
- **Freezing:** Original weights $W$ are frozen ($\nabla W = 0$).
- **Update:** $ \Delta W = B \times A $, where $A \in \mathbb{R}^{r \times k}$ and $B \in \mathbb{R}^{d \times r}$ with <font color="#FF5733">rank r ≪ d</font>.
- **Benefit:** Massive reduction in VRAM and storage for checkpoints.

### PEFT (Parameter-Efficient Fine-Tuning)
#### Intuition
An umbrella term for techniques that tune <1% of a model's parameters to achieve performance comparable to full fine-tuning.
#### Technical Details
- **Categories:** Includes <font color="#33FF57">Additive</font> (adapters/LoRA), <font color="#33FF57">Selective</font> (BitFit), and <font color="#33FF57">Reparameterization</font> (LoRA).
- **Core Value:** Prevents catastrophic forgetting and enables multi-task deployment via lightweight "swappable" adapters.

### Reinforcement Learning (RL)
#### Intuition
Learning through trial and error to maximize a cumulative reward signal.
#### Technical Details
- **Components:** Agent, Environment, State ($S$), Action ($A$), and Reward ($R$).
- **Policy ($\pi$):** The strategy the agent uses to determine the next action based on the current state.
- **Bellman Equation:** The fundamental recursive step for calculating <font color="#3357FF">Value Functions</font>.

### VLMs (Vision-Language Models)
#### Intuition
Multimodal models capable of processing and reasoning across both visual and textual data.
#### Technical Details
- **Cross-Modal Alignment:** Uses a <font color="#FF33E9">projection layer</font> to map visual features into the same embedding space as text tokens.
- **Common Backbones:** CLIP (Vision Encoder) paired with an LLM (e.g., LLaVA, Flamingo).

### Embeddings
#### Intuition
Converting discrete data (text/images) into continuous high-dimensional vectors that capture semantic meaning.
#### Technical Details
- **Geometric Relationship:** Distance in vector space (Euclidean or Cosine) represents <font color="#FFBD33">semantic similarity</font>.
- **Dimensionality:** Typically ranges from 768 to 1536+ dimensions in modern transformer models.
- **Utility:** Core component for Semantic Search and RAG (Retrieval-Augmented Generation).

---

**Initial Query:** *LoRA PEFT Reinforcement Learning VLMs Embeddings*

#### 1. <span style="color:#2ecc71">LoRA (Low-Rank Adaptation)</span>
* **Concept:** Injecting tiny, trainable **rank-decomposition matrices** into a frozen model to update weights efficiently.
* **Goal:** Fine-tune massive models on consumer-grade hardware.
* **Key Mechanic:** Approximates large matrix updates using two smaller matrices ($d \times r$ and $r \times d$).
* **Gotcha:** Hard to find the optimal rank ($r$); not ideal for teaching completely new fundamental knowledge.
* > *Layman Example:* Instead of rewriting an entire massive textbook to make an update, you just write a transparent sticky note and place it over the specific page.

#### 2. <span style="color:#3498db">PEFT (Parameter-Efficient Fine-Tuning)</span>
* **Concept:** The umbrella term for adapting models by updating only a tiny fraction (often **<1%**) of parameters.
* **Goal:** Enable highly scalable, multi-tenant AI deployments.
* **Key Mechanic:** Keeps a large base model frozen in memory and dynamically swaps small **adapters** in and out based on the task.
* **Gotcha:** Adds complexity to the inference pipeline; adapters can conflict if stacked improperly.
* > *Layman Example:* A drill (base model) stays the same, but you quickly swap out different tiny drill bits (adapters) depending on whether you are drilling wood, metal, or concrete.

#### 3. <span style="color:#e74c3c">Reinforcement Learning (RL / RLHF)</span>
* **Concept:** Training an agent (or LLM) to maximize a **reward function** through trial and error.
* **Goal:** Align models with human preferences and safe behaviors.
* **Key Mechanic:** Uses algorithms like **PPO** to update the model based on a separate "reward model" trained on human feedback.
* **Gotcha:** Highly unstable; models often engage in **reward hacking** (finding lazy loopholes to get points).
* > *Layman Example:* Training a dog with treats. If you aren't careful, the dog learns to just sit and stare at the treat bag (reward hacking) instead of actually fetching the newspaper.

#### 4. <span style="color:#9b59b6">VLMs (Vision-Language Models)</span>
* **Concept:** Multimodal architectures combining a **vision encoder** with an **LLM backbone**.
* **Goal:** Allow AI to "see" and reason about images, charts, and video alongside text.
* **Key Mechanic:** Converts pixels into visual tokens that the LLM processes exactly like word tokens.
* **Gotcha:** Extremely expensive inference (images equal lots of tokens); prone to **visual hallucinations**.
* > *Layman Example:* Giving a brain (the LLM) a pair of highly advanced eyes (the vision encoder) so it can describe a painting instead of just reading about it.

#### 5. <span style="color:#f1c40f">Embeddings</span>
* **Concept:** Translating raw data (text, images) into dense arrays of numbers (**vectors**) in high-dimensional space.
* **Goal:** Enable machines to mathematically measure semantic similarity.
* **Key Mechanic:** Similar concepts end up grouped together in vector space; measured using **cosine similarity**. The backbone of **RAG pipelines** and vector databases.
* **Gotcha:** General embedding models fail on niche jargon; retrieval quality relies heavily on your text **chunking strategy**.
* > *Layman Example:* Plotting library books on a massive 3D map. Books about cooking are placed physically close together, while books about quantum physics are placed on the exact opposite side of the map.


<br/><br/>
<br/><br/>

---



### Receptive Fields & Context Spans
#### Intuition
The "vision/memory window" of a model. In CNNs, it's local and grows deeper; in Transformers, it's global but computationally expensive.
#### Technical Details
- **CNN Receptive Field:** Determined by <font color="#FF5733">kernel size, stride, and padding</font>.
- **Attention Span:** Limited by the <font color="#FF5733">Context Window</font> length (n). Complexity is $O(n^2)$ unless using sparse/linear attention.

### JPEG & DCT (Discrete Cosine Transform)
#### Intuition
JPEG breaks images into 8x8 blocks and uses DCT to store "frequencies" instead of raw pixels. We can delete high-frequency data (fine detail) that humans can't see anyway.
#### Technical Details
- **The 8x8 Choice:** A balance between <font color="#33FF57">local stationarity</font> (pixels being similar) and <font color="#33FF57">computational efficiency</font>.
- **Quantization:** The step where lossy compression actually happens by dividing DCT coefficients by a "quality matrix."

### Fourier & SVD
#### Intuition
**Fourier:** Any signal is a sum of sines. 
**SVD:** Any matrix can be compressed by keeping only its most "powerful" components (Singular Values).
#### Technical Details
- **Fourier Transform:** Maps signal from <font color="#3357FF">Time/Space Domain → Frequency Domain</font>.
- **SVD Formula:** $A = U\Sigma V^T$. 
- **Rank-k Approximation:** $A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$. Used for noise reduction and compression.

### Feature Hierarchy (Representation Learning)
#### Intuition
The progressive steps a model takes to understand an image, moving from pixels to semantic meaning.
#### Hierarchy
- **Low-Level:** <font color="#FFBD33">Gradients and Edges</font> (Gabor filters).
- **Mid-Level:** <font color="#FFBD33">Textures and Motifs</font> (circles, grids).
- **High-Level:** <font color="#FFBD33">Parts and Whole Objects</font> (faces, buildings).

### Spatial Frequency in Images
#### Intuition
Frequency refers to the **rate of change** in pixel intensity across space.
- **High Frequency:** Rapid changes over small distances (Edges, Texture, Detail).
- **Low Frequency:** Slow changes over large distances (Gradients, Global shapes, Color blobs).

#### Technical Details
- **Edges as High Freq:** An edge is a <font color="#FF5733">mathematical discontinuity</font>. Moving one pixel across an edge causes a massive jump in value, which requires high-frequency waves to represent.
- **Filtering:** - **Low-pass filter:** Removes high freq, resulting in a <font color="#33FF57">blurred image</font>.
  - **High-pass filter:** Removes low freq, resulting in an <font color="#3357FF">edge-detected image</font> (looks like a pencil sketch).
- **Compression:** JPEG exploits human vision by heavily <font color="#FFBD33">quantizing (compressing)</font> high-frequency coefficients more than low-frequency ones.


---

**Initial Query:** *receptive fields - images and attention spans - text context jpeg image compression dct discrete cosine transforms -- 64, can make any picture why 8x8 and not 16x16; how did one arrive at 8x8 is enough what are fourier svd - rank approximation edges and gradients textures and patterns part of objects objects*

#### 1. <span style="color:#2ecc71">Receptive Fields vs. Context Spans</span>
* **Concept:** The model's "horizon." **Receptive fields** are the 2D spatial pixel area a CNN neuron can see. **Context/Attention spans** are the 1D text token limit an LLM can process.
* **Goal:** Ensure the model has enough raw input context to make an accurate prediction.
* **Gotcha:** LLMs with massive context windows suffer from "Lost in the Middle" (forgetting center text).
* > *Layman Example:* Receptive field is looking through a peephole vs. a bay window. Attention span is trying to remember the last 5 words spoken to you vs. the last 5 hours of conversation.

#### 2. <span style="color:#3498db">JPEG & DCT (Discrete Cosine Transforms)</span>
* **Concept:** Converts an image into the frequency domain. Splits the image into $8 \times 8$ blocks and maps them to a weighted sum of **64 basis functions** (cosine waves).
* **Goal:** Massive file compression by heavily rounding (quantizing) and deleting high-frequency data.
* **Gotcha:** Destroys sharp edges; causes "ringing/mosquito noise" around text.
* > *Layman Example:* Instead of sending a detailed map of every blade of grass, you just send the message "it's mostly green here" (low frequency) and drop the exact leaf outlines (high frequency). 

#### 3. <span style="color:#e74c3c">Why 8x8 Blocks?</span>
* **Concept:** A hardware/math compromise from 1992. 
* **Goal:** Fit the DCT calculations into tiny CPU L1 caches (64 operations vs 256 for $16 \times 16$).
* **Gotcha:** Causes rigid, visible "blocky" artifacts in smooth gradients (like skies) because adjacent blocks don't perfectly align.

#### 4. <span style="color:#9b59b6">Fourier Transforms</span>
* **Concept:** Math that converts any complex signal into a sum of simple sine/cosine waves. Moves data from the Time/Space domain to the **Frequency domain**.
* **Goal:** Isolate, analyze, or delete specific frequencies (like noise cancellation).
* **Gotcha:** You lose time localization (you know a frequency exists, but not *when* it happened).

#### 5. <span style="color:#f1c40f">SVD & Rank Approximation</span>
* **Concept:** Factoring a matrix into three parts to find the **singular values** (the most important mathematical structures). 
* **Goal:** Compress matrices by dropping the lowest singular values (**Low-Rank Approximation**) while keeping 99% of the meaning.
* **Gotcha:** Exact SVD is incredibly slow ($O(N^3)$). Deep learning usually approximates this via gradient descent (which is exactly what LoRA does).

#### 6. <span style="color:#e67e22">Hierarchical Feature Learning</span>
* **Concept:** Deep CNNs learn reality in layers: **Edges $\rightarrow$ Textures $\rightarrow$ Parts $\rightarrow$ Objects**.
* **Goal:** Enables **Transfer Learning** (reusing the edge/texture layers for totally new tasks).
* **Gotcha:** Shortcut learning. The model might memorize the texture of grass to identify a cow, and fail entirely if the cow is on a road.


<br/><br/>
<br/><br/>

---

### Biological Vision & Sensors
#### Intuition
The eye captures light; the back of the brain (Occipital Lobe) interprets features.
#### Technical Details
- **Rods:** Sensitive to <font color="#FFBD33">Luminance (Light/Dark)</font>; 120M per eye; peripheral.
- **Cones:** Sensitive to <font color="#FF5733">Chrominance (Color)</font>; 6M per eye; concentrated in the Fovea.
- **Processing:** Data flows to V1 (Primary Visual Cortex) to begin edge detection.

### Color Spaces
#### Comparison
- **RGB:** Additive (Light). Standard for <font color="#3357FF">CV Models</font>.
- **CMYK:** Subtractive (Pigment). Standard for <font color="#3357FF">Physical Printing</font>.
- **YIQ/YUV:** Separates <font color="#33FF57">Brightness (Y)</font> from Color. Crucial for video compression.
- **HSV:** Intuitive for human selection (Hue, Saturation, Value).

### CNN Architecture: Channels & Kernels
#### Definitions
- **Channel:** A specific "slice" of data (e.g., the Red slice, or the "Vertical Edge" slice).
- **Kernel (Filter):** A matrix of weights that <font color="#FF5733">extracts features</font> via convolution.
#### Connectivity
- Each output channel is the result of a **unique kernel**.
- **Cross-channel communication:** Kernels do not see each other's weights during inference, but their gradients are optimized together during <font color="#FFBD33">Backpropagation</font>.

### Multimodal AI
#### Intuition
AI that processes multiple data types (text, image, audio) into a unified representation.
#### Technical Details
- **Shared Latent Space:** Mapping different modalities into a <font color="#33FF57">common vector space</font> so the model "understands" the relationship between a photo and a description.


### Latent Space
#### Intuition
The "compressed representation" of data. It is a high-dimensional mathematical map where the model stores the essential features of an object rather than raw pixels/text.
#### Technical Details
- **Compression:** Maps high-dimensional input ($x$) to a lower-dimensional <font color="#FF5733">bottleneck layer</font> ($z$).
- **Vectors:** Every point in this space is a vector. Distance between vectors represents <font color="#FF5733">semantic similarity</font>.
- **Generative Power:** In models like VAEs or Diffusion, we "sample" a point from this space to create a new, never-before-seen image.

### Shared Latent Space
#### Intuition
A universal coordinate system where different modalities (images, text, audio) are <font color="#33FF57">mathematically aligned</font>.
#### Technical Details
- **Cross-Modal Retrieval:** Allows searching for images using text because they share the same "address" in the latent space.
- **Contrastive Loss:** Uses techniques like <font color="#3357FF">InfoNCE loss</font> to maximize the cosine similarity between related pairs (e.g., image of a car + word "car").
- **Utility:** The foundation for DALL-E, Midjourney, and Multimodal LLMs.


---

### 🧠 Advanced Applied AI Concepts Cheatsheet

**Initial Query:** *brain fires outside to inside data goes to back of the head eye the black thing in the middle sensors or cones - bulbs, rods 20 to 1 neurons rgb, cmy, cmyk, yiq, hsv, hls channel - whole interpretation - similar data put together kernel - what extracts the data and puts inside channel; feature|function identifies information and puts inside channel do each channel have its own kernel does one kernel know about other kernel multimodal*

#### 1. <span style="color:#2ecc71">Biological Vision (The Blueprint for AI)</span>
* **Concept:** Light enters the **pupil** (the hole) and hits the retina. **Cones** (color/detail) and **Rods** (light/motion) exist at a ~1:20 ratio. Signal travels to the **Occipital Lobe** at the back of the head.
* **Goal:** Extract visual features hierarchically.
* **Key Mechanic:** The retina is inverted. Neurons fire "outside-in" (forward) to the optic nerve.
* **Gotcha:** Creates a biological blind spot; brain inpaints missing data.
* > *Layman Example:* Your eye is a camera where the wiring was accidentally installed *in front* of the lens, so the cable has to punch a hole through the back of the camera to reach the hard drive (brain).

#### 2. <span style="color:#3498db">Color Spaces (Math of Light)</span>
* **Concept:** Mathematical representations of color.
    * **RGB:** Light additive (Screens).
    * **CMYK:** Ink subtractive (Print).
    * **YIQ:** Luma + Chroma (Bandwidth compression for TV).
    * **HSV/HLS:** Hue, Saturation, Value (Human perception).
* **Goal:** Optimize data for specific hardware or tasks.
* **Gotcha:** Color thresholding in RGB is highly unstable under changing light. Always use **HSV** for computer vision.
* > *Layman Example:* RGB is trying to explain a color to a computer by mixing flashlights. HSV is explaining it to a human: "It's red, make it deeper, now make it darker."

#### 3. <span style="color:#e74c3c">CNNs: Channels & Kernels</span>
* **Concept:** **Channels** hold similar data (feature maps). **Kernels** (filters) are the matrices that extract that data.
* **Goal:** Identify spatial hierarchies (edges -> shapes -> objects).
* **Key Mechanics:** * A standard filter looks across *all* input channels simultaneously to output *one* new channel.
    * Kernels are totally blind to each other; they do not communicate.
* **Gotcha:** Blind kernels can become redundant ("dead filters"). Use network pruning to optimize.
* > *Layman Example:* Kernels are like independent detectives looking at a crime scene (Channel). One only looks for fingerprints, another only looks for footprints. They don't talk to each other, but the chief (Backpropagation) ensures they don't do the same job.

#### 4. <span style="color:#9b59b6">Multimodal AI</span>
* **Concept:** AI that processes text, vision, and audio natively in a **shared latent space**.
* **Goal:** Reason across different data types simultaneously without disjointed models.
* **Key Mechanic:** Aligns different modalities mathematically (image of a dog = text of "dog" = audio of bark).
* **Gotcha:** Massive token disparity. Images eat up context windows vastly faster than text, spiking inference costs.
* > *Layman Example:* Instead of having one translator for French and one for Spanish, you have a single bilingual brain that natively understands both languages as the exact same underlying concepts.


<br/><br/>


<br/><br/>


---



### Eigenvalues & Fourier
#### Intuition
**Eigenvalues:** Measure the "strength" of a specific direction in data. 
**Fourier:** Decomposes any signal into fundamental frequencies (sine waves).
#### Technical Details
- **Non-linear combination:** The use of <font color="#FF5733">Activation Functions</font> (ReLU, GeLU) to break linear limits.
- **SVD connection:** Eigenvalues are the squares of Singular Values in SVD.

### Channels vs. Dimensions
#### Intuition
They are often used interchangeably. A channel is a single "feature map" in a specific dimension of the latent space.
#### Technical Details
- **Bottleneck:** An architecture where <font color="#33FF57">Encoding dim > Latent dim < Decoding dim</font>.
- **Embedding Dim:** The fixed vector length (e.g., 512, 768, 1536) used to represent a token.

### Kernels: The Feature Detectors
#### Responsibility
To extract specific spatial features (edges, textures) via the convolution operation.
#### Lifecycle
- **Before training:** Kernels are <font color="#3357FF">random noise</font>.
- **During training:** Weights are updated via backpropagation.
- **After training:** Kernels become <font color="#3357FF">fixed feature detectors</font> (e.g., a Gabor filter for edges).
#### Decision Maker
- **Hyperparameters:** *We* decide the number of kernels (width) and layers (depth).
- **Parameters:** The *Model* learns the actual values inside the kernels.

### Receptive Fields & Biology
#### Intuition
The area of the input that "matters" to a specific neuron/pixel in a deep layer.
#### Technical Details
- **Growth:** Increases linearly with depth: $RF_{new} = RF_{old} + (k-1) \times stride$.
- **Retinotopic Mapping:** The biological equivalent where <font color="#FFBD33">spatial topology</font> is preserved from the eye to the visual cortex.
- **Dimensionality:** Can be 1D (audio/text), 2D (images), or 3D (video/volumetric scans).

### Mixture of Experts (MoE)
#### Intuition
A "divide and conquer" architecture.
#### Technical Details
- **Router:** A gating network that selects the top-$k$ experts for a given input.
- **Sparsity:** Only a fraction of total parameters are active per token, enabling <font color="#FF5733">massive scale</font> with lower inference cost.


---


#### 1. <span style="color:#2ecc71">Math Foundations</span>
* **Eigenvalues:** Scalars representing how much an **eigenvector** stretches/shrinks during linear transformation.
* **Non-Linear Combinations:** Applying curves (ReLU, Tanh) to data. *Without this, any deep network mathematically collapses into a single flat layer.*
* **Encoding/Decoding Dimensions:** Can be vastly different. Autoencoders compress high-dimensional inputs to low-dimensional bottlenecks.

#### 2. <span style="color:#3498db">Channels, Dimensions, and Embeddings</span>
* **Dimensionality:** General math term for the number of axes/features.
* **Channels:** A specific type of dimension in CNNs holding feature maps (e.g., RGB = 3). **We (engineers) decide the channel count.**
* **Embeddings:** The size of the vector representing a text token.

#### 3. <span style="color:#e74c3c">Kernels vs. Tokens & The Kernel Lifecycle</span>
* **Misconception Check:** Kernels are **NOT** tokens. Tokens are data; Kernels are the mathematical functions/weights processing the data.
* **Definition:** We define the shape/amount of kernels. The model learns the actual numbers via backpropagation.
* **Lifecycle:** They start as random, useless numbers. Post-training, they become specific feature detectors (looking like tiny edges or checkerboards).

#### 4. <span style="color:#9b59b6">Network Architecture & Receptive Fields</span>
* **Misconception Check:** Networks do **NOT** have a fixed 4 layers. They can have any number, dictated by the engineer.
* **Receptive Field:** The spatial chunk of data a neuron looks at. Grows as layers get deeper. **Rule:** *Must be larger than the object you want to detect.*
* **Dimensions:** Not always 2D. 1D (audio/text), 2D (images), 3D (video/medical scans).

#### 5. <span style="color:#f1c40f">Retinotopic Maps & fMRI</span>
* **Concept:** Spatial relationships in the real world are preserved in the physical layout of the brain's visual cortex. fMRI can see the physical shape of what you are looking at light up in your brain.
* **Impact:** The biological inspiration for CNN spatial feature maps.

#### 6. <span style="color:#e67e22">Mixture of Experts (MoE)</span>
* **Concept:** A router sends input tokens to specialized sub-networks ("experts") rather than using the whole model.
* **Goal:** High intelligence (massive total parameters) with fast inference (low active parameters).
* **Gotcha:** Requires massive VRAM to hold all experts in memory.


<br/><br/>
<br/><br/>

---

### Parameter Efficiency: CNN vs. FC
#### Intuition
CNNs use "Weight Sharing" to detect features anywhere in an image using very few parameters.
#### Technical Details
- **FC Layer:** $Input \times Output$ parameters. High memory, <font color="#FF5733">no spatial awareness</font>.
- **Conv Layer:** $Kernel\_Size \times Kernel\_Size$ parameters. Low memory, <font color="#33FF57">translation invariant</font> (finds a face whether it's in the corner or the center).

### Fully Connected (FC) Layers
#### Responsibility
The "Reasoning" layer. It maps the extracted features to the final output (e.g., Class: Dog vs. Cat).
#### Technical Details
- Also called **Dense Layers** or **MLPs** (Multi-Layer Perceptrons).
- Unlike Convolutions, they have a <font color="#3357FF">Global Receptive Field</font> (they see all inputs at once).

### Transformers vs. CNNs
#### Comparison
- **CNNs:** Use local kernels. Best for <font color="#FFBD33">Spatial data</font> (Images).
- **Transformers:** Use Self-Attention. Best for <font color="#FFBD33">Sequential/Contextual data</font> (Text).
- **The Shift:** In Transformers, "Context Window" replaces the concept of a fixed geometric receptive field.

### Universal Approximation Theorem
#### Intuition
A mathematical proof that neural networks can solve any problem if they are big enough and have non-linearity.
#### Technical Details
- Requires at least one hidden layer and a <font color="#FF5733">non-linear activation function</font> (like Sigmoid or ReLU).
- Proves that NNs are "Universal Function Approximators."

### Mapping Summary
- **Channels ($n$):** The number of different "features" we are looking for.
- **Kernels ($n$):** The specific weights that create those channels.
- **Relationship:** 1 Kernel $\to$ produces $\to$ 1 Channel.

----


**Initial Query:** *for 100x100 to be processed at once -- we need 100x100 params. but if we were to use 3x3 layers from 100 to 1 -- we need 450 params? example: face recognition model: models still detect everything but filters out everything to detect jsut faces? what does a fully connected layer do. what receptive field is for images; context or attention span is for text. LLMs are only using fully connected layers; not convolutions. nkernels represent nchannels; what is universal approximation theorem*

#### 1. <span style="color:#2ecc71">Parameter Efficiency (Weight Sharing)</span>
* **Concept:** Reaching a 1x1 output from a 100x100 input requires 10,000 params (Dense) vs. ~450 params (50 layers of 3x3 Convolutions).
* **Goal:** Reduce memory and prevent overfitting by sliding a small rule (kernel) over the whole image.
* **Gotcha:** 50 sequential layers are computationally heavier to process (latency) and suffer from vanishing gradients compared to a single dense layer.

#### 2. <span style="color:#3498db">Midway Feature Extraction</span>
* **Concept:** Middle layers of a CNN don't recognize specific objects (cars/dogs); they recognize universal geometry (curves, textures, circles). 
* **Goal:** Enables **Transfer Learning**. You can reuse these universal middle layers for totally different visual tasks.
* **Gotcha:** Overly constrained training data will cause middle layers to memorize backgrounds instead of universal geometry.

#### 3. <span style="color:#e74c3c">Fully Connected (Dense) Layers</span>
* **Concept:** The "Decision Maker" of the network. Connects every extracted feature to every output class.
* **Goal:** Calculate the final probabilities/correlations (e.g., Feature A + Feature B = Dog).
* **Gotcha:** Massive parameter hogs. They bloat model size while doing very little "spatial" reasoning.

#### 4. <span style="color:#9b59b6">LLMs: Attention vs. Convolutions</span>
* **Concept:** Receptive Field (CV) is perfectly analogous to Context Span (NLP).
* **Key Mechanic:** Transformers use **Self-Attention** (weighing every word against every word) + **Fully Connected** layers. They do *not* use convolutions.
* **Gotcha:** Because there are no convolutions sliding left-to-right, LLMs have no concept of word order without injecting **Positional Encodings**.

#### 5. <span style="color:#f1c40f">Kernels and Channels</span>
* **Concept:** $n_{kernels}$ = $n_{output\_channels}$. If you apply 64 kernels to an image, you get an output tensor with 64 channels.
* **Goal:** Each kernel extracts a distinct feature and deposits it into its own dedicated channel.
* **Gotcha:** A 2D kernel is actually 3D; it spans the full depth of the *input* channels (e.g., $3 \times 3 \times 3_{RGB}$).

#### 6. <span style="color:#e67e22">Universal Approximation Theorem</span>
* **Concept:** The mathematical proof that a neural network with just one hidden layer can map *any* continuous input to *any* output.
* **Goal:** Proves neural networks are universal function approximators.
* **Gotcha:** Proves a solution *exists*, but does not guarantee that Backpropagation will actually be able to *find* it (local minima).


<br/><br/>
<br/><br/>


Simon Wilson
