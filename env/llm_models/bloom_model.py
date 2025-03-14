from transformers import BloomForConditionalGeneration, BloomTokenizerFast

class BloomModel:
    def __init__(self):
        self.model = BloomForConditionalGeneration.from_pretrained('bigscience/bloom-1b7')
        self.tokenizer = BloomTokenizerFast.from_pretrained('bigscience/bloom-1b7')

    def summarize(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(inputs['input_ids'])
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
