from haystack.components.generators import HuggingFaceAPIGenerator
from haystack.utils import Secret



generator = HuggingFaceAPIGenerator(api_type="serverless_inference_api",
                                        api_params={"model": "meta-llama/Llama-3.2-1B-Instruct"},
                                        token=Secret.from_token("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"))