import { OAuth2Client } from 'google-auth-library';
import { promises as fs } from 'fs';
import path from 'path';
import os from 'os';

// OAuth Client Configuration
const QWEN_OAUTH_CLIENT_ID = process.env.QWEN_OAUTH_CLIENT_ID || 'your_client_id_here';

const QWEN_OAUTH_SCOPE = 'openid profile email model.completion';

// Directory for storing OAuth tokens
const RAS_DIR = path.join(os.homedir(), '.ras');

interface TokenInfo {
  access_token: string;
  refresh_token?: string;
  scope: string;
  token_type: string;
  expiry_date?: number;
}

export class QwenOAuth2 {
  private oauth2Client: OAuth2Client;
  private tokenPath: string;

  constructor() {
    this.oauth2Client = new OAuth2Client(QWEN_OAUTH_CLIENT_ID);
    this.tokenPath = path.join(RAS_DIR, 'oauth_token.json');
  }

  async getAuthUrl(): Promise<string> {
    return this.oauth2Client.generateAuthUrl({
      access_type: 'offline',
      scope: [QWEN_OAUTH_SCOPE],
      prompt: 'consent',
    });
  }

  async getTokensFromCode(code: string): Promise<TokenInfo> {
    const { tokens } = await this.oauth2Client.getToken(code);
    await this.saveTokens(tokens as TokenInfo);
    return tokens as TokenInfo;
  }

  async loadTokens(): Promise<TokenInfo | null> {
    try {
      const tokenData = await fs.readFile(this.tokenPath, 'utf8');
      const tokens = JSON.parse(tokenData) as TokenInfo;
      
      // Set the tokens on the OAuth2Client
      this.oauth2Client.setCredentials(tokens);
      
      return tokens;
    } catch (error) {
      return null;
    }
  }

  async saveTokens(tokens: TokenInfo): Promise<void> {
    // Ensure the directory exists
    await fs.mkdir(RAS_DIR, { recursive: true });
    
    // Save tokens to file
    await fs.writeFile(this.tokenPath, JSON.stringify(tokens, null, 2));
    
    // Set the tokens on the OAuth2Client
    this.oauth2Client.setCredentials(tokens);
  }

  async refreshTokens(): Promise<TokenInfo | null> {
    try {
      const tokens = await this.loadTokens();
      if (!tokens?.refresh_token) {
        return null;
      }

      // Set the refresh token and get a new access token
      this.oauth2Client.setCredentials({
        refresh_token: tokens.refresh_token
      });
      
      const { token } = await this.oauth2Client.getAccessToken();
      if (!token) {
        return null;
      }

      const refreshedTokens: TokenInfo = {
        access_token: token,
        refresh_token: tokens.refresh_token,
        scope: tokens.scope,
        token_type: 'Bearer'
      };
      
      await this.saveTokens(refreshedTokens);
      return refreshedTokens;
    } catch (error) {
      console.error('Error refreshing tokens:', error);
      return null;
    }
  }

  async getAccessToken(): Promise<string | null> {
    try {
      const tokens = await this.loadTokens();
      if (!tokens) {
        return null;
      }

      // Check if token is expired
      if (tokens.expiry_date && Date.now() >= tokens.expiry_date) {
        const refreshedTokens = await this.refreshTokens();
        return refreshedTokens?.access_token || null;
      }

      return tokens.access_token;
    } catch (error) {
      console.error('Error getting access token:', error);
      return null;
    }
  }

  async revokeTokens(): Promise<void> {
    try {
      await this.oauth2Client.revokeCredentials();
      await fs.unlink(this.tokenPath);
    } catch (error) {
      console.error('Error revoking tokens:', error);
    }
  }
}
