# RAS CLI Project Navigation Guide

This document provides an overview of the RAS CLI project structure to help navigate and understand the codebase.

## Project Overview

RAS CLI is a command-line AI workflow tool designed for Network Operations Center (NOC) professionals. It provides intelligent assistance for managing Linux servers, Cisco networking equipment, virtualization platforms, and storage systems.

## Project Structure

```
.
├── .github/                 # GitHub Actions workflows and configurations
├── .vscode/                 # VS Code workspace configurations
├── docs/                    # Documentation files
├── eslint-rules/            # Custom ESLint rules
├── integration-tests/       # Integration tests
├── packages/                # Main packages directory
│   ├── cli/                 # Core CLI implementation
│   │   ├── src/             # Source code for CLI
│   │   │   ├── acp/         # Agent Communication Protocol components
│   │   │   ├── commands/    # CLI command implementations
│   │   │   ├── config/      # Configuration management
│   │   │   ├── generated/   # Generated code
│   │   │   ├── patches/     # Patch files
│   │   │   ├── services/    # Service implementations
│   │   │   ├── test-utils/  # Test utilities
│   │   │   ├── ui/          # UI components
│   │   │   └── utils/       # Utility functions
│   │   ├── index.ts         # Entry point
│   │   └── package.json     # Package configuration
│   ├── core/                # Core backend logic
│   │   ├── src/             # Source code for core
│   │   │   ├── __mocks__/   # Mock implementations
│   │   │   ├── code_assist/ # Code assist components
│   │   │   ├── config/      # Configuration management
│   │   │   ├── core/        # Core components
│   │   │   ├── ide/         # IDE integration
│   │   │   ├── mcp/         # Model Communication Protocol
│   │   │   ├── prompts/     # Prompt templates
│   │   │   ├── qwen/        # Qwen-specific components
│   │   │   ├── services/    # Services
│   │   │   ├── telemetry/   # Telemetry components
│   │   │   ├── test-utils/  # Test utilities
│   │   │   ├── tools/       # Tools
│   │   │   └── utils/       # Utility functions
│   │   ├── index.ts         # Entry point
│   │   └── package.json     # Package configuration
│   ├── test-utils/          # Shared test utilities
│   └── vscode-ide-companion/ # VSCode IDE companion
├── scripts/                 # Build and utility scripts
├── test789/                 # Test directory
├── .editorconfig            # Editor configuration
├── .gitattributes           # Git attributes
├── .gitignore               # Git ignore patterns
├── .npmrc                   # NPM configuration
├── .nvmrc                   # Node Version Manager configuration
├── .prettierrc.json         # Prettier configuration
├── CHANGELOG.md             # Change log
├── CONTRIBUTING.md          # Contribution guidelines
├── Dockerfile               # Docker configuration
├── esbuild.config.js        # ESBuild configuration
├── eslint.config.js         # ESLint configuration
├── LICENSE                  # License information
├── Makefile                 # Build automation
├── package-lock.json        # NPM lock file
├── package.json             # Main package configuration
├── QWEN.md                  # Qwen-specific documentation
├── qwen3_coder_setup.md     # Qwen3 coder setup documentation
├── qwen3coder_tool_parser_actual.py # Qwen3 tool parser implementation
├── qwen3coder_tool_parser.py # Qwen3 tool parser
├── README.gemini.md         # Gemini-specific README
├── README.md                # Main README
├── ROADMAP.md               # Project roadmap
├── SECURITY.md              # Security guidelines
├── test_qwen3_xml.js        # Test file for Qwen3 XML
├── tsconfig.json            # TypeScript configuration
└── ...
```

## Key Components

### CLI Package (`packages/cli`)
- Contains the main command-line interface implementation
- Houses command definitions and execution logic
- Manages configuration and user interactions

### Core Package (`packages/core`)
- Contains the core backend logic and services
- Implements the AI assistant functionality
- Provides shared utilities and components

### Commands
- Located in `packages/cli/src/commands/`
- Each command is implemented as a separate module
- Follows a consistent structure for command definition and execution

### Configuration
- Managed through `packages/cli/src/config/`
- Supports multiple configuration sources (environment variables, settings files, etc.)

### Services
- Located in `packages/cli/src/services/` and `packages/core/src/services/`
- Implement various functionalities like API communication, file operations, etc.

## Development Setup

1. Clone the repository
2. Install dependencies with `npm install`
3. Build the project with `npm run build`
4. Run tests with `npm run test`
5. Start the CLI with `npm start`

## Testing

- Unit tests are located in each package's test directories
- Integration tests are in `integration-tests/`
- Tests can be run with `npm run test` or `npm run test:e2e`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.