#HackSC
#Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhangm, Ying Sun

import openai
openai.api_key = "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"

def process_data(text_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful powerpoint slides maker, you can summerize the text into a slide deck."},
            {"role": "user", "content": "Convert the following text into a powerpoint, using JSON , keep all key points"},
            {"role": "user", "content": text_data}
        ]
    )

    markdown_text = response.choices[0].message

    return markdown_text

process_data("The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.")
# def prompt():
#     openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful summerizer. "},
#             {"role": "user", "content": "Summarize the following in markdown format."},
#         ]
#     )