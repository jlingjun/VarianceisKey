import { z } from 'zod';

export const DetectTextInputSchema = z.object({
  text: z.string().min(1, 'Text cannot be empty'),
});

export type DetectTextInput = z.infer<typeof DetectTextInputSchema>;
