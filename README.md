# RAS CLI

RAS CLI is a command-line AI workflow tool designed for Network Operations Center (NOC) professionals. It provides intelligent assistance for managing Linux servers, Cisco networking equipment, virtualization platforms, and storage systems.

## Installation

### Prerequisites

Node.js version 20 or higher is required.

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
git clone https://github.com/halfaipg/ras-cli.git
cd ras-cli
npm install
npm run build
npm link
```

## Quick Start

1. **Initialize RAS CLI**:
   ```bash
   ras init
   ```

2. **Configure your API endpoint**:
   Create a `.env` file in your project directory:
   ```bash
   OPENAI_API_BASE=https://your-server.com/v1
   OPENAI_API_KEY=your_api_key
   OPENAI_MODEL=your_model_name
   ```

3. **Start using RAS CLI**:
   ```bash
   ras
   ```

## Features

- **Linux Server Management**: System administration, troubleshooting, and automation
- **Cisco Networking**: Switch configuration and network troubleshooting
- **Virtualization**: VMware vSphere and Hyper-V management
- **Storage Systems**: SAN/NAS configuration and performance optimization
- **Incident Response**: Rapid troubleshooting and resolution workflows

## Configuration

RAS CLI supports multiple authentication methods:

- **OpenAI-compatible APIs**: Use with any OpenAI-compatible server
- **Environment Variables**: Configure via `.env` files
- **Settings File**: Global configuration in `~/.ras/settings.json`

## Documentation

For detailed documentation, see the [docs](./docs/) directory.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines.

## License

Licensed under the MIT License. See [LICENSE](./LICENSE) for details.
