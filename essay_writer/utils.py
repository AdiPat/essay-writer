def get_max_output_tokens(model_name: str) -> int:
    """
    Returns the maximum number of output tokens for a given OpenAI model.

    Parameters:
    model_name (str): The name of the OpenAI model.

    Returns:
    int: The maximum number of output tokens for the specified model.
    """
    model_token_limits = {
        "gpt-3.5-turbo": 4096,  # GPT-3.5 Turbo has a context window of 4,096 tokens.
        "gpt-3.5-turbo-16k": 16384,  # GPT-3.5 Turbo 16k supports up to 16,384 tokens.
        "gpt-4": 8192,  # GPT-4 has a context window of 8,192 tokens.
        "gpt-4-32k": 32768,  # GPT-4 32k supports up to 32,768 tokens.
        "gpt-4o": 4096,  # GPT-4o has an output token limit of 4,096 tokens.
        "gpt-4o-mini": 16384,  # GPT-4o-mini supports up to 16,384 output tokens.
        "gpt-4o-turbo": 128000,  # GPT-4o-turbo has a context window of 128,000 tokens.
        "gpt-4o-128k": 128000,  # GPT-4o-128k has a context window of 128,000 tokens.
        "gpt-4o-128k-chat": 128000,  # GPT-4o-128k-chat supports up to 128,000 tokens.
        "gpt-4o-128k-text": 128000,  # GPT-4o-128k-text has a context window of 128,000 tokens.
    }

    return model_token_limits.get(
        model_name, 4096
    )  # Default to 4,096 tokens if the model is not found.
