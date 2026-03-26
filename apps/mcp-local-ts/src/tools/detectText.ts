import { LocalDetectorClient } from '../api/localClient.js';
import { DetectTextInput } from '../schemas/input.js';

const client = new LocalDetectorClient();

export const detectTextTool = {
  name: 'detect_text',
  description: 'Detect if text is AI-generated or human-written using local model',
  inputSchema: {
    type: 'object' as const,
    properties: {
      text: {
        type: 'string',
        description: 'The text to analyze for AI detection',
      },
    },
    required: ['text'],
  },
  handler: async (args: unknown) => {
    const input = args as DetectTextInput;
    
    if (!input.text || input.text.trim() === '') {
      return {
        content: [
          {
            type: 'text',
            text: 'Error: Text cannot be empty',
          },
        ],
        isError: true,
      };
    }

    try {
      const result = await client.detect({ text: input.text });
      
      return {
        content: [
          {
            type: 'text',
            text: `检测结果：${result.label}（score=${result.score}）`,
          },
        ],
        structuredContent: {
          label: result.label,
          score: result.score,
          model_name: result.model_name,
        },
      };
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      return {
        content: [
          {
            type: 'text',
            text: `Detection failed: ${errorMessage}`,
          },
        ],
        isError: true,
      };
    }
  },
};
