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
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-2xl p-6 bg-white rounded-lg shadow-md">
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-4">
          Math Problems
        </h1>
        {problems.map((problem) => (
          <div
            key={problem.id}
            className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200"
          >
            <p className="mb-2 text-lg font-medium text-gray-700 text-center">
              {problem.question}
            </p>
            {selectedProblemId === problem.id ? (
              <div className="flex flex-col">
                <input
                  type="text"
                  value={userAnswer}
                  onChange={(e) => setUserAnswer(e.target.value)}
                  className="border border-gray-300 p-2 rounded mb-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Your answer"
                />
                <button
                  onClick={() => handleSubmitAnswer(problem.id)}
                  className="bg-blue-600 text-white px-4 py-2 rounded transition duration-300 hover:bg-blue-700"
                >
                  Submit Answer
                </button>
              </div>
            ) : (
              <button
                onClick={() => setSelectedProblemId(problem.id)}
                className="bg-gray-300 text-gray-700 px-4 py-2 rounded transition duration-300 hover:bg-gray-400"
              >
                Answer
              </button>
            )}
          </div>
        ))}
        {feedback && (
          <p className="mt-4 text-green-600 font-semibold text-center text-4xl">
            {feedback}
          </p>
        )}
      </div>
    </div>
  );
};

export default ProblemsPage;
