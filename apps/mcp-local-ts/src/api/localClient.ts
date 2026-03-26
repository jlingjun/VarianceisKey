import { config } from '../config/env.js';
import { DetectTextInput } from '../schemas/input.js';
import { DetectTextOutput } from '../schemas/output.js';

export class LocalDetectorClient {
  private baseUrl: string;

  constructor(baseUrl?: string) {
    this.baseUrl = baseUrl || config.detectorApiUrl;
  }

  async detect(input: DetectTextInput): Promise<DetectTextOutput> {
    const response = await fetch(`${this.baseUrl}/detect`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: input.text }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Detector API error: ${response.status} - ${errorText}`);
    }

    return response.json();
  }

  async healthCheck(): Promise<boolean> {
    try {
      const response = await fetch(`${this.baseUrl}/health`);
      return response.ok;
    } catch {
      return false;
    }
  }
}
