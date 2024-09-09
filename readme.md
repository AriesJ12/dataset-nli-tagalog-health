# your name choices
max - maxine
pb - phoebe
gen - rosgen
drex - drexler
bru - bruce
sha - shania


# how to get premises
1. Find a tagalog article regarding a diseases
2. Go to gpt and paste this(replace the article and url)

```
You are an AI designed to extract relevant information from text written in Tagalog. I will provide you with a text related to health topics, such as diseases, treatments, or public health guidelines. Your task is to identify and extract sentences or parts of sentences that directly relate to these health topics.

1. Extracted Content: Ensure that the extracted sentences are directly related to health and retain their original meaning as closely as possible. Make only minor adjustments if necessary for clarity. Perform coreference resolution if needed.

2. Output Format: Return the results in the following JSON format:

{
  "url": "[Insert URL here]",
  "premises": [
    {"premise": "[First health-related premise]"},
    {"premise": "[Second health-related premise]"},
    ...
  ]
}
3. Specific Instructions:
- Ensure that each premise is relevant to the health topic at hand.
- Avoid altering the original language unless absolutely necessary for clarity.
- Maintain the original meaning and context of the premises.
- Make sure to mention the disease in every premise.

Here is the url:
[Insert URL here]

Here is the article:

[Insert Article Text Here]
```

3. DONT FORGET TO DOUBLE CHECK, SOMETIMES HINDI NAGMAMAKE SENSE UNG INEEXTRACT NA TEXT

4. Paste the result to the premise.py


# how to use premise.py

1. change the input_json to your premises only valid is
{
    "url": URL_HERE,
    "premises": [
        {"premise": PREMISE_1},
        {"premise": PREMISE_2},
        {"premise": PREMISE_3}
    ]
}
2. Run
```
python premise.py
```



# how to use hypothesis.py

### pre req
- make sure you have ran the premise.py first/have a bunch of premises


1. Run
```
python hypothesis.py
```

2. Check the randomly selected premise and type
3. Type your hypothesis/claim based on the type (MAKE SURE TO NOT MAKE IT AI GENERATED, IT WILL CAUSE OVERFITTING)
4. enter
5. To cancel, press Ctrl + c




# to combine 2 premise files:
1. scroll down sa pinakababa.
2. palitan mo lang ung file1, file2 variables (kung ano ang icocombine mo)
- usually eto ung file na ginawa mo + file ng ibang kgrp
3. Run
```
python combine-premise.py
```




# to combine 2 hypothesis files:
1. scroll down sa pinakababa.
2. palitan mo lang ung file1, file2 variables (kung ano ang icocombine mo)
- usually eto ung file na ginawa mo + file ng ibang kagrp
3. Run
```
python combine-hypothesis.py
```