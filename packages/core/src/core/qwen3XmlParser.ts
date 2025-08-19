/**
 * Qwen3 XML Tool Call Parser
 * 
 * This utility parses Qwen3 XML format tool calls and converts them to standard OpenAI format.
 * Format: <tool_call><function=function_name><parameter=param_name>value</parameter></function></tool_call>
 * 
 * BULLETPROOF VERSION: Handles malformed XML from the model including missing closing tags
 */

export interface Qwen3ToolCall {
  id: string;
  type: 'function';
  function: {
    name: string;
    arguments: string;
  };
}

export interface ParsedQwen3Response {
  text: string;
  toolCalls: Qwen3ToolCall[];
}

export class Qwen3XmlParser {
  private enableQwen3XmlParsing: boolean;

  constructor(enableQwen3XmlParsing: boolean = false) {
    this.enableQwen3XmlParsing = enableQwen3XmlParsing;
  }

  /**
   * Check if the response contains Qwen3 XML tool calls (including malformed)
   */
  hasQwen3XmlToolCalls(content: string): boolean {
    // Check for complete tool calls
    if (/<tool_call>.*?<\/tool_call>/s.test(content)) {
      return true;
    }
    
    // Check for malformed tool calls (missing closing tags)
    if (/<tool_call>.*?(?=<tool_call>|$)/s.test(content)) {
      return true;
    }
    
    // Check for function tags (even without tool_call wrapper)
    if (/<function=([^>]+)/.test(content)) {
      return true;
    }
    
    return false;
  }

