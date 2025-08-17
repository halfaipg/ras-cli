import { ContentGenerator, ContentGeneratorConfig, AuthType } from './contentGenerator.js';
import { Config } from '../config/config.js';

// Define the tool call interface based on the OpenAI pattern
interface Qwen3ToolCall {
  id: string;
  type: 'function';
  function: {
    name: string;
    arguments: string;
  };
}

export interface Qwen3XmlContentGeneratorConfig extends ContentGeneratorConfig {
  enableQwen3XmlParsing: boolean;
}

export class Qwen3XmlContentGenerator implements ContentGenerator {
  private enableQwen3XmlParsing: boolean;
  private config: Config;
  private model: string;

  constructor(config: Qwen3XmlContentGeneratorConfig, rasConfig: Config) {
    this.enableQwen3XmlParsing = config.enableQwen3XmlParsing;
    this.config = rasConfig;
    this.model = config.model;
  }

  /**
   * Parse Qwen3 XML tool calls from the model response
   * Format: <tool_call><function=function_name><parameter=param_name>value</parameter></function></tool_call>
   */
  private parseQwen3XmlToolCalls(content: string): Qwen3ToolCall[] {
    if (!this.enableQwen3XmlParsing) {
      return [];
    }

    const toolCalls: Qwen3ToolCall[] = [];
    
    // Regex to match complete tool calls
    const toolCallRegex = /<tool_call>(.*?)<\/tool_call>/gs;
    const functionRegex = /<function=([^>]+)>(.*?)<\/function>/gs;
    const parameterRegex = /<parameter=([^>]+)>\s*([\s\S]*?)\s*<\/parameter>/g;

    let toolCallMatch;
    while ((toolCallMatch = toolCallRegex.exec(content)) !== null) {
      const toolCallContent = toolCallMatch[1];
      
      // Extract function name and parameters
      const functionMatch = functionRegex.exec(toolCallContent);
      if (functionMatch) {
        const functionName = functionMatch[1];
        const functionContent = functionMatch[2];
        
        // Parse parameters
        const parameters: Record<string, any> = {};
        let paramMatch;
        const paramRegex = new RegExp(parameterRegex.source, 'g');
        paramRegex.lastIndex = 0;
        
        while ((paramMatch = paramRegex.exec(functionContent)) !== null) {
          const paramName = paramMatch[1];
          let paramValue = paramMatch[2].trim();
          
          // Try to parse as JSON first, then as primitive types
          try {
            if (paramValue === 'null') {
              parameters[paramName] = null;
            } else if (paramValue === 'true') {
              parameters[paramName] = true;
            } else if (paramValue === 'false') {
              parameters[paramName] = false;
            } else if (!isNaN(Number(paramValue)) && paramValue !== '') {
              parameters[paramName] = Number(paramValue);
            } else if (paramValue.startsWith('{') || paramValue.startsWith('[')) {
              parameters[paramName] = JSON.parse(paramValue);
            } else {
              parameters[paramName] = paramValue;
            }
          } catch {
            parameters[paramName] = paramValue;
          }
        }

        // Create tool call
        const toolCall: Qwen3ToolCall = {
          id: `call_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
          type: 'function',
          function: {
            name: functionName,
            arguments: JSON.stringify(parameters)
          }
        };

        toolCalls.push(toolCall);
      }
    }

    return toolCalls;
  }

  /**
   * Check if the response contains Qwen3 XML tool calls
   */
  private hasQwen3XmlToolCalls(content: string): boolean {
    return /<tool_call>.*?<\/tool_call>/s.test(content);
  }

  /**
   * Process a response that may contain Qwen3 XML tool calls
   */
  async processResponse(response: any): Promise<{ text: string; toolCalls: Qwen3ToolCall[] }> {
    const content = response.choices?.[0]?.message?.content || '';
    
    // Check if this looks like a Qwen3 XML response
    if (this.hasQwen3XmlToolCalls(content)) {
      // Remove tool calls from the text content
      const textContent = content.replace(/<tool_call>.*?<\/tool_call>/gs, '').trim();
      
      // Parse tool calls
      const toolCalls = this.parseQwen3XmlToolCalls(content);

      return {
        text: textContent,
        toolCalls
      };
    }
    
    // Fall back to standard processing
    return {
      text: content,
      toolCalls: []
    };
  }

  // Implement required ContentGenerator methods
  async generateContent(
    request: any,
    userPromptId: string,
  ): Promise<any> {
    // This would need to be implemented based on the actual content generator being used
    throw new Error('Qwen3XmlContentGenerator.generateContent not implemented');
  }

  async generateContentStream(
    request: any,
    userPromptId: string,
  ): Promise<AsyncGenerator<any>> {
    // This would need to be implemented based on the actual content generator being used
    throw new Error('Qwen3XmlContentGenerator.generateContentStream not implemented');
  }

  async countTokens(request: any): Promise<any> {
    // This would need to be implemented based on the actual content generator being used
    throw new Error('Qwen3XmlContentGenerator.countTokens not implemented');
  }

  async embedContent(request: any): Promise<any> {
    // This would need to be implemented based on the actual content generator being used
    throw new Error('Qwen3XmlContentGenerator.embedContent not implemented');
  }
}
