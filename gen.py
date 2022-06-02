import glob
import logging
import os
import pickle
import random
import re
import shutil
from typing import Dict, List, Tuple

import pandas as pd
import numpy as np
import torch

from sklearn.model_selection import train_test_split

from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset, RandomSampler, SequentialSampler
from torch.utils.data.distributed import DistributedSampler
from tqdm.notebook import tqdm, trange

from pathlib import Path


from transformers import (
    MODEL_WITH_LM_HEAD_MAPPING,
    WEIGHTS_NAME,
    AdamW,
    AutoConfig,
    AutoModelWithLMHead,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    get_linear_schedule_with_warmup,
)

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium')
model = AutoModelWithLMHead.from_pretrained('output-medium')

# Let's chat for 5 lines
while True:
  for step in range(1):
      # encode the new user input, add the eos_token and return a tensor in Pytorch
      new_user_input_ids = tokenizer.encode("Teacher_FUNGI : "+input(">> User:") + tokenizer.eos_token + "\nStudent_FUNGI : ", return_tensors='pt')

      # append the new user input tokens to the chat history
      print(step)
      bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
      #start = time.time()
      # generated a response while limiting the total chat history to 1000 tokens, 
      chat_history_ids = model.generate(
          bot_input_ids, max_length=200,
          pad_token_id=tokenizer.eos_token_id,  
          no_repeat_ngram_size=3,      
          do_sample=True, 
          top_k=50, 
          top_p=0.7,
          temperature = 0.2
      )
      #end = time.time()
      #pretty print last ouput tokens from bot
      #print("TestBot: {}".format(tokenizer.decode(chat_history_ids[0], skip_special_tokens=False)))
      print("Student: {} Time {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True), 1.0))
