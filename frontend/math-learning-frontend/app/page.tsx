"use client";

import { useState, useEffect } from "react";
import { getMathProblems, submitAnswer } from "../services/api";

interface Problem {
  id: number;
  question: string;
  correct_answer: string;
  difficulty: string;
}

const ProblemsPage = () => {
  const [problems, setProblems] = useState<Problem[]>([]);
  const [userAnswer, setUserAnswer] = useState<string>("");
  const [selectedProblemId, setSelectedProblemId] = useState<number | null>(
    null
  );
  const [feedback, setFeedback] = useState<string>("");

  useEffect(() => {
    const fetchProblems = async () => {
      try {
        const data = await getMathProblems();
        setProblems(data);
      } catch (error) {
        console.error("Error fetching problems:", error);
      }
    };

    fetchProblems();
  }, []);

  const handleSubmitAnswer = async (problemId: number) => {
    try {
      const result = await submitAnswer(problemId, userAnswer);
      if (result.is_correct) {
        setFeedback("Correct!");
      } else {
        setFeedback("Incorrect, try again.");
      }
      console.log(result);
      setUserAnswer("");
      setSelectedProblemId(null);
    } catch (error) {
      console.error("Error submitting answer:", error);
      setFeedback("Error submitting answer.");
    }
  };

  return (
    <div className="p-4 w-dvw h-dvh flex justify-center items-center flex-col">
      <h1 className="text-2xl font-bold mb-4">Math Problems</h1>
      {problems.map((problem) => (
        <div key={problem.id} className="mb-6 text-center">
          <p className="mb-2">{problem.question}</p>
          {selectedProblemId === problem.id ? (
            <div>
              <input
                type="text"
                value={userAnswer}
                onChange={(e) => setUserAnswer(e.target.value)}
                className="border p-2 mb-2"
                placeholder="Your answer"
              />
              <button
                onClick={() => handleSubmitAnswer(problem.id)}
                className="bg-blue-500 text-white px-4 py-2 rounded"
              >
                Submit Answer
              </button>
            </div>
          ) : (
            <button
              onClick={() => setSelectedProblemId(problem.id)}
              className="bg-gray-200 px-4 py-2 rounded"
            >
              Answer
            </button>
          )}
        </div>
      ))}
      {feedback && <p className="mt-4 text-green-600">{feedback}</p>}
    </div>
  );
};

export default ProblemsPage;
