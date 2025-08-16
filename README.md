# RAS CLI - NOC Edition
<div align="center">

![RAS CLI Screenshot](./ras-screenshot.png)

[![npm version](https://img.shields.io/npm/v/@ras-ai/ras-cli.svg)](https://www.npmjs.com/package/@ras-ai/ras-cli)
[![License](https://img.shields.io/github/license/QwenLM/qwen-code.svg)](./LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen.svg)](https://nodejs.org/)
[![Downloads](https://img.shields.io/npm/dm/@ras-ai/ras-cli.svg)](https://www.npmjs.com/package/@ras-ai/ras-cli)

**Rent-a-Server AI CLI Tool - Specialized for Network Operations Center (NOC) Professionals**

[Installation](#installation) • [Quick Start](#quick-start) • [NOC Features](#noc-features) • [Documentation](./docs/) • [Contributing](./CONTRIBUTING.md)

</div>

RAS CLI is a powerful command-line AI workflow tool specifically designed for **Network Operations Center (NOC) professionals** who manage Linux servers, Cisco networking equipment (Nexus & Catalyst), virtualization platforms (VMware & Hyper-V), and storage systems. It enhances your infrastructure management workflow with advanced automation, troubleshooting assistance, and intelligent infrastructure insights.

## 🎯 Built for NOC Professionals

RAS CLI is optimized for:
- **🔧 Linux Server Management** - System administration, troubleshooting, and automation
- **🌐 Cisco Networking** - Nexus & Catalyst switch configuration and monitoring
- **☁️ Virtualization** - VMware vSphere and Microsoft Hyper-V management
- **💾 Storage Systems** - SAN/NAS configuration and performance optimization
- **🚨 Incident Response** - Rapid troubleshooting and resolution workflows
- **📊 Infrastructure Monitoring** - Performance analysis and capacity planning

## 💡 Free Options Available

Get started with RAS CLI at no cost using any of these free options:

### 🔥 Qwen OAuth (Recommended)

- **2,000 requests per day** with no token limits
- **60 requests per minute** rate limit
- Simply run `ras` and authenticate with your qwen.ai account
- Automatic credential management and refresh
- Use `/auth` command to switch to Qwen OAuth if you have initialized with OpenAI compatible mode

### 🌏 Regional Free Tiers

- **Mainland China**: ModelScope offers **2,000 free API calls per day**
- **International**: OpenRouter provides **up to 1,000 free API calls per day** worldwide

For detailed setup instructions, see [Authorization](#authorization).

> [!WARNING]
> **Token Usage Notice**: RAS CLI may issue multiple API calls per cycle, resulting in higher token usage (similar to Claude Code). We're actively optimizing API efficiency.

## NOC Features

### 🔧 Linux Server Management
- **System Administration** - User management, service configuration, and system optimization
- **Troubleshooting** - Log analysis, performance diagnostics, and issue resolution
- **Automation** - Script generation for repetitive tasks and maintenance
- **Security** - Security hardening, vulnerability assessment, and compliance checks

### 🌐 Cisco Networking
- **Switch Configuration** - Nexus and Catalyst switch setup and optimization
- **Network Troubleshooting** - Connectivity issues, routing problems, and performance analysis
- **VLAN Management** - VLAN configuration, trunking, and inter-VLAN routing
- **Security** - Access control lists (ACLs), port security, and threat mitigation

### ☁️ Virtualization Platforms
- **VMware vSphere** - VM management, resource allocation, and performance tuning
- **Microsoft Hyper-V** - Virtual machine administration and cluster management
- **Resource Optimization** - Capacity planning, performance monitoring, and cost optimization
- **Disaster Recovery** - Backup strategies, replication, and business continuity

### 💾 Storage Systems
- **SAN/NAS Management** - Storage configuration, performance tuning, and capacity planning
- **Data Protection** - Backup strategies, replication, and disaster recovery
- **Performance Analysis** - I/O optimization, bottleneck identification, and capacity planning
- **Compliance** - Data retention policies and regulatory compliance

### 🚨 Incident Response
- **Rapid Diagnostics** - Quick identification of infrastructure issues
- **Escalation Procedures** - Automated escalation workflows and documentation
- **Resolution Tracking** - Incident lifecycle management and post-mortem analysis
- **Knowledge Base** - Building institutional knowledge from incident responses

## Installation

### Prerequisites

Ensure you have [Node.js version 20](https://nodejs.org/en/download) or higher installed.

```bash
curl -qL https://www.npmjs.com/install.sh | sh
```

### Install from npm

```bash
npm install -g @ras-ai/ras-cli@latest
ras --version
```

### Install from source

```bash
git clone https://github.com/QwenLM/qwen-code.git
cd qwen-code
npm install
npm install -g .
```

## Quick Start

```bash
# Start RAS CLI
ras

# NOC-specific examples
> Analyze this Linux server's performance metrics
> Help me troubleshoot this Cisco switch connectivity issue
> Generate a VMware VM migration script
> Check storage capacity and performance on this SAN
> Create an incident response playbook for network outages
```

### Session Management

Control your token usage with configurable session limits to optimize costs and performance.

#### Configure Session Token Limit

Create or edit `.ras/settings.json` in your home directory:

```json
{
  "sessionTokenLimit": 32000,
  "nocSpecialization": true,
  "defaultContext": "infrastructure"
}
```

#### Session Commands

- **`/compress`** - Compress conversation history to continue within token limits
- **`/clear`** - Clear all conversation history and start fresh
- **`/stats`** - Check current token usage and limits
- **`/noc`** - Switch to NOC-specific context and prompts

> 📝 **Note**: Session token limit applies to a single conversation, not cumulative API calls.

### Authorization

Choose your preferred authentication method based on your needs:

#### 1. Qwen OAuth (🚀 Recommended - Start in 30 seconds)

The easiest way to get started - completely free with generous quotas:

```bash
# Just run this command and follow the browser authentication
ras
```

**What happens:**

1. **Instant Setup**: CLI opens your browser automatically
2. **One-Click Login**: Authenticate with your qwen.ai account
3. **Automatic Management**: Credentials cached locally for future use
4. **NOC Optimization**: Pre-configured for infrastructure management tasks

**Free Tier Benefits:**

- ✅ **2,000 requests/day** (no token counting needed)
- ✅ **60 requests/minute** rate limit
- ✅ **Automatic credential refresh**
- ✅ **Zero cost** for individual users
- ✅ **NOC-specialized responses**
- ℹ️ **Note**: Model fallback may occur to maintain service quality

#### 2. OpenAI-Compatible API

Use API keys for OpenAI or other compatible providers:

**Configuration Methods:**

1. **Environment Variables**

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   export OPENAI_BASE_URL="your_api_endpoint"
   export OPENAI_MODEL="your_model_choice"
   ```

2. **Project `.env` File**
   Create a `.env` file in your project root:
   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_BASE_URL=your_api_endpoint
   OPENAI_MODEL=your_model_choice
   ```

**API Provider Options**

> ⚠️ **Regional Notice:**
>
> - **Mainland China**: Use Alibaba Cloud Bailian or ModelScope
> - **International**: Use Alibaba Cloud ModelStudio or OpenRouter

<details>
<summary><b>🇨🇳 For Users in Mainland China</b></summary>

**Option 1: Alibaba Cloud Bailian** ([Apply for API Key](https://bailian.console.aliyun.com/))

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
export OPENAI_MODEL="qwen3-coder-plus"
```

**Option 2: ModelScope (Free Tier)** ([Apply for API Key](https://modelscope.cn/docs/model-service/API-Inference/intro))

- ✅ **2,000 free API calls per day**
- ⚠️ Connect your Aliyun account to avoid authentication errors

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_BASE_URL="https://api-inference.modelscope.cn/v1"
export OPENAI_MODEL="Qwen/Qwen3-Coder-480B-A35B-Instruct"
```

</details>

<details>
<summary><b>🌍 For International Users</b></summary>

**Option 1: Alibaba Cloud ModelStudio** ([Apply for API Key](https://modelstudio.console.alibabacloud.com/))

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_BASE_URL="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
export OPENAI_MODEL="qwen3-coder-plus"
```

**Option 2: OpenRouter (Free Tier Available)** ([Apply for API Key](https://openrouter.ai/))

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_BASE_URL="https://openrouter.ai/api/v1"
export OPENAI_MODEL="qwen/qwen3-coder:free"
```

</details>

## Usage Examples

### 🔧 Linux Server Management

```bash
# System administration
> Analyze this server's performance and identify bottlenecks
> Help me configure a new user with sudo access
> Generate a script to monitor disk space and alert when low
> Troubleshoot this service that won't start

# Security and compliance
> Audit this server for security vulnerabilities
> Help me configure firewall rules for this application
> Generate a compliance checklist for PCI DSS
> Analyze these logs for security incidents
```

### 🌐 Cisco Networking

```bash
# Switch configuration
> Help me configure VLANs on this Nexus switch
> Generate a script to backup all switch configurations
> Troubleshoot this connectivity issue between switches
> Optimize the routing configuration for better performance

# Network monitoring
> Analyze this network topology for potential issues
> Help me configure SNMP monitoring for these switches
> Generate alerts for interface errors and utilization
> Create a network documentation template
```

### ☁️ Virtualization Management

```bash
# VMware vSphere
> Help me migrate this VM to a different datastore
> Analyze VM performance and suggest optimizations
> Generate a script to create VM snapshots before updates
> Troubleshoot this VM that won't power on

# Hyper-V
> Help me configure failover clustering for these VMs
> Generate PowerShell scripts for VM management
> Analyze storage performance for this Hyper-V cluster
> Create backup strategies for critical VMs
```

### 💾 Storage Systems

```bash
# SAN/NAS management
> Analyze storage performance and identify bottlenecks
> Help me configure RAID arrays for optimal performance
> Generate scripts to monitor storage capacity
> Troubleshoot this storage connectivity issue

# Data protection
> Create backup strategies for this storage system
> Help me configure replication between storage arrays
> Generate disaster recovery procedures
> Analyze backup job failures and suggest fixes
```

### 🚨 Incident Response

```bash
# Rapid diagnostics
> Help me quickly diagnose this network outage
> Generate an incident response checklist
> Analyze these logs for the root cause
> Create escalation procedures for this issue

# Documentation and follow-up
> Generate an incident report template
> Help me create a post-mortem analysis
> Document lessons learned from this incident
> Update runbooks based on this incident
```

## Popular NOC Tasks

### 📊 Infrastructure Monitoring

```bash
# Performance analysis
> Analyze system performance metrics and identify trends
> Help me set up monitoring thresholds for critical services
> Generate capacity planning reports
> Create dashboards for executive reporting

# Alert management
> Help me configure intelligent alerting rules
> Generate escalation procedures for different alert types
> Create runbooks for common alert scenarios
> Optimize alert noise and reduce false positives
```

### 🔧 Automation & Scripting

```bash
# Infrastructure automation
> Generate scripts for routine maintenance tasks
> Help me automate backup verification processes
> Create deployment scripts for configuration changes
> Build monitoring and alerting automation

# Workflow optimization
> Streamline incident response procedures
> Automate compliance reporting
> Create self-service tools for common tasks
> Build knowledge base automation
```

### 📋 Documentation & Knowledge Management

```bash
# Runbook creation
> Help me create runbooks for common procedures
> Generate troubleshooting guides for specific issues
> Create onboarding documentation for new team members
> Build knowledge base articles from incident responses

# Process documentation
> Document change management procedures
> Create escalation matrices
> Generate compliance documentation
> Build training materials for the team
```

## Configuration

RAS CLI supports various configuration options through environment variables, settings files, and command-line arguments. See the [Configuration Guide](./docs/cli/configuration.md) for detailed information.

### NOC-Specific Configuration

```json
{
  "nocSpecialization": true,
  "defaultContext": "infrastructure",
  "specializedPrompts": {
    "linux": "You are a senior Linux system administrator with expertise in enterprise environments",
    "networking": "You are a CCIE-level network engineer specializing in Cisco infrastructure",
    "virtualization": "You are a virtualization expert with deep VMware and Hyper-V knowledge",
    "storage": "You are a storage architect with expertise in SAN/NAS and data protection"
  }
}
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

RAS CLI is adapted from [Gemini CLI](https://github.com/google-gemini/gemini-cli) and optimized for NOC professionals managing complex infrastructure environments. We thank the Gemini CLI team for their excellent foundation.
