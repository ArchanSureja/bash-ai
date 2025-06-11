## Bash-AI 
### AI powered bash terminal utility for natural language to command transalation

#### Model and dataset links: 
- Base Model : [Byt5-small model](https://huggingface.co/google/byt5-small) 
- Finetuned Model : [byt5-small-finetuned](https://huggingface.co/archan01/byt5-small-finetuned)  
- dataset : [nl2bash](https://huggingface.co/datasets/jiacheng-ye/nl2bash)

#### What is Byte Based Model: 
 - Traditional Model  relies on tokenizer that convert the words into tokens before processed by Model
 - Different languages word are hard to tokenize in same way
 - Byte Based Model tokenize at byte level , making it perfect for language translation tasks that requires very small details like punctuation marks and symbols
 - Bash command heavily relies on symbols making this model perfect for task

#### Advantages of Byte-to-Byte model : 
 - More accuracy as every token is byte
 - Robust to noise in data
 - Less embedding parameter (only 256 * embedding size) due to less vocabulary size
 - No need of advanced tokenization algorithms
   
#### Disadvanteges of Byte-to-Byte Model:
 - Better accuracy Comes at longer sequences
 - More parameters required dedicated for the attention part of transformers
 - More Computing resources required for training / fine tuning due to longer sequences

#### Related Research Paper : 
- [ByT5: Towards a token-free future with pre-trained byte-to-byte models](https://arxiv.org/abs/2105.13626)

#### installation : 
 - Clone Repository ```git clone https://github.com/ArchanSureja/bash-ai.git ```
 - Create a virtual environment ``` python3 -m venv .venv ```
 - Activate Virtual env ``` source .venv/bin/activate ```
 - Install requirements ``` pip install -r requirements.txt ```
 - Run Script ``` python3 bashai.py ```

#### NOTE :
  - Generated Command can be wrong and harmful to execute , always review command before execution
    
#### screenshots : 
![image](https://github.com/user-attachments/assets/58929732-e693-4ff2-b36a-71be5b5d9f12)
![image](https://github.com/user-attachments/assets/35ae368f-9625-48d6-a263-d7ad2837abf9)



