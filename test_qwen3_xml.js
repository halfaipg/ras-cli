// Test script for Qwen3 XML parsing functionality
import { Qwen3XmlParser } from './packages/core/dist/src/core/qwen3XmlParser.js';

// Test the Qwen3 XML parser
const parser = new Qwen3XmlParser(true); // Enable Qwen3 XML parsing

// Test case 1: Simple tool call
const testContent1 = `
I'll create a folder called "hello1" in the current directory.
<tool_call>
<function=run_shell_command>
<parameter=command>
mkdir hello1
</parameter>
<parameter=description>
Creating directory called hello1
</parameter>
</function>
</tool_call>
`;

console.log('Test 1: Simple tool call');
console.log('Input:', testContent1);
const result1 = parser.parseResponse(testContent1);
console.log('Result:', JSON.stringify(result1, null, 2));
console.log('---');

// Test case 2: Multiple parameters
const testContent2 = `
<tool_call>
<function=create_file>
<parameter=file_path>
test.txt
</parameter>
<parameter=content>
Hello World
</parameter>
</function>
</tool_call>
`;

console.log('Test 2: Multiple parameters');
console.log('Input:', testContent2);
const result2 = parser.parseResponse(testContent2);
console.log('Result:', JSON.stringify(result2, null, 2));
console.log('---');

// Test case 3: No tool calls
const testContent3 = `
This is just regular text without any tool calls.
`;

console.log('Test 3: No tool calls');
console.log('Input:', testContent3);
const result3 = parser.parseResponse(testContent3);
console.log('Result:', JSON.stringify(result3, null, 2));
console.log('---');

// Test case 4: Complex parameters
const testContent4 = `
<tool_call>
<function=edit_file>
<parameter=target_file>
package.json
</parameter>
<parameter=instructions>
Update the version number
</parameter>
<parameter=code_edit>
{
  "version": "1.0.1"
}
</parameter>
</function>
</tool_call>
`;

console.log('Test 4: Complex parameters');
console.log('Input:', testContent4);
const result4 = parser.parseResponse(testContent4);
console.log('Result:', JSON.stringify(result4, null, 2));
console.log('---');
