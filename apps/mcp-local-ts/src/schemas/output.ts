import { z } from 'zod';

export const DetectTextOutputSchema = z.object({
  label: z.string(),
  score: z.number(),
  model_name: z.string(),
});

export type DetectTextOutput = z.infer<typeof DetectTextOutputSchema>;
