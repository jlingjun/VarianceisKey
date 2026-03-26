import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { detectTextTool } from './tools/detectText.js';

export function createServer() {
  const server = new Server(
    {
      name: 'mcp-varianceiskey',
      version: '1.0.0',
    },
    {
      capabilities: {
        tools: {},
      },
    }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => {
    return {
      tools: [
        {
          name: detectTextTool.name,
          description: detectTextTool.description,
          inputSchema: detectTextTool.inputSchema,
        },
      ],
    };
  });

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === detectTextTool.name) {
      return detectTextTool.handler(args);
    }

    throw new Error(`Unknown tool: ${name}`);
  });

  return server;
}

export async function runServer() {
  const server = createServer();
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('MCP VarianceisKey Server running on stdio');
}
