# Qwen3-Coder Tool Parser Setup Instructions

## 1. Download the parser to your server:
wget https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/raw/main/qwen3coder_tool_parser.py

## 2. Restart vLLM with the Qwen3-Coder parser:
vllm serve Qwen/Qwen3-Coder-30B-A3B-Instruct \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_xml \
  --max-model-len 32768

## 3. The parser will automatically:
- Parse the XML format: <tool_call><function=name><parameter=key>value</parameter></function></tool_call>
- Convert it to standard OpenAI tool_calls format
- Handle streaming properly

## 4. Test with curl:
curl -s -H "Authorization: Bearer rasaipg2025lfg5512" \
  -H "Content-Type: application/json" \
  -d '{"model":"Qwen/Qwen3-Coder-30B-A3B-Instruct","messages":[{"role":"user","content":"Create a directory called testing"}],"tools":[{"type":"function","function":{"name":"run_shell_command","description":"Run a shell command","parameters":{"type":"object","properties":{"command":{"type":"string","description":"The shell command to run"}},"required":["command"]}}}],"tool_choice":"auto"}' \
  https://kimi.quantumdesk.io/v1/chat/completions