  /**
   * Parse Qwen3 XML tool calls from the model response (BULLETPROOF VERSION)
   */
  parseQwen3XmlToolCalls(content: string): Qwen3ToolCall[] {
    if (!this.enableQwen3XmlParsing) {
      return [];
    }

    const toolCalls: Qwen3ToolCall[] = [];
    
    // First try to find JSON format inside <tool_call> tags (most common case)
    const jsonToolCallMatches = content.match(/<tool_call>\s*(.*?)\s*<\/tool_call>/gs);
    if (jsonToolCallMatches) {
      for (const match of jsonToolCallMatches) {
        const jsonContent = match.replace(/<tool_call>\s*/, '').replace(/\s*<\/tool_call>/, '');
        try {
          const toolData = JSON.parse(jsonContent.trim());
          if (toolData && typeof toolData === 'object' && toolData.name) {
            toolCalls.push({
              id: `call_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
              type: 'function',
              function: {
                name: toolData.name,
                arguments: JSON.stringify(toolData.arguments || {})
              }
            });
          }
        } catch (error) {
          // Not JSON, continue to XML parsing
        }
      }
      
      if (toolCalls.length > 0) {
        return toolCalls;
      }
    }
    
    // Try to find malformed tool calls (missing closing tags)
    const malformedToolCallMatches = content.match(/<tool_call>\s*(.*?)(?=<tool_call>|$)/gs);
    if (malformedToolCallMatches) {
      for (const match of malformedToolCallMatches) {
        const toolCallContent = match.replace(/<tool_call>\s*/, '');
        const toolCall = this.parseMalformedToolCall(toolCallContent);
        if (toolCall) {
          toolCalls.push(toolCall);
        }
      }
      
      if (toolCalls.length > 0) {
        return toolCalls;
      }
    }
    
    // Try to find function tags directly (without tool_call wrapper)
    const functionMatches = content.match(/<function=([^>]+)/g);
    if (functionMatches) {
      for (const functionMatch of functionMatches) {
        const functionName = functionMatch.match(/<function=([^>]+)/)?.[1];
        if (functionName) {
          const toolCall = this.parseFunctionFromContent(content, functionName);
          if (toolCall) {
            toolCalls.push(toolCall);
          }
        }
      }
    }
    
    return toolCalls;
  }

  /**
   * Parse a malformed tool call (missing closing tags)
   */
  private parseMalformedToolCall(toolCallContent: string): Qwen3ToolCall | null {
    // Extract function name
    const functionMatch = toolCallContent.match(/<function=([^>]+)/);
    if (!functionMatch) {
      return null;
    }
    
    const functionName = functionMatch[1];
    
    // Extract parameters with robust parsing
    const parameters: Record<string, any> = {};
    const paramMatches = toolCallContent.match(/<parameter=([^>]+)>\s*([\s\S]*?)(?=<parameter=|<\/function>|$)/g);
    
    if (paramMatches) {
      for (const paramMatch of paramMatches) {
        const paramNameMatch = paramMatch.match(/<parameter=([^>]+)>\s*([\s\S]*?)(?=<parameter=|<\/function>|$)/);
        if (paramNameMatch) {
          const paramName = paramNameMatch[1];
          let paramValue = paramNameMatch[2].trim();
          
          // Clean up parameter value
          paramValue = this.cleanParameterValue(paramValue);
          
          // Parse parameter value
          parameters[paramName] = this.parseParameterValue(paramValue);
        }
      }
    }
    
    return {
      id: `call_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      type: 'function',
      function: {
        name: functionName,
        arguments: JSON.stringify(parameters)
      }
    };
  }

  /**
   * Parse a function from the entire content (when no tool_call wrapper)
   */
  private parseFunctionFromContent(content: string, functionName: string): Qwen3ToolCall | null {
    const parameters: Record<string, any> = {};
    
    // Find all parameter tags for this function
    const paramMatches = content.match(new RegExp(`<parameter=([^>]+)>\\s*([\\s\\S]*?)(?=<parameter=|</function>|$)`, 'g'));
    
    if (paramMatches) {
      for (const paramMatch of paramMatches) {
        const paramNameMatch = paramMatch.match(/<parameter=([^>]+)>\s*([\s\S]*?)(?=<parameter=|<\/function>|$)/);
        if (paramNameMatch) {
          const paramName = paramNameMatch[1];
          let paramValue = paramNameMatch[2].trim();
          
          // Clean up parameter value
          paramValue = this.cleanParameterValue(paramValue);
          
          // Parse parameter value
          parameters[paramName] = this.parseParameterValue(paramValue);
        }
      }
    }
    
    return {
      id: `call_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      type: 'function',
      function: {
        name: functionName,
        arguments: JSON.stringify(parameters)
      }
    };
  }

  /**
   * Clean up parameter value (remove extra whitespace, newlines, etc.)
   */
  private cleanParameterValue(value: string): string {
    return value
      .replace(/^\s+/, '')  // Remove leading whitespace
      .replace(/\s+$/, '')  // Remove trailing whitespace
      .replace(/\n+$/, '')  // Remove trailing newlines
      .replace(/^\n+/, ''); // Remove leading newlines
  }

  /**
   * Parse parameter value with type detection
   */
  private parseParameterValue(value: string): any {
    // Handle null, boolean, and number types
    if (value === 'null') {
      return null;
    } else if (value === 'true') {
      return true;
    } else if (value === 'false') {
      return false;
    } else if (!isNaN(Number(value)) && value !== '') {
      return Number(value);
    }
    
    // Try to parse as JSON
    try {
      if (value.startsWith('{') || value.startsWith('[')) {
        return JSON.parse(value);
      }
    } catch (error) {
      // Not valid JSON, return as string
    }
    
    // Return as string
    return value;
  }

  /**
   * Process a response that may contain Qwen3 XML tool calls
   */
  parseResponse(content: string): ParsedQwen3Response {
    // Check if this looks like a Qwen3 XML response
    if (this.hasQwen3XmlToolCalls(content)) {
      // Remove tool calls from the text content (handle both complete and malformed)
      let textContent = content
        .replace(/<tool_call>.*?<\/tool_call>/gs, '')  // Remove complete tool calls
        .replace(/<tool_call>.*?(?=<tool_call>|$)/gs, '')  // Remove malformed tool calls
        .replace(/<function=([^>]+)>.*?(?=<function=|$)/gs, '')  // Remove function tags
        .trim();
      
      // Parse tool calls
      const toolCalls = this.parseQwen3XmlToolCalls(content);

      // Extract description from tool calls for display
      let description = '';
      if (toolCalls.length > 0) {
        try {
          const firstToolCall = toolCalls[0];
          const args = JSON.parse(firstToolCall.function.arguments);
          description = args.description || '';
        } catch (error) {
          // Silently ignore description parsing errors
        }
      }

      // If the content is ONLY tool calls (no other text), return the description
      const hasOtherText = textContent.length > 0;
      
      return {
        text: hasOtherText ? textContent : description,
        toolCalls
      };
    }
    
    // Fall back to standard processing
    return {
      text: content,
      toolCalls: []
    };
  }

  /**
   * Convert Qwen3 XML tool calls to standard OpenAI format
   */
  convertToOpenAIFormat(qwen3ToolCalls: Qwen3ToolCall[]): any[] {
    return qwen3ToolCalls.map(toolCall => ({
      id: toolCall.id,
      type: toolCall.type,
      function: {
        name: toolCall.function.name,
        arguments: toolCall.function.arguments
      }
    }));
  }
}
