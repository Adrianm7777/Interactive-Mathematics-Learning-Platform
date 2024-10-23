export const getMathProblems = async () => {
  const response = await fetch("http://localhost:8000/api/problems/");
  if (!response.ok) {
    throw new Error("Failed to fetch math problems");
  }

  return response.json();
};

export const submitAnswer = async (problemId: number, userAnswer: string) => {
  const response = await fetch("http://localhost:8000/api/answers/", {
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
  const response = await fetch(`http://localhost:8000/api/progress/`);
  if (!response.ok) {
    throw new Error("Failed to fetch user progress");
  }
  return response.json();
};
