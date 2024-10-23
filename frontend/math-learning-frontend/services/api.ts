import { BASE_URL } from "./endpoints";

export const getMathProblems = async () => {
  const response = await fetch(`${BASE_URL}/problems`);
  if (!response.ok) {
    throw new Error("Failed to fetch math problems");
  }

  return response.json();
};

export const submitAnswer = async (problemId: number, userAnswer: string) => {
  const response = await fetch(`${BASE_URL}/answers`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      problem: problemId,
      user_answer: userAnswer,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to submit answer");
  }
  return response.json();
};

export const getUserProgess = async () => {
  const response = await fetch(`${BASE_URL}/progress`);
  if (!response.ok) {
    throw new Error("Failed to fetch user progress");
  }
  return response.json();
};
