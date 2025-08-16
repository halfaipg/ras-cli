/**
 * @license
 * Copyright 2025 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { NOC_SPECIALIZATIONS } from '../config/noc-prompts.js';

export function getNOCHelpText(domain?: string): string {
  const specialization = domain ? NOC_SPECIALIZATIONS[domain] : null;
  const allDomains = Object.keys(NOC_SPECIALIZATIONS);

  let helpText = `
🎯 RAS CLI - NOC Edition Help
Specialized for Network Operations Center Professionals

`;

  if (specialization) {
    helpText += `📋 ${specialization.domain.toUpperCase()} Specialization

Example Commands:
${specialization.examples.map(example => `• ${example}`).join('\n')}

Common Commands:
${specialization.commands.slice(0, 8).join(', ')}

System Prompt:
${specialization.systemPrompt.substring(0, 200)}...
`;
  } else {
    helpText += `Available Specializations:

${allDomains.map(domain => {
  const spec = NOC_SPECIALIZATIONS[domain];
  return `🔧 ${domain.toUpperCase()}
${spec.systemPrompt.substring(0, 100)}...
Use: /noc ${domain} to switch to this specialization
`;
}).join('\n\n')}
`;
  }

  helpText += `
NOC-Specific Commands:
• /noc [domain] - Switch to specific specialization
• /incident [priority] - Generate incident response procedures
• /runbook [type] - Create runbook templates
• /monitoring [tool] - Generate monitoring configurations
• /automation [tool] - Create automation scripts

Quick Examples:
• "Help me troubleshoot this Cisco switch connectivity issue"
• "Generate a VMware VM migration script"
• "Analyze this Linux server's performance metrics"
• "Create an incident response playbook for network outages"
• "Check storage capacity and performance on this SAN"

For more information, visit: https://github.com/QwenLM/qwen-code
`;

  return helpText;
}
